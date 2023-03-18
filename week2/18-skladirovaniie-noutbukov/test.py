import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun(['300','100','200','1','2','3'], main)
        expected_result = "1000000\n"
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun(['100','100','1','2','2','2'], main)
        expected_result = "0\n"
        self.assertEqual(expected_result, value)
