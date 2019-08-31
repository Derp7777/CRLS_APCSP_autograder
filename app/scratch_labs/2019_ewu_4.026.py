import random


# Input parameters - p_bonus - represents the bonus to the roll (integer)
# Returns - Number of dead raised
# Description - Simulates rolling a 20-sided dice to decide if Atwood successfully calls animate_dead.
#               If she rolls 5 or under, she will raise zero undead.
#               Otherwise, she raises the number of undead equal to (roll + p_bonus)
#               Example 1: p_bonus = 4.   Necromancer Atwood rolls 8 on a 20 sided dice.  She raises 12 undead.
#               return 12.
#               Example 2: p_bonus = -4.  Necromancer Atwood rolls 8 on a 20 sided dice.
#               8 - 4 < 5 and she raises 0 undead.  return 0.
def animate_dead(p_bonus):
    roll = random.randint(1, 20)
    roll_plus_bonus = roll + p_bonus
    if roll_plus_bonus < 5:
        return 0
    else:
        return roll_plus_bonus


# Input parameters - none
# Returns - A list representing the number of controlled and uncontrolled undead
# #         list[0] is controlled list[1] is uncontrolled.
# Description - Calls animate_dead function for each cemetery Necromancer Atwood visits
#                She will visit central burying ground, granary burying ground, King's chapel burying ground
#             - Each burying ground has different bonuses to raising the dead.
#                Central Burying Ground - keep her winning chance unchanged.
#                Granary Burying Ground - Give her a +2 chance to raise the dead. A bard friend gave her a bonus.
#                King's Chapel Burying Ground - Give her a -2 chance to raise the dead. John Winthrop isn't here for it.
#             - Immediately after calling animate_dead,
#                   there is a 25% chance she will lose control of the dead she just raised for that burying ground.
#             - If she raises dead (or raises 0) and keeps control of them, print out
#                 "Necromancer Atwood raised XXX undead in <cemetery name>"
#             -  If she raises dead and loses control of them, print out
#                 "Necromancer Atwood raised x undead in <cemetery name> but loses control of them"
#             - update the undead_data list
#             - At the end, Necromancer Atwood can only control 20 undead for long enough to do the dance.
#               At the end, any number of controlled undead become controlled.
#               Calculate if any of the controlled dead become uncontrolled.  If so, prints out
#                 "Necromancer Atwood can't control that many undead! x become uncontrolled" and update list.def raise
# _army():

def raise_army():
    undead = animate_dead(0)
    undead_data = [0, 0]
    roll = random.randint(1, 4)
    if roll < 4:
        undead_data[0] += undead
        print("Necromancer Atwood raised " + str(undead) + " undead in Central Burying Ground")
    else:
        undead_data[1] += undead
        print("Necromancer Atwood raised " + str(undead) + " undead in Central Burying Ground, "
                                                           "but loses control of them.")

    undead = animate_dead(2)
    roll = random.randint(1, 4)
    if roll < 4:
        undead_data[0] += undead
        print("Necromancer Atwood raised " + str(undead) + " undead in Granary Burying Ground")
    else:
        undead_data[1] += undead
        print("Necromancer Atwood raised " + str(undead) + " undead in Granary Burying Ground, "
                                                           "but loses control of them.")

    undead = animate_dead(-2)
    roll = random.randint(1, 4)
    if roll < 4:
        undead_data[0] += undead
        print("Necromancer Atwood raised " + str(undead) + " undead in King's chapel Burying Ground")
    else:
        undead_data[1] += undead
        print("Necromancer Atwood raised " + str(undead) + " undead in King's chapel Burying Ground, "
                                                           "but loses control of them.")

    if undead_data[0] > 20:
        undead_data[1] += undead_data[0] - 20
        undead_data[0] = 20

    return undead_data

# Input - list of integers that represents each possible outcome.
# Returns - list of integers that represents each possible outcome.
# Description - calls raise_army and determines the result
# sim_data[0] = Atwood gets dance party, but undead take over Boston common.
# sim_data[1] = Atwood gets dance party, and not enough undead take over Boston common.
# sim_data[2] = Atwood does not get dance party, but undead take over Boston common.
# sim_data[3] = Atwood does not get dance party, and not enough undead take over Boston common.
# Scores are kept  similar to College chooser
# The autograder will look for the following strings:
# "Dance party" for Necromancer Atwood getting dance party (enough  controlled undead)
# "No dance party" for Necromancer Atwood not getting dance party (not enough  controlled undead)
# "Taking over Boston common" for enough uncontrolled undead to take over Boston common
# "Not taking over Boston common" for not enough uncontrolled undead taking over Boston common
# capitalization does not matter


def dance(p_sim_data):

    undead_data = raise_army()
    controlled = undead_data[0]
    uncontrolled = undead_data[1]

    print(undead_data)
    if controlled > 10:
        print("Necromancer Atwood raised enough dead for the flash mob.  Yay Dance party!")
    else:
        print("Necromancer Atwood did not raise enough dead for the flash mob dance party. No Dance party.")
    if uncontrolled > 10:
        print("The uncontrolled undead are too much.  Oh no undead taking over Boston common!")
    else:
        print("The uncontrolled undead are not taking over Boston common.")

    if controlled > 10:
        if uncontrolled > 10:
            p_sim_data[0] += 1
        else:
            p_sim_data[1] += 1
    else:
        if uncontrolled > 10:
            p_sim_data[2] += 1
        else:
            p_sim_data[3] += 1
    return p_sim_data

# Input - list of integers, integers. list represents number of tournament wins. int represents the number of times
# the simulation ran
# Output - none
# Description - prints how many tournaments and Grand Slams Serena won and her win percentage


def data_analysis(p_sim_data, p_num_simulations):

    print("\n\n\nAn undead army dances Thriller while another overtakes Boston Common " + str(p_sim_data[0]) +
          " times out of " + str(p_num_simulations) + " simulations. " +
          str(int(p_sim_data[0]) / int(p_num_simulations) * 100) + "% of the time\n")

    print("An undead army dances Thriller " + str(p_sim_data[1]) +
          " times out of " + str(p_num_simulations) + " simulations.  Yay! " +
          str(int(p_sim_data[1]) / int(p_num_simulations) * 100) + "% of the time\n")
    print("Necromancer Atwood does not get her dance party, but an uncontrolled undead army takes over Boston Common."
          "  Oops.  \nThis event happens  " +
          str(p_sim_data[2]) +
          " times out of " + str(p_num_simulations) + " simulations.  " +
          str(int(p_sim_data[2]) / int(p_num_simulations) * 100) + "% of the time\n")

    print("No dance party, no undead takeover.  It\'s like nothing happened " + str(p_sim_data[3]) +
          " times out of " + str(p_num_simulations) + " simulations. " +
          str(int(p_sim_data[3]) / int(p_num_simulations) * 100) + "% of the time\n")


# Input - list of integers, float. list represents number of tournament wins.
# Output - list of integers that represents the various outcomes for Necromancer Atwood
# Description - calls dance the number of times the simulation needs to run and then calls data_analysis
def run_simulation(p_num_simulations):
    sim_data = [0, 0, 0, 0]
    for index in range(p_num_simulations):
        print("Simulation " + str(index + 1) + ":")
        sim_data = dance(sim_data)
    # call data_analysis after all the seasons are simulated
    data_analysis(sim_data, p_num_simulations)
    return sim_data


num_simulations = int(input("How many times to run simulation? "))
simulation_data = run_simulation(num_simulations)

# This is a fake help from martians
