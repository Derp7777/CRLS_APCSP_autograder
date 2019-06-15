
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
      def test_1(self):
            self.assertEqual(could_it_be_a_martian_word('bcdefgijnpqrstuvwxyz'), [],
                             "<br> If argument to could_it_a_martian_word is 'bebcdefgijnpqrstuvwxyz', <br>"
                             "function should return a BLANK list.  (note list, not string).<br>")
            
      def test_2(self):
            self.assertEqual(could_it_be_a_martian_word('ba'), ['a'],
                             "<br> If argument to could_it_a_martian_word is 'ba',<br> function should "
                             "return ['a'].  (note list, not string).<br>")


      def test_3(self):
            self.assertEqual(could_it_be_a_martian_word('baa'), ['a'],
                             "<br> If argument to could_it_a_martian_word is 'baa',  <br>  function should "
                             "return ['a'].  (note list, not string).<br>")


if __name__ == '__main__':
   unittest.main() 
