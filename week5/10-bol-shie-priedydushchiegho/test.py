import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun("""1 5 2 4 3""".splitlines(), main)
        expected_result = """5 4
"""
        self.assertEqual(expected_result, value)
    def test_case2(self):
        value = mockAndRun("""1 2 3 4 5""".splitlines(), main)
        expected_result = """2 3 4 5
"""
        self.assertEqual(expected_result, value)
    def test_case3(self):
        value = mockAndRun("""5 4 3 2 1""".splitlines(), main)
        expected_result = """
"""
        self.assertEqual(expected_result, value)
    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
