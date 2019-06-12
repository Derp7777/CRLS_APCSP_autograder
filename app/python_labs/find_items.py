# Inputs: p_filename_data, contents of the file (string).

# Output: Dictionary of test_list_created
# This module finds if there is a list


def find_list(p_filename_data):
    import re

    # test for a list that is created (i.e. abc = [asdf]
    p_search_object = re.search(r". \s* = \s* \[ .* \]", p_filename_data, re.X | re.M | re.S)

    p_test_list = {"name": "Testing that there is something that looks like a list being created.",
                   "pass": True,
                   "pass_message": "Pass! Submitted file has something that looks like a list being created.",
                   "fail_message": "Submitted file does not look like it has a list being created.",
                   }
    if p_search_object:
        p_test_list['pass'] = True
    else:
        p_test_list['pass'] = False
    return p_test_list

# Inputs: p_filename_data, contents of the file (string).
# Output: Dictionary of test_loop, created
# This module finds if there is a loop


def find_loop(p_filename_data, p_points):
    import re

    # test for a list that is created (i.e. abc = [asdf]
    p_search_object = re.search(r"(for|while)", p_filename_data, re.X | re.M | re.S)

    p_test_loop = {"name": "Testing that there is a loop. (" + str(p_points) + " points)<br>",
                   "pass": True,
                   "pass_message": "Pass! There is a loop in the code selection",
                   "fail_message": "Fail.  There is not a loop in the selected code.  Selected code is this:<br>"
                                   "" + p_filename_data,
                   }
    if p_search_object:
        p_test_loop['pass'] = True
    else:
        p_test_loop['pass'] = False
    return p_test_loop


def find_string(p_filename_data, p_search_string, p_num, *, points=0, minmax='min'):
    """
    This function looks for a regex string within a larger string X times
    :param p_filename_data: The larger string to search
    :param p_search_string: The regex to look for
    :param p_num: number of times you require regex to appear in larger string
    :param points: points this is worth (int)
    :param minmax: whether you want p_num to be MIN or MAX times string can appear.  Default is min.
    :return: dictionary of test info
    """
    import re

    p_matches = len(re.findall(p_search_string, p_filename_data, re.X | re.M | re.S))
    p_test_find_string = {"name": "Testing that this string is there: " + p_search_string + " at least " +
                                  str(p_num) + " times (" + str(points) +
                                  " points) <br>",
                          "pass": True,
                          "pass_message": "<h5 style=\"color:green;\">Pass!</h5> Found this string: "
                                          + p_search_string + " at least " +
                                          str(p_num) + " times.<br>",
                          "fail_message": "<h5 style=\"color:red;\">Fail.</h5>  Didn't find this string:"
                                          + p_search_string + " at least " +
                                          str(p_num) + " times.<br>",
                          'points': 0
                          }
    if minmax == 'max':
        if p_matches <= p_num:
            passed = True
        else:
            passed = False
    elif minmax == 'min':
        if p_matches >= p_num:
            passed = True
        else:
            passed = False
    else:
        raise Exception("variable minmax must be either 'min' or 'max'")

    if not passed:
        p_test_find_string['pass'] = False
        p_test_find_string['fail_message'] += "Found match " + str(p_matches) + " times in this string:. <br>" + \
                                              p_filename_data
    else:
        p_test_find_string['points'] += points
    return p_test_find_string


# Inputs: p_filename_data, contents of the file (string).
#         p_search_strings, list of what you are looking for, literally (string)
#         p_points, number of points this test is worth (int)
# Output: Dictionary of test_find_all_strings
# This module finds if all strings are there


