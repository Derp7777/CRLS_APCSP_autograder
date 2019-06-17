def find_double_for(p_function_data):
    import re
    matches = len(re.findall(r'(for|while)', p_function_data, re.X | re.M | re.S))
    if matches >= 2:
        return True
    else:
        return False


def find_cheat_loop(p_function_data):
    import re
    matches = len(re.findall(r'in \s+ range\(1\)', p_function_data, re.X | re.M | re.S))
    if matches > 0:
        return False
    else:
        return True


def find_good_print(p_function_data):
    import re
    matches = len(re.findall(r'^\s \s \s \s print\(', p_function_data, re.X | re.M | re.S))
    if matches > 0:
        return True
    else:
        return False


def python_4_031_good_prints(p_filename):
    from app.python_labs.function_test import extract_all_functions, extract_single_function

    programs = ['loop1', 'loop2', 'loop3', 'loop4', 'loop5', 'loop6', 'loop7', 'loop8']
    extract_all_functions(p_filename)
    failed_tests = []

    for program in programs:
        function_data = extract_single_function(p_filename, program)
        good_print = find_good_print(function_data)
        if good_print is False:
            failed_tests.append(program)
    p_test = {"name": "The code should be efficient about prints (5 points). <br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  The is efficient about prints",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The code is not efficient about prints.  You should print at the END, not in the middle "
                              "of loops.   Printing at the end gives you a chance to make changes all the way "
                              "up until the time you print.   Functions without good prints are "
                              "the following: " + str(failed_tests),
              "points": 5,
              }
    if failed_tests:
        p_test['pass'] = False
        p_test['points'] = 0
    return p_test


def python_4_031_double_loops(p_filename):
    from app.python_labs.function_test import extract_all_functions, extract_single_function

    programs = ['loop4', 'loop5', 'loop6', 'loop7', 'loop8']
    extract_all_functions(p_filename)
    failed_tests = []

    for program in programs:
        function_data = extract_single_function(p_filename, program)
        double_loop = find_double_for(function_data)
        cheat_loop = find_cheat_loop(function_data)
        print(' double ' + str(double_loop) + ' cheat ' + str(cheat_loop))
        if double_loop is False or cheat_loop is False:
            failed_tests.append(program)
    p_test = {"name": "The code must have double loops EVERYWHERE (10 points). <br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  The has double loops in all required codes",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The code does not have double loops everywhere.  Functions without double loops are "
                              "the following: " + str(failed_tests) + "<br>  Note, a loop that only loops once does "
                                                                      "NOT count as a double loop.<br>",
              "points": 15,
              }
    if failed_tests:
        p_test['pass'] = False
        p_test['points'] = 0
    return p_test
