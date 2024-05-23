import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun("""4
1 2 6 10
2
7 3""".splitlines(), main)
        expected_result = """2 2 1 1
"""
        self.assertEqual(expected_result, value)
    def test_case2(self):
        value = mockAndRun("""1
1
1
2""".splitlines(), main)
        expected_result = """1
"""
        self.assertEqual(expected_result, value)
    def test_case3(self):
        value = mockAndRun("""10
79 64 13 8 38 29 58 20 56 17
10
53 19 20 85 82 39 58 46 51 69""".splitlines(), main)
        expected_result = """5 10 2 2 6 3 7 3 7 2
"""
        self.assertEqual(expected_result, value)
    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