def find_all_strings(p_filename_data, p_search_strings, p_points):
    """
    function looks for all strings
    :param p_filename_data: The larger string to search
    :param p_search_strings: The regexes (PLURAL) to look for (string)
    :param p_points:  points this is worth (int)
    :return: dictionary of test info
    """
    passed = []
    debug = []
    for p_search_string in p_search_strings:
        test_find_string = find_string(p_filename_data, p_search_string, 1, points=0)
        if test_find_string['pass']:
            passed.append(p_search_string)
            debug.append(test_find_string)

    p_test_find_strings = {"name": "Testing that ALL of these strings are there: " + str(p_search_strings) +
                                   " (" + str(p_points) + " points) <br>",
                           "pass": True,
                           "pass_message": "<h5 style=\"color:green;\">Pass!</h5> Found ALL of these these strings: " + str(p_search_strings) + ".<br>",
                           "fail_message": "<h5 style=\"color:red;\">Fail.</h5> Didn't find all strings in " + str(p_search_strings) + ". <br" +
                                           " But did find these strings: " + str(passed) + ". <br>",
                           'points': 0
                           }
    if passed != p_search_strings:
        p_test_find_strings['pass'] = False
    else:
        p_test_find_strings['points'] = p_points
    return p_test_find_strings

# Inputs: p_filename_data, contents of the file (string).
#         p_function_name, function name I am looking for (string)
#         p_num_parameters, number of parameters I expect (integer)
#         p_points, points this is worth (int)
# Output: Dictionary of test_function_exists
# This module finds if there is a function with a certain name and certain parameters


def find_function(p_filename, p_function_name, p_num_parameters, p_points):
    import delegator

    # Check for function return_min
    cmd_string = ''
    if p_num_parameters == 0:
        cmd_string = 'grep "^def ' + p_function_name + '(\s*):"'
    elif p_num_parameters == 1:
        cmd_string = 'grep "^def ' + p_function_name + '(\s*[a-zA-Z_]\+[^,]\s*)"'
    elif p_num_parameters == 2:
        cmd_string = 'grep "^def ' + p_function_name + '(\s*[a-zA-Z_]\+,\s*[a-zA-Z_]\+[^,]\s*)"'
    elif p_num_parameters == 3:
        cmd_string = 'grep "^def ' + p_function_name + '(\s*[a-zA-Z_]\+,\s*[a-zA-Z_]\+,\s*[a-zA-Z_]\+[^,])\s*"'

    p_test_function_exists = {"name": "Testing that there is a function " + p_function_name +
                                      " with " + str(p_num_parameters) + " input parameters. (" + str(p_points) +
                                      " points). <br>",
                              "pass": True,
                              "pass_message": "Pass! There is a function " + p_function_name +
                                              " with " + str(p_num_parameters) + " input parameters. <br>",
                              "fail_message": "There is NOT a function " + p_function_name +
                                              " with " + str(p_num_parameters) + " input parameters. <br>",
                              }

    cmd = cmd_string + ' ' + p_filename
    c = delegator.run(cmd)
    if c.err:
        p_test_function_exists['pass'] = False
        p_test_function_exists['fail_message'] += "Error message: " + c.err
    elif c.out:
        p_test_function_exists['pass_message'] += "Found this: " + c.out
    else:
        p_test_function_exists['pass'] = False
        cmd = 'grep "def" ' + p_filename
        c = delegator.run(cmd)
        p_test_function_exists['fail_message'] += "The file " + p_filename + " has these functions: <br> " +\
                                                  c.out + "<br>" + " but not " + p_function_name + " with" +\
                                                  " exactly " + str(p_num_parameters) + " input parameter(s). <br>"
    return p_test_function_exists


# Inputs: p_filename_data, contents of the file (string).
#         p_class_name, function name I am looking for (string)
#         p_parent, number of parameters I expect (integer)
#         p_points, points this is worth (int)
# Output: Dictionary of test_class_exists
# This module finds if there is a class with a certain name and certain parameters

def find_class(p_filename, p_class_name, p_parent, p_points):
    import delegator

    # Check for function return_min
    cmd_string = 'grep "^class " + p_class_name + " \(" + p_parent + "object\)"'

    cmd = cmd_string + ' ' + p_filename
    c = delegator.run(cmd)
    p_test_class_exists = {}
    p_test_class_exists['name'] = "Looking for this class " + p_class_name + " with this parent " + " p_parent (" + \
                        p_points +  " points). "
    if c.err:
        p_test_class_exists['pass'] = False
        p_test_class_exists['fail_message'] += "Error message: " + c.err
    elif c.out:
        p_test_class_exists['pass_message'] += "Found this: " + c.out
        p_test_class_exists['score'] = p_points
    else:
        p_test_class_exists['pass'] = False
        cmd = 'grep "class" ' + p_filename
        c = delegator.run(cmd)
        p_test_class_exists['fail_message'] += "The file " + p_filename + " has these classes: <br> " +\
                                                  c.out + "<br>" + " but not " + p_class_name + " with" +\
                                                  " this parent " + str(p_parent) + " input parameter(s). <br>"
    return p_test_class_exists

