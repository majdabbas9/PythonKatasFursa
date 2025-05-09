import unittest
from katas.semantic_version_comparator import compare_versions

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(compare_versions("1.0", "1.0"), 0)

    def test_2(self):
        self.assertEqual(compare_versions("1.0.0", "1"), 0)

    def test_3(self):
        self.assertEqual(compare_versions("0.1", "0.1.0.0"), 0)

    def test_4(self):
        self.assertEqual(compare_versions("1.01", "1.001"), 0)

    def test_5(self):
        self.assertEqual(compare_versions("1.0.1", "1.0.1"), 0)

    def test_6(self):
        self.assertEqual(compare_versions("1.0", "1.1"), -1)

    def test_7(self):
        self.assertEqual(compare_versions("0.1", "1.1"), -1)

    def test_8(self):
        self.assertEqual(compare_versions("1.0.0.0", "1.0.1"), -1)

    def test_9(self):
        self.assertEqual(compare_versions("1.0.2", "1.0.10"), -1)

    def test_10(self):
        self.assertEqual(compare_versions("1.10", "1.10.1"), -1)

    def test_11(self):
        self.assertEqual(compare_versions("1.0.1", "1.1"), -1)

    def test_12(self):
        self.assertEqual(compare_versions("1.0.1", "1.0.1.1"), -1)

    def test_13(self):
        self.assertEqual(compare_versions("2.0", "2.0.0.1"), -1)

    def test_14(self):
        self.assertEqual(compare_versions("1.0.33", "1.0.34"), -1)

    def test_15(self):
        self.assertEqual(compare_versions("3.2.1", "3.2.2"), -1)

    def test_16(self):
        self.assertEqual(compare_versions("1.1", "1.0"), 1)

    def test_17(self):
        self.assertEqual(compare_versions("1.1.1", "1.1"), 1)

    def test_18(self):
        self.assertEqual(compare_versions("1.10", "1.2"), 1)

    def test_19(self):
        self.assertEqual(compare_versions("2.1", "1.9.9.9.9"), 1)

    def test_20(self):
        self.assertEqual(compare_versions("1.0.1", "1"), 1)

    def test_21(self):
        self.assertEqual(compare_versions("1.1.1", "1.1.0"), 1)

    def test_22(self):
        self.assertEqual(compare_versions("1.0.0.0.1", "1"), 1)

    def test_23(self):
        self.assertEqual(compare_versions("2.0.1", "2"), 1)

    def test_24(self):
        self.assertEqual(compare_versions("4.3.2", "4.3.1.9.9"), 1)

    def test_25(self):
        self.assertEqual(compare_versions("10.0.0", "9.9.9"), 1)

    def test_26(self):
        self.assertEqual(compare_versions("1.0.0", "1"), 0)

    def test_27(self):
        self.assertEqual(compare_versions("1.0.0.0", "1.0"), 0)

    def test_28(self):
        self.assertEqual(compare_versions("1.01", "1.001"), 0)

    def test_29(self):
        self.assertEqual(compare_versions("1.0.0.0.0.0", "1"), 0)

    def test_30(self):
        self.assertEqual(compare_versions("0.0.1", "0.0.0.1"), 1)