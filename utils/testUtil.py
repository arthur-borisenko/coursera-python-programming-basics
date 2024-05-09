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


def fileTest(input_file_name, output_file_name, input_text, method):
    try:
        open(input_file_name, "x").close()
    finally:
        input_file = open(input_file_name, "w")
        input_file.write(input_text)
    method()
    try:
        open(output_file_name).close()
    finally:
        f = open(output_file_name, "r")
        output = f.read()
        return output
