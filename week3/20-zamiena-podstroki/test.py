import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''1+1=2'''.splitlines(), main)
        expected_result = """one+one=2\n"""
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun('''Hello, 2345678990'''.splitlines(), main)
        expected_result = """Hello, 2345678990\n"""
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun('''1'''.splitlines(), main)
        expected_result = """one\n"""
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
