
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
      def test_could_it_be_a_martian_word_1(self):
            self.assertEqual(could_it_be_a_martian_word('bcdefgijnpqrstuvwxyz'), [])
            
      def test_could_it_be_a_martian_word_2(self):
            self.assertEqual(could_it_be_a_martian_word('ba'), ['a'])


      def test_could_it_be_a_martian_word_3(self):
            self.assertEqual(could_it_be_a_martian_word('baa'), ['a'])


if __name__ == '__main__':
   unittest.main() 
