def green_flag(p_json, p_points):
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Testing that there is a green flag.  The rest of your code should be under the green flag " 
                      "(" + str(p_points) + " points)",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              "You have a green flag with a question and variable setting under it.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              "Did not find a green flag AND a question under the green flag AND setting a "
                              "variable setting under the green flag and question. <br>",
              'points': 0
              }
    test_flag = match_string(r'event_whenflagclicked', p_json)
    if test_flag['pass'] is False:
        p_test['fail_message'] += 'Did not find a green flag at all.'
    if test_flag['pass'] is False:
        p_test['fail_message'] += 'Did not find a green flag at all.'
    test_flag_and_question = match_string(r'event_whenflagclicked .+ sensing_askandwait', p_json)
    if test_flag_and_question['pass'] is False:
        p_test['fail_message'] += 'There needs to be a question under the flag.'
    test_flag_and_question_and_variable = match_string(r'event_whenflagclicked .+ sensing_askandwait .+'
                                                       r' data_setvariableto', p_json)

    test_flag_and_question_and_variable_2 = match_string(r'event_whenflagclicked .+ data_setvariableto .+ '
                                                         r'sensing_askandwait .+', p_json)
    if test_flag_and_question_and_variable['pass'] is False and test_flag_and_question_and_variable_2['pass'] is False:
        p_test['fail_message'] += 'There needs to be a question and setting a variable under the flag.'
    if test_flag['pass'] and test_flag_and_question['pass'] and (test_flag_and_question_and_variable['pass'] or
                                                                 test_flag_and_question_and_variable_2['pass']):
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def color_variables(p_scripts, p_points):
    """
    tests to see if set color to answer
    :param p_scripts: the scripts given by arrange_karel
    :param p_points: points this is worth
    :return: test dictionary
    """
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Testing that you are setting a variable 'color' to an answer to a question."
                      " (" + str(p_points) + " points).",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              " There is a setting a variable 'color' to an answer to a question.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              " Does not appear to be setting a variable 'color' to an answer to a question.<br>",
              'points': 0
              }

    for key in p_scripts:
        print("aaa script {}".format(p_scripts[key]))
        test_variable = match_string(r"\['data_setvariableto',\s'color',\s'sensing_answer']", p_scripts[key])
        if test_variable:
            p_test['pass'] = True
    print("aaa p_test['pass'] {}".format(p_test['pass']))
    if p_test['pass']:
        p_test['points'] += p_points
    return p_test


def test_color_change(p_scripts, p_points):
    """
    tests to see if stage changes color if it answers 'blue
    :param p_scripts: the scripts given by arrange_karel
    :param p_points: points this is worth
    :return: test dictionary
    """
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Testing that there is a background change if the user answers 'blue' for favorite color"
                      " (" + str(p_points) + " points).",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              " There is a background change if the user answers 'blue' for favorite color.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              " Does not appear to be  a background change if the user answers 'blue' for"
                              " favorite color. <br>",
              'points': 0
              }
    test_if = match_string(r'control_if .+ operator_equals .+ VARIABLE_color .+ blue', p_scripts)
    if test_if['pass'] is False:
        p_test['fail_message'] += 'Does not appear to be an if color = blue<br>' \
                                  'variable color must be exactly color (spelling and capitalization count) and ' \
                                  'blue must be exactly "blue" (spelling and capitalization count) <br>'
    test_if_change_nextbackdrop = match_string(r'control_if .+ operator_equals .+ VARIABLE_color .+ blue .+'
                                               r' (looks_switchbackdropto|looks_nextbackdrop)', p_scripts)
    test_receive_broadcast = match_string(r'event_whenbroadcastreceived .+ '
                                          r'(looks_switchbackdropto|looks_nextbackdrop)', p_scripts)
    test_if_broadcast = match_string(r'control_if .+ event_broadcast', p_scripts)
    if test_if['pass'] is False:
        p_test['fail_message'] += 'Does not appear to be an if color = blue<br>' \
                                  'variable color must be exactly color (spelling and capitalization count) and ' \
                                  'blue must be exactly "blue" (spelling and capitalization count) <br>'
    if not (test_if_change_nextbackdrop['pass'] or (test_receive_broadcast['pass'] and test_if_broadcast['pass'])):
        p_test['fail_message'] += 'You must have a switchbackdrop OR nextbackdrop inside your if.<br>' \
                                  'Alternatively, you can broadcast a message to the stage and have' \
                                  ' the stage change background.<br>'
    if test_if['pass'] and (test_if_change_nextbackdrop['pass'] or
                            (test_receive_broadcast['pass'] and test_if_broadcast['pass'])):
        p_test['pass'] = True
        p_test['points'] += p_points
    print(test_receive_broadcast['pass'])
    print(test_if_broadcast['pass'])

    return p_test


