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
        result = file_test("""hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme""", task.main)
        self.assertEqual(result, """damme
is
name
van
bond
claude
hi
my
james
jean
what
your
""")
    def test_case2(self):
        result = file_test("""oh you touch my tralala
mmm my ding ding dong""", task.main)
        self.assertEqual(result, """ding
my
dong
mmm
oh
touch
tralala
you
""")
    def test_case3(self):
        result = file_test("""ai ai ai ai ai ai ai ai ai ai""", task.main)
        self.assertEqual(result, """ai
""")
    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
