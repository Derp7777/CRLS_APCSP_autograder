import random
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
      def test_mcglathery_1(self):
            mcglathery_dict = {}
            self.assertEqual(add(mcglathery_dict, 'fire', 'charmander'), {'fire':['charmander']})

      def test_mcglathery_2(self):
            mcglathery_dict = {'fire':'charmander', 'ice','iceperson'}
            self.assertEqual(add(mcglathery_dict, 'ice', 'iceperson2'), {'fire':['charmander'], 'ice':['iceperson','iceperson2']})
            
      def test_mcglathery_3(self):
            mcglathery_dict = {'fire':['charmander']}
            answer = get(mcglathery_dict, 'fire')
            search_object = re.search(r"charmander", answer, re.X| re.M | re.S)             
            self.assertEqual(True, search_object)

      def test_mcglather_4(self):
            mcglathery_dict = {'fire':['charmander', 'fireperson']}
            answer = get(mcglathery_dict, 'fire')
            search_object = re.search(r"charmander", answer, re.X| re.M | re.S)
            search_object2 = re.search(r"fireperson", answer, re.X| re.M | re.S)             
            self.assertEqual(True, search_object and search_object2)

if __name__ == '__main__':
   unittest.main() 
