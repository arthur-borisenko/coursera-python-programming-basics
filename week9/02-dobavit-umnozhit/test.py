import unittest
from os import system
from utils.testUtil import mockAndRun
from task import Matrix


class Test(unittest.TestCase):
    def test_case1(self):
        # Task 2 check 1
        m = Matrix([[10, 10], [0, 0], [1, 1]])
        value = m.size()
        expected_result = (3, 2)
        self.assertEqual(expected_result, value)

    def test_case2(self):
        # Task 2 check 2
        m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
        value = str(m1 + m2)
        expected_result = """1	1	0
20	1	-1
-1	-2	1"""
        self.assertEqual(expected_result, value)

    def test_case3(self):
        # Task 2 check 3
        m = Matrix([[1, 1, 0], [0, 2, 10], [10, 15, 30]])
        alpha = 15
        values = [str(m * alpha)]
        values.append(str(alpha * m))
        expected_result = """15	15	0
0	30	150
150	225	450
15	15	0
0	30	150
150	225	450"""
        self.assertEqual(expected_result, "\n".join(values))

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
