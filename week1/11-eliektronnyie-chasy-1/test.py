import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):

    def test_case1(self):
        value = mockAndRun(['150'], main)
        expected_result = "2 30\n"
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun(['90'], main)
        expected_result = "1 30\n"
        self.assertEqual(expected_result, value)

    def test_case3(self):
        value = mockAndRun([str(24*60+1)], main)
        expected_result = "0 1\n"
        self.assertEqual(expected_result, value)
