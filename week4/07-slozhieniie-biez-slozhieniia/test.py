import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''2
2'''.splitlines(), main)
        expected_result = """4\n"""
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun('''123
456'''.splitlines(), main)
        expected_result = """579\n"""
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun('''179
0'''.splitlines(), main)
        expected_result = """179\n"""
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
