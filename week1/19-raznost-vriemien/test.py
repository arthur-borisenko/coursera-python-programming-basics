import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        input = """\
1
1
1
2
2
2"""
        value = mockAndRun(input.splitlines(), main)
        expected_result = "3661\n"
        self.assertEqual(expected_result, value)