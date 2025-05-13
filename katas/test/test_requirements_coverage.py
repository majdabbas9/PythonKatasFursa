import unittest
from katas.requirements_coverage import select_minimal_test_cases

class Test(unittest.TestCase):

    def test1(self):
        test_cases = [
            [1, 2, 3],
            [1, 4],
            [2, 3, 4],
            [1, 5],
            [3, 5]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertTrue(set.union(*[set(test_cases[i]) for i in result]) == {1, 2, 3, 4, 5})
        self.assertLessEqual(len(result), 3)

    def test2(self):
        test_cases = [
            [1],
            [2],
            [3],
            [4],
            [5]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(set.union(*[set(test_cases[i]) for i in result]), {1, 2, 3, 4, 5})
        self.assertEqual(len(result), 5)

    def test3(self):
        test_cases = [
            [1, 2, 3, 4, 5]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(result, [0])

    def test4(self):
        test_cases = [
            [1, 2],
            [2, 3],
            [3, 4],
            [4, 5],
            [1, 5]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(set.union(*[set(test_cases[i]) for i in result]), {1, 2, 3, 4, 5})

    def test5(self):
        test_cases = [
            [1, 2],
            [3],
            [4],
            [5],
            [1, 3, 4, 5]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(set.union(*[set(test_cases[i]) for i in result]), {1, 2, 3, 4, 5})
        self.assertLessEqual(len(result), 2)

    def test6(self):
        test_cases = [
            [1, 2],
            [2, 3],
            [1, 3],
            [4],
            [5]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(set.union(*[set(test_cases[i]) for i in result]), {1, 2, 3, 4, 5})

    def test7(self):
        test_cases = [
            [1, 2],
            [2, 3, 4],
            [4, 5],
            [1, 5]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(set.union(*[set(test_cases[i]) for i in result]), {1, 2, 3, 4, 5})

    def test8(self):
        test_cases = [[1], [1], [1]]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(set.union(*[set(test_cases[i]) for i in result]), {1})
        self.assertEqual(len(result), 1)

    def test9(self):
        test_cases = [[1, 2], [2, 3], [1, 3]]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(set.union(*[set(test_cases[i]) for i in result]), {1, 2, 3})

    def test10(self):
        test_cases = [[1, 2, 3], [2, 3, 4], [4, 5], [5]]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(set.union(*[set(test_cases[i]) for i in result]), {1, 2, 3, 4, 5})

    def test11(self):
        test_cases = [[1], [2, 3], [3, 4], [4, 5], [5, 1]]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(set.union(*[set(test_cases[i]) for i in result]), {1, 2, 3, 4, 5})

    def test12(self):
        test_cases = [[1, 2], [3, 4], [5], [1, 3, 5]]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(set.union(*[set(test_cases[i]) for i in result]), {1, 2, 3, 4, 5})

    def test13(self):
        test_cases = [[1], [2], [3], [4], [5], [1, 2, 3, 4, 5]]
        result = select_minimal_test_cases(test_cases)
        self.assertIn(5, result)
        self.assertEqual(len(result), 1)

    def test14(self):
        test_cases = [[1, 2], [3, 4], [5], [2, 4], [1, 5]]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(set.union(*[set(test_cases[i]) for i in result]), {1, 2, 3, 4, 5})

    def test15(self):
        test_cases = [[1], [2], [3], [4, 5], [1, 5]]
        result = select_minimal_test_cases(test_cases)
        self.assertTrue({1, 2, 3, 4, 5}.issubset(set.union(*[set(test_cases[i]) for i in result])))

    def test16(self):
        test_cases = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(set.union(*[set(test_cases[i]) for i in result]), {1, 2, 3, 4, 5})

    def test17(self):
        test_cases = [[1, 2, 3], [4, 5], [2, 5]]
        result = select_minimal_test_cases(test_cases)
        self.assertIn(0, result)
        self.assertIn(1, result)

    def test18(self):
        test_cases = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(len(result), 10)

    def test19(self):
        test_cases = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(result, [0])

    def test20(self):
        test_cases = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(set.union(*[set(test_cases[i]) for i in result]), {1, 2, 3, 4, 5})

    def test21(self):
        test_cases = [[1, 2], [3], [4], [5], [2, 4], [1, 5]]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(set.union(*[set(test_cases[i]) for i in result]), {1, 2, 3, 4, 5})

    def test22(self):
        test_cases = [[1, 3], [2, 4], [3, 5], [1, 5]]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(set.union(*[set(test_cases[i]) for i in result]), {1, 2, 3, 4, 5})

    def test23(self):
        test_cases = [[1], [2], [3], [1, 2, 3]]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(result, [3])

    def test24(self):
        test_cases = [[1], [2], [3], [4], [1, 2], [3, 4]]
        result = select_minimal_test_cases(test_cases)
        self.assertLessEqual(len(result), 2)

    def test25(self):
        test_cases = [[1, 2, 3], [2, 3, 4], [4, 5, 6], [5, 6, 7], [1, 7]]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(set.union(*[set(test_cases[i]) for i in result]), {1, 2, 3, 4, 5, 6, 7})

    def test26(self):
        test_cases = [[1], [2], [3], [4], [5], [6], [1, 2, 3, 4, 5, 6]]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(result, [6])

    def test27(self):
        test_cases = [[1, 2], [3, 4], [5, 6], [1, 3, 5], [2, 4, 6]]
        result = select_minimal_test_cases(test_cases)
        self.assertLessEqual(len(result), 2)

    def test28(self):
        test_cases = [[1, 2], [2, 3], [3, 4], [1, 4]]
        result = select_minimal_test_cases(test_cases)
        self.assertLessEqual(len(result), 2)

    def test29(self):
        test_cases = [[1], [2, 3], [3, 4, 5], [1, 5]]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(set.union(*[set(test_cases[i]) for i in result]), {1, 2, 3, 4, 5})

    def test30(self):
        test_cases = [[1, 2], [3, 4], [5, 6], [7], [8, 9, 10]]
        result = select_minimal_test_cases(test_cases)
        covered = set.union(*[set(test_cases[i]) for i in result])
        self.assertEqual(covered, {1, 2, 3, 4, 5, 6, 7, 8, 9, 10})

