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
        value = mockAndRun("""10
1""".splitlines(), main)
        expected_result = """10 9 8 7 6 5 4 3 2 1
"""
        self.assertEqual(expected_result, value)
    def test_case3(self):
        value = mockAndRun("""179
179""".splitlines(), main)
        expected_result = """179
"""
        self.assertEqual(expected_result, value)
    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
