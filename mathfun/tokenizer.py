from typing import List, Dict
from math import gcd

VARIABLES = ["a", "b", "c", "x", "y", "z"]
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
OPERATORS = ["+", "-", "*", "/"]
PAREN_OPEN = "PARENTHESIS_OPEN"
PAREN_CLOSE = "PARENTHESIS_CLOSE"

CONSTANT = "CONSTANT"
VARIABLE = "VARIABLE"
OPERATOR = "OPERATOR"

class Token():
    def __init__(self, t, v):
        self.type = t
        self.val = v
        if t == OPERATOR:
            if v in ["+", "-"]:
                self.precedence = 2
            elif v in ["*", "/"]:
                self.precedence = 1
        elif t == PAREN_OPEN:
            self.precedence = 10
        else:
            self.precedence = None
    def __str__(self):
        return "Token[" + self.type + ", " + self.val + "]"
    def __repr__(self):
        return "Token[" + self.type + ", " + self.val + ", " + str(self.precedence) + "]"

class Node():
    def __init__(self, val: str, left, right):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        if self.left == None and self.right == None:
            return self.val
        else:
            return "(" + str(self.left) + self.val + str(self.right) + ")"

    def evaluate(self, dict: Dict) -> float:
        raise Exception("Go away!!!")
    
    def derivative(self, var: str):
        raise Exception("Go away!!!")

    def reduce(self):
        return (self, False)

class Operator(Node):
    def __init__(self, val: str, left: Node, right: Node):
        super().__init__(val, left, right)

    def evaluate(self, dict: Dict) -> float:
        if self.val == "+":
            return self.left.evaluate(dict) + self.right.evaluate(dict)
        elif self.val == "-":
            return self.left.evaluate(dict) - self.right.evaluate(dict)
        elif self.val == "*":
            return self.left.evaluate(dict) * self.right.evaluate(dict)
        elif self.val == "/":
            return self.left.evaluate(dict) / self.right.evaluate(dict)

    def derivative(self, var: str) -> Node:
        if self.val == "+":
            return Operator("+", self.left.derivative(var), self.right.derivative(var))
        elif self.val == "-":
            return Operator("-", self.left.derivative(var), self.right.derivative(var))
        elif self.val == "*":
            return Operator("+", Operator("*", self.left.derivative(var), self.right), Operator("*", self.left, self.right.derivative(var)))
        elif self.val == "/":
            return Operator("/", Operator("-", Operator("*", self.left.derivative(var), self.right), Operator("*", self.left, self.right.derivative(var))), Operator("*", self.right, self.right))

    def reduce(self): # -> Tuple(Node, bool): # The boolean return value is "True" iff the syntax tree was reduced
        if self.val == "+":
            if isinstance(self.left, Constant) and self.left.val == "0":
                (rr, _) = self.right.reduce()
                return (rr, True)
            elif isinstance(self.right, Constant) and self.right.val == "0":
                (lr, _) = self.left.reduce()
                return (lr, True)
            elif isinstance(self.left, Constant) and isinstance(self.right, Constant):
                return (Constant(str(int(self.left.val) + int(self.right.val))), True)
        if self.val == "-":
            # if isinstance(self.left, Constant) and self.left.val == "0":
                # (rr, _) = self.right.reduce()
                # return (rr, True)
            if isinstance(self.right, Constant) and self.right.val == "0":
                (lr, _) = self.left.reduce()
                return (lr, True)
            elif isinstance(self.left, Constant) and isinstance(self.right, Constant):
                return (Constant(str(int(self.left.val) - int(self.right.val))), True)
        if self.val == "*":
            if isinstance(self.left, Constant) and self.left.val == "0":
                return (Constant("0"), True)
            elif isinstance(self.right, Constant) and self.right.val == "0":
                return (Constant("0"), True)
            elif isinstance(self.left, Constant) and self.left.val == "1":
                (rr, _) = self.right.reduce()
                return (rr, True)
            elif isinstance(self.right, Constant) and self.right.val == "1":
                (lr, _) = self.left.reduce()
                return (lr, True)
            elif isinstance(self.left, Constant) and isinstance(self.right, Constant):
                return (Constant(str(int(self.left.val) * int(self.right.val))), True)
        if self.val == "/":
            if isinstance(self.left, Constant) and self.left.val == "0":
                return (Constant("0"), True)
            elif isinstance(self.right, Constant) and self.right.val == "0":
                raise Exception("Division by 0")
            # elif isinstance(self.left, Constant) and self.left.val == "1":
                # (rr, _) = self.right.reduce()
                # return (rr, True)
            elif isinstance(self.right, Constant) and self.right.val == "1":
                (lr, _) = self.left.reduce()
                return (lr, True)
            elif isinstance(self.left, Constant) and isinstance(self.right, Constant):
                nominator = int(self.left.val)
                denominator = int(self.right.val)
                if nominator % denominator == 0:
                    return (Constant(str(int(nominator / denominator))), True)
                else:
                    # Where is Euclid when you need him the most???
                    divisor = gcd(nominator, denominator)
                    l = Constant(str(int(nominator / divisor)))
                    r = Constant(str(int(denominator / divisor)))
                    return (Operator("/", l, r), True if divisor > 1 else False)

        # Catch-all for all operators - try to reduce both left and right child
        (lr, left_trigger_reduce) = self.left.reduce()
        (rr, right_trigger_reduce) = self.right.reduce()
        if left_trigger_reduce == True or right_trigger_reduce == True:
            return Operator(self.val, lr, rr).reduce()
        else:
            return (Operator(self.val, lr, rr), False)


