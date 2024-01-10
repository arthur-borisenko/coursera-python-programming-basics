import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''1
7
7
9
1
0'''.splitlines(), main)
        expected_result = """2\n"""
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun('''1
2
3
4
5
6
7
8
9
10
11
0'''.splitlines(), main)
        expected_result = """1\n"""
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun('''4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
0'''.splitlines(), main)
        expected_result = """15\n"""
        self.assertEqual(expected_result, value)
    def test_case4(self):
        value = mockAndRun('''7
        6
        5
        4
        3
        2
        1
        7
        7
        7
        8
        8
        8
        8
        7
        7
        7'''.splitlines(), main)
        expected_result = """4\n"""
        self.assertEqual(expected_result, value)
    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)