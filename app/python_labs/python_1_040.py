def statement_variables(p_filename_data):

    from app.python_labs.find_items import find_questions, find_string

    p_test_find_six_questions = find_questions(p_filename_data, 5, 0)
    p_test_find_statement_variables = find_string(p_filename_data,
                                                  "[a-z0-9]{1,2} \s* = \s* input \( [^'\\\")]+ \) ", 3, 0)

    print(p_test_find_statement_variables)
    p_statement_variables = {"name": "Testing asks 6 question AND statements as variables. <br>" +
                                     "i.e. Checks that Genie put repeated strings into variables - "
                                     "see question 3. (5 points) <br>",
                             "pass": True,
                             "pass_message": "Pass! Found 6 questions AND they were variables. <br> ",
                             "fail_message": "Fail.  Result of finding 6 questions: " +
                                             str(p_test_find_six_questions['pass']) +
                                             "<br> Result of finding strings in variables: " +
                                             str(p_test_find_statement_variables['pass']) +
                                             "<br>  Both need to pass.<br> ",
                             }

    if not p_test_find_six_questions['pass'] or not p_test_find_statement_variables['pass']:
        p_statement_variables['pass'] = False

    return p_statement_variables


if __name__ == "__main__":
    print("yes")
    filename_data = 'abc = "gimme wish wish1 = input(abc) wish2 = input(abc) wish3 = input(abc) print("your wishes are " + wish1 + ", " + wish2 + ", " + wish3) wish4 = input(abc) wish5 = input(abc) wish6 = input(abc) print("your wishes are " + wish5 + ", " + wish6 + ", " + wish4) # Joe helped me'
    abc = statement_variables(filename_data)
    print(abc)
