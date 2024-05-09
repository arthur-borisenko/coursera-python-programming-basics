import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''17.9'''.splitlines(), main)
        epilson = 10 ** -6
        expected_result = """0.9\n"""
        self.assertLessEqual(abs(float(expected_result) - float(value)),epilson)

    def test_case2(self):
        value = mockAndRun('''10.34'''.splitlines(), main)
        epilson = 10 ** -6
        expected_result = """0.34\n"""
        self.assertLessEqual(abs(float(expected_result) - float(value)),epilson)

    def test_case3(self):
        value = mockAndRun('''0.001'''.splitlines(), main)
        epilson=10**-6
        expected_result = """0.001\n"""
        self.assertLessEqual(abs(float(expected_result) - float(value)),epilson)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
