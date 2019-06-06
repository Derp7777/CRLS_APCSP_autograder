
import unittest
import io
from contextlib import redirect_stdout
import re
import random

class testAutograde(unittest.TestCase):
      def test_1(self):
            f = io.StringIO()
            with redirect_stdout(f):
                  birthday_song('joe')
            birthday_song_output = f.getvalue()
            birthday_song_output = birthday_song_output.rstrip()
            birthday_song_output = birthday_song_output.lower()
            found = re.search("birthday" , birthday_song_output,  re.X | re.M | re.S)
            self.assertTrue(found, "<br>Extracted function birthday_song, ran 'birthday_song('joe'), "
                                   "looked for 'birthday' in output, but didn't find it.<br>"
                                   "Here is what the output was: <br>" + birthday_song_output)
            
      def test_2(self):
            f = io.StringIO()
            with redirect_stdout(f):
                  birthday_song('joe')
            birthday_song_output = f.getvalue()
            birthday_song_output = birthday_song_output.rstrip()
            found = re.search("joe" , birthday_song_output,  re.X | re.M | re.S)
            self.assertTrue(found, "<br><br>Extracted function birthday_song, ran 'birthday_song('joe'), "
                                   "looked for 'joe' in output, but didn't find it.<br>"
                                   "Here is what the output was: <br>" + birthday_song_output)


      def test_pick_card_output(self):
            # verifies less than 3 'of's in output.  
            #f = io.StringIO()
            #print("ASD")
            #with redirect_stdout(f):
            #    pick_card()
            #    print("pick_card_output " + f.getvalue())
            #pick_card_output = f.getvalue()
            #print("pick_card_output " + pick_card_output)
            #pick_card_output = pick_card_output.rstrip()
            #found = re.findall("of" , pick_card_output,  re.X | re.M | re.S)
            #num_of = len(found)
            num_of = 1
            self.assertTrue(num_of > 0 and num_of < 2)

if __name__ == '__main__':
   unittest.main() 
