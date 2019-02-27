
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
      def test_serena_1(self):
            percent = 0.75
            wins = 0
            pass = False
            for i in range(1000):
                  if game(percent):
                        wins += 1
            if wins > 730 and wins < 780:
                  pass = true
            self.assertTrue(pass)
            
      def test_serena_2(self):
            f = io.StringIO()
            with redirect_stdout(f):
                  play_tournament(0.75, 'wimbledon')
            play_tournament_output = f.getvalue()
            play_tournament_output = play_tournament_output.rstrip()
            play_tournament_output = play_tournament_output.lower()
            found = re.search("round" , play_tournament_output,  re.X | re.M | re.S)
            self.assertTrue(found)

      def test_serena_3(self):
            f = io.StringIO()
            with redirect_stdout(f):
                  play_tournament(1.0, 'wimbledon')
            play_tournament_output = f.getvalue()
            play_tournament_output = play_tournament_output.rstrip()
            play_tournament_output = play_tournament_output.lower()
            found = re.search("win" , play_tournament_output,  re.X | re.M | re.S)
            self.assertTrue(found)

      def test_serena_4(self):
            sim_data = [ 25, 50, 75 ]
            num_simulations = 100
            f = io.StringIO()
            
            with redirect_stdout(f):
                  data_analysis(sim_data, num_simulations)
            data_analysis_output = f.getvalue()
            data_analysis_output = data_analysis_output.rstrip()
            data_analysis_output = data_analysis_output.lower()
            found1 = re.search("25" , data_analysis_output,  re.X | re.M | re.S)
            found2 = re.search("50" , data_analysis_output,  re.X | re.M | re.S)
            found3 = re.search("75" , data_analysis_output,  re.X | re.M | re.S)
            foundall == found1 and found2 and found3
            self.assertTrue(foundall)

            
            



if __name__ == '__main__':
   unittest.main() 
