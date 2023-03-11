import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):
    def test_case1(self):
        value = mockAndRun("""1
        1
        2
        """.splitlines(), main)
        expected_result = "1 1 2\n"
        self.assertEqual(expected_result, value)

    def test_case2(self):
        value = mockAndRun(['13',
                            '12',
                            '1'], main)
        expected_result = "1 12 13\n"
        self.assertEqual(expected_result, value)
