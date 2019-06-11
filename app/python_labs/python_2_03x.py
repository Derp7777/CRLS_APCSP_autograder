def python_2_032a(p_filename, p_filename_data, *, debug_statement=''):
    """
    Function runs the test for python 2.032a lab
    :param p_filename: name of python code being graded (string)
    :param p_filename_data: contents of python code, (string)
    :param debug_statement: debug string for this particular test (2.032a for example says something
                            about order  of inputs) (string)
    :return: dictionary of test results
    """
    from app.python_labs.find_items import find_string
    from app.python_labs.io_test import io_test
    test_and_or = find_string(p_filename_data, r'(and|or) \s+ .+ \s+ (and|or)', 1)
    if test_and_or['pass']:
        ands = True
    else:
        ands = False

    p_pass_tests = {"name": "8 test cases for 2.032a work (12 points) <br>",
                    "pass": True,
                    "pass_message": "Pass!  All 8 test cases work",
                    "fail_message": "Fail.  Check your 8 test cases.<br>"
                                    "Please review the table that is after the 2.032a program run in your assignment."
                                    " <br> "
                                    "As part of this assignment, you should have populated that table.<br>"
                                    "You should test your code with the data from this table.<br>"
                                    "You need to figure out which ones, we do not tell you.<br>",
                    "points": 0,
                    "pass_and": ands,
                    "debug": ''
                    }

    if not ands:
        p_pass_tests['fail_message'] = '<h5 style=\"color:red;\">Fail.</h5>  ' \
                                       'Program needs to contain either ands or ors and what you have is ' \
                                       'not correct. <br>' \
                                       '(We aren\'t telling you which of ands or ors you need).<br>' \
                                       'Your code should look like this: <br>' \
                                       'print(2 == 3 and 2 == 4 or 2 == 3) <br>' \
                                       'That is, 3 tests with' \
                                       '"and" or "or" in between, with possible parentheses.<br>' \
                                       'Please edit your python code and try again.<br>'
        p_pass_tests['pass'] = False
        return p_pass_tests
    pass_count = 0
    test_1 = io_test(p_filename, r'False', 1)
    test_2 = io_test(p_filename, r'False', 2)
    test_3 = io_test(p_filename, r'True', 3)
    test_4 = io_test(p_filename, r'False', 4)
    test_5 = io_test(p_filename, r'False', 5)
    test_6 = io_test(p_filename, r'False', 6)
    test_7 = io_test(p_filename, r'False', 7)
    test_8 = io_test(p_filename, r'False', 8)

    if test_1['pass']:
        pass_count += 1
        p_pass_tests['debug'] += '1 '
    if test_2['pass']:
        pass_count += 1
        p_pass_tests['debug'] += '2 '
    if test_3['pass']:
        pass_count += 1
        p_pass_tests['debug'] += '3 '
    if test_4['pass']:
        pass_count += 1
        p_pass_tests['debug'] += '4 '
    if test_5['pass']:
        pass_count += 1
        p_pass_tests['debug'] += '5 '
    if test_6['pass']:
        pass_count += 1
        p_pass_tests['debug'] += '6 '
    if test_7['pass']:
        pass_count += 1
        p_pass_tests['debug'] += '7 '
    if test_8['pass']:
        pass_count += 1
        p_pass_tests['debug'] += '8 '

    p_pass_tests['pass_message'] = "You have " + str(pass_count) + "/8 tests pass.<br>" +\
                                   "These passed tests translate to a score of " + str(pass_count * 1.5) +\
                                   "/12.<br>Hints in case you did not pass all tests:<br>"
    p_pass_tests['pass_message'] += debug_statement

    p_pass_tests['points'] = pass_count * 1.5
    if pass_count == 8:
        p_pass_tests['pass_message'] = "<h5 style=\"color:green;\">Pass!</h5>" + p_pass_tests['pass_message']

    return p_pass_tests