def one_question(p_scripts, p_points):
    """
    Tests to see if there is one reasonable question with an if/else and two says
    :param p_scripts: the scripts given by arrange_karel
    :param p_points: points this is worth
    :return: test dictionary
    """
    from app.scratch_labs.scratch import match_string

    p_test = {"name": "Testing that there is question being asked and a reply given depending on answer"
                      " (" + str(p_points) + " points).",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              " There is question being asked and a reply given depending on answer.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              " Does not appear that there is question being asked and a reply given depending "
                              "on answer. <br>",
              'points': 0
              }
    from app.scratch_labs.scratch import match_string
    test_q_and_if = match_string(r'sensing_askandwait .+ control_if_else', p_scripts)
    if test_q_and_if['pass'] is False:
        p_test['fail_message'] += "Does not appear that you have a question and an if/else.<br>" \
                                  "Need an if/else, because you will have a different response " \
                                  "depending on how the user answers the question.<br>"

    test_all_one = match_string(r'sensing_askandwait .+ control_if_else .+ \[ .+ \[ .+ looks_say .+ ] .+ '
                                r'\[ .+ looks_say .+ ] .+ ] ', p_scripts)

    if test_all_one['pass'] is False:
        p_test['fail_message'] += "Does not appear that you have a question AND an if/else AND two 'says' inside " \
                                  "the if/else.  <br>"
    if test_q_and_if['pass'] and test_all_one['pass']:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def two_question(p_scripts, p_points):
    """
    Tests to see if there is two reasonable question with an if/else and two says
    :param p_scripts: the scripts given by arrange_karel
    :param p_points: points this is worth
    :return: test dictionary
    """
    from app.scratch_labs.scratch import match_string

    p_test = {"name": "Testing that there are TWO questions being asked and a reply given depending on answer"
                      " (" + str(p_points) + " points).",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              " There is question being asked and a reply given depending on answer.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              " Does not appear that there is question being asked and a reply given depending "
                              "on answer. <br>",
              'points': 0
              }
    from app.scratch_labs.scratch import match_string
    test_all_two = match_string(r'sensing_askandwait .+ control_if_else .+ \[ .+ looks_say .+ ] .+ '
                                r'\[ .+ looks_say .+ ]  .+'
                                r'sensing_askandwait .+ control_if_else .+ \[ .+  looks_say .+ ] .+ '
                                r'\[ .+ looks_say .+ ]  .+ ', p_scripts)

    if test_all_two['pass'] is False:
        p_test['fail_message'] += "Does not appear that you have TWO question AND an if/else AND two 'says' inside " \
                                  "the if/else for both questions.  <br>"
    if test_all_two['pass']:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def name_variable_x4(p_scripts, p_points):
    """
    Tests to see if name variable shows up 4x.
    :param p_scripts: the scripts given by arrange_karel
    :param p_points: points this is worth
    :return: test dictionary
    """
    from app.scratch_labs.scratch import match_string

    p_test = {"name": "Testing that you using the name variable when talking to user."
                      " (" + str(p_points) + " points).",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              " You are using the name variable when talking to user.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              " Does not appear you using the name variable when talking to user. <br>"
                              "The name variable needs to show up 4 times.<br>",
              'points': 0
              }
    from app.scratch_labs.scratch import match_string
    test_name_x4 = match_string(r'VARIABLE_name .+ VARIABLE_name .+ VARIABLE_name .+ VARIABLE_name  ', p_scripts)

    if test_name_x4['pass'] is False:
        p_test['fail_message'] += "Does not appear that you are using the name variable when asking questions.<br>" \
                                 "Your question should be something like 'Mr. Kann, what is your favorite food?'<br>" \
                                 "You should NOT hard-code a particular name like Mr. Kann.  <br>Instead" \
                                 " you should use a variable so if the person answering questions changes " \
                                 "who they are, the program still works."
    if test_name_x4['pass']:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test
