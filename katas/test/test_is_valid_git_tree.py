import unittest
from katas.is_valid_git_tree import is_valid_git_tree
class Test(unittest.TestCase):
    def test_1(self):
        tree = {"A": ["B", "C"], "B": [], "C": []}
        self.assertTrue(is_valid_git_tree(tree))

    def test_2(self):
        tree = {"A": ["B"], "B": ["C"], "C": ["A"]}
        self.assertFalse(is_valid_git_tree(tree))

    def test_3(self):
        tree = {"A": ["B"], "B": ["C"], "C": ["D"], "D": []}
        self.assertTrue(is_valid_git_tree(tree))

    def test_4(self):
        tree = {"A": ["B"], "C": ["D"], "B": [], "D": []}
        self.assertFalse(is_valid_git_tree(tree))

    def test_5(self):
        tree = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": []}
        self.assertTrue(is_valid_git_tree(tree))

    def test_6(self):
        tree = {"A": ["B"], "B": ["C"], "C": ["A", "D"], "D": []}
        self.assertFalse(is_valid_git_tree(tree))

    def test_7(self):
        tree = {"A": ["B"], "B": ["C"], "C": ["D"], "D": ["E"], "E": []}
        self.assertTrue(is_valid_git_tree(tree))

    def test_8(self):
        tree = {"A": ["B"], "B": [], "C": ["D"], "D": []}
        self.assertFalse(is_valid_git_tree(tree))

    def test_9(self):
        tree = {"A": ["B", "C"], "B": [], "C": ["A"]}
        self.assertFalse(is_valid_git_tree(tree))

    def test_10(self):
        tree = {"A": []}
        self.assertTrue(is_valid_git_tree(tree))

    def test_11(self):
        tree = {"A": ["B"], "B": ["C"], "C": ["D"], "D": ["A"]}
        self.assertFalse(is_valid_git_tree(tree))

    def test_12(self):
        tree = {"A": ["B"], "B": ["C"], "C": []}
        self.assertTrue(is_valid_git_tree(tree))

    def test_13(self):
        tree = {"A": ["B"], "B": ["C"], "C": [], "D": []}
        self.assertFalse(is_valid_git_tree(tree))

    def test_14(self):
        tree = {"A": ["B", "C", "D"], "B": [], "C": [], "D": []}
        self.assertTrue(is_valid_git_tree(tree))

    def test_15(self):
        tree = {"A": ["B"], "B": ["C"], "C": ["D"], "D": [], "E": ["F"], "F": []}
        self.assertFalse(is_valid_git_tree(tree))

    def test_16(self):
        tree = {"A": ["B"], "B": ["C"], "C": ["D", "E"], "D": [], "E": []}
        self.assertTrue(is_valid_git_tree(tree))

    def test_17(self):
        tree = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
        self.assertTrue(is_valid_git_tree(tree))

    def test_18(self):
        tree = {"A": ["B"], "B": ["C"], "C": ["A"]}
        self.assertFalse(is_valid_git_tree(tree))

    def test_19(self):
        tree = {}
        self.assertFalse(is_valid_git_tree(tree))

    def test_20(self):
        tree = {"A": []}
        self.assertTrue(is_valid_git_tree(tree))

    def test_21(self):
        tree = {"A": ["B"], "B": ["C"], "C": ["D"], "D": ["E"], "E": ["F"], "F": ["G"], "G": ["H"], "H": ["I"],
                "I": ["J"], "J": []}
        self.assertTrue(is_valid_git_tree(tree))

    def test_22(self):
        tree = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": ["A"]}
        self.assertFalse(is_valid_git_tree(tree))

    def test_23(self):
        tree = {"A": ["B"], "B": ["C"], "C": ["D"], "D": [], "X": []}
        self.assertFalse(is_valid_git_tree(tree))

    def test_24(self):
        tree = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": ["F"], "E": ["F"], "F": []}
        self.assertTrue(is_valid_git_tree(tree))

    def test_25(self):
        tree = {"root": ["child"], "child": ["leaf"], "leaf": []}
        self.assertTrue(is_valid_git_tree(tree))

    def test_26(self):
        tree = {"1": ["2"], "2": ["3"], "3": ["4"], "4": ["1"]}
        self.assertFalse(is_valid_git_tree(tree))

    def test_27(self):
        tree = {"root": ["A", "B"], "A": ["C", "D"], "B": ["E"], "C": [], "D": [], "E": []}
        self.assertTrue(is_valid_git_tree(tree))

    def test_28(self):
        tree = {"A": ["B"], "B": ["C"], "C": [], "D": ["E"], "E": []}
        self.assertFalse(is_valid_git_tree(tree))

    def test_29(self):
        tree = {"A": ["B"], "B": [], "C": []}
        self.assertFalse(is_valid_git_tree(tree))

    def test_30(self):
        tree = {"A": ["B"], "B": ["C"], "C": ["A"]}
        self.assertFalse(is_valid_git_tree(tree))
