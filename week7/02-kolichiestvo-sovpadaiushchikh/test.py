import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun("""1 3 2
4 3 2""".splitlines(), main)
        expected_result = """2
"""
        self.assertEqual(expected_result, value)
    def test_case2(self):
        value = mockAndRun("""1 2 6 4 5 7
10 2 3 4 8""".splitlines(), main)
        expected_result = """2
"""
        self.assertEqual(expected_result, value)
    def test_case3(self):
        value = mockAndRun("""1 7 3 8 10 2 5
6 5 2 8 4 3 7""".splitlines(), main)
        expected_result = """5
"""
        self.assertEqual(expected_result, value)
    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
