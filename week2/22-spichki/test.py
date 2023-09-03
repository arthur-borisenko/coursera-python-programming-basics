import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''0
2
4
5
3
6'''.splitlines(), main)
        expected_result = "1\n"
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun('''1
2
9
10
12
20'''.splitlines(), main)
        expected_result = "3\n"
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun('''1
5
0
1
4
8'''.splitlines(), main)
        expected_result = "0\n"
        self.assertEqual(expected_result, value)

    def test_case4(self):
        value = mockAndRun('''10
15
0
1
4
8'''.splitlines(), main)
        expected_result = "1\n"
        self.assertEqual(expected_result, value)

    def test_case5(self):
        value = mockAndRun('''10
15
0
10
4
8'''.splitlines(), main)
        expected_result = "0\n"
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
