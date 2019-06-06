import random
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
      def test_1(self):
            kann_list = ['fantastic spaghetti', 'fantastic spaghetti', 'garlic bread', 'noodles noodles', 'noodles noodles', 'Gooey gelato', 'fantastic spaghetti']
            self.assertEqual(item_list_to_dictionary(kann_list), {'fantastic spaghetti': 3, 'garlic bread': 1, 'noodles noodles':2, 'Gooey gelato':1})

      def test_2(self):
            kann_dict =  {'fantastic spaghetti': 3, 'garlic bread': 1, 'noodles noodles':2, 'Gooey gelato':99}
            self.assertEqual(min_item(kann_dict), 'garlic bread')
            

if __name__ == '__main__':
   unittest.main() 
