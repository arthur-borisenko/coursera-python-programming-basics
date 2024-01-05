import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun('''179
20'''.splitlines(), main)
        expected_result = """-1
:2
-1
:2
:2
-1
-1
"""
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun('''1024
        1'''.splitlines(), main)
        expected_result = """:2
:2
:2
:2
:2
:2
:2
:2
:2
:2
"""
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun('''1023
        1'''.splitlines(), main)
        expected_result = """-1
:2
-1
:2
-1
:2
-1
:2
-1
:2
-1
:2
-1
:2
-1
:2
-1
:2
"""
        self.assertEqual(expected_result, value)
    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)