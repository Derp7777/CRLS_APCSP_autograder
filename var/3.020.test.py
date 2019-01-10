import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
      def test_happy_birthday(self):
            f = io.StringIO()
            with redirect_stdout(f):
                  birthday_song('joe')
            birthday_song_output = f.getvalue()
            birthday_song_output = birthday_song_output.rstrip()
            birthday_song_output = birthday_song_output.lower()
            found = re.search("birthday" , birthday_song_output,  re.X | re.M | re.S)
            self.assertTrue(found)
            
      def test_happy_birthday_output(self):
            f = io.StringIO()
            with redirect_stdout(f):
                  birthday_song('joe')
            birthday_song_output = f.getvalue()
            birthday_song_output = birthday_song_output.rstrip()
            found = re.search("joe" , birthday_song_output,  re.X | re.M | re.S)
            self.assertTrue(found)
            
if __name__ == '__main__':
   unittest.main() 
