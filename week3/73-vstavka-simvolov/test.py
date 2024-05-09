import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''Python'''.splitlines(), main)
        expected_result = """P*y*t*h*o*n\n"""
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun('''Hello'''.splitlines(), main)
        expected_result = """H*e*l*l*o\n"""
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun('''A'''.splitlines(), main)
        expected_result = """A\n"""
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
