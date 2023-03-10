import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun(['2234','2324'], main)
        expected_result = "2\n"
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun(['123','123'], main)
        expected_result = "0\n"
        self.assertEqual(expected_result, value)
