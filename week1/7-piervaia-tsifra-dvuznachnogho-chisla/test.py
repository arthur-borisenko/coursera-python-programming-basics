import unittest

import utils.testUtil
from task import main


class Test(unittest.TestCase):
    def test_when42_then4(self):
        value = utils.tester.mockAndRun(['42'], main)
        expected_result = "4\n"
        self.assertEqual(expected_result, value)


if __name__ == '__main__':
    unittest.main()
