import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun(['1','1','2','2'], main)
        expected_result = "YES\n"
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun(['1','1','3','3'], main)
        expected_result = "YES\n"
        self.assertEqual(expected_result, value)
    def test_case3(self):
        value = mockAndRun(['1','1','2','3'], main)
        expected_result = "NO\n"
        self.assertEqual(expected_result, value)
