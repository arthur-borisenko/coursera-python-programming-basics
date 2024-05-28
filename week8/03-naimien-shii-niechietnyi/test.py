import unittest
from os import system
from utils.testUtil import mockAndRun


def main():
    with open("task.py") as task:
        exec(task.read())


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun("""0 1 2 3 4
""".splitlines(), main)
        expected_result = """1
"""
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun("""2 4 6 8 10 19""".splitlines(), main)
        expected_result = """19
"""
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun("""5 4 3 2 1 0 -1 -2 -3 -4
""".splitlines(), main)
        expected_result = """-3
"""
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