# Inputs: p_filename, contents of the file (string).
#         p_class_name, fclass name I am looking for (string)
#         p_times, number of times object needs to be created, minimum (int)
#         p_points, points this is worth (int)
# Output: Dictionary of test_function_called
# This module finds if there is a function with a certain name and certain parameters


def function_called(p_filename, p_class_name, p_times, p_points):

    from app.python_labs.read_file_contents import read_file_contents
    import re
    p_test_function_called = {"name": "Testing that there are objects of type  " + p_class_name +
                                      " that gets created in the main program at least " +
                                      str(p_times) + " times.  (" + str(p_points) + " points).<br>"
                                      + "). <br>",
                              "pass": False,
                              "pass_message": "Pass! There is object of type " + p_class_name +
                                              " that gets created enough times "
                                              "<br>",
                              "fail_message": "Fail.  The class " + p_class_name +
                                              " does NOT have enough objects of that type in the program. <br>"
                                              " If this doesn't make sense, look at the presentations for help"
                                              " <br>",
                              "score" : p_points
                              }
    regex = r"[a-zA-Z0-9]\s*=\s*" + p_class_name
    matches = 0
    with open(p_filename) as infile:
        for line in infile.readlines():
            match = re.search(regex, line, re.X | re.M | re.S)
            if match:
                matches += 1
    infile.close()
    if matches >= p_times:
        p_test_function_called['pass'] = True
    else:
        p_test_function_called['score'] = 0
        filename_data = read_file_contents(p_filename)
        p_test_function_called["fail_message"] += "Found this many matches: " + str(matches) + \
                                                  " of objects of class type:" + p_class_name + \
                                                  " in file with this data: <br> " + filename_data
    return p_test_function_called


# Inputs: p_filename, contents of the file (string).
#         p_function_name, function name I am looking for (string)
#         p_times, number of times function needs to be called, minimum
#         p_points, points this is worth (int)
# Output: Dictionary of test_function_called
# This module finds if there is a function with a certain name and certain parameters


def object_created(p_filename, p_function_name, p_times, p_points):

    from app.python_labs.read_file_contents import read_file_contents
    import re
    p_test_object_created = {"name": "Testing that there is a function " + p_function_name +
                                      " that gets called in the main program at least " +
                                      str(p_times) + " times.  (" + str(p_points) + " points).<br>"
                                      + "). <br>",
                              "pass": False,
                              "pass_message": "Pass! There is a function " + p_function_name +
                                              " that gets called in the main program (i.e. not part of a function). "
                                              "<br>",
                              "fail_message": "Fail.  The function " + p_function_name +
                                              " is NOT called in the main program enough times. <br>"
                                              " If this doesn't make sense, look"
                                              "in the presentation examples 1-6 to see calling functions in action."
                                              " <br>",
                              "score" : p_points
                              }
    regex = r"(?<!def \s)" + p_function_name
    matches = 0
    with open(p_filename) as infile:
        for line in infile.readlines():
            match = re.search(regex, line, re.X | re.M | re.S)
            if match:
                matches += 1
    infile.close()
    if matches >= p_times:
        p_test_object_created['pass'] = True
    else:
        p_test_object_created['score'] = 0
        filename_data = read_file_contents(p_filename)
        p_test_object_created["fail_message"] += "Found this many matches: " + str(matches) + \
                                                  " of " + p_function_name + \
                                                  " in file with this data: <br> " + filename_data
    return p_test_object_created


