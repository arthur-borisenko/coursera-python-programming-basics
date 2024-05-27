import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun("""3
Hello Hi
Bye Goodbye
List Array
Goodbye""".splitlines(), main)
        expected_result = """Bye
"""
        self.assertEqual(expected_result, value)
    def test_case2(self):
        value = mockAndRun("""1
beep Car
Car""".splitlines(), main)
        expected_result = """beep
"""
        self.assertEqual(expected_result, value)
    def test_case3(self):
        value = mockAndRun("""2
Ololo Ololo
Numbers 1234567890
Numbers""".splitlines(), main)
        expected_result = """1234567890
"""
        self.assertEqual(expected_result, value)
    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
