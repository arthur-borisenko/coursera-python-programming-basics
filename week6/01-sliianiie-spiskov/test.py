import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun("""1 5 7
2 4 4 5""".splitlines(), main)
        expected_result = """1 2 4 4 5 5 7
"""
        self.assertEqual(expected_result, value)
    def test_case2(self):
        value = mockAndRun("""1 4 7
1 5 6""".splitlines(), main)
        expected_result = """1 1 4 5 6 7
"""
        self.assertEqual(expected_result, value)
    def test_case3(self):
        value = mockAndRun("""1
1""".splitlines(), main)
        expected_result = """1 1
"""
        self.assertEqual(expected_result, value)
    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
