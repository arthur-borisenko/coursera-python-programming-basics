import unittest
from os import system
from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun("""3""".splitlines(), main)
        expected_result = """+___ +___ +___ 
|1 / |2 / |3 / 
|__\\ |__\\ |__\\ 
|    |    |    
"""
        self.assertEqual(expected_result, value)
    def test_case2(self):
        value = mockAndRun("""1""".splitlines(), main)
        expected_result = """+___ 
|1 / 
|__\\ 
|    
"""
        self.assertEqual(expected_result, value)
    def test_case3(self):
        value = mockAndRun("""2""".splitlines(), main)
        expected_result = """+___ +___ 
|1 / |2 / 
|__\\ |__\\ 
|    |    
"""
        self.assertEqual(expected_result, value)
    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
