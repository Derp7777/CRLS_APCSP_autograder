import random
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
    def test_1(self):
        hits = {"I got a scratch story to tell": 1500,
                "mo history mo problems": 3000,
                "The ten CRLS commandments": 3500,
                "One more AP exam": 10000,
                "Gimme the lunch money": 15000,
                "Machine Fun Funk": 8000
                }
        answer = worst_hit(hits)
        self.assertEqual(answer, 'I got a scratch story to tell'
                         ,"<br>Checking that worst_hit works.<br>   Input dictionary: <br> " + str(hits) +
                         "<br>Expected 'I got a scratch story to tell' <br>Got this: " + str(answer)
                         )

    def test_2(self):
        hits = {"I got a scratch story to tell": 9500,
                "mo history mo problems": 3000,
                "The ten CRLS commandments": 3500,
                "One more AP exam": 10000,
                "Gimme the lunch money": 15000,
                "Machine Fun Funk": 8000
                }
        answer = worst_hit(hits)
        self.assertEqual(answer, 'mo history mo problems'
                         , "<br>Checking that worst_hit works.<br>   Input dictionary: <br> " + str(hits) +
                         "<br>Expected 'I got a scratch story to tell' <br>Got this: " + str(answer)
                         )

    def test_3(self):
        hits = {"I got a scratch story to tell": 9500,
                "mo history mo problems": 3000,
                "The ten CRLS commandments": 3500,
                "One more AP exam": 10000,
                "Gimme the lunch money": 15000,
                "Machine Fun Funk": 8000
                }
        answer = top_hits(hits)
        self.assertEqual(answer,
                         ['I got a scratch story to tell', 'One more AP exam', 'Gimme the lunch money',
                          'Machine Fun Funk']
                         , "<br>Checking that worst_hit works.<br>   Input dictionary: <br> " + str(hits) +
                         "<br>Expected 'I got a scratch story to tell' <br>Got this: " + str(answer)
                         )
    def test_4(self):
        hits = {"I got a scratch story to tell": 1500,
                "mo history mo problems": 3000,
                "The ten CRLS commandments": 13500,
                "One more AP exam": 110000,
                "Gimme the lunch money": 15000,
                "Machine Fun Funk": 18000,
                "oh holy night": 9999
                }
        answer = top_hits(hits)
        self.assertEqual(answer,
                         ['The ten CRLS commandments', 'One more AP exam', 'Gimme the lunch money', 'Machine Fun Funk',
                          'oh holy night']
                         , "<br>Checking that worst_hit works.<br>   Input dictionary: <br> " + str(hits) +
                         "<br>Expected 'I got a scratch story to tell' <br>Got this: " + str(answer)
                         )

if __name__ == '__main__':
   unittest.main() 
