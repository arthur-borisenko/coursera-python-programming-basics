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
        result = file_test("""10
1 2 3 4 5
2 4 6 8 10
HELP""", task.main)
        self.assertEqual(result, """NO
YES
6 8 10
""")
    def test_case2(self):
        result = file_test("""10
1
2
3
4
5
6
7
8
9
HELP""", task.main)
        self.assertEqual(result, """NO
NO
NO
NO
NO
NO
NO
NO
NO
10
""")
    def test_case3(self):
        result = file_test("""16
1 2 3 4 5 6 7 8
9 10 11 12
13 14
16
HELP""", task.main)
        self.assertEqual(result, """NO
NO
NO
NO
15
""")
    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
