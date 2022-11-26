import unittest
from tokenizer import Token, Variable, tokenize, tokenize_constant, tokens2rpn, rpn2nodes

class TestTokenizer(unittest.TestCase):

    def test_0010_dummy(self):
        x = [2, 5, 6, 8]
        self.assertEqual(4, len(x))

    def test_0020_token(self):
        a = Token("CONSTANT", "17")
        self.assertEqual("Token[CONSTANT, 17]", str(a))

    def test_0030_empty(self):
        tokens = tokenize("")
        self.assertEqual(0, len(tokens))
        tokens = tokenize(None)
        self.assertEqual(0, len(tokens))
        tokens = tokenize("         ")
        self.assertEqual(0, len(tokens))

    def test_0040_constant(self):
        tokens = tokenize("  65  ")
        self.assertEqual(1, len(tokens))
        t0 = tokens[0]
        self.assertEqual("CONSTANT", t0.type)
        self.assertEqual("65", t0.val)

    def test_0050_constant(self):
        self.assertEqual("6.7", tokenize_constant("  6.7abcsdf", 2))
        self.assertEqual("", tokenize_constant("  6.7abcsdf", 6))
        self.assertEqual("", tokenize_constant("  6.7abcsdf", 56))
        self.assertEqual("4.8", tokenize_constant(" abcsdf 4.8", 8))
        self.assertEqual("119.4", tokenize_constant("119.4 abcsdf 4.8", 0))

    def test_0060_expr(self):
        tokens = tokenize("  x  *3.14159   ")
        self.assertEqual(3, len(tokens))

        t0 = tokens[0]
        self.assertEqual("VARIABLE", t0.type)
        self.assertEqual("x", t0.val)
        
        t1 = tokens[1]
        self.assertEqual("OPERATOR", t1.type)
        self.assertEqual("*", t1.val)
        
        t2 = tokens[2]
        self.assertEqual("CONSTANT", t2.type)
        self.assertEqual("3.14159", t2.val)

    def test_0070_expr(self):
        tokens = tokenize(" 4 * ( x+ 19.7) / 8 +   b")
        self.assertEqual(11, len(tokens))
        self.assertEqual("PARENTHESIS_CLOSE", tokens[6].type)

    def test_0080_rpn(self):
        tokens = tokenize("7 + 2")
        rpn = tokens2rpn(tokens)
        self.assertEqual(3, len(rpn))
        self.assertEqual("7", rpn[0].val)
        self.assertEqual("2", rpn[1].val)
        self.assertEqual("+", rpn[2].val)

        tokens = tokenize("7 + 2 - 5 + 1")
        rpn = tokens2rpn(tokens)
        self.assertEqual(7, len(rpn))
        self.assertEqual("7", rpn[0].val)
        self.assertEqual("2", rpn[1].val)
        self.assertEqual("+", rpn[2].val)
        self.assertEqual("5", rpn[3].val)
        self.assertEqual("-", rpn[4].val)
        self.assertEqual("1", rpn[5].val)
        self.assertEqual("+", rpn[6].val)

        tokens = tokenize("7 + 2 / 5")
        rpn = tokens2rpn(tokens)
        self.assertEqual(5, len(rpn))
        self.assertEqual("7", rpn[0].val)
        self.assertEqual("2", rpn[1].val)
        self.assertEqual("5", rpn[2].val)
        self.assertEqual("/", rpn[3].val)
        self.assertEqual("+", rpn[4].val)

    def test_0090_syntax_tree(self):
        tokens = tokenize("7 + 2 / 5 * 8 - 9 + x / b")
        self.assertEqual(13, len(tokens))
        rpn = tokens2rpn(tokens)
        self.assertEqual(13, len(rpn))
        nodes = rpn2nodes(rpn)
        self.assertEqual(1, len(nodes))
        # print(nodes[0])
        self.assertEqual("(((7+((2/5)*8))-9)+(x/b))", str(nodes[0]))

    def test_0100_syntax_tree(self):
        rpn = tokenize("a b c * +")
        nodes = rpn2nodes(rpn)
        self.assertEqual(1, len(nodes))
        self.assertEqual("(a+(b*c))", str(nodes[0]))

    def test_0110_stack(self):
        l = [3, 8, 1, 9]
        self.assertEqual(9, l.pop())
        self.assertEqual(1, l.pop())
        self.assertEqual(8, l.pop())
        self.assertEqual(3, l.pop())
        self.assertEqual(0, len(l))

    def test_0120_syntax_tree(self):
        tokens = tokenize("(a + b) * c")
        self.assertEqual(7, len(tokens))
        rpn = tokens2rpn(tokens)
        self.assertEqual(5, len(rpn))
        nodes = rpn2nodes(rpn)
        self.assertEqual(1, len(nodes))
        self.assertEqual("((a+b)*c)", str(nodes[0]))

    def test_0130_syntax_tree(self):
        tokens = tokenize("7 + 2 / (5 * 8 - 9 + x) / b")
        self.assertEqual(15, len(tokens))
        rpn = tokens2rpn(tokens)
        self.assertEqual(13, len(rpn))
        nodes = rpn2nodes(rpn)
        self.assertEqual(1, len(nodes))
        syntax_tree = nodes[0]
        self.assertEqual("(7+((2/(((5*8)-9)+x))/b))", str(syntax_tree))
        dict = {"b": 2, "x": 4}
        self.assertAlmostEqual(7.0285714, syntax_tree.evaluate(dict))

    def test_0140_syntax_tree(self):
        tokens = tokenize("a / b")
        rpn = tokens2rpn(tokens)
        nodes = rpn2nodes(rpn)
        syntax_tree = nodes[0]
        dict = {"a": 2, "b": 5}
        self.assertAlmostEqual(0.4, syntax_tree.evaluate(dict))
        
    def test_0150_variable_node(self):
        v1 = Variable("a")
        self.assertEqual("0", str(v1.derivative("x")))
        v2 = Variable("x")
        self.assertEqual("1", str(v2.derivative("x")))

    def test_0160_variable_node(self):
        tokens = tokenize("2 * x + x * x")
        rpn = tokens2rpn(tokens)
        nodes = rpn2nodes(rpn)
        expr = nodes[0]
        print(expr)
        d = expr.derivative("x")
        print(d)
        (r1, b1) = d.reduce()
        print(r1)
        # print(d.reduce().reduce())

    def test_0170_reduce(self):
        tokens = tokenize("2+0 + x")
        rpn = tokens2rpn(tokens)
        nodes = rpn2nodes(rpn)
        expr = nodes[0]
        (r, b) = expr.reduce()
        self.assertEqual("(2+x)", str(r))
        self.assertFalse(b)

    def test_0180_reduce(self):
        expr = rpn2nodes(tokens2rpn(tokenize("((b*2)*(x*(0*x*8+6*(30444+22)*0))")))[0]
        (r, b) = expr.reduce()
        self.assertEqual("0", str(r))

if __name__ == "__main__":
    unittest.main()