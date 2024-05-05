import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


def assertIsFloatEqual(self: unittest.TestCase, a, b, eps=1e-6, msg=None):
    self.assertLess(abs(a - b), eps, msg=msg)


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''1
0.000
1.000
1.000'''.splitlines(), main)
        expected_result = """1\n"""
        self.assertEqual(value, expected_result)

    def test_case2(self):
        value = mockAndRun('''2
0.500
1.000
1.000
1.000'''.splitlines(), main)
        expected_result = """1.75\n"""
        self.assertEqual(value, expected_result)

    def test_case3(self):
        value = float(mockAndRun('''5
7.100
1.000
2.000
3.000
4.000
5.000
6.000'''.splitlines(), main))
        expected_result = 24441.5
        assertIsFloatEqual(self, value, expected_result, eps=1e-1)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
