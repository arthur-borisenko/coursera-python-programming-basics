import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun(['2002'], main)
        expected_result = "1\n"
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun(['220'], main)
        expected_result = "1\n"
        self.assertEqual(expected_result, value)
    def test_case3(self):
        value = mockAndRun(['202'], main)
        expected_result = "0\n"
        self.assertEqual(expected_result, value)

    def test_case4(self):
        value = mockAndRun(['10'], main)
        expected_result = "0\n"
        self.assertEqual(expected_result, value)
    def test_case5(self):
        value = mockAndRun(['10001'], main)
        expected_result = "1\n"
        self.assertEqual(expected_result, value)
