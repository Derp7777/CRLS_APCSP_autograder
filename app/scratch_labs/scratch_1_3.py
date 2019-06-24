def press_zero(p_json_data, p_points):
    """

    :param p_json_data: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch import match_string
    import re

    p_test = {"name": "Checking that there is a script that has 'when 0 key is pressed' along with a "
                      "pen down, goto 0 0, clear, and point 90. (" + str(p_points) + " points)<br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "We found the strings in the code!<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Code does not find string we were looking for.<br>",
              "points": 0
              }
    zero_pen_down = \
        r"{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+{'KEY_OPTION':\s+\['0',\s+None\]}}" \
        r".+" \
        r"{'opcode':\s+'pen_penDown',\s+'inputs':\s+{},\s+'fields':\s+{}}"

    zero_goto_zero_zero = \
        r"{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+{'KEY_OPTION':\s+\['0',\s+None\]}}" \
        r".+" \
        r"{'opcode':\s+'motion_gotoxy',\s+'inputs':\s+{'X':\s+\[1,\s+\[4,\s+'0']]," \
        r"\s+'Y':\s+\[1,\s+\[4,\s+'0']]},\s+'fields':\s+{}}"

    zero_clear = \
        r"{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+{'KEY_OPTION':\s+\['0',\s+None\]}}" \
        r".+" \
        r"{'opcode':\s+'pen_clear',\s+'inputs':\s+{},\s+'fields':\s+{}}"

    zero_point_right = \
        r"{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+{'KEY_OPTION':\s+\['0',\s+None\]}}" \
        r".+" \
        r"{'opcode':\s+'motion_pointindirection',\s+" \
        r"'inputs':\s+{'DIRECTION':\s+\[1,\s+\[8,\s+'90']]},\s+'fields':\s+{}}"

    script_of_interest = []
    for key in p_json_data:
        print("SRIPT")
        print(p_json_data[key])
        match_zero = re.search(r"{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':"
                               r"\s+{'KEY_OPTION':\s+\['0',\s+None]}}", str(p_json_data[key]))
        if match_zero:
            script_of_interest = p_json_data[key]
    print("SCRipT OF INTERSET")
    print(script_of_interest)
    if script_of_interest is False:
        p_test['pass'] = False
    else:
        match_zero_pen_down = match_string(zero_pen_down, script_of_interest)
        if match_zero_pen_down['pass'] is False:
            p_test['fail_message'] += match_zero_pen_down['fail_message'] + "<br>" +\
                                      "Could not find Pen down inside when press zero. <br> "
        match_zero_goto_zero_zero = match_string(zero_goto_zero_zero, script_of_interest)
        if match_zero_goto_zero_zero['pass'] is False:
            p_test['fail_message'] += match_zero_goto_zero_zero['fail_message'] + "<br>" + \
                                      "Could not find go to zero zero inside when press zero.<br> "
        match_zero_clear = match_string(zero_clear, script_of_interest)
        if match_zero_clear['pass'] is False:
            p_test['fail_message'] += match_zero_clear['fail_message'] + "<br>" +\
                                      "Could not find erase all inside when press zero. <br> "
        match_zero_point_right = match_string(zero_point_right, script_of_interest)
        if match_zero_point_right['pass'] is False:
            p_test['fail_message'] += match_zero_point_right['fail_message'] + "<br>" +\
                                      "Could not find point 90 degrees (point to right) inside when press zero.<br> "
        if match_zero_pen_down['pass'] and match_zero_goto_zero_zero['pass'] and match_zero_clear['pass'] and \
                match_zero_point_right['pass']:
            p_test['points'] += p_points
        else:
            p_test['pass'] = False
    return p_test


def press_one(p_json_data, p_points):

    from app.scratch_labs.scratch import match_string
    import re

    [{'opcode': 'event_whenkeypressed', 'inputs': {}, 'fields': {'KEY_OPTION': ['1', None]}},
     {'opcode': 'motion_movesteps', 'inputs': {'STEPS': [1, [4, '100']]}, 'fields': {}},
     {'opcode': 'motion_turnleft', 'inputs': {'DEGREES': [1, [4, '90']]}, 'fields': {}},
     {'opcode': 'motion_movesteps', 'inputs': {'STEPS': [1, [4, '100']]}, 'fields': {}},
     {'opcode': 'motion_turnleft', 'inputs': {'DEGREES': [1, [4, '90']]}, 'fields': {}},
     {'opcode': 'motion_movesteps', 'inputs': {'STEPS': [1, [4, '100']]}, 'fields': {}},
     {'opcode': 'motion_turnleft', 'inputs': {'DEGREES': [1, [4, '90']]}, 'fields': {}},
     {'opcode': 'motion_movesteps', 'inputs': {'STEPS': [1, [4, '100']]}, 'fields': {}},
     {'opcode': 'motion_turnleft', 'inputs': {'DEGREES': [1, [4, '90']]}, 'fields': {}}]

    [{'opcode': 'event_whenkeypressed', 'inputs': {}, 'fields': {'KEY_OPTION': ['1', None]}},
     {'opcode': 'motion_turnleft', 'inputs': {'DEGREES': [1, [4, '90']]}, 'fields': {}},
     {'opcode': 'motion_movesteps', 'inputs': {'STEPS': [1, [4, '100']]}, 'fields': {}},
     {'opcode': 'motion_turnleft', 'inputs': {'DEGREES': [1, [4, '90']]}, 'fields': {}},
     {'opcode': 'motion_movesteps', 'inputs': {'STEPS': [1, [4, '100']]}, 'fields': {}},
     {'opcode': 'motion_turnleft', 'inputs': {'DEGREES': [1, [4, '90']]}, 'fields': {}},
     {'opcode': 'motion_movesteps', 'inputs': {'STEPS': [1, [4, '100']]}, 'fields': {}},
     {'opcode': 'motion_turnleft', 'inputs': {'DEGREES': [1, [4, '90']]}, 'fields': {}},
     {'opcode': 'motion_movesteps', 'inputs': {'STEPS': [1, [4, '100']]}, 'fields': {}}]

    [{'opcode': 'event_whenkeypressed', 'inputs': {}, 'fields': {'KEY_OPTION': ['1', None]}},
     {'opcode': 'motion_turnright', 'inputs': {'DEGREES': [1, [4, '90']]}, 'fields': {}},
     {'opcode': 'motion_movesteps', 'inputs': {'STEPS': [1, [4, '100']]}, 'fields': {}},
     {'opcode': 'motion_turnright', 'inputs': {'DEGREES': [1, [4, '90']]}, 'fields': {}},
     {'opcode': 'motion_movesteps', 'inputs': {'STEPS': [1, [4, '100']]}, 'fields': {}},
     {'opcode': 'motion_turnright', 'inputs': {'DEGREES': [1, [4, '90']]}, 'fields': {}},
     {'opcode': 'motion_movesteps', 'inputs': {'STEPS': [1, [4, '100']]}, 'fields': {}},
     {'opcode': 'motion_turnright', 'inputs': {'DEGREES': [1, [4, '90']]}, 'fields': {}},
     {'opcode': 'motion_movesteps', 'inputs': {'STEPS': [1, [4, '100']]}, 'fields': {}}]

    [{'opcode': 'event_whenkeypressed', 'inputs': {}, 'fields': {'KEY_OPTION': ['1', None]}},
     {'opcode': 'motion_movesteps', 'inputs': {'STEPS': [1, [4, '100']]}, 'fields': {}},
     {'opcode': 'motion_turnright', 'inputs': {'DEGREES': [1, [4, '90']]}, 'fields': {}},
     {'opcode': 'motion_movesteps', 'inputs': {'STEPS': [1, [4, '100']]}, 'fields': {}},
     {'opcode': 'motion_turnright', 'inputs': {'DEGREES': [1, [4, '90']]}, 'fields': {}},
     {'opcode': 'motion_movesteps', 'inputs': {'STEPS': [1, [4, '100']]}, 'fields': {}},
     {'opcode': 'motion_turnright', 'inputs': {'DEGREES': [1, [4, '90']]}, 'fields': {}},
     {'opcode': 'motion_movesteps', 'inputs': {'STEPS': [1, [4, '100']]}, 'fields': {}},
     {'opcode': 'motion_turnright', 'inputs': {'DEGREES': [1, [4, '90']]}, 'fields': {}}]



    p_test = {"name": "Checking that there is a script that has 'when 1 key is pressed' that draws a square. (" +
                      str(p_points) + " points)<br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '1' draws a square!!<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Code does not match bank of correct answers.  Possible problems:<br>"
                              "- Code has extra things (only use move and turn). <br>"
                              "- Code is uneven (you should end up where you started, pointing in the same direction."
                              "<br> - You did a repeat, but did it a less-than ideal number of times.<br> ",
              "points": 0
              }
    zero_pen_down = \
        r"{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+{'KEY_OPTION':\s+\['0',\s+None\]}}" \
        r".+" \
        r"{'opcode':\s+'pen_penDown',\s+'inputs':\s+{},\s+'fields':\s+{}}"

    zero_goto_zero_zero = \
        r"{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+{'KEY_OPTION':\s+\['0',\s+None\]}}" \
        r".+" \
        r"{'opcode':\s+'motion_gotoxy',\s+'inputs':\s+{'X':\s+\[1,\s+\[4,\s+'0']]," \
        r"\s+'Y':\s+\[1,\s+\[4,\s+'0']]},\s+'fields':\s+{}}"

    zero_clear = \
        r"{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+{'KEY_OPTION':\s+\['0',\s+None\]}}" \
        r".+" \
        r"{'opcode':\s+'pen_clear',\s+'inputs':\s+{},\s+'fields':\s+{}}"

    zero_point_right = \
        r"{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':\s+{'KEY_OPTION':\s+\['0',\s+None\]}}" \
        r".+" \
        r"{'opcode':\s+'motion_pointindirection',\s+" \
        r"'inputs':\s+{'DIRECTION':\s+\[1,\s+\[8,\s+'90']]},\s+'fields':\s+{}}"

    script_of_interest = []
    for key in p_json_data:
        print("SRIPT")
        print(p_json_data[key])
        match_zero = re.search(r"{'opcode':\s+'event_whenkeypressed',\s+'inputs':\s+{},\s+'fields':"
                               r"\s+{'KEY_OPTION':\s+\['0',\s+None]}}", str(p_json_data[key]))
        if match_zero:
            script_of_interest = p_json_data[key]
    print("SCRipT OF INTERSET")
    print(script_of_interest)
    if script_of_interest is False:
        p_test['pass'] = False
    else:
        match_zero_pen_down = match_string(zero_pen_down, script_of_interest)
        if match_zero_pen_down['pass'] is False:
            p_test['fail_message'] += match_zero_pen_down['fail_message'] + "<br>" +\
                                      "Could not find Pen down inside when press zero. <br> "
        match_zero_goto_zero_zero = match_string(zero_goto_zero_zero, script_of_interest)
        if match_zero_goto_zero_zero['pass'] is False:
            p_test['fail_message'] += match_zero_goto_zero_zero['fail_message'] + "<br>" + \
                                      "Could not find go to zero zero inside when press zero.<br> "
        match_zero_clear = match_string(zero_clear, script_of_interest)
        if match_zero_clear['pass'] is False:
            p_test['fail_message'] += match_zero_clear['fail_message'] + "<br>" +\
                                      "Could not find erase all inside when press zero. <br> "
        match_zero_point_right = match_string(zero_point_right, script_of_interest)
        if match_zero_point_right['pass'] is False:
            p_test['fail_message'] += match_zero_point_right['fail_message'] + "<br>" +\
                                      "Could not find point 90 degrees (point to right) inside when press zero.<br> "
        if match_zero_pen_down['pass'] and match_zero_goto_zero_zero['pass'] and match_zero_clear['pass'] and \
                match_zero_point_right['pass']:
            p_test['points'] += p_points
        else:
            p_test['pass'] = False
    return p_test
