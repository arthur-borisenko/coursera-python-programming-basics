import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''1'''.splitlines(), main)
        expected_result = """1\n"""
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun('''100'''.splitlines(), main)
        expected_result = """18\n"""
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun('''10'''.splitlines(), main)
        expected_result = """9\n"""
        self.assertEqual(expected_result, value)
    def test_case4(self):
        value = mockAndRun('''101'''.splitlines(), main)
        expected_result = """19\n"""
        self.assertEqual(expected_result, value)
    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)