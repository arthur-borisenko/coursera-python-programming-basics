import unittest
from os import system
from utils.testUtil import mockAndRun


def main():
    with open('task.py') as solution:
        exec(solution.read())
class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun("""1 1 1 2""".splitlines(), main)
        expected_result = """32
"""
        self.assertEqual(expected_result, value)
    def test_case2(self):
        value = mockAndRun("""2 1 1 2 2""".splitlines(), main)
        expected_result = """32768
"""
        self.assertEqual(expected_result, value)
    def test_case3(self):
        value = mockAndRun("""10 100 1000 10000 2""".splitlines(), main)
        expected_result = """3200000000000000000000000000000000000000000000000000
"""
        self.assertEqual(expected_result, value)
    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
