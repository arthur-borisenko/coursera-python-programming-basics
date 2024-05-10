import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''1
0
0
1
3
3'''.splitlines(), main).split(" ")
        expected_result = """2 3 3\n""".split(" ")
        self.assertLess(float(expected_result[0]) - float(value[0]),
                        10 ** 0)
        self.assertLess(float(expected_result[1]) - float(value[1]),
                        10 ** 0)

    def test_case2(self):
        value = mockAndRun('''1
1
2
2
1
2'''.splitlines(), main)
        expected_result = """1 -1 1\n"""
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun('''0
2
0
4
1
2'''.splitlines(), main).split(" ")
        expected_result = """4 0.5\n""".split(" ")
        self.assertLess(float(expected_result[0]) - float(value[0]),
                        10 ** 0)
        self.assertLess(float(expected_result[1]) - float(value[1]),
                        10 ** 0)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
