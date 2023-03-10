import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_when42_then4(self):
        value = mockAndRun(['42'], main)
        expected_result = "4\n"
        self.assertEqual(expected_result, value)
