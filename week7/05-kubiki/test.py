import os.path
from os import system
import unittest
import task


def file_test(i, m):
    if not os.path.exists("input.txt"):
        open("input.txt", "x").close()
    input_file = open("input.txt", "w")
    try:
        input_file.write(i)
    finally:
        input_file.close()
    if not os.path.exists("output.txt"):
        open("output.txt", "x").close()
    output_file = open("output.txt", "r")
    try:
        m()
        result = output_file.read()
    finally:
        output_file.close()
    return result


class TestCase(unittest.TestCase):
    def test_case1(self):
        result = file_test("""4 3
0
1
10
9
1
3
0""", task.main)
        self.assertEqual(result, """2
0 1
2
9 10
1
3
""")
    def test_case2(self):
        result = file_test("""2 2
1
2
2
3""", task.main)
        self.assertEqual(result, """1
2
1
1
1
3
""")
    def test_case3(self):
        result = file_test("""0 0""", task.main)
        self.assertEqual(result, """0

0

0

""")
    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
