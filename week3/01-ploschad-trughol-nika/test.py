import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''3
4
5
'''.splitlines(), main)
        expected_result = """6\n"""
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun('''1
1
1'''.splitlines(), main)
        expected_result = """0.433013\n"""
        self.assertEqual(expected_result, '{0:.6f}\n'.format(float(value.replace("\n", ""))))

    def test_case3(self):
        value = mockAndRun('''5
        12
        13'''.splitlines(), main)
        expected_result = """30\n"""
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
