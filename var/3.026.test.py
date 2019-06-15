
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
      def test_1(self):
            self.assertEqual(return_min([-1, 3, 5, 99]), -1,
                             "<br>With a list of -1, 3, 5, 99, function should return -1.  <br>")
            
      def test_2(self):
            self.assertEqual(return_min([-1, 3, 5, -99]), -99,
                             "<br>With  a list of -1, 3, 5, -99, function should return -99. <br>")

      def test_3(self):
            self.assertEqual(return_min([5]), 5,  "<br>With  a list of -5, function should return 5. <br>")

      def test_4(self):
            self.assertEqual(return_min([5, 4, 99, -11, 44, -241, -444, 999, 888, -2]), -444,
                             "<br>With  a list of 5, 4, 99, -11, 44, -241, -444, 999, 888, and -2, function  should "
                             "return -444.  <br>")


if __name__ == '__main__':
   unittest.main() 
