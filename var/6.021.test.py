import random
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
      def test_martinez_1(self):
            martinez_list = ['Goku', 'Goku', 'Goku', 'Goku', 'Goku']
            self.assertEqual(martinez_dictionary(martinez_list), {'Goku': 500})

            
      def test_martinez_2(self):
            martinez_list = ['Goku', 'Goku', 'Trunks', 'Vegeta', 'Vegeta', 'Krillan', 'Goku']
            self.assertEqual(martinez_dictionary(martinez_list), {'Goku': 300, 'Trunks': 100, 'Vegeta':200, 'Krillan':100})

            
      def test_martinez_3(self):
            names = ['Brolly', 'Goku', 'Gohan', 'Piccolo', 'Vegeta' ]
            answer1 = data_generator(names, 20)
            answer2 = data_generator(names, 20)
            self.assertNotEqual(answer1, answer2)

      def test_martinez_4(self):
            names = ['Brolly', 'Goku', 'Gohan', 'Piccolo', 'Vegeta' ]
            answer = data_generator(names, 100)
            success = False
            if 'Brolly' in answer and 'Goku' in answer and 'Gohan' in answer and 'Piccolo' in answer and 'Vegeta' in answer:
                  success = True
            self.assertEqual(True, success)

if __name__ == '__main__':
   unittest.main() 
