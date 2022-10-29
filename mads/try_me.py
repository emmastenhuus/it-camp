from util.parser import tokenize, reverse_polish_notation, rpn_to_parse_tree, eval_expr, to_infix_str_and_eval_expr, derivative, derivative_reduce, to_rpn_str, to_infix_str

# Just a bunch of test functions

def fun1():
    print(to_rpn_str("sin(fact(b))"))
    print(to_rpn_str("sin(b!)"))
    print(to_rpn_str("sin(b)!")) # FIXME: This is wrong!!!
    print(to_infix_str("sin(fact(b))"))
    print(to_infix_str("sin(b!)"))
    print(to_infix_str("sin(b)!")) # FIXME: This is wrong!!!

def fun2():
    expr = "1-sin(0.3)^(1/2)*5"
    tokens = tokenize(expr)
    rpn_tokens = reverse_polish_notation(tokens)
    parse_tree = rpn_to_parse_tree(rpn_tokens)
    print(expr + " = " + parse_tree.to_infix_str())
    print(expr + " = " + parse_tree.to_rpn_str())
    print(parse_tree.evaluate())

def fun3():
    print(eval_expr("sin(7 + 7.2)"))
    print(eval_expr("4.59511/ln(4)"))
    print(eval_expr("sin(pi*2.2)"))
    print(eval_expr("inv(7)"))
    print(eval_expr("f + g * sin(x/5)", {"f" : 1, "g" : 4, "x" : 3.11}))
    print(eval_expr("e^.4"))
    print(eval_expr("exp(.4)"))
    print(reverse_polish_notation(tokenize("sin(f1+f2)!")))

def fun4():
    res = to_infix_str_and_eval_expr("e + f ^ 3", {"f" : 3})
    print(res[0] + " = " + str(res[1]))
    res = to_infix_str_and_eval_expr("i+j!", {"i" : 4, "j" : 3})
    print(res[0] + " = " + str(res[1]))

def fun5():
    res2 = to_infix_str_and_eval_expr("sin(m+n)!", {"m" : 4, "n" : 3})
    print(res2[0] + " = " + str(res2[1]))

def fun6():
    expr = "a*x-y*x*x*x*0"
    print("derivative(" + expr + ") = " + derivative(expr) + " = " + derivative_reduce(expr))
    print("derivative(" + "x*x" + ") = " + derivative("x*x") + " = " + derivative_reduce("x*x"))
    print("derivative(" + "x*x*x*x*x" + ") = " + derivative("x*x*x*x*x") + " = " + derivative_reduce("x*x*x*x*x"))

def fun7():
    # s = "sin(m)!"
    # s = "x!"
    # s = "sin(cos(x))!"
    s = "sin(cos(x)!)"
    # s = "x!*3" 
    # s = "x^2-1^3" 
    # s = "fact(x)*3" 
    toks = tokenize(s)
    rpn = reverse_polish_notation(toks)
    pt = rpn_to_parse_tree(rpn)
    res = pt.to_rpn_str()
    print(res)


# fun1()
# fun2()
# fun3()
# fun4()
# fun5()
# fun6()
fun7()


# TODO: Reduce expressions -- current implementation is very rudimentary
# TODO: Derivative -- very limited support
# TODO: Factorial -- there is something wrong with the precedence of the "!" operator (shunting yard algorithm)
# TODO: Zero solving
