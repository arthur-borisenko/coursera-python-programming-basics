import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''1
7
9
0'''.splitlines(), main)
        epilson = 10 ** -11
        expected_result = """4.16333199893\n"""
        self.assertLessEqual(abs(float(expected_result) - float(value)),epilson)

    def test_case2(self):
        value = mockAndRun('''1
2
3
0'''.splitlines(), main)
        epilson = 10 ** -6
        expected_result = """1.0\n"""
        self.assertLessEqual(abs(float(expected_result) - float(value)),epilson)

    def test_case3(self):
        value = mockAndRun('''1
1
1
1
1
1
1
1
1
1
0
'''.splitlines(), main)
        epilson=10**-6
        expected_result = """0.0\n"""
        self.assertLessEqual(abs(float(expected_result) - float(value)),epilson)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
