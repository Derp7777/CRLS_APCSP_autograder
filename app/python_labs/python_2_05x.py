def python_2_051a(p_filename, p_filename_data):

    import re
    from app.python_labs.find_items import find_list_items
    from app.python_labs.io_test import io_test

    prizes = find_list_items(p_filename_data, 'prizes \s* = \s* \[ (.+) \] $')
    test_1 = io_test(p_filename, prizes[0], 1, 0)
    test_2 = io_test(p_filename, prizes[1], 2, 0)
    test_3 = io_test(p_filename, prizes[2], 3, 0)
    test_4 = io_test(p_filename, prizes[3], 4, 0)

    p_pass_tests = {"name": "4 test cases for 2.051a work (8 points) <br>",
                    "pass": True,
                    "pass_message": "Pass!  All 4 test cases work",
                    "fail_message": "Fail.  Check your 4 test cases.<br>"
                                    "If you run the program, and I type '1', it should print out 0th element of prizes"
                                    "list somehow."
                                    " <br> "
                                    "Same for prize2, prize3, and prize4. <br>"
                                    "User should input '1', '2', '3', or '4', not 'door1', 'prize1' or anything like "
                                    "that",
                    "score": 0,
                    }

    debug_string = ''
    if test_1['pass']:
        p_pass_tests['score'] += 2
        debug_string += ' <br>1  prize passed '
    if test_2['pass']:
        p_pass_tests['score'] += 2
        debug_string += ' 2 prize passed '
    if test_3['pass']:
        p_pass_tests['score'] += 2
        debug_string += ' 3 prize passed'
    if test_4['pass']:
        p_pass_tests['score'] += 2
        debug_string += ' 4 prize pass'
    if p_pass_tests['score'] != 8:
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