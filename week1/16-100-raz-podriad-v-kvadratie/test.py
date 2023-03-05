import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun(['0'], main)
        expected_result = "0\n"
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun(['1'], main)
        expected_result = "1234567901234567901234567901234567901234567901234567901234567901234567901234567901234567901234567900987654320987654320987654320987654320987654320987654320987654320987654320987654320987654320987654321\n"
        self.assertEqual(expected_result, value)
