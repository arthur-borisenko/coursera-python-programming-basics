import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun("""1
2
3
0""".splitlines(), main)
        expected_result = """0
3
2
1
"""
        self.assertEqual(expected_result, value)
    def test_case2(self):
        value = mockAndRun("""8
7
2
3
1
4
5
0""".splitlines(), main)
        expected_result = """0
5
4
1
3
2
7
8
"""
        self.assertEqual(expected_result, value)
    def test_case3(self):
        value = mockAndRun("""1
0""".splitlines(), main)
        expected_result = """0
1
"""
        self.assertEqual(expected_result, value)
    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
