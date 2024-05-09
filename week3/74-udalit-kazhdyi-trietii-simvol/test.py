import os.path
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
        result = file_test("Python", task.main)
        self.assertEqual(result, "yton")

    def test_case2(self):
        result = file_test("Hello", task.main)
        self.assertEqual(result, "elo")

    def test_case3(self):
        result = file_test("qwer", task.main)
        self.assertEqual(result, "we")
    def test_pep8(self):
        os.system("python -m pycodestyle --first task.py")

if __name__ == '__main__':
    unittest.main()
