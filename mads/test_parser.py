import unittest
from util.parser import to_infix_str, to_rpn_str, eval_expr

class Test(unittest.TestCase):

    def test_fact(self):
        self.assertEqual(eval_expr("1*2*3*4*5*6*7"), eval_expr("fact(7)"))
        self.assertEqual(eval_expr("1*2*3*4*5*6*7"), eval_expr("fact(b)", {"b" : 7}))

    def test_infix_str(self):
        self.assertEqual("a + b", to_infix_str("a+b"))
        self.assertEqual("a!", to_infix_str("a  !"))
        self.assertEqual("sin(x) ^ b", to_infix_str("sin (  x)^  b"))

    def test_reverse_polish_notation_str1(self):
        self.assertEqual("x 2 ^", to_rpn_str("x^2"))
        self.assertEqual("x a sin ^", to_rpn_str("x^sin(a)"))
        self.assertEqual("b fact", to_rpn_str("b !"))
        self.assertEqual("b fact", to_rpn_str("fact(b)")) # "fact()" function and "!" operator are synonymous

    def test_reverse_polish_notation_str2(self):
        self.assertEqual("b fact sin", to_rpn_str("sin(fact(b))"))
        self.assertEqual("b fact sin", to_rpn_str("sin(b!)"))
        # self.assertEqual("b sin fact", to_rpn_str("sin(b)!")) 
        # self.assertEqual("x cos sin fact", to_rpn_str("sin(cos(x))!")) 
        # self.assertEqual("x cos fact sin", to_rpn_str("sin(cos(x)!)")) 
        # self.assertEqual("a x sin fact 3 * -", to_rpn_str("a-sin(x)!*3")) # TODO -- "fact" is fishy 

if __name__ == "__main__":
    unittest.main()