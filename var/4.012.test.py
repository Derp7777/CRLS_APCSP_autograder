
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
      def test_1(self):
            self.assertEqual(samuel_l_algorithm('Birdman or (The Unexpected Virtue of Ignorance)'), 'bad',
                             "<br> If argument to samuel_l_algorithm is "
                             "'Birdman or (The Unexpected Virtue of Ignorance)', <br>"
                             "function should return 'bad'.<br>")
            
      def test_2(self):
            self.assertEqual(samuel_l_algorithm('Snakes on a plane'), 'good',
                             "<br> If argument to csamuel_l_algorithm is 'Snakes on a plane',<br> function should "
                             "return 'good'.<br>")


      def test_3(self):
            self.assertEqual(samuel_l_algorithm('aladdin'), 'maybe',
                             "<br> If argument to samuel_l_algorithm is 'aladdin',  <br>  function should "
                             "return 'maybe'. <br>")


if __name__ == '__main__':
   unittest.main() 
