import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun(['1','2','3','3','2','1'], main)
        expected_result = "Boxes are equal\n"
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun(['2','2','3','3','2','1'], main)
        expected_result = "The first box is larger than the second one\n"
        self.assertEqual(expected_result, value)
