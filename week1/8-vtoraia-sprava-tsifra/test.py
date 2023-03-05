import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):

    def test_when73_then7(self):
        value = mockAndRun(['73'], main)
        expected_result = "7\n"
        self.assertEqual(expected_result, value)

