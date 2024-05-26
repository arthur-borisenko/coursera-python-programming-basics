import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun("""10
1 2 3 4 5
YES
2 4 6 8 10
NO
HELP""".splitlines(), main)
        expected_result = """1 3 5
"""
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun("""10
1 2 3 4 5 6 7 8 9 10
YES
1
NO
2
NO
3
NO
4
NO
6
NO
7
NO
8
NO
9
NO
10
NO
HELP""".splitlines(), main)
        expected_result = """5
"""
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun("""100
1 2 3 4 5 6 7 8 9 10
NO
HELP""".splitlines(), main)
        expected_result = """11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100
"""

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
