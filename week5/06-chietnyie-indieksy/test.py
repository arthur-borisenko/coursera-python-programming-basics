import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun("""1 2 3 4 5""".splitlines(), main)
        expected_result = """1 3 5
"""
        self.assertEqual(expected_result, value)
    def test_case2(self):
        value = mockAndRun("""4 5 3 4 2 3""".splitlines(), main)
        expected_result = """4 3 2
"""
        self.assertEqual(expected_result, value)
    def test_case3(self):
        value = mockAndRun("""9 4 5 2 3""".splitlines(), main)
        expected_result = """9 5 3
"""
        self.assertEqual(expected_result, value)
    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
