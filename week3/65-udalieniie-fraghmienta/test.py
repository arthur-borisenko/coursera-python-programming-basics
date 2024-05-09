import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''In the hole in the ground there lived a hobbit'''.splitlines(), main)
        expected_result = """In tobbit\n"""
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun('''qwertyhasdfghzxcvb'''.splitlines(), main)
        expected_result = """qwertyzxcvb\n"""
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun('''asdfghhzxcvb'''.splitlines(), main)
        expected_result = """asdfgzxcvb\n"""
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
