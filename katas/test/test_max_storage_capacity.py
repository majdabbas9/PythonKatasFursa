import unittest
from katas.max_storage_capacity import max_storage_area


class TestLargestRectangleArea(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(max_storage_area([2, 1, 5, 6, 2, 3]), 10)

    def test_case2(self):
        self.assertEqual(max_storage_area([2, 4]), 4)

    def test_case3(self):
        self.assertEqual(max_storage_area([1, 1, 1, 1]), 4)

    def test_case4(self):
        self.assertEqual(max_storage_area([6, 2, 5, 4, 5, 1, 6]), 12)

    def test_case5(self):
        self.assertEqual(max_storage_area([1]), 1)

    def test_case6(self):
        self.assertEqual(max_storage_area([100]), 100)

    def test_case7(self):
        self.assertEqual(max_storage_area([1, 2, 3, 4, 5]), 9)

    def test_case8(self):
        self.assertEqual(max_storage_area([5, 4, 3, 2, 1]), 9)

    def test_case9(self):
        self.assertEqual(max_storage_area([2, 1, 2]), 3)

    def test_case10(self):
        self.assertEqual(max_storage_area([0, 1, 0, 1]), 1)

    def test_case11(self):
        self.assertEqual(max_storage_area([2, 1, 2, 3, 1]), 5)

    def test_case12(self):
        self.assertEqual(max_storage_area([2, 3, 2, 1, 2]), 6)

    def test_case13(self):
        self.assertEqual(max_storage_area([1, 2, 3, 2, 1]), 6)

    def test_case14(self):
        self.assertEqual(max_storage_area([1, 2, 2, 2, 1]), 6)

    def test_case15(self):
        self.assertEqual(max_storage_area([]), 0)

    def test_case16(self):
        self.assertEqual(max_storage_area([0]), 0)

    def test_case17(self):
        self.assertEqual(max_storage_area([1, 0, 1]), 1)

    def test_case18(self):
        self.assertEqual(max_storage_area([3, 3, 3, 3]), 12)

    def test_case19(self):
        self.assertEqual(max_storage_area([1, 2, 3, 4, 5, 6]), 12)

    def test_case20(self):
        self.assertEqual(max_storage_area([6, 5, 4, 3, 2, 1]), 12)

    def test_case21(self):
        self.assertEqual(max_storage_area([2, 1, 4, 5, 1, 3, 3]), 8)

    def test_case22(self):
        self.assertEqual(max_storage_area([3, 6, 5, 7, 4, 8, 1, 0]), 20)

    def test_case23(self):
        self.assertEqual(max_storage_area([2] * 100), 200)

    def test_case24(self):
        self.assertEqual(max_storage_area(list(range(1, 101))), 2550)

    def test_case25(self):
        self.assertEqual(max_storage_area(list(range(100, 0, -1))), 2550)

    def test_case26(self):
        self.assertEqual(max_storage_area([1] * 10000), 10000)

    def test_case27(self):
        self.assertEqual(max_storage_area([0, 0, 0, 0]), 0)

    def test_case28(self):
        self.assertEqual(max_storage_area([2, 2, 2, 1, 2, 2, 2]), 7)

    def test_case29(self):
        self.assertEqual(max_storage_area([1, 3, 2, 1, 2]), 5)

    def test_case30(self):
        self.assertEqual(max_storage_area([4, 2, 0, 3, 2, 5]), 6)