def python_2_032b(p_filename, p_filename_data, *, debug_statement=''):
    """
    Function runs the test for python 2.032a lab
    :param p_filename: name of python code being graded (string)
    :param p_filename_data: contents of python code, (string)
    :param debug_statement: debug string for this particular test (2.032a for example says something
                            about order  of inputs) (string)
    :return: dictionary of test results
    """
    from app.python_labs.find_items import find_string
    from app.python_labs.io_test import io_test
    test_and_or = find_string(p_filename_data, r'(and|or) \s+ .+ \s+ (and|or)', 1)
    if test_and_or['pass']:
        ands_or = True
    else:
        ands_or = False

    p_pass_tests = {"name": "8 test cases for 2.032b work (8 points) <br>",
                    "pass": True,
                    "pass_message": "Pass!  All 8 test cases work",
                    "fail_message": "Fail.  Check your 8 test cases.<br>"
                                    "Please review the table that is after the 2.032b program run in your assignment."
                                    " <br> "
                                    "As part of this assignment, you should have populated that table.<br>"
                                    "You should test your code with the data from this table.<br>"
                                    "You need to figure out which ones, we do not tell you.<br>",
                    "score": 0,
                    "pass_and_or": ands_or,
                    "debug": ''
                    }

    if not ands_or:
        p_pass_tests['fail_message'] = '<h5 style=\"color:red;\">Fail.</h5>  ' \
                                       'Program needs to contain either ands or ors and what you have is ' \
                                       'not correct. <br>' \
                                       '(We aren\'t telling you which of ands or ors you need).<br>' \
                                       'Your code should look like this: <br>' \
                                       'print(2 == 3 and 2 == 4 or 2 == 3) <br>' \
                                       'That is, 3 tests with' \
                                       '"and" or "or" in between, with possible parentheses.<br>' \
                                       'Please edit your python code and try again.<br>'
        p_pass_tests['pass'] = False
        return p_pass_tests

    pass_count = 0
    test_1 = io_test(p_filename, 'True', 1)
    test_2 = io_test(p_filename, 'False', 2)
    test_3 = io_test(p_filename, 'True', 3)
    test_4 = io_test(p_filename, 'False', 4)
    test_5 = io_test(p_filename, 'True', 5)
    test_6 = io_test(p_filename, 'False', 6)
    test_7 = io_test(p_filename, 'False', 7)
    test_8 = io_test(p_filename, 'False', 8)

    if test_1['pass']:
        pass_count += 1
        p_pass_tests['debug'] += '1 '
    if test_2['pass']:
        pass_count += 1
        p_pass_tests['debug'] += '2 '
    if test_3['pass']:
        pass_count += 1
        p_pass_tests['debug'] += '3 '
    if test_4['pass']:
        pass_count += 1
        p_pass_tests['debug'] += '4 '
    if test_5['pass']:
        pass_count += 1
        p_pass_tests['debug'] += '5 '
    if test_6['pass']:
        pass_count += 1
        p_pass_tests['debug'] += '6 '
    if test_7['pass']:
        pass_count += 1
        p_pass_tests['debug'] += '7 '
    if test_8['pass']:
        pass_count += 1
        p_pass_tests['debug'] += '8 '

    p_pass_tests['score'] = pass_count

    p_pass_tests['pass_message'] = "You have " + str(pass_count) + "/8 tests pass.<br>" +\
                                   "These passed tests translate to a score of " + str(pass_count * 1.5) +\
                                   "/12.<br>Hints in case you did not pass all tests:<br>"
    p_pass_tests['pass_message'] += debug_statement

    p_pass_tests['points'] = pass_count * 1.5
    if pass_count == 8:
        p_pass_tests['pass_message'] = "<h5 style=\"color:green;\">Pass!</h5>" + p_pass_tests['pass_message']

    return p_pass_tests


if __name__ == "__main__":
    print("yes")
    filename_data = 'universe = input("Are you DC or Marvel? ") age = input("How old are you? ") ' \
                    'age = int(age) power = input("What is your power amount? ") power = (int(power)) ' \
                    'print(universe == "DC" and age <= 18 and power > 100)'
    python_2_032a('filename', filename_data)
