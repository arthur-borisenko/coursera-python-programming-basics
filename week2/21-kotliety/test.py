import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''1
5
1
'''.splitlines(), main)
        expected_result = "10\n"
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun('''1
2
5'''.splitlines(), main)
        expected_result = "20\n"
        self.assertEqual(expected_result, value)
    def test_case3(self):
        value = mockAndRun('''7
1
11
'''.splitlines(), main)
        expected_result = "4\n"
        self.assertEqual(expected_result, value)
    def test_case4(self):
        value = mockAndRun('''7
1
9
'''.splitlines(), main)
        expected_result = "3\n"
        self.assertEqual(expected_result, value)
    def test_case5(self):
        value = mockAndRun('''2
1
3
'''.splitlines(), main)
        expected_result = "3\n"
        self.assertEqual(expected_result, value)
    def test_pep8(self):
        value=system("python -m pycodestyle --first task.py")
        self.assertIs(value,0)

