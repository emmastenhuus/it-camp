'''
type
VARIABLE
OPERATOR
CONSTANT
val "sin" "17" "+" "*" 
'''
from typing import List

VARIABLES = ["a", "b", "c", "x", "y", "z"]
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
OPERATORS = ["+", "-", "*", "/"]
PAREN_OPEN = "PARENTHESIS_OPEN"
PAREN_CLOSE = "PARENTHESIS_CLOSE"

class Token():
    def __init__(self, t, v):
        self.type = t
        self.val = v
    def __str__(self):
        return "Token[" + self.type + ", " + self.val + "]"

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
                tokens.append(Token("CONSTANT", constant))
                index = index + len(constant)
            elif ch in VARIABLES:
                variable = tokenize_variable(expr, index)
                tokens.append(Token("VARIABLE", variable))
                index = index + len(variable)
            elif ch in OPERATORS:
                tokens.append(Token("OPERATOR", ch))
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
