import sys
from io import StringIO
from unittest import mock


def mockAndRun(input_lines: list, method):
    with mock.patch('builtins.input', side_effect=input_lines):
        old_stdout = sys.stdout
        sys.stdout = capturedStdOut = StringIO()
        method()
        sys.stdout = old_stdout
        value = capturedStdOut.getvalue()
        return value
