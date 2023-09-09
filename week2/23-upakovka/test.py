import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''2
2
3
3
3
3
3
5
3'''.splitlines(), main)
        expected_result = "YES\n"
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun('''2
3
3
3
2
3
4
4
4'''.splitlines(), main)
        expected_result = "YES\n"
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun('''4
1
2
3
3
2
4
3
4'''.splitlines(), main)
        expected_result = "YES\n"
        self.assertEqual(expected_result, value)

    def test_case4(self):
        value = mockAndRun('''1
1
4
1
1
3
10
10
3'''.splitlines(), main)
        expected_result = "NO\n"
        self.assertEqual(expected_result, value)

    def test_case5(self):
        value = mockAndRun('''3
2
2
3
1
2
5
2
3'''.splitlines(), main)
        expected_result = "NO\n"
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
