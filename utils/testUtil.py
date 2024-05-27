import io
import sys, os
from io import StringIO
from unittest import mock


def mockAndRun(input_lines: list, method):
    new_stdin = io.TextIOWrapper(
        io.BytesIO(
            "\n".join(input_lines)
            .encode('utf-8')),
        encoding='utf-8')
    with mock.patch(
            'sys.stdin', new=new_stdin):
        old_stdout = sys.stdout
        sys.stdout = capturedStdOut = StringIO()
        method()
        sys.stdout = old_stdout
        value = capturedStdOut.getvalue()
        return value
