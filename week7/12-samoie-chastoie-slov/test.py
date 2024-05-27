import os.path
from os import system
import unittest
import task


def file_test(i, m):
    if not os.path.exists("input.txt"):
        open("input.txt", "x").close()
    input_file = open("input.txt", "w")
    try:
        input_file.write(i)
    finally:
        input_file.close()
    if not os.path.exists("output.txt"):
        open("output.txt", "x").close()
    output_file = open("output.txt", "r")
    try:
        m()
        result = output_file.read()
    finally:
        output_file.close()
    return result


class TestCase(unittest.TestCase):
    def test_case1(self):
        result = file_test("""apple orange banana banana orange""", task.main)
        self.assertEqual(result, """banana
""")
    def test_case2(self):
        result = file_test("""oh you touch my tralala mmm my ding ding dong""", task.main)
        self.assertEqual(result, """ding
""")
    def test_case3(self):
        result = file_test("""q w e r t y u i o p
a s d f g h j k l
z x c v b n m""", task.main)
        self.assertEqual(result, """a
""")
    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
