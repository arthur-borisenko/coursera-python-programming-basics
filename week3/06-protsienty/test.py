import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''12
179
0'''.splitlines(), main)
        expected_result = """200 48\n"""
        self.assertEqual(value, expected_result)
    def test_case2(self):
        value = mockAndRun('''13
179
0'''.splitlines(), main)
        expected_result = """202 27\n"""
        self.assertEqual(value, expected_result)

    def test_case3(self):
        value = mockAndRun('''10
100
0'''.splitlines(), main)
        expected_result = """110 0\n"""
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
