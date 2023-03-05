import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun(['7'], main)
        expected_result = "8\n"
        self.assertEqual(expected_result, value)
    def test_case2(self):
        value = mockAndRun(['8'], main)
        expected_result = "10\n"
        self.assertEqual(expected_result, value)
