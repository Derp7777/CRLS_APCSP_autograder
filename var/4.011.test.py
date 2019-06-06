
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
      def test_1(self):
            self.assertEqual(could_it_be_a_martian_word('bcdefgijnpqrstuvwxyz'), [], "<br> The argument to "
                                                                                     "could_it_a_martian_word is"
                                                                                     "bebcdefgijnpqrstuvwxyz.  <br>"
                                                                                     "It should "
                                                                                     "return a BLANK LIST.  (not empty"
                                                                                     " string).<br>")
            
      def test_2(self):
            self.assertEqual(could_it_be_a_martian_word('ba'), ['a'], "<br> The argument to "
                                                                      "could_it_a_martian_word is"
                                                                      "ba.  <br>"
                                                                      "It should "
                                                                      "return ['a'].  (not a string).<br>")


      def test_3(self):
            self.assertEqual(could_it_be_a_martian_word('baa'), ['a'], "<br> The argument to "
                                                                      "could_it_a_martian_word is"
                                                                      "baa.  <br>"
                                                                      "It should "
                                                                      "return ['a'].  (not a string).<br>")


if __name__ == '__main__':
   unittest.main() 
