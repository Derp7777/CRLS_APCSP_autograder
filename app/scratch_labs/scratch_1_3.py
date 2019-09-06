def press_zero(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch import match_string

    p_test = {"name": "Checking that there is a script that has 'when 0 key is pressed' along with a "
                      "pen down, goto 0 0, clear, and point 90. (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "We found the strings in the code!<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Code does not find string we were looking for.<br>"
                              "Be sure that there is only one 'when 0 key is pressed'<br>",
              "points": 0
              }
    print("aaa asdfasdf {} ".format(p_scripts))
    test_pendown = match_string(r"\['event_whenkeypressed', \s* '0'] .+ 'pen_penDown'", p_scripts)
    if test_pendown['pass'] is False:
        p_test['fail_message'] += "Did not find a when 0 pressed followed by a pen erase all.<br>"
    test_clear = match_string(r"\['event_whenkeypressed', \s* '0'] .+ 'pen_clear'", p_scripts)
    if test_clear['pass'] is False:
        p_test['fail_message'] += "Did not find a when 0 pressed followed by an erase all.<br>"
    test_point = match_string(r"\['event_whenkeypressed', \s* '0'] .+ \['motion_pointindirection', \s '90'],",
                              p_scripts)
    if test_point['pass'] is False:
        p_test['fail_message'] += "Did not find a when 0 pressed followed by a point in direction 90.<br>"
    test_goto = match_string(r"\['event_whenkeypressed', \s* '0'] .+ \['motion_gotoxy', \s '0', \s '0'],",
                             p_scripts)
    if test_goto['pass'] is False:
        p_test['fail_message'] += "Did not find a when 0 pressed followed by goto 0 0 .<br>"
    if test_pendown['pass'] and test_clear['pass'] and test_point['pass'] and test_goto['pass']:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def press_one(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch import match_string, unique_coordinates, is_square
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite

    p_test = {"name": "Checking that there is a script that has 'when 1 key is pressed' that draws a square"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a script that has 'when 1 key is pressed' that draws a "
                              "square.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not a script that has 'when 1 key is pressed' that draws a "
                              "square<br>",
              "points": 0
              }
    test_two = match_string(r"'event_whenkeypressed',\s'1'", p_scripts)
    sprite = brickLayer(0, 0, 0, pendown=False)
    if test_two['pass'] is False:
        p_test['fail_message'] += "Did not find a 'when key 1 is pressed' in the code .<br>"
    move_success = False
    if test_two['pass']:
        for key in p_scripts:
            script = p_scripts[key]
            if len(script) > 1:
                if script[0] == ['event_whenkeypressed', '1']:
                    move_success = do_sprite(sprite, script, True)
    coords = unique_coordinates(sprite.move_history)
    if len(coords) != 4:
        p_test['fail_message'] += "After pressing 1, sprite should land on 4 unique coordinates, but does not.<br>"
    square = is_square(coords)
    if square is False:
        p_test['fail_message'] += "Failed test for square <br>.<br>"
    if test_two['pass'] and square and move_success:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def press_two(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch import match_string, unique_coordinates, is_equilateral_triangle
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite

    p_test = {"name": "Checking that there is a script that has 'when 2 key is pressed' that draws an "
                      "equilateral triangle. (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a script that has 'when 2 key is pressed' that draws an "
                              "equilateral triangle.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not a script that has 'when 2 key is pressed' that draws an "
                              "equilateral triangle.<br>",
              "points": 0
              }
    test_two = match_string(r"'event_whenkeypressed',\s'2'", p_scripts)
    sprite = brickLayer(0, 0, 0, pendown=False)
    if test_two['pass'] is False:
        p_test['fail_message'] += "Did not find a 'when key 2 is pressed' in the code .<br>"
    move_success = False
    if test_two['pass']:
        for key in p_scripts:
            script = p_scripts[key]
            if len(script) > 1:
                if script[0] == ['event_whenkeypressed', '2']:
                    move_success = do_sprite(sprite, script, True)
    coords = unique_coordinates(sprite.move_history)
    if len(coords) != 3:
        p_test['fail_message'] += "After pressing 2, sprite should land on 3 unique coordinates, but does not.<br>"
    equilateral = is_equilateral_triangle(coords)
    if equilateral is False:
        p_test['fail_message'] += "Failed test for equilateral triangle (all sides equal length) <br>.<br>"
    if test_two['pass'] and equilateral and move_success:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test




# def press_two(p_json_data, p_points):
#     from app.scratch_labs.scratch import extract_move_steps, match_string
#     import re
#     p_test = {"name": "Checking that there is a script that has 'when 2 key is pressed' that draws an equilateral "
#                       "triangle. (" +
#                       str(p_points) + " points)<br>",
#               "pass": True,
#               "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
#                               "Pressing '2' draws an equilateral triangle!!<br>",
#               "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
#                               "Code does not match bank of correct answers.  Possible problems:<br>"
#                               "- Code has extra things (only use move and turn, and no more than required). <br>"
#                               "- Code is uneven (you should end up where you started, pointing in the same direction)."
#                               "<br> - You did a repeat, but did it a less-than ideal number of times."
#                               "<br> - You do not have any 'when 2 key is pressed'. "
#                               "<br> - You have more than one 'when 2 key is pressed'. <br>",
#               "points": 0
#               }
#
#     # Get move steps
#     move_steps = 0
#     for key in p_json_data:
#         match_two = re.search(r"{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':"
#                               r"\s+{'KEY_OPTION':\s+\['2',\s+None]}}", str(p_json_data[key]))
#         if match_two:
#             matches_move = extract_move_steps(p_json_data[key])
#             if matches_move:
#                 move_steps = str(matches_move[0])
#             else:
#                 p_test['pass'] = False
#                 return p_test
#     if move_steps == 0:
#         p_test['pass'] = False
#         return p_test
#
#     solution_1 = r"\[{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+" \
#                  r"{'KEY_OPTION':\s+\['2',\s+None]}},\s+"\
#                  r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" +\
#                  move_steps + r"']]},\s+'fields':\s+{}},\s+" \
#                  r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'120']]},\s+" \
#                               r"'fields':\s+{}},\s+" \
#                  r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
#                  move_steps + r"']]},\s+'fields':\s+{}},\s+" \
#                  r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'120']]},\s+" \
#                               r"'fields':\s+{}},\s+" \
#                  r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
#                  move_steps + r"']]},\s+'fields':\s+{}},\s+" \
#                  r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'120']]},\s+" \
#                               r"'fields':\s+{}}]"
#
#     solution_2 = r"\[{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+" \
#                  r"{'KEY_OPTION':\s+\['2',\s+None]}},\s+"\
#                  r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" +\
#                  move_steps + r"']]},\s+'fields':\s+{}},\s+" \
#                  r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'120']]},\s+" \
#                               r"'fields':\s+{}},\s+" \
#                  r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
#                  move_steps + r"']]},\s+'fields':\s+{}},\s+" \
#                  r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'120']]},\s+" \
#                               r"'fields':\s+{}},\s+" \
#                  r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
#                  move_steps + r"']]},\s+'fields':\s+{}},\s+" \
#                  r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'120']]},\s+" \
#                               r"'fields':\s+{}}]"
#
#     solution_3 = r"\[{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+" \
#                  r"{'KEY_OPTION':\s+\['2',\s+None]}},\s+" \
#                  r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'120']]},\s+" \
#                  r"'fields':\s+{}},\s+" \
#                  r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
#                  move_steps + r"']]},\s+'fields':\s+{}},\s+" \
#                  r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'120']]},\s+" \
#                  r"'fields':\s+{}},\s+" \
#                  r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
#                  move_steps + r"']]},\s+'fields':\s+{}},\s+" \
#                  r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'120']]},\s+" \
#                               r"'fields':\s+{}},\s+" \
#                  r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
#                  move_steps + r"']]},\s+'fields':\s+{}}]"
#
#     solution_4 = r"\[{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+" \
#                  r"{'KEY_OPTION':\s+\['2',\s+None]}},\s+" \
#                  r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'120']]},\s+" \
#                  r"'fields':\s+{}},\s+" \
#                  r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
#                  move_steps + r"']]},\s+'fields':\s+{}},\s+" \
#                  r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'120']]},\s+" \
#                  r"'fields':\s+{}},\s+" \
#                  r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
#                  move_steps + r"']]},\s+'fields':\s+{}},\s+" \
#                  r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'120']]},\s+"\
#                               \
#                               r"'fields':\s+{}},\s+" \
#                  r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
#                  move_steps + r"']]},\s+'fields':\s+{}}]"
#
#     solution_5 = r"\[{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+" \
#                  r"{'KEY_OPTION':\s+\['2',\s+None]}},\s+{'opcode':\s+'control_repeat',\s+" \
#                  r"'inputs':\s+{'TIMES':\s+\[1,\s+\[6,\s+'3']],\s+'SUBSTACK':\s+\[2,\s+'.+',\s+" \
#                  r"\[{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + move_steps + \
#                  r"']]}," \
#                  r"\s+'fields':\s+{}},\s+" \
#                  r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'120']]},\s+" \
#                  r"'fields':\s+{}}]]},\s+" \
#                  r"'fields':\s+{}}]"
#
#     solution_6 = r"\[{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+" \
#                  r"{'KEY_OPTION':\s+\['2',\s+None]}},\s+{'opcode':\s+'control_repeat',\s+" \
#                  r"'inputs':\s+{'TIMES':\s+\[1,\s+\[6,\s+'3']],\s+'SUBSTACK':\s+\[2,\s+'.+',\s+" \
#                  r"\[{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + move_steps + \
#                  r"']]}," \
#                  r"\s+'fields':\s+{}},\s+" \
#                  r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'120']]},\s+" \
#                  r"'fields':\s+{}}]]},\s+" \
#                  r"'fields':\s+{}}]"
#
#     solution_7 = r"\[{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+" \
#                  r"{'KEY_OPTION':\s+\['2',\s+None]}},\s+{'opcode':\s+'control_repeat',\s+" \
#                  r"'inputs':\s+{'TIMES':\s+\[1,\s+\[6,\s+'3']],\s+'SUBSTACK':\s+\[2,\s+'.+',\s+" \
#                  r"\[{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'120']]},\s+" \
#                  r"'fields':\s+{}},\s+" \
#                  r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + move_steps + \
#                  r"']]}," \
#                  r"\s+'fields':\s+{}}]]},\s+" \
#                  r"'fields':\s+{}}]"
#
#     solution_8 = r"\[{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+" \
#                  r"{'KEY_OPTION':\s+\['2',\s+None]}},\s+{'opcode':\s+'control_repeat',\s+" \
#                  r"'inputs':\s+{'TIMES':\s+\[1,\s+\[6,\s+'3']],\s+'SUBSTACK':\s+\[2,\s+'.+',\s+" \
#                  r"\[{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'120']]},\s+" \
#                  r"'fields':\s+{}},\s+" \
#                  r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + move_steps + \
#                  r"']]}," \
#                  r"\s+'fields':\s+{}}]]},\s+" \
#                  r"'fields':\s+{}}]"
#
#     script_of_interest = []
#     for key in p_json_data:
#         match_two = re.search(r"{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':"
#                               r"\s+{'KEY_OPTION':\s+\['2',\s+None]}}", str(p_json_data[key]))
#         if match_two:
#             script_of_interest = p_json_data[key]
#     if script_of_interest is False:
#         p_test['pass'] = False
#     else:
#         match_soln_one = match_string(solution_1, script_of_interest)
#         match_soln_two = match_string(solution_2, script_of_interest)
#         match_soln_three = match_string(solution_3, script_of_interest)
#         match_soln_four = match_string(solution_4, script_of_interest)
#         match_soln_five = match_string(solution_5, script_of_interest)
#         match_soln_six = match_string(solution_6, script_of_interest)
#         match_soln_seven = match_string(solution_7, script_of_interest)
#         match_soln_eight = match_string(solution_8, script_of_interest)
#         if match_soln_one['pass'] or match_soln_two['pass'] or match_soln_three['pass'] or match_soln_four['pass']\
#                 or match_soln_five['pass'] or match_soln_six['pass'] or match_soln_seven['pass']  \
#                 or match_soln_eight['pass']:
#             p_test['points'] += p_points
#         else:
#             p_test['pass'] = False
#     return p_test


def press_four(p_json_data, p_points):
    from app.scratch_labs.scratch import extract_move_steps, match_string
    import re
    p_test = {"name": "Checking that there is a script that has 'when 4 key is pressed' that draws a pentagon (" +
                      str(p_points) + " points)<br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '4' draws a pentagon!!<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Code does not match bank of correct answers.  Possible problems:<br>"
                              "- Code has extra things (only use move and turn, and no more than required). <br>"
                              "- Code is uneven (you should end up where you started, pointing in the same direction)."
                              "<br> - You did a repeat, but did it a less-than ideal number of times."
                              "<br> - You do not have any 'when 4 key is pressed'."
                              "<br> - You have more than one 'when 4 key is pressed'. <br>",
              "points": 0
              }

    # Get move steps
    move_steps = 0
    for key in p_json_data:
        match = re.search(r"{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':"
                          r"\s+{'KEY_OPTION':\s+\['4',\s+None]}}", str(p_json_data[key]))
        if match:
            matches_move = extract_move_steps(p_json_data[key])
            if matches_move:
                move_steps = str(matches_move[0])
            else:
                p_test['pass'] = False
                return p_test
    if move_steps == 0:
        p_test['pass'] = False
        return p_test
    solution_1 = r"\[{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+" \
                 r"{'KEY_OPTION':\s+\['4',\s+None]}},\s+"\
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" +\
                 move_steps + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'72']]},\s+" \
                              r"'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 move_steps + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'72']]},\s+" \
                              r"'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 move_steps + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'72']]},\s+" \
                              r"'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 move_steps + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'72']]},\s+" \
                              r"'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 move_steps + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'72']]},\s+" \
                              r"'fields':\s+{}}]"

    solution_2 = r"\[{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+" \
                 r"{'KEY_OPTION':\s+\['4',\s+None]}},\s+"\
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" +\
                 move_steps + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'72']]},\s+" \
                              r"'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 move_steps + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'72']]},\s+" \
                              r"'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 move_steps + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'72']]},\s+" \
                              r"'fields':\s+{}},\s+"\
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" +\
                 move_steps + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'72']]},\s+" \
                              r"'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 move_steps + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'72']]},\s+" \
                              r"'fields':\s+{}}]"

    solution_3 = r"\[{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+" \
                 r"{'KEY_OPTION':\s+\['4',\s+None]}},\s+" \
                 r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'72']]},\s+" \
                 r"'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 move_steps + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'72']]},\s+" \
                              r"'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 move_steps + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'72']]},\s+" \
                              r"'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 move_steps + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'72']]},\s+" \
                 r"'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 move_steps + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'72']]},\s+" \
                              r"'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 move_steps + r"']]},\s+'fields':\s+{}}]"

    solution_4 = r"\[{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+" \
                 r"{'KEY_OPTION':\s+\['4',\s+None]}},\s+" \
                 r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'72']]},\s+" \
                 r"'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 move_steps + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'72']]},\s+" \
                              r"'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 move_steps + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'72']]},\s+" \
                              r"'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 move_steps + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'72']]},\s+" \
                 r"'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 move_steps + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'72']]},\s+"\
                              \
                              r"'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 move_steps + r"']]},\s+'fields':\s+{}}]"

    solution_5 = r"\[{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+" \
                 r"{'KEY_OPTION':\s+\['4',\s+None]}},\s+{'opcode':\s+'control_repeat',\s+" \
                 r"'inputs':\s+{'TIMES':\s+\[1,\s+\[6,\s+'5']],\s+'SUBSTACK':\s+\[2,\s+'.+',\s+" \
                 r"\[{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + move_steps + \
                 r"']]}," \
                 r"\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'72']]},\s+" \
                 r"'fields':\s+{}}]]},\s+" \
                 r"'fields':\s+{}}]"

    solution_6 = r"\[{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+" \
                 r"{'KEY_OPTION':\s+\['4',\s+None]}},\s+{'opcode':\s+'control_repeat',\s+" \
                 r"'inputs':\s+{'TIMES':\s+\[1,\s+\[6,\s+'5']],\s+'SUBSTACK':\s+\[2,\s+'.+',\s+" \
                 r"\[{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + move_steps + \
                 r"']]}," \
                 r"\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'72']]},\s+" \
                 r"'fields':\s+{}}]]},\s+" \
                 r"'fields':\s+{}}]"

    solution_7 = r"\[{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+" \
                 r"{'KEY_OPTION':\s+\['4',\s+None]}},\s+{'opcode':\s+'control_repeat',\s+" \
                 r"'inputs':\s+{'TIMES':\s+\[1,\s+\[6,\s+'5']],\s+'SUBSTACK':\s+\[2,\s+'.+',\s+" \
                 r"\[{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'72']]},\s+" \
                 r"'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + move_steps + \
                 r"']]}," \
                 r"\s+'fields':\s+{}}]]},\s+" \
                 r"'fields':\s+{}}]"

    solution_8 = r"\[{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+" \
                 r"{'KEY_OPTION':\s+\['4',\s+None]}},\s+{'opcode':\s+'control_repeat',\s+" \
                 r"'inputs':\s+{'TIMES':\s+\[1,\s+\[6,\s+'5']],\s+'SUBSTACK':\s+\[2,\s+'.+',\s+" \
                 r"\[{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'72']]},\s+" \
                 r"'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + move_steps + \
                 r"']]}," \
                 r"\s+'fields':\s+{}}]]},\s+" \
                 r"'fields':\s+{}}]"

    script_of_interest = []
    for key in p_json_data:
        match = re.search(r"{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':"
                          r"\s+{'KEY_OPTION':\s+\['4',\s+None]}}", str(p_json_data[key]))
        if match:
            script_of_interest = p_json_data[key]
    if script_of_interest is False:
        p_test['pass'] = False
    else:
        match_soln_one = match_string(solution_1, script_of_interest)
        match_soln_two = match_string(solution_2, script_of_interest)
        match_soln_three = match_string(solution_3, script_of_interest)
        match_soln_four = match_string(solution_4, script_of_interest)
        match_soln_five = match_string(solution_5, script_of_interest)
        match_soln_six = match_string(solution_6, script_of_interest)
        match_soln_seven = match_string(solution_7, script_of_interest)
        match_soln_eight = match_string(solution_8, script_of_interest)
        if match_soln_one['pass'] or match_soln_two['pass'] or match_soln_three['pass'] or match_soln_four['pass']\
                or match_soln_five['pass'] or match_soln_six['pass'] or match_soln_seven['pass']  \
                or match_soln_eight['pass']:
            p_test['points'] += p_points
        else:
            p_test['pass'] = False
    return p_test


