import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):

    def test_when3_14_then2(self):
        value = mockAndRun(['3', '14'], main)
        expected_result = "2\n"
        self.assertEqual(expected_result, value)


if __name__ == '__main__':
    unittest.main()
