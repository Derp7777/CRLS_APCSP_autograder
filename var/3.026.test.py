
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
      def test_1(self):
            self.assertEqual(return_min([-1, 3, 5, 99]), -1)
            
      def test_2(self):
            self.assertEqual(return_min([-1, 3, 5, -99]), -99)

      def test_3(self):
            self.assertEqual(return_min([5]), 5)

      def test_4(self):
            self.assertEqual(return_min([5, 4, 99, -11, 44, -241, -444, 999, 888, -2]), -444)


if __name__ == '__main__':
   unittest.main() 
