# Input p_filename, filename to search for 3 questions
# Output p_test_inputs_1, a single test (dictionary)
# This runs the test of 3 questions


def three_questions(p_filename):

    import re

    from app.python_labs.read_file_contents import read_file_contents

    p_file_contents = read_file_contents(p_filename)

    matches = len(re.findall(r".{1,2} \s* = \s* input\(", p_file_contents, re.X | re.M | re.S))
    p_test_three_questions = {"name": "Testing that genie asks at least 3 questions (first part of lab) ( 5 points )",
                              "pass": True,
                              "pass_message": "Pass!  Genie asks at least 3 questions (first part of lab)",
                              "fail_message": "Fail.  Code does not ask at leat 3 questions (first part of lab).<br>"
                                              "The Genie needs to ask for 3 wishes from user for the first part.<br>"
                                              "Please fix error and resubmit (other tests not run). <br>",
                              }
    if matches < 3:
        p_test_three_questions['pass'] = False
        p_test_three_questions['fail_message'] += "<br>  Found this many questions: " + str(matches) + ".<br>"
    return p_test_three_questions


# Inputs: p_filename, filename to search for help.
# Output: p_tests, list of various tests.  Each test is a dictionary
# This module runs tests required for Python 1.040
def python_1_040(p_filename):

    from app.python_labs.read_file_contents import read_file_contents

    p_tests = []  # blank, will fill this later

    p_file_contents = read_file_contents(p_filename)

    return p_tests
