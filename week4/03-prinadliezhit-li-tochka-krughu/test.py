import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''0.5
0.5
0
0
1'''.splitlines(), main)
        expected_result = """YES\n"""
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun('''0.5
0.5
1
1
0.1'''.splitlines(), main)
        expected_result = """NO\n"""
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun('''0
0
1
0
1'''.splitlines(), main)
        expected_result = """YES\n"""
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
