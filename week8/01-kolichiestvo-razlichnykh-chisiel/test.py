import unittest
from os import system
from utils.testUtil import mockAndRun
import sys
import importlib

first_load = True


def main():
    global first_load
    if not first_load:
        importlib.reload(sys.modules['task'])
    if first_load:
        import task
        first_load = False


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun("""1 2 3 2 1""".splitlines(), main)
        expected_result = """3
"""
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun("""1 2 3 4 5 6 7 8 9 10""".splitlines(),
                           main)
        expected_result = """10
"""
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun("""1 2 3 4 5 1 2 1 2 7 3""".splitlines(),
                           main)
        expected_result = """6
"""
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
