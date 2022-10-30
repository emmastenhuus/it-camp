from re import match
import math

# REF: https://blog.klipse.tech/javascript/2017/02/08/tiny-compiler-tokenizer.html
# REF: https://en.wikipedia.org/wiki/Shunting-yard_algorithm

class ENode:

    def __init__(self, node, children):
        self.node = node
        self.children = children

    def to_rpn_str(self):
        n = self.node
        f3 = self.children
        tp = n[0]
        if tp == OP:
            return f3[0].to_rpn_str() + " " + f3[1].to_rpn_str() + " " + n[1] 
        elif tp == NAME or tp == NUM:
            return n[1]
        elif tp == FUNC:
            return f3[0].to_rpn_str() + " " + n[1]
        else:
            return "ERROR"

    def _to_infix_str(self):
        n = self.node
        f3 = self.children
        tp = n[0]
        if tp == OP:
            return "(" + f3[0]._to_infix_str() + " " + n[1] + " " + f3[1]._to_infix_str() + ")"
        elif tp == NAME or tp == NUM:
            return n[1]
        elif tp == FUNC:
            if n[1] == "fact":
                return f3[0]._to_infix_str() + "!"
            else:
                return n[1] + "(" + f3[0]._to_infix_str() + ")"
        else:
            return "ERROR"

    def to_infix_str(self):
        res = self._to_infix_str()
        if res.startswith("(") and res.endswith(")"):
            return res[1:-1] # Strip outer parentheses
        else:
            return res

    def evaluate(self, variables = {}):
        n = self.node
        f3 = self.children
        tp = n[0]
        if tp == OP:
            op_type = n[1]
            v0 = f3[0].evaluate(variables)
            v1 = f3[1].evaluate(variables)
            if op_type == "+":
                return v0 + v1
            elif op_type == "-":
                return v0 - v1
            elif op_type == "*":
                return v0 * v1
            elif op_type == "/":
                return v0 / v1
            elif op_type == "^":
                return v0 ** v1
            else:
                raise Exception("ERROR")
        elif tp == NAME:
            nm = n[1]
            if nm == "pi":
                return math.pi
            elif nm == "e":
                return math.e
            elif nm in variables:
                return variables[nm]
            else:
                raise Exception("Unbound variable: " + str(nm))
        elif tp == NUM:
            return float(n[1])
        elif tp == FUNC:
            fname = n[1]
            if fname == "sin":
                return math.sin(f3[0].evaluate(variables))
            elif fname == "cos":
                return math.cos(f3[0].evaluate(variables))
            elif fname == "tan":
                return math.tan(f3[0].evaluate(variables))
            elif fname == "log":
                return math.log10(f3[0].evaluate(variables))
            elif fname == "ln":
                return math.log(f3[0].evaluate(variables))
            elif fname == "exp":
                return math.exp(f3[0].evaluate(variables))
            elif fname == "inv":
                return 1 / f3[0].evaluate(variables)
            elif fname == "fact":
                return float(math.factorial(round(f3[0].evaluate(variables))))
            else:
                raise Exception("ERROR")
        else:
            raise Exception("ERROR")
        
# Derivative rules:
# f(x) = k  =>  f'(x) = 0
# f(x) = x  =>  f'(x) = 1
# f(x) = x^n  =>  f'(x) = x^(n-1)
# f(x) = g(x) * h(x)  =>  f'(x) = g'(x) * h(x) + g(x) * h'(x)

    def derivative(self, dv = "x"):
        n = self.node
        f3 = self.children
        tp = n[0]
        if tp == NUM:
            return ENode((NUM, "0", 0, 0), None)
        elif tp == NAME:
            if n[1] == dv:
                return ENode((NUM, "1", 0, 0), None)
            else:
                return ENode((NUM, "0", 0, 0), None)
        elif tp == OP:
            op_type = n[1]
            d0 = f3[0].derivative(dv)
            d1 = f3[1].derivative(dv)
            if op_type == "+":
                return ENode((OP, "+", 2, 1), [d0, d1])
            elif op_type == "-":
                return ENode((OP, "-", 2, 1), [d0, d1])
            elif op_type == "*":
                r0 = ENode((OP, "*", 3, 1), [d0, f3[1]])
                r1 = ENode((OP, "*", 3, 1), [f3[0], d1])
                return ENode((OP, "+", 2, 1), [r0, r1])
