import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):

    def test_case1(self):
        value = mockAndRun(['10','15','2'], main)
        expected_result = "20 30\n"
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun(['2','50','4'], main)
        expected_result = "10 0\n"
        self.assertEqual(expected_result, value)

