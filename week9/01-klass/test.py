import unittest
from os import system
from utils.testUtil import mockAndRun


def main():
    with open("task.py") as solution:
        exec(solution.read())


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun("""# Task 1 check 1
m = Matrix([[1, 0], [0, 1]])
print(m)
m = Matrix([[2, 0, 0], [0, 1, 10000]])
print(m)
m = Matrix([[-10, 20, 50, 2443], [-5235, 12, 4324, 4234]])
print(m)""".splitlines(), main)
        expected_result = """1	0
0	1
2	0	0
0	1	10000
-10	20	50	2443
-5235	12	4324	4234
"""
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun("""# Task 1 check 2
m1 = Matrix([[1, 0, 0], [1, 1, 1], [0, 0, 0]])
m2 = Matrix([[1, 0, 0], [1, 1, 1], [0, 0, 0]])
print(str(m1) == str(m2))""".splitlines(), main)
        expected_result = """True
"""
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun("""# Task 1 check 3
m = Matrix([[1, 1, 1], [0, 100, 10]])
print(str(m))""".splitlines(), main)
        expected_result = """1\t1\t1\n0\t100\t10
"""
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