#             elif op_type == "^":
#                 f3[0].node
#                 
#                 r1 = ENode((OP, "*", 3, 1), [d0, f3[1]])
#                 r2 = ENode((OP, "*", 3, 1), [f3[0], d1])
#                 return ENode((OP, "+", 2, 1), [r1, r2])

        raise Exception("Not yet implemented")
    
    def reduce(self):
        n = self.node
        f3 = self.children
        tp = n[0]
        if tp == OP:
            op_type = n[1]
            r0 = f3[0].reduce()
            r1 = f3[1].reduce()
            if r0.node[0] == NUM and r1.node[0] == NUM and op_type == "*":
#                print(r0.node[0], r0.node[1])
#                print(r1.node[0], r1.node[1])
                return ENode((NUM, str(float(r0.node[1]) * float(r1.node[1])), 0, 0), None)
            if op_type == "+":
                if r0.node[1] == "0":
                    return r1
                elif r1.node[1] == "0":
                    return r0
                else:
                    return ENode((OP, "+", 2, 1), [r0, r1])
            elif op_type == "-":
                if r1.node[1] == "0":
                    return r0
                else:
                    return ENode((OP, "-", 2, 1), [r0, r1])
            elif op_type == "*":
                if r0.node[1] == "0" or r1.node[1] == "0":
                    return ENode((NUM, "0", 0, 0), None)
                elif r0.node[1] == "1":
                    return r1
                elif r1.node[1] == "1":
                    return r0
                else:
                    return ENode((OP, "*", 3, 1), [r0, r1])
#            elif r0.node[0] == NUM:
#                print(r0.node[0], r0.node[1])
                    
        return self
        

PAREN_OPEN = "PAREN_OPEN"
PAREN_CLOSE = "PAREN_CLOSE"
NUM = "NUMBER"
NAME = "NAME"
FUNC = "FUNCTION"
OP = "OPERATOR"
FACTORIAL = "FACTORIAL"

# t: Type of character
# v: Value of character
# p: Pattern
# i: Input string
# f3: Current location
def tokenizeCharPattern(t, p, i, f3):
    if match(p, i[f3]):
        return (1, (t, i[f3]))
    else:
        return (0, None)

# i: Input string
# f3: Current location
def tokenizeParenOpen(i, f3):
    return tokenizeCharPattern(PAREN_OPEN, "[(]", i, f3)

# i: Input string
# f3: Current location
def tokenizeParenClose(i, f3):
    return tokenizeCharPattern(PAREN_CLOSE, "[)]", i, f3)

# i: Input string
# f3: Current location
def tokenizeFactorial(i, f3):
    return tokenizeCharPattern(FACTORIAL, "[!]", i, f3)

# i: Input string
# f3: Current location
def tokenizeOperator(i, f3):
    return tokenizeCharPattern(OP, "[+\-\*/^]", i, f3)

# t: Type of character
# p: Pattern matching
# i: Input string
# f3: Current location
def tokenizePattern(t, p, i, f3):
    consumedChars = 0
    value = ""
    while True:
        idx = f3 + consumedChars
        if idx < len(i) and match(p, i[idx]):
            value += i[idx]
            consumedChars += 1
        else:
            if (consumedChars == 0):
                return (0, None)
            else:
                return (consumedChars, (t, value))

def tokenizeNumber(i, f3):
    return tokenizePattern(NUM, "[0-9\.]", i, f3)

def tokenizeName(i, f3):
    return tokenizePattern(NAME, "[a-z]", i, f3)

# m = match("\w+", "dsfm sdf sdf", flags=0)
# print(m)
# print(tokenizeName("dsfdLsf453.689bcbcb", 0))

# i: Input string
# f3: Current location
def skipWhiteSpace(i, f3):
    if match("\s", i[f3]):
        return (1, None)
    else:
        return (0, None)


tokenizers = [skipWhiteSpace, tokenizeParenOpen, tokenizeParenClose, tokenizeOperator, tokenizeNumber, tokenizeName, tokenizeFactorial]

def post_process_tokens(tokens):
    pp = []
    for tok in tokens:
        token_type = tok[0]
        if token_type == NAME:
            val = tok[1]
            found = False
            for f in ["sin", "cos", "tan", "log", "ln", "exp", "inv", "fact"]:
                if val == f:
                    pp.append((FUNC, val, 0, 0))
                    found = True
                    break
            if not found:
                pp.append((tok[0], tok[1], 0, 0))
        elif token_type == OP:
            val = tok[1]
            if val == "+":
                pp.append((OP, "+", 2, 1))
            elif val == "-":
                pp.append((OP, "-", 2, 1))
            elif val == "*":
                pp.append((OP, "*", 3, 1))
            elif val == "/":
                pp.append((OP, "/", 3, 1))
            elif val == "^":
                pp.append((OP, "^", 4, 0))
            else:
                raise Exception("Unknown operator: " + str(OP))
        else:
            pp.append((tok[0], tok[1], 0, 0))
    return pp

