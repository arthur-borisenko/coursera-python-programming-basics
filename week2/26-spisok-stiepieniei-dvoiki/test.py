import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''50'''.splitlines(), main)
        expected_result = "1 2 4 8 16 32\n"
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun('''10'''.splitlines(), main)
        expected_result = "1 2 4 8\n"
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun('''8'''.splitlines(), main)
        expected_result = "1 2 4 8\n"
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
