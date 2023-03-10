import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun(['-10016723674556546436378373767466363565463763762726743645465346456'], main)
        expected_result = "-1\n"
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun(['0'], main)
        expected_result = "0\n"
        self.assertEqual(expected_result, value)
