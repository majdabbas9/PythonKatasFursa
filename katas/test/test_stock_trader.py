import unittest
from katas.stock_trader import max_profit  # adjust the path to your module

class TestMaxProfit(unittest.TestCase):

    def test_case1(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(max_profit(prices), 5)

    def test_case2(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(max_profit(prices), 0)

    def test_case3(self):
        prices = [1, 2, 3, 4, 5]
        self.assertEqual(max_profit(prices), 4)

    def test_case4(self):
        prices = [3, 3, 3, 3, 3]
        self.assertEqual(max_profit(prices), 0)

    def test_case5(self):
        prices = [5, 10, 1, 100]
        self.assertEqual(max_profit(prices), 99)

    def test_case6(self):
        prices = [100, 180, 260, 310, 40, 535, 695]
        self.assertEqual(max_profit(prices), 655)

    def test_case7(self):
        prices = [1]
        self.assertEqual(max_profit(prices), 0)

    def test_case8(self):
        prices = []
        self.assertEqual(max_profit(prices), 0)

    def test_case9(self):
        prices = [2, 4, 1]
        self.assertEqual(max_profit(prices), 2)

    def test_case10(self):
        prices = [3, 2, 6, 1, 3]
        self.assertEqual(max_profit(prices), 4)

if __name__ == '__main__':
    unittest.main()
