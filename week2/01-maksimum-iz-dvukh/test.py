import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun(['123456','654321'], main)
        expected_result = "654321\n"
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun(['8888','11111'], main)
        expected_result = "11111\n"
        self.assertEqual(expected_result, value)
