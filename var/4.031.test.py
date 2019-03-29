import random
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
      def test_draw_1(self):
            f = io.StringIO()
            with redirect_stdout(f):
                  loop1()
            loop_output = f.getvalue()
            loop_output = loop_output.rstrip()
            loop_output = loop_output.lower()
            found = re.search("\* \s \* \s \* \s \* \s \* \s \*" , loop_output,  re.X | re.M | re.S)
            self.assertTrue(found)

      def test_draw_2(self):
            f = io.StringIO()
            with redirect_stdout(f):
                  loop2()
            loop_output = f.getvalue()
            loop_output = loop_output.rstrip()
            loop_output = loop_output.lower()
            found = re.search("4 \s 5 \s 6 \s 7 \s 8 \s 9 \s 10 \s 11" , loop_output,  re.X | re.M | re.S)
            self.assertTrue(found)

      def test_draw_3(self):
            f = io.StringIO()
            with redirect_stdout(f):
                  loop3()
            loop_output = f.getvalue()
            loop_output = loop_output.rstrip()
            loop_output = loop_output.lower()
            found = re.search("1 \s  \* \s 3 \s \* \s 5 \s \* \s 7 \s \* \s 9 \s \* \s 11" , loop_output,  re.X | re.M | re.S)
            self.assertTrue(found)

      def test_draw_4(self):
            f = io.StringIO()
            with redirect_stdout(f):
                  loop4()
            loop_output = f.getvalue()
            loop_output = loop_output.rstrip()
            loop_output = loop_output.lower()
            found = re.search("\* \s \* \s \* \s \* \s \* \s \* \s* \n 
                               \* \s \* \s \* \s \* \s \* \s \* \s* \n 
                               \* \s \* \s \* \s \* \s \* \s \* \s* \n 
                               \* \s \* \s \* \s \* \s \* \s \* \s* \n 
                               \* \s \* \s \* \s \* \s \* \s \* \s* \n 
                               \* \s \* \s \* \s \* \s \* \s \* \s* \n " , loop_output,  re.X | re.M | re.S)
            self.assertTrue(found)

      def test_draw_5(self):
            f = io.StringIO()
            with redirect_stdout(f):
                  loop5()
            loop_output = f.getvalue()
            loop_output = loop_output.rstrip()
            loop_output = loop_output.lower()
            found = re.search("2 \s 3 \s 4 \s 5 \s 6 \s 7 \s* \n 2 \s 3 \s 4 \s 5 \s 6 \s 7 \s* \n 2 \s 3 \s 4 \s 5 \s 6 \s 7 \s* \n 2 \s 3 \s 4 \s 5 \s 6 \s 7 \s* \n  2 \s 3 \s 4 \s 5 \s 6 \s 7 \s* \n 2 \s 3 \s 4 \s 5 \s 6 \s 7\s* " , loop_output,  re.X | re.M | re.S)
            self.assertTrue(found)
            
      def test_draw_6(self):
            f = io.StringIO()
            with redirect_stdout(f):
                  loop6()
            loop_output = f.getvalue()
            loop_output = loop_output.rstrip()
            loop_output = loop_output.lower()
            found = re.search("1-1 \s 1-2 \s 1-3 \s 1-4 \s 1-5 \s 1-6 \s* \n 2-1 \s 2-2 \s 2-3 \s 2-4 \s 2-5 \s 2-6 \s* \n 3-1 \s 3-2 \s 3-3 \s 3-4 \s 3-6 \s 3-6 \s* \n 4-1 \s 4-2 \s 4-3 \s 4-4 \s 4-5 \s 4-6 \s* \n  5-1 \s 5-2 \s 5-3 \s 5-4 \s 5-5 \s 5-6 \s* \n 6-1 \s 6-2 \s 6-3 \s 6-4 \s 6-5 \s 6-6 \s*" , loop_output,  re.X | re.M | re.S)
            self.assertTrue(found)
            
      def test_draw_7(self):
            f = io.StringIO()
            with redirect_stdout(f):
                  loop7()
            loop_output = f.getvalue()
            loop_output = loop_output.rstrip()
            loop_output = loop_output.lower()
            found = re.search("1 \s* \n 1 \s 2 \s* \n 1 \s 2 \s 3 \s* \n 1 \s 2 \s 3 \s 4 \s* \n  1 \s 2 \s 3 \s 4 \s 5 \s* \n 1 \s 2 \s 3 \s 4 \s 5 \s 6 \s* " , loop_output,  re.X | re.M | re.S)
            self.assertTrue(found)

      def test_draw_8(self):
            f = io.StringIO()
            with redirect_stdout(f):
                  loop8()
            loop_output = f.getvalue()
            loop_output = loop_output.rstrip()
            loop_output = loop_output.lower()
            found = re.search("\* \s* \n \* \s 2 \s* \n \* \s 2 \s \* \s* \n \* \s 2 \s \* \s 4 \s* \n  \* \s 2 \s 3\* \s 4 \s \* \s* \n \* \s 2 \s \* \s 4 \s \* \s 6 \s* " , loop_output,  re.X | re.M | re.S)
            self.assertTrue(found)

            
            
if __name__ == '__main__':
   unittest.main() 
