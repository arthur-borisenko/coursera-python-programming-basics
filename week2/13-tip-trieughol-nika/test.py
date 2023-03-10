import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun(['3','4','5'], main)
        expected_result = "rectangular\n"
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun(['3','5','4'], main)
        expected_result = "rectangular\n"
        self.assertEqual(expected_result, value)
    def test_case3(self):
        value = mockAndRun(['10','10','20'], main)
        expected_result = "impossible\n"
        self.assertEqual(expected_result, value)
    def test_case4(self):
        value = mockAndRun(['10','10','00'], main)
        expected_result = "impossible\n"
        self.assertEqual(expected_result, value)