def press_five(p_json_data, p_points):
    from app.scratch_labs.scratch import extract_move_steps, match_string, extract_turn_degrees
    import re

    p_test = {"name": "Checking that there is a script that has 'when 5 key is pressed' that draws a parallelogram. (" +
                      str(p_points) + " points)<br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '5' draws a parallelogram!!<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Code does not match bank of correct answers.  Possible problems:<br>"
                              "- Draws a rhombus, not a parallelogram (rhombus sides are all same length but "
                              "parallelogram sides are not all same length) <br>"
                              "- Code has extra things (only use move and turn, and no more than required). <br>"
                              "- Code is uneven (you should end up where you started, pointing in the same direction)."
                              "<br> - You did a repeat, but did it a less-than ideal number of times."
                              "<br> - You do not have any 'when 5 key is pressed'."
                              "<br> - You have more than one 'when 5 key is pressed'. <br>",
              "points": 0
              }

    # Get move steps
    first_move = 0
    second_move = 0
    first_angle = 0
    second_angle = 0
    print(p_json_data)
    for key in p_json_data:
        print(p_json_data[key])
        match = re.search(r"{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':"
                          r"\s+{'KEY_OPTION':\s+\['5',\s+None]}}", str(p_json_data[key]))
        if match:
            matches_move = extract_move_steps(p_json_data[key])
            matches_turn = extract_turn_degrees(p_json_data[key])
            if matches_move:
                first_move = str(matches_move[0])
                second_move = str(matches_move[1])
            if matches_turn:
                first_angle = int(matches_turn[0][1])
                second_angle = 180 - first_angle
                first_angle = str(first_angle)
                second_angle = str(second_angle)
            else:
                p_test['pass'] = False
                return p_test
    if first_move == 0:
        p_test['pass'] = False
        return p_test
    print("MOVES AND ANGLES")
    if first_move == second_move:
        p_test['pass'] = False
        p_test['fail_message'] += 'This is the problem:<br>' \
                                  'First move and second move can not be equal (draw parallelogram not rhombus).<br>'
        return p_test
    print(first_move)
    print(second_move)
    print(first_angle)
    print(second_angle)
    solution_1 = r"\[{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+" \
                 r"{'KEY_OPTION':\s+\['5',\s+None]}},\s+"\
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" +\
                 first_move + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'" + first_angle + \
                 r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 second_move + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'" + second_angle + \
                 r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 first_move + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'" + first_angle + \
                 r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 second_move + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'" + second_angle + \
                 r"']]},\s+'fields':\s+{}}]"

    solution_2 = r"\[{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+" \
                 r"{'KEY_OPTION':\s+\['5',\s+None]}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 first_move + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'" + first_angle + \
                 r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 second_move + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'" + second_angle + \
                 r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 first_move + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'" + first_angle + \
                 r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 second_move + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'" + second_angle + \
                 r"']]},\s+'fields':\s+{}}]"

    solution_3 = r"\[{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+" \
                 r"{'KEY_OPTION':\s+\['5',\s+None]}},\s+" \
                 r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'" + first_angle + \
                 r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" +\
                 first_move + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'" + second_angle + \
                 r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 second_move + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'" + first_angle + \
                 r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 first_move + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'" + second_angle + \
                 r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 second_move + r"']]},\s+'fields':\s+{}}" \
                 r"]"

    solution_4 = r"\[{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+" \
                 r"{'KEY_OPTION':\s+\['5',\s+None]}},\s+" \
                 r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'" + first_angle + \
                 r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" +\
                 first_move + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'" + second_angle + \
                 r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 second_move + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'" + first_angle + \
                 r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 first_move + r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'" + second_angle + \
                 r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + \
                 second_move + r"']]},\s+'fields':\s+{}}" \
                 r"]"

    solution_5 = r"\[{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+" \
                 r"{'KEY_OPTION':\s+\['5',\s+None]}},\s+{'opcode':\s+'control_repeat',\s+" \
                 r"'inputs':\s+{'TIMES':\s+\[1,\s+\[6,\s+'2']],\s+'SUBSTACK':\s+\[2,\s+'.+',\s+" \
                 r"\[{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + first_move + \
                 r"']]}, \s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'" + first_angle + \
                 r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + second_move + \
                 r"']]}, \s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'" + second_angle + \
                 r"']]},\s+" \
                 r"'fields':\s+{}}" \
                 r"]]},\s+'fields':\s+{}}]"

    solution_6 = r"\[{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+" \
                 r"{'KEY_OPTION':\s+\['5',\s+None]}},\s+{'opcode':\s+'control_repeat',\s+" \
                 r"'inputs':\s+{'TIMES':\s+\[1,\s+\[6,\s+'2']],\s+'SUBSTACK':\s+\[2,\s+'.+',\s+" \
                 r"\[{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + first_move + \
                 r"']]}, \s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'" + first_angle + \
                 r"']]},\s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + second_move + \
                 r"']]}, \s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'" + second_angle + \
                 r"']]},\s+" \
                 r"'fields':\s+{}}" \
                 r"]]},\s+'fields':\s+{}}]"

    solution_7 = r"\[{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+" \
                 r"{'KEY_OPTION':\s+\['5',\s+None]}},\s+{'opcode':\s+'control_repeat',\s+" \
                 r"'inputs':\s+{'TIMES':\s+\[1,\s+\[6,\s+'2']],\s+'SUBSTACK':\s+\[2,\s+'.+',\s+" \
                 r"\[{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'" + first_angle + \
                 r"']]},\s+" \
                 r"'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + first_move + \
                 r"']]}, \s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnright',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'" + second_angle + \
                 r"']]},\s+" \
                 r"'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + second_move + \
                 r"']]}, \s+'fields':\s+{}}" \
                 r"]]},\s+'fields':\s+{}}]"

    solution_8 = r"\[{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+" \
                 r"{'KEY_OPTION':\s+\['5',\s+None]}},\s+{'opcode':\s+'control_repeat',\s+" \
                 r"'inputs':\s+{'TIMES':\s+\[1,\s+\[6,\s+'2']],\s+'SUBSTACK':\s+\[2,\s+'.+',\s+" \
                 r"\[{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'" + first_angle + \
                 r"']]},\s+" \
                 r"'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + first_move + \
                 r"']]}, \s+'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_turnleft',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'" + second_angle + \
                 r"']]},\s+" \
                 r"'fields':\s+{}},\s+" \
                 r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'" + second_move + \
                 r"']]}, \s+'fields':\s+{}}" \
                 r"]]},\s+'fields':\s+{}}]"

    script_of_interest = []
    for key in p_json_data:
        match_zero = re.search(r"{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':"
                               r"\s+{'KEY_OPTION':\s+\['5',\s+None]}}", str(p_json_data[key]))
        if match_zero:
            script_of_interest = p_json_data[key]
    if script_of_interest is False:
        p_test['pass'] = False
    else:
        match_soln_one = match_string(solution_1, script_of_interest)
        match_soln_two = match_string(solution_2, script_of_interest)
        match_soln_three = match_string(solution_3, script_of_interest)
        match_soln_four = match_string(solution_4, script_of_interest)
        match_soln_five = match_string(solution_5, script_of_interest)
        match_soln_six = match_string(solution_6, script_of_interest)
        match_soln_seven = match_string(solution_7, script_of_interest)
        match_soln_eight = match_string(solution_8, script_of_interest)
        if match_soln_one['pass'] or match_soln_two['pass'] or match_soln_three['pass'] or match_soln_four['pass']\
                or match_soln_five['pass'] or match_soln_six['pass'] or match_soln_seven['pass']  \
                or match_soln_eight['pass']:
            p_test['points'] += p_points
        else:
            p_test['pass'] = False
    return p_test