def find_questions(p_filename_data, p_num, p_points):
    """ This function finds if file has any questions in it (i.e. input = ) a certain number of times.
    Input parameters: p_filename_data - contains the entire python file (string)
                      p_num - minimum number of times you want to find a question (int).
                              i.e. you require minimum 3 strings that look like blah = input('question here')
                      p_points - number of points this question is worth
    Output: Dictionary of test_function_exists"""
    import re

    matches = len(re.findall(r".{1,2} \s* = \s* input\(", p_filename_data, re.X | re.M | re.S))
    matches_int = len(re.findall(r".{1,2} \s* = \s* int\( input\(", p_filename_data, re.X | re.M | re.S))
    matches_float = len(re.findall(r".{1,2} \s* = \s* float\( input\(", p_filename_data, re.X | re.M | re.S))

    p_test_find_questions = {"name": "Testing that there are least " + str(p_num) + " question(s) (" + str(p_points) +
                                     " points)<br>",
                             "pass": True,
                             "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                                             "Code asks at least " + str(p_num) + " questions ",
                             "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                                             "Code does not ask at least " + str(p_num) + " questions .<br>" +
                                             "Note: You should not put extra parentheses around the inputs,"
                                             "as this can confuse coders (who might think it's a tuple, which is "
                                             "like a list).  Extra parentheses will not score.<br>",
                             "points": 0
                             }
    if matches < p_num and matches_int < p_num and matches_float < p_num:
        p_test_find_questions['pass'] = False
        p_test_find_questions['fail_message'] += "<br>  Found this many questions: " + str(matches) + ".<br>"
    if p_test_find_questions['pass']:
        p_test_find_questions['points'] = p_points
    return p_test_find_questions


def find_list_items(p_filename_data, p_string):
    """
    Looks for a string
    :param p_filename_data: contains the entire python file (string)
    :param p_string: The list you are looking for (string)
    :return: A list, items are items in the list you are searching for
    """
    import re
    find_this_list = p_string + r' \s* = \s* \[ ([^\]]+) \] '
    print(find_this_list)
    print(p_filename_data)
    p_search_object = re.search(find_this_list, p_filename_data, re.X | re.M | re.S)
    match = p_search_object.group(1)
    print('initial match ' + str(match))
    new_item = ''
    on_off = -1
    reconstructed_list = []
    quotation = ''
    for letter in str(match):
        if letter == '"' or letter == "'":
            if on_off == -1:
                on_off *= -1  # turn on
                quotation = letter
                new_item = ''
            else:
                if quotation == letter:
                    on_off *= -1  # turn off
                    reconstructed_list.append(new_item)
                else:
                    new_item += letter
        else:
            new_item += letter
    print("reconstructed list")
    print(reconstructed_list)

    return reconstructed_list


if __name__ == "__main__":
    # find_function('/tmp/abc.py', 'hello', 3)
    # asdf = "[a-z]{1,2} \s* = \s* input \( [^']+ \) "
    # filename_data = '# print("yes") abc  = input(asdf) input(asdf) wish1 =' \
    #                 ' input("give me wish")n wish2 = input("give me wish")n wish3 = input("give me wish")  ' \
    #                 'print("your wishes are " + wish1 + ", " + wish2 + ", " + wish3)# Joe helped me'
    #
    # abc = find_string(filename_data, asdf, 1, 0)
    # print(abc)
    # asdf = '(verb|noun|adjective|adverb|preposition) .+ \s* = \s* input\('
    # filename_data = 'print("asdf") verb = input("yes") noun = input("yes") adjective = input("yes") ' \
    #                 'noun3 = input("yes") adjective10 = input("yes") print(verb + " " + ' \
    #                 'noun + " .?! " + adjective + " noun" + noun3 + " " + adjective10) # joe helped me '
    # abc = find_string(filename_data, asdf, 5, 0)
    # print(abc)
    filename_data = "hello world    prizes = [\"asdf\", '23', 'llll']"
    # abc = find_list_items('prizes \s* = \s* \[ (.+) \]', filename_data)
    abc = find_list_items(filename_data, r'prizes \s* = \s* \[ (.+) \]')

