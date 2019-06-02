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
# This module finds if there is a list


def find_string(p_filename_data, p_search_string, p_num):
    import re

    # test for a list that is created (i.e. abc = [asdf]
    p_matches = len(re.findall(p_search_string, p_filename_data, re.X | re.M | re.S))

    p_test_find_string = {"name": "Testing that this string is there: " + p_search_string + " (" + str(p_num) +
                                  ") points <br>",
                          "pass": True,
                          "pass_message": "Pass! Found this string: " + p_search_string,
                          "fail_message": "Fail.  Didn't find this string:" + p_search_string,
                          }

    if p_matches >= p_num:
        print("yes!!")
        p_test_find_string['pass'] = True
    else:
        print("no")
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
    p_test_find_questions = {"name": "Testing that genie asks at least " + str(p_num) + " questions (" + str(p_points) +
                                     " points)<br>",
                             "pass": True,
                             "pass_message": "Pass!  Genie asks at least " + str(p_num) + " questions ",
                             "fail_message": "Fail.  Code does not ask at least " + str(p_num) + " questions .<br>",
                             }
    if matches < p_num:
        p_test_find_questions['pass'] = False
        p_test_find_questions['fail_message'] += "<br>  Found this many questions: " + str(matches) + ".<br>"
    return p_test_find_questions


# Inputs: p_filename, filename to search for help.
# Output: p_tests, list of various tests.  Each test is a dictionary
# This module runs tests required for Python 1.040
if __name__ == "__main__":
    find_function('/tmp/abc.py', 'hello', 3)
    asdf = "input \( (\"') "
    filename_data = '# print("yes") wish1 = input("give me wish")n wish2 = input("give me wish")n wish3 = input("give me wish")  print("your wishes are " + wish1 + ", " + wish2 + ", " + wish3)# Joe helped me'
  #  asdf = 'print'
    find_string(filename_data, asdf, 1)
