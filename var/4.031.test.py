import random
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
    def test_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            loop1()
        loop_output = f.getvalue().rstrip().lower()
        print(loop_output)
        found = re.search(r"\* \s \* \s \* \s \* \s \* \s \* ", loop_output, re.X | re.M | re.S)
        self.assertTrue(found, r'Looked for this: r"\* \s \* \s \* \s \* \s \* \s \*" <br>'
                               'In this string: <br> ' + loop_output)

    def test_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            loop2()
        loop_output = f.getvalue().rstrip().lower()
        found = re.search("4 \s 5 \s 6 \s 7 \s 8 \s 9 \s 10 \s 11", loop_output, re.X | re.M | re.S)
        self.assertTrue(found, r'Looked for this: r"4 \s 5 \s 6 \s 7 \s 8 \s 9 \s 10 \s 11" <br>'
                               'In this string: <br>' + loop_output)

    def test_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            loop3()
        loop_output = f.getvalue().rstrip().lower()
        found = re.search("1 \s  \* \s 3 \s \* \s 5 \s \* \s 7 \s \* \s 9 \s \* \s 11", loop_output,
                          re.X | re.M | re.S)
        self.assertTrue(found, r'Looked for this: r"1 \s  \* \s 3 \s \* \s 5 \s \* \s 7 \s \* \s 9 \s \* \s 11" '
                               r'<br>'
                               r'In this string: <br> ' + loop_output)

    def test_4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            loop4()
        loop_output = f.getvalue().rstrip().lower()
        found = re.search(r"\* \s \* \s \* \s \* \s \* \s \* \s* \n "
                          r"\* \s \* \s \* \s \* \s \* \s \* \s* \n "
                          r"\* \s \* \s \* \s \* \s \* \s \* \s* \n "
                          r"\* \s \* \s \* \s \* \s \* \s \* \s* \n "
                          r"\* \s \* \s \* \s \* \s \* \s \* \s* \n "
                          r"\* \s \* \s \* \s \* \s \* \s \* \s* ", loop_output, re.X | re.M | re.S)
        self.assertTrue(found, r'Looked for this: r"\* \s \* \s \* \s \* \s \* \s \* \s* \n '
                               r' \* \s \* \s \* \s \* \s \* \s \* \s* \n '
                               r'\* \s \* \s \* \s \* \s \* \s \* \s* \n '
                               r' \* \s \* \s \* \s \* \s \* \s \* \s* \n '
                               r'\* \s \* \s \* \s \* \s \* \s \* \s* \n '
                               r'\* \s \* \s \* \s \* \s \* \s \* \s* \n "" <br>'
                               'In this string: <br>' + loop_output)

    def test_5(self):
        f = io.StringIO()
        with redirect_stdout(f):
            loop5()
        loop_output = f.getvalue().rstrip().lower()
        found = re.search(r"2 \s 3 \s 4 \s 5 \s 6 \s 7 \s* \n 2 \s 3 \s 4 \s 5 \s 6 \s 7 \s* \n 2 \s 3 \s 4 \s 5 "
                          r"\s 6 \s 7 \s* \n 2 \s 3 \s 4 \s 5 \s 6 \s 7 \s* \n  2 \s 3 \s 4 \s 5 \s 6 \s 7 \s* \n"
                          r" 2 \s 3 \s 4 \s 5 \s 6 \s 7\s* ", loop_output, re.X | re.M | re.S)
        self.assertTrue(found, r'Looked for this: 2 \s 3 \s 4 \s 5 \s 6 \s 7 \s* \n 2 \s 3 \s 4 \s 5 \s 6 \s 7 \s*'
                               r' \n 2 \s 3 \s 4 \s 5 \s 6 \s 7 \s* \n 2 \s 3 \s 4 \s 5 \s 6 \s 7 \s* \n  '
                               r'2 \s 3 \s 4 \s 5 \s 6 \s 7 \s* \n 2 \s 3 \s 4 \s 5 \s 6 \s 7\s* <br>'
                               r'In this string: <br>' + loop_output)

    def test_6(self):
        f = io.StringIO()
        with redirect_stdout(f):
            loop6()
        loop_output = f.getvalue().rstrip().lower()
        found = re.search(r"1-1 \s 1-2 \s 1-3 \s 1-4 \s 1-5 \s 1-6 \s* \n 2-1 \s 2-2 \s 2-3 \s 2-4 \s 2-5 \s 2-6 "
                          r"\s* \n 3-1 \s 3-2 \s 3-3 \s 3-4 \s 3-5 \s 3-6 \s* \n 4-1 \s 4-2 \s 4-3 \s 4-4 "
                          r"\s 4-5 \s 4-6 \s* \n  5-1 \s 5-2 \s 5-3 \s 5-4 \s 5-5 \s 5-6 \s* \n 6-1 \s"
                          r" 6-2 \s 6-3 \s 6-4 \s 6-5 \s 6-6 \s*", loop_output, re.X | re.M | re.S)
        self.assertTrue(found, r'Looked for this: 1-1 \s 1-2 \s 1-3 \s 1-4 \s 1-5 \s 1-6 \s* \n '
                               r'2-1 \s 2-2 \s 2-3 \s 2-4 \s 2-5 \s 2-6 \s* \n '
                               r'3-1 \s 3-2 \s 3-3 \s 3-4 \s 3-6 \s 3-6 \s* \n '
                               r'4-1 \s 4-2 \s 4-3 \s 4-4 \s 4-5 \s 4-6 \s* \n '
                               r' 5-1 \s 5-2 \s 5-3 \s 5-4 \s 5-5 \s 5-6 \s* \n '
                               r'6-1 \s 6-2 \s 6-3 \s 6-4 \s 6-5 \s 6-6 \s* <br>'
                               r' In this string: <br> ' + loop_output)

    def test_7(self):
        f = io.StringIO()
        with redirect_stdout(f):
            loop7()
        loop_output = f.getvalue().rstrip().lower()
        found = re.search(r"1 \s* \n "
                          r"1 \s 2 \s* \n "
                          r"1 \s 2 \s 3 \s* \n "
                          r"1 \s 2 \s 3 \s 4 \s* \n  "
                          r"1 \s 2 \s 3 \s 4 \s 5 \s* \n "
                          r"1 \s 2 \s 3 \s 4 \s 5 \s 6 \s* ", loop_output, re.X | re.M | re.S)
        self.assertTrue(found, '<br>Looked for this:<br>'
                               r"1 \s* \n "
                               r"1 \s 2 \s* \n "
                               r"1 \s 2 \s 3 \s* \n "
                               r"1 \s 2 \s 3 \s 4 \s* \n  "
                               r"1 \s 2 \s 3 \s 4 \s 5 \s* \n "
                               r"1 \s 2 \s 3 \s 4 \s 5 \s 6 \s* <br>"
                               r"In this string: <br>" + loop_output, )

    def test_8(self):
        f = io.StringIO()
        with redirect_stdout(f):
            loop8()
        loop_output = f.getvalue().rstrip().lower()
        found = re.search(r"\* \s* \n "
                          r"\* \s 2 \s* \n "
                          r"\* \s 2 \s \* \s* \n "
                          r"\* \s 2 \s \* \s 4 \s* \n "
                          r"\* \s 2 \s \* \s 4 \s \* \s* \n "
                          r"\* \s 2 \s \* \s 4 \s \* \s 6 \s* ", loop_output, re.X | re.M | re.S)
        self.assertTrue(found, 'Looked for this:  <br>'
                               r"\* \s* \n "
                               r"\* \s 2 \s* \n "
                               r"\* \s 2 \s \* \s* \n "
                               r"\* \s 2 \s \* \s 4 \s* \n "
                               r"\* \s 2 \s \* \s 4 \s \* \s* \n "
                               r"\* \s 2 \s \* \s 4 \s \* \s 6 \s* <br> "
                               r"In this string: <br> " + loop_output)


if __name__ == '__main__':
    unittest.main()
