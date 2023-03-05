import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):

    def test_when179_then17(self):
        value = mockAndRun(['179'], main)
        expected_result = "17\n"
        self.assertEqual(expected_result, value)

