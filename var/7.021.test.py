import random
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
      def test_atwood_1(self):
            leia = Collectible('Leia action figure', 'poor', 400)
            attribute_dict = vars(leia)
            attributes = []
            retrieved_value = -99999
            value_key = ''
            retrieved_string1 = ''
            attr2 = ''
            retrieved_string2 = ''
            attr3 = ''
            for key in attribute_dict:
                  if isinstance(getattr(leia, key), int):
                        retrieved_value = attribute_dict[key]
                        value_key = key
                  else:
                        if retrieved_string1 != '':
                              retrieved_string1 = getattr(leia, key)
                              attr2 = key
                        else:
                              retrieved_stirng2 = getattr(leia, key)
                              attr3 = key
            success = False
            if getattr(leia, value_key) == 400 and ( getattr(leia,attr2) == 'Leia action figure' and getattr(leia,attr3)=='poor' or \
                                                     getattr(leia,attr3) == 'Leia action figure' and getattr(leia,attr2)=='poor')
                  success = True
            self.assertEqual(True, success)
            

      def test_atwood_2(self):
            leia = Collectible('Leia action figure', 'poor', 400)
            rey = Collectible('Rey in her racer', 'new', 30)
            collectibles = [leia, rey]
            output = collectible_printer(collectibles)
            search_object = re.search(r"Leia \s action \ figure", output, re.X| re.M | re.S)
            search_object2 = re.search(r"Rey \s in \s her \ racer", output, re.X| re.M | re.S)
            self.assertEqual(True, search_object and search_object2)

      def test_atwood_3(self):
            leia = Collectible('Leia action figure', 'poor', 400)
            rey = Collectible('Rey in her racer', 'new', 30)
            collectibles = [leia, rey]
            output = collectible_printer(collectibles)
            search_object = re.search(r"50", output, re.X| re.M | re.S)
            self.assertEqual(True, search_object)

            

if __name__ == '__main__':
   unittest.main() 
