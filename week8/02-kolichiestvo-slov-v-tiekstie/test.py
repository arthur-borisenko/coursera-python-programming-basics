import unittest
from os import system
from utils.testUtil import mockAndRun
import sys
import importlib

first_load = True


def main():
    with open("task.py") as task:
        exec(task.read())

class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun("""She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are sea shore shells.""".splitlines(), main)
        expected_result = """19
"""
        self.assertEqual(expected_result, value)

    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