class Variable(Node):
    def __init__(self, val: str):
        super().__init__(val, None, None)

    def evaluate(self, dict: Dict) -> float:
        if self.val in dict.keys():
            return float(dict[self.val])
        else:
            raise Exception("Unbound variable: " + self.val)

    def derivative(self, var: str) -> Node:
        if self.val == var:
            return Constant("1")
        else:
            return Constant("0")


class Constant(Node):
    def __init__(self, val: str):
        super().__init__(val, None, None)

    def evaluate(self, dict: Dict) -> float:
        return float(self.val)

    def derivative(self, var: str) -> Node:
        return Constant("0")

class Function(Node):
    def __init__(self, val: str, left: Node):
        super().__init__(val, left, None)

def tokenize(expr: str) -> List[Token]:
    if expr == None or expr == "":
        return []
    else:
        tokens = []
        index = 0
        while index < len(expr):
            ch = expr[index]
            if ch == " ":
                index = index + 1 # Skip white space
            elif ch in NUMBERS:
                constant = tokenize_constant(expr, index)
                tokens.append(Token(CONSTANT, constant))
                index = index + len(constant)
            elif ch in VARIABLES:
                variable = tokenize_variable(expr, index)
                tokens.append(Token(VARIABLE, variable))
                index = index + len(variable)
            elif ch in OPERATORS:
                tokens.append(Token(OPERATOR, ch))
                index = index + 1
            elif ch == "(":
                tokens.append(Token(PAREN_OPEN, ch))
                index = index + 1
            elif ch == ")":
                tokens.append(Token(PAREN_CLOSE, ch))
                index = index + 1
            else:
                index = index + 1 # For now, just ignore; to be handled later using exception...
        pass
        return tokens

def tokenize_constant(expr: str, index: int) -> str:
    constant = ""
    while index < len(expr):
        ch = expr[index]
        if ch in NUMBERS:
            constant = constant + ch
        else:
            return constant
        index = index + 1
    return constant

def tokenize_variable(expr: str, index: int) -> str:
    variable = ""
    while index < len(expr):
        ch = expr[index]
        if ch in VARIABLES:
            variable = variable + ch
        else:
            return variable
        index = index + 1
    return variable

def tokens2rpn(tokens: List[Token]) -> List[Token]:
    rpn: List[Token] = []
    stack: List[Token] = []

    for token in tokens:
        if token.type == CONSTANT or token.type == VARIABLE:
            rpn.append(token)
        elif token.type == OPERATOR:
            while len(stack) > 0 and stack[-1].precedence <= token.precedence:
                rpn.append(stack.pop())
            stack.append(token)
        elif token.type == PAREN_OPEN:
            stack.append(token)
        elif token.type == PAREN_CLOSE:
            while len(stack) > 0 and stack[-1].type != PAREN_OPEN:
                rpn.append(stack.pop())
            if len(stack) == 0:
                pass # TODO - This is an error, should be handled
            stack.pop()
        else:
            pass # TODO need to add rule for parentheses etc.

    for stack_item in reversed(stack):
        rpn.append(stack_item)

    return rpn

def rpn2nodes(rpn: List[Token]) -> List[Node]:
    nodes: List[Node] = []

    for token in rpn:
        if token.type == CONSTANT:
            nodes.append(Constant(token.val))
        elif token.type == VARIABLE:
            nodes.append(Variable(token.val))
        elif token.type == OPERATOR:
            right_child = nodes.pop()
            left_child = nodes.pop()
            nodes.append(Operator(token.val, left_child, right_child))

    return nodes

def rpn2syntax_tree(rpn: List[Token]) -> List[Node]:
    nodes: List[Node] = rpn2nodes(rpn)
    if len(nodes) != 1:
        raise Exception("Unexpected tokens in input, length: " + str(len(nodes)))
    return nodes[0]
