import unittest
from katas.stock_trader_v2 import max_profit  # adjust the import path as needed

class TestMaxProfitMultipleTransactions(unittest.TestCase):

    def test_case1(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(max_profit(prices), 7)

    def test_case2(self):
        prices = [1, 2, 3, 4, 5]
        self.assertEqual(max_profit(prices), 4)

    def test_case3(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(max_profit(prices), 0)

    def test_case4(self):
        prices = [1, 2, 1, 2, 1, 2]
        self.assertEqual(max_profit(prices), 3)

    def test_case5(self):
        prices = [5, 4, 3, 2, 1]
        self.assertEqual(max_profit(prices), 0)

    def test_case6(self):
        prices = [1, 5, 3, 8, 4, 9]
        self.assertEqual(max_profit(prices), 14)

    def test_case7(self):
        prices = [1]
        self.assertEqual(max_profit(prices), 0)

    def test_case8(self):
        prices = []
        self.assertEqual(max_profit(prices), 0)

    def test_case9(self):
        prices = [2, 1, 2, 0, 1]
        self.assertEqual(max_profit(prices), 2)

    def test_case10(self):
        prices = [3, 3, 5, 0, 0, 3, 1, 4]
        self.assertEqual(max_profit(prices), 8)

if __name__ == '__main__':
    unittest.main()
