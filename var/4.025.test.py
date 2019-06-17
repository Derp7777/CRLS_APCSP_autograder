
import unittest
import io
from contextlib import redirect_stdout
import re
import random


class testAutograde(unittest.TestCase):
    def test_1(self):
        percent = 0.75
        wins = 0
        passed = False
        for i in range(1000):
            if game(percent):
                wins += 1
        if 710 < wins < 790:
            passed = True
        self.assertTrue(passed, "<br>Ran 1000 sims, should get between 710 and 790 wins.  "
                                "Got this many wins: " + str(wins) + "<br>")


    def test_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            play_tournament(0.75, 'Wimbledon')
        play_tournament_output = f.getvalue()
        play_tournament_output = play_tournament_output.rstrip()
        play_tournament_output = play_tournament_output.lower()
        found = re.search("wimbledon", play_tournament_output,  re.X | re.M | re.S)
        self.assertTrue(found, "<br>Called  play_tournament(0.75, 'Wimbledon')<br>"
                               "Looked for 'Wimbledon' in play_tournament's output.  Output is this:<br>"
                               + play_tournament_output)

    def test_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            play_tournament(1.0, 'wimbledon')
        play_tournament_output = f.getvalue()
        play_tournament_output = play_tournament_output.rstrip()
        play_tournament_output = play_tournament_output.lower()
        found = re.search(r"won \s wimbledon", play_tournament_output,  re.X | re.M | re.S)
        self.assertTrue(found, "<br>Called  play_tournament(1.00, 'Wimbledon')<br>"
                               "Looked for 'won wimbledon' in play_tournament's output.  Output is this:<br>"
                               + play_tournament_output)

    def test_4(self):
        percent = 0.60
        sim_data = [0, 0, 0, 0]
        passed = False
        f = io.StringIO()
        with redirect_stdout(f):
            for i in range(10000):
                sim_data = play_season(sim_data, percent)
        if sim_data[2] < sim_data[0] and sim_data[2] < sim_data[1]:
            passed = True
        self.assertTrue(passed, "<br>Ran 1000 sims with win pecentage of 50%.  Serena should win US open the most,"
                                "Wimbledon next most, and French open the least.<br>  "
                                "Serena won Wimbledon: " + str(sim_data[0]) +
                                " Serena won US open: " + str(sim_data[1]) +
                                " Serena won French open: " + str(sim_data[2]))

    def test_5(self):
        sim_data = [25, 50, 75, 3]
        num_simulations = 250
        f = io.StringIO()

        with redirect_stdout(f):
            data_analysis(sim_data, num_simulations)
        data_analysis_output = f.getvalue()
        data_analysis_output = data_analysis_output.rstrip()
        data_analysis_output = data_analysis_output.lower()
        found1 = len(re.findall(r"10\.0", data_analysis_output,  re.X | re.M | re.S))
        found2 = len(re.findall(r"20\.0", data_analysis_output,  re.X | re.M | re.S))
        found3 = len(re.findall(r"30\.0", data_analysis_output,  re.X | re.M | re.S))
        found4 = len(re.findall(r"1\.2", data_analysis_output,  re.X | re.M | re.S))
        foundall = found1 > 0 and found2 > 0 and found3 > 0 and found4 > 0
        self.assertTrue(foundall, "<br> Ran data_analysis with p_sim of [25, 50, 75, 3] and 200 simulations.<br>"
                                  "Expect to see certain percentages printed out.<br>"
                                  "Output is this: <br>" + data_analysis_output + "<br>"
                                  "Expected 12.5, matches: " + str(found1) + "<br> " +
                        "Expected 25, matches: " + str(found2) + "<br>"
                                                                 "Expected 37.5, matches: " + str(found3) + "<br> " +
                        "Expected 1.5, matches: " + str(found4) + "<br>")

    def test_6(self):
        num_simulations = 13
        win_chance = 100000
        f = io.StringIO()
        with redirect_stdout(f):
            run_simulation(num_simulations, win_chance)
        run_simulation_output = f.getvalue()
        run_simulation_output = run_simulation_output.rstrip()
        run_simulation_output = run_simulation_output.lower()
        found1 = len(re.findall(r"out\sof\s13\ssimulations", run_simulation_output,  re.X | re.M | re.S))
        foundall = found1 >= 3
        self.assertTrue(foundall, "<br> Ran run_simulation(13, 10000).  Expected to see 'of 13 simulations' 3 times."
                                  "<br>" + run_simulation_output + "<br>" +
                                  "Matched this many times: " + str(found1))


if __name__ == '__main__':
    unittest.main()
