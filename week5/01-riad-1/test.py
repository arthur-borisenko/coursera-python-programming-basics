import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun("""1
10""".splitlines(), main)
        expected_result = """1 2 3 4 5 6 7 8 9 10
"""
        self.assertEqual(expected_result, value)
    def test_case2(self):
        value = mockAndRun("""-3
14""".splitlines(), main)
        expected_result = """-3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
"""
        self.assertEqual(expected_result, value)
    def test_case3(self):
        value = mockAndRun("""0
0""".splitlines(), main)
        expected_result = """0
"""
        self.assertEqual(expected_result, value)
    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
