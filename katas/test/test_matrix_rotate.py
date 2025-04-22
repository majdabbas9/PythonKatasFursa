import unittest
from katas.matrix_rotate import rotate_matrix
def is_matrcies_equal(m1,m2):
    for i in range(len(m1)):
            for j in range(len(m1[0])):
                if m1[i][j] != m2[i][j]:
                    return False
    return True            

class TestHelloWorld(unittest.TestCase):
    def test_1(self):
        m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

        mr = [
        [7,4,1],
        [8,5,2],
        [9,6,3]]
        rotate_matrix(m)

        self.assertTrue(is_matrcies_equal(m,mr))

    def test_2(self):
        m = [[1]]

        mr = [[1]]
        rotate_matrix(m)

        self.assertTrue(is_matrcies_equal(m,mr))

    def test_3(self):
        m = [[1,2],
             [3,4]]

        mr = [[3,1],
              [4,2]]
        rotate_matrix(m)

        self.assertTrue(is_matrcies_equal(m,mr))

    def test_4(self):
        m = [[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12],
             [13,14,15,16]]

        mr = [[13,9,5,1],
              [14,10,6,2],
              [15,11,7,3],
              [16,12,8,4]]
        rotate_matrix(m)

        self.assertTrue(is_matrcies_equal(m,mr))              

                                    