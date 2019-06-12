def python_2_051a(p_filename, p_filename_data):
    """
    Does the tests for 2.051a
    :param p_filename: filename (string)
    :param p_filename_data: contents of the filename (string)
    :return: A dictionary of test info
    """
    from app.python_labs.find_items import find_list_items
    from app.python_labs.io_test import io_test

    prizes = find_list_items(p_filename_data, 'prizes')
    test_2 = io_test(p_filename, prizes[1], 2)
    test_3 = io_test(p_filename, prizes[2], 3)

    p_pass_tests = {"name": "2 test cases for 2.051a work (8 points) <br>",
                    "pass": True,
                    "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  2 test cases work",
                    "fail_message": "<h5 style=\"color:red;\">Fail.</h5>  Check your 2 test cases.<br>"
                                    "If you run the program, and I type '1', it should print out 0th element of prizes "
                                    "list."
                                    " <br> "
                                    "Same for prize2, prize3, and prize4. <br>"
                                    "User should input '1', '2', '3', or '4', not 'door1', 'prize1' or anything like "
                                    "that",
                    "points": 0,
                    }

    debug_string = ''

    if test_2['pass']:
        p_pass_tests['points'] += 4
        debug_string += ' 2 prize passed '
    else:
        p_pass_tests['fail_message'] += test_2['fail_message'] + "<br> This was result after entering " \
                                                                 "'2' at keyboard.<br>"
    if test_3['pass']:
        p_pass_tests['points'] += 4
        debug_string += ' 3 prize passed'
    else:
        p_pass_tests['fail_message'] += test_3['fail_message'] + "<br> This was result after entering " \
                                                                 "'3' at keyboard.<br>"
    if p_pass_tests['points'] != 8:
        p_pass_tests['pass'] = False
        p_pass_tests['debug'] = debug_string
    return p_pass_tests


if __name__ == "__main__":
    from app.python_labs.read_file_contents import read_file_contents
    print("yes")
#    filename = '/home/ewu/abc/2.040/2019_mayasater_2.040.py'
    filename = '/Users/dimmyfinster/PycharmProjects/untitled5/2019_anais_2.050a.py'
    filename_data = read_file_contents(filename)
    bbb = python_2_051a(filename, filename_data)
    print(bbb)
