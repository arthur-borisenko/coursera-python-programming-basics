import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):

    def test_when3_14_then4(self):
        value = mockAndRun(['3', '14'], main)
        expected_result = "4\n"
        self.assertEqual(expected_result, value)