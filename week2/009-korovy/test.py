import unittest

from task import *
from util.TestUtil import console_test


class Test(unittest.TestCase):
    def test_exam_1(self):
        console_test("""2""", lambda: run(), lambda out_text: self.assertEqual(out_text, '''2 korovy'''))

    def test_exam_2(self):
        console_test("""1""", lambda: run(), lambda out_text: self.assertEqual(out_text, '''1 korova'''))

    def test_exam_3(self):
        console_test("""3""", lambda: run(), lambda out_text: self.assertEqual(out_text, """3 korovy"""))

    def test_exam_90(self):
        console_test("""90""", lambda: run(), lambda out_text: self.assertEqual(out_text, """90 korov"""))

    def test_exam_91(self):
        console_test("""91""", lambda: run(), lambda out_text: self.assertEqual(out_text, """91 korova"""))

    def test_exam_11(self):
        console_test("""11""", lambda: run(), lambda out_text: self.assertEqual(out_text, """11 korov"""))


if __name__ == '__main__':
    unittest.main()
