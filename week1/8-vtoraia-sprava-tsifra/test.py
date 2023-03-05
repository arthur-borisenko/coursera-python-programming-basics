import sys
import unittest
from io import StringIO
from unittest import mock

from task import main


class Test(unittest.TestCase):

    @mock.patch('builtins.input', side_effect=['73'])
    def test_when73_then7(self, params):
        old_stdout = sys.stdout
        sys.stdout = capturedStdOut = StringIO()
        main()
        sys.stdout = old_stdout
        value = capturedStdOut.getvalue()
        print("Output")
        print(value)
        expected_result = "7\n"
        self.assertEqual(expected_result, value)


if __name__ == '__main__':
    unittest.main()
