import unittest
from os import system
from utils.testUtil import mockAndRun


def main():
    with open('task.py') as solution:
        exec(solution.read())
class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun("""0 0 1 1
0 1 0 1""".splitlines(), main)
        expected_result = """0 1 1 0
"""
        self.assertEqual(expected_result, value)
    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
