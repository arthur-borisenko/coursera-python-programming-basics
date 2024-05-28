import unittest
from os import system
from utils.testUtil import mockAndRun


def run():
    with open("task.py") as solution:
        exec(solution.read())


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun("""3
4
19
14""".splitlines(), run)
        expected_result = """False
"""
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun("""7
8
8
8
12
12
11
28""".splitlines(), run)
        expected_result = """False
"""
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun("""7
0
20
9
14
5
29
4""".splitlines(), run)
        expected_result = """True
"""
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
