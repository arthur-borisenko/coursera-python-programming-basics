import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):

    def test_when73_then7(self):
        value = mockAndRun(['Harry'], main)
        expected_result = "Hello, Harry!\n"
        self.assertEqual(expected_result, value)