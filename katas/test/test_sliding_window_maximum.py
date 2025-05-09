import unittest
from katas.sliding_window_maximum import max_sliding_window

class TestSlidingWindowMax(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(max_sliding_window([1,3,-1,-3,5,3,6,7], 3), [3,3,5,5,6,7])

    def test_case2(self):
        self.assertEqual(max_sliding_window([1], 1), [1])

    def test_case3(self):
        self.assertEqual(max_sliding_window([1, -1], 1), [1, -1])

    def test_case4(self):
        self.assertEqual(max_sliding_window([9, 11], 2), [11])

    def test_case5(self):
        self.assertEqual(max_sliding_window([4, -2], 2), [4])

    def test_case6(self):
        self.assertEqual(max_sliding_window([1,3,1,2,0,5], 3), [3,3,2,5])

    def test_case7(self):
        self.assertEqual(max_sliding_window([1,3,1,2,0,5], 6), [5])

    def test_case8(self):
        self.assertEqual(max_sliding_window([1,3,1,2,0,5], 2), [3,3,2,2,5])

    def test_case9(self):
        self.assertEqual(max_sliding_window([1,2,3,4,5,6], 3), [3,4,5,6])

    def test_case10(self):
        self.assertEqual(max_sliding_window([6,5,4,3,2,1], 3), [6,5,4,3])

    def test_case11(self):
        self.assertEqual(max_sliding_window([1]*1000, 10), [1]*991)

    def test_case12(self):
        self.assertEqual(max_sliding_window([i for i in range(1000)], 100), [i + 99 for i in range(901)])

    def test_case13(self):
        self.assertEqual(max_sliding_window([i for i in range(1000, 0, -1)], 50), [1000 - i for i in range(951)])

    def test_case14(self):
        self.assertEqual(max_sliding_window([1,2,3,2,1,4,5,6,7,6], 4), [3,3,4,5,6,7,7])

    def test_case15(self):
        self.assertEqual(max_sliding_window([], 0), [])

    def test_case16(self):
        self.assertEqual(max_sliding_window([1,2,3], 0), [])

    def test_case17(self):
        self.assertEqual(max_sliding_window([1,2,3], 1), [1,2,3])

    def test_case18(self):
        self.assertEqual(max_sliding_window([5,5,5,5,5], 3), [5,5,5])

    def test_case19(self):
        self.assertEqual(max_sliding_window([10, 9, 8, 7, 6, 5], 2), [10,9,8,7,6])

    def test_case20(self):
        self.assertEqual(max_sliding_window([0, 1, 0, 2, 0, 3], 2), [1,1,2,2,3])

    def test_case21(self):
        self.assertEqual(max_sliding_window([1, 3, 2, 5, 4, 6], 4), [5,5,6])

    def test_case22(self):
        self.assertEqual(max_sliding_window([7, 2, 4], 2), [7, 4])

    def test_case23(self):
        self.assertEqual(max_sliding_window([9, 10, 9, -7, -4, -8, 2, -6], 5), [10, 10, 9, 2])

    def test_case24(self):
        self.assertEqual(max_sliding_window([1]*50000, 100), [1]*49901)

    def test_case25(self):
        self.assertEqual(max_sliding_window([i%10 for i in range(1000)], 50), [9]*951)

    def test_case26(self):
        self.assertEqual(max_sliding_window([-1, -2, -3, -4], 2), [-1, -2, -3])

    def test_case27(self):
        self.assertEqual(max_sliding_window([1, 1000000], 2), [1000000])

    def test_case28(self):
        self.assertEqual(max_sliding_window([1000000, 1], 2), [1000000])

    def test_case29(self):
        self.assertEqual(max_sliding_window([1,3,2,5,4,6,7,0,8], 3), [3,5,5,6,7,7,8])

    def test_case30(self):
        self.assertEqual(max_sliding_window([1]*999 + [2], 1000), [2])
