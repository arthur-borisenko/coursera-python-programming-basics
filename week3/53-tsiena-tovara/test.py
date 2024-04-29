import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''10.35'''.splitlines(), main)
        expected_result = """10 35\n"""
        self.assertEqual(value, expected_result)
    def test_case2(self):
        def test_case1(self):
            value = mockAndRun('''1.99'''.splitlines(), main)
            expected_result = """1 99\n"""
            self.assertEqual(value, expected_result)

    def test_case3(self):
        value = mockAndRun('''3.50'''.splitlines(), main)
        expected_result = """3 50\n"""
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
