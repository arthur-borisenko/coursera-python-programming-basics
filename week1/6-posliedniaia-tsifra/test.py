import unittest

from task import main
from utils.testUtil import mockAndRun


class Test(unittest.TestCase):

    def test_when179_then9(self):
        value = mockAndRun(['179'], main)
        expected_result = "9\n"
        self.assertEqual(expected_result, value)


if __name__ == '__main__':
    unittest.main()
