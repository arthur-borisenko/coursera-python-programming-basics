import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun(['179'], main)
        expected_result = "The next number for the number 179 is 180.\nThe previous number for the number 179 is 178.\n"
        self.assertEqual(expected_result, value)
