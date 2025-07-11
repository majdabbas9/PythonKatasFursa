import unittest
import io
import sys
from katas.curcular_buffer import CircularBuffer
def test_func(n):
    buffer = CircularBuffer(3)
    output = []
    if n == 1:
        output.append(buffer.is_empty())
        output.append(buffer.get())
    elif n == 2:
        buffer.add(1)
        buffer.add(2)
        buffer.add(3)
        output.append(buffer.get())  # 1
        output.append(buffer.get())  # 2
        output.append(buffer.get())  # 3
        output.append(buffer.get())  # -1
    elif n == 3:
        buffer.add(1)
        buffer.add(2)
        buffer.add(3)
        buffer.add(4)  # overwrites 1
        output.append(buffer.get())  # 2
    elif n == 4:
        buffer.add(1)
        buffer.add(2)
        buffer.get()
        buffer.get()
        output.append(buffer.is_empty())  # True
    elif n == 5:
        buffer.add(1)
        buffer.add(2)
        buffer.add(3)
        output.append(buffer.is_full())  # True
    elif n == 6:
        buffer.add(1)
        buffer.get()
        buffer.add(2)
        buffer.add(3)
        buffer.add(4)
        output.append(buffer.get())  # 2
        output.append(buffer.get())  # 3
        output.append(buffer.get())  # 4
    elif n == 7:
        buffer.add(1)
        buffer.add(2)
        buffer.add(3)
        buffer.get()
        buffer.get()
        buffer.add(4)
        buffer.add(5)
        output.append(buffer.get())  # 3
        output.append(buffer.get())  # 4
        output.append(buffer.get())  # 5
    elif n == 8:
        output.append(buffer.is_full())  # False
        buffer.add(10)
        output.append(buffer.is_empty())  # False
    elif n == 9:
        buffer.add(1)
        buffer.add(2)
        buffer.get()
        buffer.get()
        buffer.add(3)
        output.append(buffer.get())  # 3
    elif n == 10:
        buffer.add(1)
        buffer.add(2)
        buffer.add(3)
        buffer.add(4)
        buffer.add(5)
        output.append(buffer.get())  # 3
        output.append(buffer.get())  # 4
        output.append(buffer.get())  # 5
        output.append(buffer.get())  # -1

    return output, output.copy()
class Test(unittest.TestCase):
    def test1(self):
        captured_output, str_test = test_func(1)
        self.assertEqual(captured_output, str_test)

    def test2(self):
        captured_output, str_test = test_func(2)
        self.assertEqual(captured_output, str_test)

    def test3(self):
        captured_output, str_test = test_func(3)
        self.assertEqual(captured_output, str_test)

    def test4(self):
        captured_output, str_test = test_func(4)
        self.assertEqual(captured_output, str_test)

    def test5(self):
        captured_output, str_test = test_func(5)
        self.assertEqual(captured_output, str_test)

    def test6(self):
        captured_output, str_test = test_func(6)
        self.assertEqual(captured_output, str_test)

    def test7(self):
        captured_output, str_test = test_func(7)
        self.assertEqual(captured_output, str_test)

    def test8(self):
        captured_output, str_test = test_func(8)
        self.assertEqual(captured_output, str_test)

    def test9(self):
        captured_output, str_test = test_func(9)
        self.assertEqual(captured_output, str_test)

    def test10(self):
        captured_output, str_test = test_func(10)
        self.assertEqual(captured_output, str_test)

if __name__ == '__main__':
    unittest.main()
