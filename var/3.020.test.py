
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
        found = re.search("birthday", birthday_song_output,  re.X | re.M | re.S)
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

    def test_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            birthday_song('joe')
        birthday_song_output = f.getvalue()
        birthday_song_output = birthday_song_output.rstrip()
        matches = len(re.findall(r"Happy \s [bB]irthday \s to \s you", birthday_song_output, re.X | re.M | re.S))
        if matches >= 2:
            two_happy_birthday = True
        else:
            two_happy_birthday = False
        found = re.search(r"Happy \s [bB]irthday \s [dD]ear \s joe", birthday_song_output, re.X | re.M | re.S)
        self.assertTrue(two_happy_birthday and found, "<br><br>Extracted function birthday_song, "
                                                      "ran 'birthday_song('joe').  In output, looked for"
                                                      "'Happy Birthday to you' 2 times, and found it " + str(matches) +
                        " times.<br> "
                        "Looked for 'Happy Birthday dear joe'.  Did I find it? " +
                        str(bool(found)) + "<br>Here is what the output was: <br>" +
                        birthday_song_output + "<br><br> Capitalization matters.<br>")

    def test_4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            pick_card()
        pick_card_output = f.getvalue()
        pick_card_output = pick_card_output.rstrip()

        matches = len(re.findall(r"\s of \s", pick_card_output, re.X | re.M | re.S))
        self.assertTrue(0 < matches < 2, "<br>Running the pick_card function should give ONE card and there"
                                        " should be a printout with 'of' in it.  For example, 2 of hearts."
                                        "<br>We do NOT want to pick all five cards here because that makes"
                                        " the program less reusable.  For example, if your pick_card picks"
                                        " one card, you can reuse it for poker, blackjack, and any other "
                                        "game.  If your pick_card picks 5, you can ONLY use it for a "
                                        "game where you pick 5.<br>"
                                        "If this failed unexpectedly, check your spacing.<br>"
                                        "Here is what the output was:<br>" + pick_card_output)

if __name__ == '__main__':
    unittest.main()
