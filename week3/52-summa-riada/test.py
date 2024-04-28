import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''3'''.splitlines(), main)
        expected_result = """1.36111"""
        epilson=10**-5
        self.assertLess(abs(float(expected_result)-float(value)), epilson)
    def test_case2(self):
        value = mockAndRun('''2'''.splitlines(), main)
        expected_result = """1.25"""
        epilson=0
        self.assertEqual(abs(float(expected_result)-float(value)), epilson)

    def test_case3(self):
        value = mockAndRun('''1'''.splitlines(), main)
        expected_result = """1\n"""
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
