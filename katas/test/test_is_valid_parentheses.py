import unittest
from katas.is_valid_parentheses import is_valid_parentheses


class TestIsValidParentheses(unittest.TestCase):

    def test_case1(self):
        self.assertTrue(is_valid_parentheses("()[]{}"))

    def test_case2(self):
        self.assertFalse(is_valid_parentheses("(]"))

    def test_case3(self):
        self.assertFalse(is_valid_parentheses("([)]"))

    def test_case4(self):
        self.assertTrue(is_valid_parentheses("{[]()}"))

    def test_case5(self):
        self.assertTrue(is_valid_parentheses("(((((({{{{[[[]]]}}}}))))))"))

    def test_case6(self):
        s = "({[]})" * 10000
        self.assertTrue(is_valid_parentheses(s))

    def test_case7(self):
        s = "({[]})" * 9999 + "("
        self.assertFalse(is_valid_parentheses(s))

    def test_case8(self):
        s = "({[]})" * 5000 + "([)]" + "({[]})" * 5000
        self.assertFalse(is_valid_parentheses(s))

    def test_case9(self):
        s = "(" * 10000
        self.assertFalse(is_valid_parentheses(s))

    def test_case10(self):
        s = "({[]})" * 1000 + "(]" + "({[]})" * 1000
        self.assertFalse(is_valid_parentheses(s))
