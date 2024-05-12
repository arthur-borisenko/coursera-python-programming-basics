import unittest
from os import system
from utils.testUtil import mockAndRun
from task import main

class Test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(mockAndRun([],main),"36\n")
    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
