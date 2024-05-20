import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun("""3 4 5 2 1""".splitlines(), main)
        expected_result = """3 4 1 2 5
"""
        self.assertEqual(expected_result, value)
    def test_case2(self):
        value = mockAndRun("""1 5 4 3 2""".splitlines(), main)
        expected_result = """5 1 4 3 2
"""
        self.assertEqual(expected_result, value)
    def test_case3(self):
        value = mockAndRun("""-30000 30000""".splitlines(), main)
        expected_result = """30000 -30000
"""
        self.assertEqual(expected_result, value)
    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
