import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun(['700','750'], main)
        expected_result = "2\n"
        self.assertEqual(expected_result, value)

