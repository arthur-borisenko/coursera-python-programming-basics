import unittest
from os import system
from utils.testUtil import mockAndRun
from task import *


class Test(unittest.TestCase):
    def test_case1(self):
        values = []
        # Task 5 check 1
        m = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        values.append(str(m.solve([1, 1, 1])))
        expected_result = """[1.0, 1.0, 1.0]"""
        self.assertEqual(expected_result, "\n".join(values))

    def test_case2(self):
        values = []
        m = Matrix([[1, 1, 1], [0, 2, 0], [0, 0, 4]])
        values.append(str(m.solve([1, 1, 1])))
        expected_result = """[0.25, 0.5, 0.25]"""
        self.assertEqual(expected_result, "\n".join(values))

    def test_case3(self):
        values = []
        # Task 5 check 3
        m = Matrix([[1, 1, 1], [0, 1, 2], [0.5, 1, 1.5]])
        try:
            s = m.solve([1, 1, 1])
            values.append('WA No solution')
        except Exception as e:
            values.append('OK')

        expected_result = """OK"""
        self.assertEqual(expected_result, "\n".join(values))

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
