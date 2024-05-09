import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''2.3'''.splitlines(), main)
        expected_result = """2\n"""
        self.assertEqual(value, expected_result)
    def test_case2(self):
        value = mockAndRun('''2.5'''.splitlines(), main)
        expected_result = """3\n"""
        self.assertEqual(value, expected_result)

    def test_case3(self):
        value = mockAndRun('''2.7'''.splitlines(), main)
        expected_result = """3\n"""
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
