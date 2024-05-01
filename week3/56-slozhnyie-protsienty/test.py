import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''12
179
0
5'''.splitlines(), main)
        expected_result = """315 43\n"""
        self.assertEqual(value, expected_result)
    def test_case2(self):
        def test_case1(self):
            value = mockAndRun('''13
179
0
100'''.splitlines(), main)
            expected_result = """36360285 50\n"""
            self.assertEqual(value, expected_result)

    def test_case3(self):
        value = mockAndRun('''1
        1
        0
        1000'''.splitlines(), main)
        expected_result = """11881 92\n"""
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
