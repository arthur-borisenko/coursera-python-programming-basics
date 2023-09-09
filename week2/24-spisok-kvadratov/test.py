import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''50'''.splitlines(), main)
        expected_result = "1 4 9 16 25 36 49\n"
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun('''10'''.splitlines(), main)
        expected_result = "1 4 9\n"
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun('''9'''.splitlines(), main)
        expected_result = "1 4 9\n"
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
