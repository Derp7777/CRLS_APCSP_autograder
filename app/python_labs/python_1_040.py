def statement_variables(p_filename_data, p_points):
    """
    Statement variables checks to see if the statements inside the inputs are variables (since they are all the same)
    :param p_filename_data: the contents of the python file (string)
    :param p_points: number of points this question is worth (int)
    :return: dictionary which contains the info of the test
    """
    from app.python_labs.find_items import find_questions, find_string

    p_test_find_six_questions = find_questions(p_filename_data, 5, 0)
    p_test_find_statement_variables = find_string(p_filename_data,
                                                  r"[a-z0-9]{1,2} \s* = \s* input \( [^'\\\")]+ \) ", 3, 0)

    p_statement_variables = {"name": "Testing asks 6 question AND statements as variables. <br>" +
                                     "i.e. Checks that Genie put repeated strings into variables. "
                                     " (" + str(p_points) + ") <br>",
                             "pass": True,
                             "pass_message": "<h5 style=\"color:green;\">Pass!</h5>"
                                             " Found 6 questions AND they were variables. <br> ",
                             "fail_message": "<h5 style=\"color:red;\">Fail.</h5>  Result of finding 6 questions: " +
                                             str(p_test_find_six_questions['pass']) +
                                             "<br> Result of finding strings in variables: " +
                                             str(p_test_find_statement_variables['pass']) +
                                             "<br>  Both need to pass.<br> "
                                             "The ENTIRE string inside of input('question here')  needs to be a "
                                             "variable.  So for example input('Yo sucker ' + variable) will fail.<br>"
                                             "See question 3 on the assignment if you have no idea what this is.",
                             'points': 0
                             }

    if not p_test_find_six_questions['pass'] or not p_test_find_statement_variables['pass']:
        p_statement_variables['pass'] = False
    else:
        p_statement_variables['points'] += p_points
    return p_statement_variables


if __name__ == "__main__":
    print("yes")
    filename_data = 'abc = "gimme wish wish1 = input(abc) wish2 = input(abc) wish3 = ' \
                    'input(abc) print("your wishes are " + wish1 + ", " + wish2 + ", " + wish3) ' \
                    'wish4 = input(abc) wish5 = input(abc) wish6 = input(abc) ' \
                    'print("your wishes are " + wish5 + ", " + wish6 + ", " + wish4) # Joe helped me'
    abc = statement_variables(filename_data, 5)
    print(abc)
