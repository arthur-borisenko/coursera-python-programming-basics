import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun(['3602'], main)
        expected_result = "1:00:02\n"
        self.assertEqual(expected_result, value)
    def test_case2(self):
        value = mockAndRun(['0'], main)
        expected_result = "0:00:00\n"
        self.assertEqual(expected_result, value)
    def test_case3(self):
        value = mockAndRun(['86401'], main)
        expected_result = "0:00:01\n"
        self.assertEqual(expected_result, value)
    def test_case4(self):
        value = mockAndRun(['36610'], main)
        expected_result = "10:10:10\n"
        self.assertEqual(expected_result, value)