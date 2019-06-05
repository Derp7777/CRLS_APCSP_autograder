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
#         p_search_string, what you are looking for, literally (string)
#         p_num, number of times you need to find the string
# Output: Dictionary of test_find_string
# This module finds if there is a search string within the file


def find_string(p_filename_data, p_search_string, p_num, p_points):
    import re

    print(p_search_string)
    print(p_filename_data)
    p_matches = len(re.findall(p_search_string, p_filename_data, re.X | re.M | re.S))
    p_test_find_string = {"name": "Testing that this string is there: " + p_search_string + " at least " +
                                  str(p_num) + " times (" + str(p_points) +
                                  " points) <br>",
                          "pass": True,
                          "pass_message": "Pass! Found this string: " + p_search_string + " at least " +
                                          str(p_num) + " times.<br>",
                          "fail_message": "Fail.  Didn't find this string:" + p_search_string + " at least " +
                                          str(p_num) + " times.<br>",
                          }

    if p_matches < p_num:
        p_test_find_string['pass'] = False
        p_test_find_string['fail_message'] += "Found match " + str(p_matches) + " times. <br>"
    return p_test_find_string


# Inputs: p_filename_data, contents of the file (string).
#         p_search_strings, list of what you are looking for, literally (string)
#         p_points, number of points this test is worth (int)
# Output: Dictionary of test_find_all_strings
# This module finds if all strings are there


def find_all_strings(p_filename_data, p_search_strings, p_points):

    passed = []
    debug = []
    for p_search_string in p_search_strings:
        test_find_string = find_string(p_filename_data, p_search_string, 1, 0)
        if test_find_string['pass']:
            passed.append(p_search_string)
            debug.append(test_find_string)

    p_test_find_strings = {"name": "Testing that ALL of these strings are there: " + str(p_search_strings) +
                                   " (" + str(p_points) + " points) <br>",
                           "pass": True,
                           "pass_message": "Pass! Found ALL of these these strings: " + str(p_search_strings) + ".<br>",
                           "fail_message": "Fail.  Didn't find all strings in " + str(p_search_strings) + ". <br" +
                                           " But did find these strings: " + str(passed) + ". <br>",
                           }
    if passed != p_search_strings:
        p_test_find_strings['pass'] = False
    return p_test_find_strings


# Inputs: p_filename_data, contents of the file (string).
#         p_search_string, what you are looking for, literally (string)
#         p_num_max, MAX number of times you can find the string
# Output: Dictionary of test_find_string
# This module finds if there is a string, maximum number of times


def find_string_max(p_filename_data, p_search_string, p_num_max, p_points):
    import re

    # test for a list that is created (i.e. abc = [asdf]
    p_matches = len(re.findall(p_search_string, p_filename_data, re.X | re.M | re.S))
    p_test_find_string = {"name": "Testing that this string is there maximum times: " +
                                  p_search_string + " (" + str(p_points) +
                                  " points) <br>",
                          "pass": True,
                          "pass_message": "Pass! Found this string: " + p_search_string + " no more than " +
                                          str(p_num_max) + " times. <br>",
                          "fail_message": "Fail.  Found this string " + p_search_string + " more than " +
                                          str(p_num_max) + "times. <br>",
                          }

    if p_matches > p_num_max:
        p_test_find_string['pass'] = False
    return p_test_find_string


# Inputs: p_filename_data, contents of the file (string).
#         p_function_name, function name I am looking for (string)
#         p_num_parameters, number of parameters I expect (integer)
# Output: Dictionary of test_function_exists
# This module finds if there is a function with a certain name and certain parameters


def find_function(p_filename, p_function_name, p_num_parameters):
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
                                      " with " + str(p_num_parameters) + " input parameters.",
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

# Input parameters: p_filename_data - contains the entire python file (string)
#                   p_num - minimum number of times you want to find a question (int).  i.e. you require minimum
#                           3 strings that look like blah = input('question here')
# Output: Dictionary of test_function_exists
# This module finds if user gets asked questions (input = ) a certain number of times


def find_questions(p_filename_data, p_num, p_points):

    import re

    matches = len(re.findall(r".{1,2} \s* = \s* input\(", p_filename_data, re.X | re.M | re.S))
    p_test_find_questions = {"name": "Testing that there are least " + str(p_num) + " questions (" + str(p_points) +
                                     " points)<br>",
                             "pass": True,
                             "pass_message": "Pass!  Code asks at least " + str(p_num) + " questions ",
                             "fail_message": "Fail.  Code does not ask at least " + str(p_num) + " questions .<br>" +
                                             "For now, autograder code will fail checks like "
                                             "abc = int(input('question') do it in two steps.<br>",
                             }
    if matches < p_num:
        p_test_find_questions['pass'] = False
        p_test_find_questions['fail_message'] += "<br>  Found this many questions: " + str(matches) + ".<br>"
    return p_test_find_questions


# Input parameters: p_filename_data - contains the entire python file (string)
#                   p_string - regex string that extracts the list you are looking for
# Output: list of items in the string
# This module finds a list with a particular name in the code and returns as list to user


def find_list_items(p_filename_data, p_string):

    import re

    p_search_object = re.search(p_string, p_filename_data, re.X | re.M | re.S)
    match = p_search_object.group(1)
    match = match.replace('"', '')
    match = match.replace("'", '')
    match = re.sub(r",\s+", "~", match)
    items = match.split('~')
    return items


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
    abc = find_list_items(filename_data, 'prizes \s* = \s* \[ (.+) \]')


