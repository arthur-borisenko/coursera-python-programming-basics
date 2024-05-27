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
        result = file_test("""3
3
Russian
English
Japanese
2
Russian
English
1
English""", task.main)
        value=result.splitlines()
        a=value[0]
        b=set(value[1:2])
        c=value[2]
        d=set(value[3:])
        exp_res=("1",{"English"},"3",{"Russian","English","Japanese"})
        self.assertEqual(exp_res, (a,b,c,d))
    def test_pep8(self):
        value = system("python -m pycodestyle --first task.py")
        print(value)
        self.assertIs(value, 0)
