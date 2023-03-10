import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun(['3','3','5','1'], main)
        expected_result = "YES\n"
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun(['3','3','-5','1'], main)
        expected_result = "NO\n"
        self.assertEqual(expected_result, value)
