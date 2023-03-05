import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun(['60','2'], main)
        expected_result = "11\n"
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun(['-1','2'], main)
        expected_result = "107\n"
        self.assertEqual(expected_result, value)
