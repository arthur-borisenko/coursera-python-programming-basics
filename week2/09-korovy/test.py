import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun(['10'], main)
        expected_result = "10 korov\n"
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun(['3'], main)
        expected_result = "3 korovy\n"
        self.assertEqual(expected_result, value)
