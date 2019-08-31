
import unittest
import io
from contextlib import redirect_stdout
import re
import random
import sys

class testAutograde(unittest.TestCase):
    def test_1(self):
        bonus = 0
        raised = 0
        passed = False
        for i in range(2000):
            raised += animate_dead(bonus)
        if 18200 < raised < 21000:
            passed = True
        self.assertTrue(passed, "<br>Ran 2000 sims, should get between 18200 and 21000 raised dead.  "
                                "Got this many raised dead: " + str(raised) + "<br>")

    def test_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            for _ in range(100):
                raise_army()
        raise_army_output = f.getvalue()
        raise_army_output = raise_army_output.rstrip()
        raise_army_output = raise_army_output.lower()
        found1 = re.search(
            r"necromancer \s* atwood \s raised \s* ([0-9]+) .+? central \b (?!loses) \b .+?  necro .+? necro ",
            raise_army_output,
            re.X | re.M | re.S)
        found2 = re.search(r"necromancer .+? necromancer \s* atwood \s raised \s* ([0-9]+) .+?granary. "
                           r"\b (?!loses) \b +? necro",
                           raise_army_output,
                           re.X | re.M | re.S)
        found3 = re.search(r"necromancer .+? necromancer .+? necromancer \s* atwood \s raised \s* ([0-9]+) .+?"
                           r" king \b (?!loses) \b  "
                           r".+? $", raise_army_output,
                           re.X | re.M | re.S)
        found4 = re.search(r"necromancer \s* atwood \s raised \s* ([0-9]+) .+? central .+? loses .+? necro "
                           r".+? necro", raise_army_output, re.X | re.M | re.S)
        found5 = re.search(r"necromancer .+? necromancer .+?  \s* atwood \s raised \s* ([0-9]+) .+? granary .+? "
                           r"loses .+? necro", raise_army_output, re.X | re.M | re.S)
        found6 = re.search(
            r"necromancer .+? necromancer .+? necromancer \s* atwood \s raised \s* ([0-9]+) .+? king .+? loses .+? $",
            raise_army_output, re.X | re.M | re.S)
        #
        # found1 = re.search(r"necromancer \s* atwood \s raised \s* [0-9] .+? central", raise_army_output,
        #                    re.X | re.M | re.S)
        # found2 = re.search(r"necromancer \s* atwood \s raised \s* [0-9] .+? granary", raise_army_output,
        #                    re.X | re.M | re.S)
        # found3 = re.search(r"necromancer \s* atwood \s raised \s* [0-9] .+? king ", raise_army_output,
        #                    re.X | re.M | re.S)
        # found4 = re.search(r"necromancer \s* atwood \s raised \s* [0-9] .+? central .+? loses \s control",
        #                    raise_army_output, re.X | re.M | re.S)
        # found5 = re.search(r"necromancer \s* atwood \s raised \s* [0-9] .+? granary .+? loses \s control",
        #                    raise_army_output, re.X | re.M | re.S)
        # found6 = re.search(r"necromancer \s* atwood \s raised \s* [0-9] .+? king .+? loses \s control",
        #                    raise_army_output, re.X | re.M | re.S)
        passed = False
        if found1 and found2 and found3 and found4 and found5 and found6:
            passed = True
        self.assertTrue(passed,
                        "<br>Called  raise_army 100 times<br>"
                        "Looked for things in output.  Looked for:<br>"
                        "test1: necromancer atwood raised [NUMBER] ... central.  <br>"
                        "test2: necromancer atwood raised [NUMBER] ... granary . <br>"
                        "test3: necromancer atwood raised [NUMBER] ... king  <br>"
                        "test4: necromancer atwood raised [NUMBER] ... central ...loses control  <br>"\
                        "test5: necromancer atwood raised [NUMBER] ... granary ...loses control.<br> "
                        "test6: necromancer atwood raised [NUMBER] ... king ... loses control.<br> "
                        "Capitalization does not matter. <br><br>  Output is this:<br>" +
                        raise_army_output)

    def test_3(self):
        passed = True
        error_message = ''
        for _ in range(5):
            f = io.StringIO()
            with redirect_stdout(f):
                raised = raise_army()
                expected_raised = [0, 0]
                raise_army_output = f.getvalue()
                raise_army_output = raise_army_output.rstrip()
                raise_army_output = raise_army_output.lower()
                found1 = re.search(
                    r"necromancer \s* atwood \s raised \s* ([0-9]+) .+? central \b (?!loses) \b .+?  necro .+? necro ",
                    raise_army_output,
                    re.X | re.M | re.S)
                found2 = re.search(r"necromancer .+? necromancer \s* atwood \s raised \s* ([0-9]+) .+?granary. "
                                   r"\b (?!loses) \b +? necro",
                                   raise_army_output,
                                   re.X | re.M | re.S)
                found3 = re.search(r"necromancer .+? necromancer .+? necromancer \s* atwood \s raised \s* ([0-9]+) .+?"
                                   r" king \b (?!loses) \b  "
                                   r".+? $", raise_army_output,
                                   re.X | re.M | re.S)
                found4 = re.search(r"necromancer \s* atwood \s raised \s* ([0-9]+) .+? central .+? loses .+? necro "
                                   r".+? necro", raise_army_output, re.X | re.M | re.S)
                found5 = re.search(
                    r"necromancer .+? necromancer .+?  \s* atwood \s raised \s* ([0-9]+) .+? granary .+? "
                    r"loses .+? necro", raise_army_output, re.X | re.M | re.S)
                found6 = re.search(
                    r"necromancer .+? necromancer .+? necromancer \s* atwood \s raised \s* ([0-9]+) .+? king .+? loses .+? $",
                    raise_army_output, re.X | re.M | re.S)
                if found1:
                    expected_raised[0] += int(found1.group(1))
                    print("Found is this found1 xxx" + found1.group(1))
                # print("exptected is this " + str(expected_raised))
                if found2:
                    expected_raised[0] += int(found2.group(1))
                    print("found is this found2 xxx" + found2.group(1))

                # print("exptected is this " + str(expected_raised))

                if found3:
                    expected_raised[0] += int(found3.group(1))
                    print("found is this found3 xxx" + found3.group(1))

                    # print(found3.group(0))

                # print("exptected is this " + str(expected_raised))

                if found4:
                    expected_raised[1] += int(found4.group(1))
                    print("found is this found4 xxx" + found4.group(1))

                print(expected_raised)

                if found5:
                    expected_raised[1] += int(found5.group(1))
                    print("found is this found5 xxx" + found5.group(1))

                print(expected_raised)

                if found6:
                    expected_raised[1] += int(found6.group(1))
                    print("found is this found6 xxx" + found6.group(1))

                print(expected_raised)

                if expected_raised[0] > 20:
                    expected_raised[1] += expected_raised[0] - 20
                    expected_raised[0] = 20
                raise_army_output = f.getvalue()
                raise_army_output = raise_army_output.rstrip()
                raise_army_output = raise_army_output.lower()

                if expected_raised[0] != raised[0] or expected_raised[1] != raised[1]:
                    error_message += "Got an undead_data of " + str(raised) + "<br> Expected : " + \
                                     str(expected_raised) + "<br> from this data: " + raise_army_output
                    passed = False
                    break
            f.close()
        self.assertTrue(passed, error_message)

    def test_4(self):

        passed = True
        error_message = ''
        for _ in range(500):
            f = io.StringIO()
            with redirect_stdout(f):
                sim_data = [0, 0, 0, 0]
                sim_data = dance(sim_data)
                dance_output = f.getvalue()
                dance_output = dance_output.rstrip()
                dance_output = dance_output.lower()
                print("next round " + str(dance_output) + " simd ata " + str(sim_data), file=sys.stderr)

                found1 = re.search(r"yay \s* dance \s* party ", dance_output, re.X | re.M | re.S)
                found2 = re.search(r"no \s* dance \s* party ", dance_output,re.X | re.M | re.S)
                found3 = re.search(r"oh \s* no \s* undead \s* taking \s over \s boston \s common ", dance_output, re.X | re.M | re.S)
                found4 = re.search(r"not \s* taking \s* over \s* boston \s* common ", dance_output, re.X | re.M | re.S)
                matched = 0
                if found1:
                    matched += 1
                if found2:
                    matched += 1
                if found3:
                    matched += 1
                if found4:
                    matched += 1
                if matched != 2:
                    error_message += "Needed to match at least two conditions of dance party, no dance party, " \
                                     "taking over boston common, and not taking over boston common <br>" \
                                     "(capitalization does not matter).  <br> Got this output: <br>" + dance_output
                    passed = False
                    break
                if found1 and found3:
                    print("FOUND1 foud3 ", file=sys.stderr)

                    if sim_data[0] != 1 and sim_data[1] != 0 and sim_data[2] != 0 and sim_data[3] != 0:
                        error_message += "From dance, got p_sim of  " + str(sim_data) + \
                                        "<br> Expected : [1, 0, 0, 0]  <br> from this data: " + dance_output
                        passed = False
                        break
                if found1 and found4 and sim_data[1] != 1:
                    error_message += "From dance, got p_sim of  " + str(sim_data) + \
                                     "<br> Expected : [0, 1, 0, 0]  <br> from this data: " + dance_output
                    passed = False
                    break
                if found2 and found3 and sim_data[2] != 1:
                    error_message += "From dance, got p_sim of  " + str(sim_data) + \
                                     "<br> Expected : [0, 0, 1, 0]  <br> from this data: " + dance_output
                    passed = False
                    break
                if found2 and found4 and sim_data[3] != 1:
                    error_message += "From dance, got p_sim of  " + str(sim_data) + \
                                     "<br> Expected : [0, 0, 0, 1]  <br>from this data: " + dance_output
                    passed = False
                    break

            f.close()
            # f.flush()
            # print(f.closed)
            # f = ''
            # print("f is " + f)
            # sys.stdout.flush()
        self.assertTrue(passed, error_message)

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
            run_simulation(num_simulations)
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
