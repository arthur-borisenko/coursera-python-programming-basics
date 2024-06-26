import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''Hello, world!'''.splitlines(), main)
        expected_result = """world! Hello,\n"""
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun('''A B'''.splitlines(), main)
        expected_result = """B A\n"""
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun('''Q WERTYUIOP'''.splitlines(), main)
        expected_result = """WERTYUIOP Q\n"""
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
