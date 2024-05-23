import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''3
Ivanov 15
Petrov 10
Sidorov 20'''.splitlines(), main)
        expected_result = """Sidorov
Ivanov
Petrov\n"""
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun('''3
Ivanov 15
Petrov 20
Sidorov 10'''.splitlines(), main)
        expected_result = """Petrov
Ivanov
Sidorov\n"""
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun('''3
Ivanov 10
Petrov 15
Sidorov 20'''.splitlines(), main)
        expected_result = """Sidorov
Petrov
Ivanov\n"""
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
