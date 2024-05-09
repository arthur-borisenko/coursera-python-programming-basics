import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''1
-1
-2'''.splitlines(), main)
        expected_result = """2 -1 2\n"""
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun('''1
        2
        1'''.splitlines(), main)
        expected_result = """1 -1\n"""
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun('''1
-7.5
3'''.splitlines(), main).split(" ")
        expected_result = """2 0.423966 7.07603\n""".split(" ")
        epilson1 = 10 ** -6
        epilson2 = 10 ** -5
        self.assertEqual(expected_result[0], value[0])
        self.assertLessEqual(
            abs(float(expected_result[1]) - float(value[1])),
            epilson1,
            msg="float {} is not equal to {} with epilson {}".
            format(expected_result[1], value[1],
                   epilson1))
        self.assertLessEqual(
            abs(float(expected_result[2]) - float(value[2])),
            epilson2,
            msg="float {} is not equal to {} with epilson {}".
            format(expected_result[2], value[2],
                   epilson2))

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
