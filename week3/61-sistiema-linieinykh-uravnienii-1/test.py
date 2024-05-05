import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''1
0
0
1
3
3'''.splitlines(), main)
        expected_result = """3 3\n"""
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun('''1
2
3
4
-1
-1'''.splitlines(), main)
        expected_result = """1 -1\n"""
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun('''3
5
4
4
11
12'''.splitlines(), main).split(" ")
        expected_result = """2 1\n""".split(" ")
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
