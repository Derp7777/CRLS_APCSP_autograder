def python_2_032a(p_filename, p_filename_data):

    from app.python_labs.find_items import find_string
    from app.python_labs.io_test import io_test
    test_and = find_string(p_filename_data, 'and \s+ .+ \s+ and', 1, 0)
    if test_and:
        ands = True
    else:
        ands = False

    p_pass_tests = {"name": "8 test cases for 2.032a work (8 points) <br>",
                    "pass": True,
                    "pass_message": "Pass!  All 8 test cases work",
                    "fail_message": "Fail.  Check your 8 test cases.<br>"
                                    "Please review the table that is after the 2.032a program run in your assignment. <br> "
                                    "As part of this assignment, you should have populated that table.<br>"
                                    "You should test your code with the data from this table.<br>"
                                    "You need to figure out which ones, we do not tell you.<br>",
                    "score" : 0,
                    "pass_and" : ands,
                    "debug": ''
                    }

    pass_count = 0
    test_1 = io_test(p_filename, 'False', 1, 0)
    test_2 = io_test(p_filename, 'False', 1, 0)
    test_3 = io_test(p_filename, 'True', 1, 0)
    test_4 = io_test(p_filename, 'False', 1, 0)
    test_5 = io_test(p_filename, 'False', 1, 0)
    test_6 = io_test(p_filename, 'False', 1, 0)
    test_7 = io_test(p_filename, 'False', 1, 0)
    test_8 = io_test(p_filename, 'False', 1, 0)

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

    if not test_and:
        p_pass_tests['fail_message'] += 'Program did not contain some strings required to make it work properly. <br>' \
                                        '(We aren\'t telling you what they are). Edit the program and try it again.<br>'
        p_pass_tests['pass'] = False
    elif p_pass_tests['score'] != 8:
        p_pass_tests['pass'] = False

    return p_pass_tests


if __name__ == "__main__":
    print("yes")
    filename_data = 'universe = input("Are you DC or Marvel? ") age = input("How old are you? ") age = int(age) power = input("What is your power amount? ") power = (int(power)) print(universe == "DC" and age <= 18 and power > 100)'
    python_2_032a(filename_data)