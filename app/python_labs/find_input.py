# Inputs: p_filename_data, contents of the file (string)
#         p_number, the number of times I want to find input (integer)
#         p_points, the number of points this is worth (integer)
# Output: Dictionary of test_find_input
# This module finds if there is a a certain number of "input"


def find_input(p_filename_data, p_number, p_points):
    import re

    matches = len(re.findall(r".{1,2} \s* = \s* input\(", p_filename_data, re.X | re.M | re.S))
    p_test_find_input = {"name": "Testing that asking " + p_number + " questions from user (" + p_points + " points )",
                         "pass": True,
                         "pass_message": "Pass!  Computer asks at least " + p_number + "questions",
                         "fail_message": "Fail.  Code does not ask at least " + p_number + " questions.<br>"
                                         "Please fix error and resubmit (other tests not run). <br>",
                         }
    if matches < p_number:
        p_test_find_input['pass'] = False
        p_test_find_input['fail_message'] += "<br>  Found this many questions: " + str(matches) + ".<br>"
    return p_test_find_input

