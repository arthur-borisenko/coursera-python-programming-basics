import unittest
from os import system
from utils.testUtil import mockAndRun
from task import *


class Test(unittest.TestCase):
    def test_case1(self):
        values = []
        m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
        values.append(str(m1 + m2))

        m2 = Matrix([[0, 1, 0], [20, 0, -1]])
        try:
            m = m1 + m2
        except MatrixError as e:
            values.append(str(e.matrix1))
            values.append(str(e.matrix2))
        expected_result = """1	1	0
20	1	-1
-1	-2	1
1	0	0
0	1	0
0	0	1
0	1	0
20	0	-1"""
        self.assertEqual(expected_result, "\n".join(values))

    def test_case2(self):
        values = []
        # Task 3 check 2
        m = Matrix([[10, 10], [0, 0], [1, 1]])
        values.append(str(m))
        m1 = m.transpose()
        values.append(str(m))
        values.append(str(m1))
        expected_result = """10	10
0	0
1	1
10	0	1
10	0	1
10	0	1
10	0	1"""
        self.assertEqual(expected_result, "\n".join(values))

    def test_case3(self):
        values = []
        # Task 3 check 3
        m = Matrix([[10, 10], [0, 0], [1, 1]])
        values.append(str(m))
        values.append(str(Matrix.transposed(m)))
        values.append(str(m))
        expected_result = """10	10
0	0
1	1
10	0	1
10	0	1
10	10
0	0
1	1"""
        self.assertEqual(expected_result, "\n".join(values))

    def test_case4(self):
        values = []
        # Task 3 check 3
        m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
        values.append(str(Matrix.transposed(m2)))
        expected_result = """0\t20\t-1
1\t0\t-2
0\t-1\t0"""
        self.assertEqual(expected_result, "\n".join(values))

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
