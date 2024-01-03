import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''2
1
4
0'''.splitlines(), main)
        expected_result = "2\n"
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun('''2
4
0'''.splitlines(), main)
        expected_result = "2\n"
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun('''1
3
5
7
9
1
3
5
7
9
0'''.splitlines(), main)
        expected_result = "0\n"
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