# Tokens:
#   0 : type
#   1 : value
#   2 : precedence (0 means: don't care)
#   3 : left-associative if 1, right-associative if 0

def tokenize(i):
    f3 = 0
    tokens = []
    while f3 < len(i):
        tokenized = False
        for tok_fn in tokenizers:
            if not tokenized:
                (consumedChars, token) = tok_fn(i, f3)
                if consumedChars > 0:
                    tokenized = True
                    f3 += consumedChars
                if token:
                    tokens.append(token)
        if not tokenized:
            raise Exception("Syntax error at position: " + str(f3) + " - '" + i[f3:] + "'")
    return post_process_tokens(tokens)

def relevant_operator_on_stack(stack, token):
    top_stack = stack[-1]
    if (top_stack[0] == FUNC):
        return True
    top_stack_precedence = top_stack[2]
    token_precedence = token[2]
    if top_stack_precedence > token_precedence:
        return True
    if top_stack_precedence == token_precedence and top_stack[3] == 1:
        return True
    return False

# Implementation of shunting-yard algorithm
def reverse_polish_notation(tokens):
    output_queue = []
    operator_stack = []

    for tok in tokens:
        token_type = tok[0]
       
        if token_type == NUM or token_type == NAME:
            output_queue.append(tok)
        elif token_type == FUNC:
            operator_stack.append(tok)
        elif token_type == FACTORIAL:
            # operator_stack.insert(len(operator_stack) - 1, tok)
            # operator_stack.append(tok)
            output_queue.append(tok)
        elif token_type == OP:
            while len(operator_stack) > 0 and relevant_operator_on_stack(operator_stack, tok) and operator_stack[-1][0] != PAREN_OPEN:
                op = operator_stack.pop()
                output_queue.append(op)
            operator_stack.append(tok)
        elif token_type == PAREN_OPEN:
            operator_stack.append(tok)
        elif token_type == PAREN_CLOSE:
            while len(operator_stack) > 0 and (operator_stack[-1][0] != PAREN_OPEN):
                op = operator_stack.pop()
                output_queue.append(op)
            if len(operator_stack) > 0 and operator_stack[-1][0] == PAREN_OPEN:
                operator_stack.pop() # Discard
            else:
                raise Exception("Mismatched parenthesis: " + str(output_queue))
        else:
            raise Exception("Unknown token: " + str(tok))

    for op in reversed(operator_stack):
        output_queue.append(op)

    return output_queue

def rpn_to_parse_tree(rpn_tokens):
    q = []
    for t in rpn_tokens:
        tok_type = t[0]
        if tok_type == NUM or tok_type == NAME:
            q.append(ENode(t, None))
        elif tok_type == FUNC:
            q.append(ENode(t, [q.pop()]))
        elif tok_type == FACTORIAL:
            q.append(ENode((FUNC, "fact", 0, 0), [q.pop()]))
        elif tok_type == OP:
            c1 = q.pop();
            c2 = q.pop()
            n = ENode(t, [c2, c1])
            q.append(n)
    return q[0]

def eval_expr(s, variables = {}):
    return rpn_to_parse_tree(reverse_polish_notation(tokenize(s))).evaluate(variables)

def to_infix_str_and_eval_expr(s, variables = {}):
    parse_tree = rpn_to_parse_tree(reverse_polish_notation(tokenize(s)))
    return (parse_tree.to_infix_str(), parse_tree.evaluate(variables))

def to_infix_str(s):
    return rpn_to_parse_tree(reverse_polish_notation(tokenize(s))).to_infix_str()

def to_rpn_str(s):
    return rpn_to_parse_tree(reverse_polish_notation(tokenize(s))).to_rpn_str()

def derivative(s, dv = "x"):
    return rpn_to_parse_tree(reverse_polish_notation(tokenize(s))).derivative(dv).to_infix_str()

def derivative_reduce(s, dv = "x"):
    return rpn_to_parse_tree(reverse_polish_notation(tokenize(s))).derivative(dv).reduce().to_infix_str()
