def numbers_list(p_json, p_points):
    """
     verifies the 3 lists are there
     :param p_json: json of scratch file (dict)
     :param p_points: points this is worth (int)
     :return: a test dictionary
     """
    from app.scratch_labs.scratch import find_list
    p_test = {"name": "Checking that there is list that exists: numbers "
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "The list numbers exists .<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The list numbers does not exist.<br>"
                              "The lists must be named EXACTLY CORRECT with no caps and the 's' at the end.<br>"
                              "An 's' at the end tells you that it is plural (lists are potentially plural) and "
                              "this is a good trick to help you keep track of things.<br>",
              "points": 0
              }

    find_names = find_list(p_json, 'numbers', 5)
    if find_names['pass']:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def numbers_list_min_items(p_json, p_points):
    """
     verifies min number of items
     :param p_json: json of scratch file (dict)
     :param p_points: points this is worth (int)
     :return: a test dictionary
     """
    from app.scratch_labs.scratch import find_list
    p_test = {"name": "Checking that there is list numbers with minimum 4 items"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "The list numbers exists with minimum 4 items .<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The list numbers does not have 4 or more items.",
              "points": 0
              }

    find_numbers_items = find_list(p_json, 'numbers', 5,  min_items=4)
    if find_numbers_items['pass']:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def two_looks_ok(p_scripts, p_points):
    """
      :param p_scripts: json data from file, which is the code of the scratch file. (dict)
      :param p_points: Number of points this test is worth (int)
      :return: The test dictionary
      """
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that pressing '2' key looks approximately correct"
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '2' key looks approximately correct.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '2' key does not look approximately correct. <br>",
              "points": 0
              }

    press = '2'
    found_key = False
    for key in p_scripts:
        script = p_scripts[key]
        test_found_2 = match_string(r"event_whenkeypressed', \s '2'", script)
        if test_found_2['pass']:
            found_key = True
            test_setvar2 = match_string(r"event_whenkeypressed', \s '2' .+  data_setvariableto "
                                        r".+  data_setvariableto", script)

            test_repeat = match_string(r"event_whenkeypressed', \s '2' .+  control_repeat", script)
            test_changevar = match_string(r"event_whenkeypressed', \s '2' .+  control_repeat  "
                                          r".+  data_changevariableby .+  data_changevariableby ", script)
            test_looksay = match_string(r"event_whenkeypressed', \s '2'  .+  control_repeat "
                                        r".+ looks_sayforsecs", script)
    if found_key is False:
        p_test['fail_message'] += "Did not find 'when " + press + " key is pressed ' <br>"
    else:
        if test_setvar2['pass'] is False:
            p_test['fail_message'] += "Did not find any example of TWICE setting a variable after key is pressed.  You" \
                                      "will need a counter variable of some sort to loop through the list" \
                                      "and also a sum variable of some sort to keep track of sum.<br>"
        if test_repeat['pass'] is False:
            p_test['fail_message'] += "You need to loop through the list multiple times. " \
                                      " Need a repeat (or better, repeat until)" \
                                      " of some sort ' <br>"
        if test_changevar['pass'] is False:
            p_test['fail_message'] += "Did not find any example of TWICE changing a variable after key is pressed.  You" \
                                      "will need a counter variable of some sort to loop through the list" \
                                      "and also a sum variable of some sort to keep track of sum.<br>"
        if test_looksay['pass'] is False:
            p_test['fail_message'] += "You need to say the average at the end.  Needs a 'say for XXX seconds' " \
                                      "block after the repeat is over.<br>"

        if found_key and test_setvar2['pass'] and test_repeat['pass'] and test_changevar['pass'] and\
                test_looksay['pass']:
            p_test['pass'] = True
            p_test['points'] += p_points
    return p_test


def three_looks_ok(p_scripts, p_points):
    """
      :param p_scripts: json data from file, which is the code of the scratch file. (dict)
      :param p_points: Number of points this test is worth (int)
      :return: The test dictionary
      """
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that pressing '3' key looks approximately correct"
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '3' key looks approximately correct.  Note, there are many ways to solve"
                              "this problem so this test is not very exacting.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '3' key does not look approximately correct. <br>",
              "points": 0
              }

    press = '3'
    found_key = False
    for key in p_scripts:
        script = p_scripts[key]
        test_found_3 = match_string(r"event_whenkeypressed', \s '3'", script)
        if test_found_3['pass']:
            found_key = True
            test_setvar = match_string(r"event_whenkeypressed', \s '3' .+  data_setvariableto ", script)

            test_repeat = match_string(r"event_whenkeypressed', \s '3' .+  control_repeat", script)
            test_changevar = match_string(r"event_whenkeypressed', \s '3' .+  control_repeat  "
                                          r".+  data_changevariableby ", script)
            test_looksay = match_string(r"event_whenkeypressed', \s '3'  .+  control_repeat "
                                        r".+ looks_sayforsecs", script)
    if found_key is False:
        p_test['fail_message'] += "Did not find 'when " + press + " key is pressed ' <br>"
    else:
        if test_setvar['pass'] is False:
            p_test['fail_message'] += "Did not find any example of setting a variable after key is pressed.  You" \
                                      "will need a counter variable of some sort to loop through the list <br>"
        if test_repeat['pass'] is False:
            p_test['fail_message'] += "You need to loop through the list multiple times. " \
                                      " Need a repeat (or better, repeat until)" \
                                      " of some sort ' <br>"
        if test_changevar['pass'] is False:
            p_test['fail_message'] += "Did not find any example of changing a variable after key is pressed.  You" \
                                      "will need a counter variable of some sort to loop through the list <br>"
        if test_looksay['pass'] is False:
            p_test['fail_message'] += "You need to say True or False at the end.  Needs a 'say for XXX seconds' " \
                                      "block after the repeat is over.<br>"

        if found_key and test_setvar['pass'] and test_repeat['pass'] and test_changevar['pass'] and\
                test_looksay['pass']:
            p_test['pass'] = True
            p_test['points'] += p_points
    return p_test


def four_looks_ok(p_scripts, p_points):
    """
      :param p_scripts: json data from file, which is the code of the scratch file. (dict)
      :param p_points: Number of points this test is worth (int)
      :return: The test dictionary
      """
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that pressing '4' key looks approximately correct"
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '4' key looks approximately correct.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '4' key does not look approximately correct. <br>",
              "points": 0
              }

    press = '4'
    found_key = False
    for key in p_scripts:
        script = p_scripts[key]
        test_found_4 = match_string(r"event_whenkeypressed', \s '4'", script)
        if test_found_4['pass']:
            found_key = True
            test_setvar2 = match_string(r"event_whenkeypressed', \s '4' .+  data_setvariableto "
                                        r".+  data_setvariableto", script)

            test_repeat = match_string(r"event_whenkeypressed', \s '4' .+  control_repeat", script)
            test_changevar = match_string(r"event_whenkeypressed', \s '4' .+  control_repeat  "
                                          r".+  data_changevariableby ", script)
            test_if = match_string(r"event_whenkeypressed', \s '4' .+ control_repeat  .+ control_if", script)
            test_looksay = match_string(r"event_whenkeypressed', \s '4'  .+  control_repeat "
                                        r".+ looks_sayforsecs", script)
    if found_key is False:
        p_test['fail_message'] += "Did not find 'when " + press + " key is pressed ' <br>"
    else:
        if test_setvar2['pass'] is False:
            p_test['fail_message'] += "Did not find any example of TWICE setting a variable after key is pressed.  " \
                                      "You" \
                                      "will need a counter variable of some sort to loop through the list " \
                                      "and also a max variable of some sort to keep track of max.<br>"
        if test_repeat['pass'] is False:
            p_test['fail_message'] += "You need to loop through the list multiple times. " \
                                      " Need a repeat (or better, repeat until)" \
                                      " of some sort ' <br>"

        if test_if['pass'] is False:
            p_test['fail_message'] += "You need an 'if' of some sort inside the loop" \
                                      " to test to see if number is the maximum" \
                                      ".<br>"

        if test_changevar['pass'] is False:
            p_test['fail_message'] += "Did not find any example of changing a variable after key is pressed.  You" \
                                      "will need a counter variable of some sort to loop through the list" \
                                      " .<br>"
        if test_looksay['pass'] is False:
            p_test['fail_message'] += "You need to say the average at the end.  Needs a 'say for XXX seconds' " \
                                      "block after the repeat is over.<br>"

        if found_key and test_setvar2['pass'] and test_repeat['pass'] and test_changevar['pass'] and\
                test_looksay['pass']:
            p_test['pass'] = True
            p_test['points'] += p_points
    return p_test


def five_looks_ok(p_scripts, p_points):
    """
      :param p_scripts: json data from file, which is the code of the scratch file. (dict)
      :param p_points: Number of points this test is worth (int)
      :return: The test dictionary
      """
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that pressing '5' key looks approximately correct"
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '5' key looks approximately correct.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '5' key does not look approximately correct. <br>",
              "points": 0
              }

    press = '5'
    found_key = False
    for key in p_scripts:
        script = p_scripts[key]
        test_found_5 = match_string(r"event_whenkeypressed', \s '5'", script)
        if test_found_5['pass']:
            found_key = True
            test_setvar = match_string(r"event_whenkeypressed', \s '5' .+  data_setvariableto ", script)

            test_delete_list = match_string(r"event_whenkeypressed', \s '5' .+  data_deletealloflist ", script)
            test_repeat = match_string(r"event_whenkeypressed', \s '5' .+  control_repeat", script)
            test_changevar = match_string(r"event_whenkeypressed', \s '5' .+  control_repeat  "
                                          r".+  data_changevariableby ", script)
            test_if = match_string(r"event_whenkeypressed', \s '5' .+ control_repeat  .+ control_if", script)
            test_looksay = match_string(r"event_whenkeypressed', \s '5'  .+  control_repeat "
                                        r".+ looks_sayforsecs", script)
    if found_key is False:
        p_test['fail_message'] += "Did not find 'when " + press + " key is pressed ' <br>"
    else:
        if test_setvar['pass'] is False:
            p_test['fail_message'] += "Did not find any example of setting a variable after key is pressed.  " \
                                      "You" \
                                      "will need a counter variable of some sort to loop through the list.<br>"

        if test_delete_list['pass'] is False:
            p_test['fail_message'] += "Did not find any example of deleting everything in list after key is pressed.  " \
                                      "The program assumes you created a list already.  This list will need to be blank" \
                                      "as each time you run the program you will be tarting this new list over.<br>"
        if test_repeat['pass'] is False:
            p_test['fail_message'] += "You need to loop through the list multiple times. " \
                                      " Need a repeat (or better, repeat until)" \
                                      " of some sort ' <br>"

        if test_if['pass'] is False:
            p_test['fail_message'] += "You need an 'if' of some sort inside the loop" \
                                      " to test to see if number is negative or positive" \
                                      ".<br>"

        if test_changevar['pass'] is False:
            p_test['fail_message'] += "Did not find any example of changing a variable after key is pressed.  You" \
                                      "will need a counter variable of some sort to loop through the list" \
                                      " .<br>"
        if test_looksay['pass'] is False:
            p_test['fail_message'] += "You need to say the new list at the end.  Needs a 'say for XXX seconds' " \
                                      "block after the repeat is over.<br>"

        if found_key and test_setvar['pass'] and  test_delete_list['pass'] and \
                test_repeat['pass'] and test_changevar['pass'] and\
                test_looksay['pass']:
            p_test['pass'] = True
            p_test['points'] += p_points
    return p_test


def six_looks_ok(p_scripts, p_points):
    """
      :param p_scripts: json data from file, which is the code of the scratch file. (dict)
      :param p_points: Number of points this test is worth (int)
      :return: The test dictionary
      """
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that pressing '6' key looks approximately correct"
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '6' key looks approximately correct.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '6' key does not look approximately correct. <br>",
              "points": 0
              }

    press = '6'
    found_key = False
    for key in p_scripts:
        script = p_scripts[key]
        test_found_6 = match_string(r"event_whenkeypressed', \s '6'", script)
        if test_found_6['pass']:
            found_key = True
            test_setvar = match_string(r"event_whenkeypressed', \s '6' .+  data_setvariableto ", script)

            test_delete_list = match_string(r"event_whenkeypressed', \s '6' .+  data_deletealloflist ", script)
            test_repeat = match_string(r"event_whenkeypressed', \s '6' .+  control_repeat", script)
            test_changevar = match_string(r"event_whenkeypressed', \s '6' .+  control_repeat  "
                                          r".+  data_changevariableby ", script)
            test_if = match_string(r"event_whenkeypressed', \s '6' .+ control_repeat  .+ control_if", script)
            test_looksay = match_string(r"event_whenkeypressed', \s '6'  .+  control_repeat "
                                        r".+ looks_sayforsecs", script)
            test_mod = match_string(r"event_whenkeypressed', \s '6'  .+  control_repeat "
                                    r".+ operator_mod", script)
    if found_key is False:
        p_test['fail_message'] += "Did not find 'when " + press + " key is pressed ' <br>"
    else:
        if test_setvar['pass'] is False:
            p_test['fail_message'] += "Did not find any example of setting a variable after key is pressed.  " \
                                      "You" \
                                      "will need a counter variable of some sort to loop through the list.<br>"

        if test_delete_list['pass'] is False:
            p_test['fail_message'] += "Did not find any example of deleting everything in list after key is pressed.  " \
                                      "The program assumes you created a list already.  This list will need to be blank" \
                                      "as each time you run the program you will be tarting this new list over.<br>"
        if test_repeat['pass'] is False:
            p_test['fail_message'] += "You need to loop through the list multiple times. " \
                                      " Need a repeat (or better, repeat until)" \
                                      " of some sort ' <br>"

        if test_if['pass'] is False:
            p_test['fail_message'] += "You need an 'if' of some sort inside the loop" \
                                      " to test to see if number is negative or positive" \
                                      ".<br>"

        if test_changevar['pass'] is False:
            p_test['fail_message'] += "Did not find any example of changing a variable after key is pressed.  You" \
                                      "will need a counter variable of some sort to loop through the list" \
                                      " .<br>"
        if test_looksay['pass'] is False:
            p_test['fail_message'] += "You need to say the new list at the end.  Needs a 'say for XXX seconds' " \
                                      "block after the repeat is over.<br>"
        if test_mod['pass'] is False:
            p_test['fail_message'] += "You need to say mod in the loop to test if a number is even.<br>"

        if found_key and test_setvar['pass'] and  test_delete_list['pass'] and \
                test_repeat['pass'] and test_changevar['pass'] and\
                test_looksay['pass'] and test_mod['pass']:
            p_test['pass'] = True
            p_test['points'] += p_points
    return p_test


def one_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that pressing '1' key sums up the numbers in the list.  See instructions "
                      "from what this should look like "
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '1' key sums up the numbers in the list.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '1' key does not sums up the numbers in the list. <br><br>",
              "points": 0
              }
    found_1 = False
    test_1 = False
    test_2 = False
    test_3 = False

    for key in p_scripts:
        script = p_scripts[key]
        test_1_key = match_string(r"event_whenkeypressed', \s '1' .+  data_setvariableto .+ control_repeat .+ "
                                  r"looks_sayforsecs", script)
        if test_1_key['pass']:
            found_1 = True
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"numbers": [5, 2, -4, 0, ]
                                                                   })
            run_1 = do_sprite(sprite, script, True)
            match_this = r"^3"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_1 = True
            if test_1 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['5, 2, -4, 0']<br> " \
                                          "Expected output: <br>3 <br><br>" \
                                          "Actual output: <br>" + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"numbers": [999, ]})
            run_2 = do_sprite(sprite, script, True)
            match_this = r"^999"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_2 = True
            if test_2 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: [999]<br> " \
                                          "Expected output: <br>999<br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"
            print("eee start 1c")
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"numbers": [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555, ]
                                                                   })
            run_3 = do_sprite(sprite, script, True)
            match_this = r"^555"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_3 = True
            if test_3 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555,]<br> " \
                                          "Expected output: <br>555 <br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"

    if found_1 is False:
        p_test['fail_message'] += "In your code, did not find 'when 1 key pressed' in your code " \
                                  "followed by some expected elements - setting a variable to a value " \
                                  "(to track the index or counter)," \
                                  "a repeat of some sort, and a say of some sort.<br><br>"

    p_test['fail_message'] += "<b>Be sure you are not hard-coding the number of items in the list.</b><br>" \
                              "The code has to work with lists of length 1 and 5 (and 205), not just length 4.<br>"
    if found_1 and test_1 and test_2 and test_3 and run_1 and run_2 and run_3:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def two_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that pressing '2' key gives average of the numbers in the list.  See instructions "
                      "from what this should look like "
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '2' key gives average of the numbers in the list.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '2' key does not give average of the numbers in the list. <br><br>",
              "points": 0
              }
    found_2 = False
    test_1 = False
    test_2 = False
    test_3 = False

    for key in p_scripts:
        script = p_scripts[key]
        test_2_key = match_string(r"event_whenkeypressed', \s '2' .+  data_setvariableto .+ control_repeat .+ "
                                  r"looks_sayforsecs", script)
        if test_2_key['pass']:
            found_2 = True
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"numbers": [5, 2, -4, 0, ]
                                                                   })
            run_1 = do_sprite(sprite, script, True)
            match_this = r"^0\.75"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_1 = True
            if test_1 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['5, 2, -4, 0']<br> " \
                                          "Expected output: <br>3 <br><br>" \
                                          "Actual output: <br>" + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"numbers": [999, ]})
            run_2 = do_sprite(sprite, script, True)
            match_this = r"^999"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_2 = True
            if test_2 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: [999]<br> " \
                                          "Expected output: <br>999<br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"numbers": [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555, ]
                                                                   })
            run_3 = do_sprite(sprite, script, True)
            match_this = r"^50\.45"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_3 = True
            if test_3 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555,]<br> " \
                                          "Expected output: <br>50.454545 <br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"

    if found_2 is False:
        p_test['fail_message'] += "In your code, did not find 'when 2 key pressed' in your code " \
                                  "followed by some expected elements - setting a variable to a value " \
                                  "(to track the index or counter)," \
                                  "a repeat of some sort, and a say of some sort.<br><br>"

    p_test['fail_message'] += "<b>Be sure you are not hard-coding the number of items in the list.</b><br>" \
                              "The code has to work with lists of length 1 and 5 (and 205), not just length 4.<br>"
    if found_2 and test_1 and test_2 and test_3 and run_1 and run_2 and run_3:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def three_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that pressing '3' key says 'True' if there is a negative number, 'False' if not."
                      "  See instructions "
                      "from what this should look like "
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '3' key says 'True' if there is a negative number, 'False' if not.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '3' key does not says 'True' if there is a negative number, "
                              "'False' if not. <br><br>",
              "points": 0
              }
    found_3 = False
    test_1 = False
    test_2 = False
    test_3 = False

    for key in p_scripts:
        script = p_scripts[key]
        test_3_key = match_string(r"event_whenkeypressed', \s '3' .+  data_setvariableto .+ control_repeat .+ "
                                  r"looks_sayforsecs", script)
        if test_3_key['pass']:
            found_3 = True
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"numbers": [5, 2, -4, 0, ]
                                                                   })
            run_1 = do_sprite(sprite, script, True)
            match_this = r"^True"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_1 = True
            if test_1 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['5, 2, -4, 0']<br> " \
                                          "Expected output: <br>True <br><br>" \
                                          "Actual output: <br>" + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"numbers": [999, ]})
            run_2 = do_sprite(sprite, script, True)
            match_this = r"^False"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_2 = True
            if test_2 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: [999]<br> " \
                                          "Expected output: <br>False<br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"numbers": [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555, ]
                                                                   })
            run_3 = do_sprite(sprite, script, True)
            match_this = r"^True"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_3 = True
            if test_3 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555,]<br> " \
                                          "Expected output: <br>True <br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"

    if found_3 is False:
        p_test['fail_message'] += "In your code, did not find 'when 3 key pressed' in your code " \
                                  "followed by some expected elements - setting a variable to a value " \
                                  "(to track the index or counter)," \
                                  "a repeat of some sort, and a say of some sort.<br><br>"

    p_test['fail_message'] += "<b>Be sure you are not hard-coding the number of items in the list.</b><br>" \
                              "The code has to work with lists of length 1 and 5 (and 205), not just length 4.<br>"
    if found_3 and test_1 and test_2 and test_3 and run_1 and run_2 and run_3:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def four_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that pressing '4' key says the maximum number of the list. "
                      "  See instructions "
                      "from what this should look like "
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '4' key says says the maximum number of the list.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '4' key does not say the maximum number of the list. <br><br>",
              "points": 0
              }
    found_4 = False
    test_1 = False
    test_2 = False
    test_3 = False

    for key in p_scripts:
        script = p_scripts[key]
        test_4_key = match_string(r"event_whenkeypressed', \s '4' .+  data_setvariableto .+ control_repeat .+ "
                                  r"looks_sayforsecs", script)
        if test_4_key['pass']:
            found_4 = True
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"numbers": [5, 2, -4, 0, ]
                                                                   })
            run_1 = do_sprite(sprite, script, True)
            match_this = r"^5"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_1 = True
            if test_1 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['5, 2, -4, 0']<br> " \
                                          "Expected output: <br>5 <br><br>" \
                                          "Actual output: <br>" + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"numbers": [999, ]})
            run_2 = do_sprite(sprite, script, True)
            match_this = r"^999"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_2 = True
            if test_2 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: [999]<br> " \
                                          "Expected output: <br>999<br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"numbers": [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555, ]
                                                                   })
            run_3 = do_sprite(sprite, script, True)
            match_this = r"^555"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_3 = True
            if test_3 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555,]<br> " \
                                          "Expected output: <br>555 <br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"

    if found_4 is False:
        p_test['fail_message'] += "In your code, did not find 'when 4 key pressed' in your code " \
                                  "followed by some expected elements - setting a variable to a value " \
                                  "(to track the index or counter)," \
                                  "a repeat of some sort, and a say of some sort.<br><br>"

    p_test['fail_message'] += "<b>Be sure you are not hard-coding the number of items in the list.</b><br>" \
                              "The code has to work with lists of length 1 and 5 (and 205), not just length 4.<br>"
    if found_4 and test_1 and test_2 and test_3 and run_1 and run_2 and run_3:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def five_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that pressing '5' key makes and says "
                      "a new list, same as the old list but all numbers positive."
                      "  See instructions "
                      "from what this should look like "
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '5' key makes a new list, same as the old list but all numbers positive.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '5' key does not  make a new list same as the old list but "
                              "all numbers positive.<br>"
                              "Your new list MUST be called new_list."
                              " <br><br>",
              "points": 0
              }
    found_5 = False
    test_1 = False
    test_2 = False
    test_3 = False

    for key in p_scripts:
        script = p_scripts[key]
        test_5_key = match_string(r"event_whenkeypressed', \s '5' .+  data_setvariableto .+ control_repeat .+ "
                                  r"looks_sayforsecs", script)
        if test_5_key['pass']:
            found_5 = True
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"numbers": [5, 2, -4, 0, ], 'new_list': [3, 1],
                                                                   })
            run_1 = do_sprite(sprite, script, True)
            match_this = r"^\['5',\s*'2',\s*'4',\s*'0']"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_1 = True
            if test_1 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['5, 2, -4, 0']<br> " \
                                          "Expected output: <br>['5', '2', '4', '0'] <br><br>" \
                                          "Actual output: <br>" + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"numbers": [999, ], 'new_list': [3, 1], })
            run_2 = do_sprite(sprite, script, True)
            match_this = r"^\['999']"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_2 = True
            if test_2 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: [999]<br> " \
                                          "Expected output: <br>['999']<br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"numbers": [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555, ]
                                                                   , 'new_list': [3, 1],})
            run_3 = do_sprite(sprite, script, True)
            match_this = r"^\['1',\s*'2',\s*'3',\s*'4',\s*'5',\s*'1',\s*'2',\s*'3',\s*'4',\s*'5',\s*'555']"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_3 = True
            if test_3 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555,]<br> " \
                                          "Expected output: <br>['1', '2', '3', '4', '5', '1', " \
                                          "'2', '3', '4', '5', '555'] <br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"

    if found_5 is False:
        p_test['fail_message'] += "In your code, did not find 'when 5 key pressed' in your code " \
                                  "followed by some expected elements - setting a variable to a value " \
                                  "(to track the index or counter)," \
                                  "a repeat of some sort, and a say of some sort.<br><br>"

    p_test['fail_message'] += "<b>Be sure you are not hard-coding the number of items in the list.</b><br>" \
                              "The code has to work with lists of length 1 and 5 (and 205), not just length 4.<br>"
    if found_5 and test_1 and test_2 and test_3 and run_1 and run_2 and run_3:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def six_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that pressing '6' key makes and says "
                      "a new list, with only even numbers from original list."
                      "  See instructions "
                      "from what this should look like "
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '6' key makes and says a new list, "
                              "with only even numbers from original list.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '6' key does not make a new list with only even numbers from original list.<br>"
                              "Your new list MUST be called new_list."
                              " <br><br>",
              "points": 0
              }
    found_6 = False
    test_1 = False
    test_2 = False
    test_3 = False

    for key in p_scripts:
        script = p_scripts[key]
        test_6_key = match_string(r"event_whenkeypressed', \s '6' .+  data_setvariableto .+ control_repeat .+ "
                                  r"looks_sayforsecs", script)
        if test_6_key['pass']:
            found_6 = True
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"numbers": [5, 2, -4, 0, ], 'new_list': [3, 1],
                                                                   })
            run_1 = do_sprite(sprite, script, True)
            match_this = r"^\['2',\s*'-4',\s*'0']"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_1 = True
            if test_1 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['5, 2, -4, 0']<br> " \
                                          "Expected output: <br>['2', '-4', '0'] <br><br>" \
                                          "Actual output: <br>" + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"numbers": [999, ], 'new_list': [3, 1], })
            run_2 = do_sprite(sprite, script, True)
            match_this = r"^\[]"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_2 = True
            if test_2 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: [999]<br> " \
                                          "Expected output: <br><br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"numbers": [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555, ]
                                                                   , 'new_list': [3, 1], })
            run_3 = do_sprite(sprite, script, True)
            match_this = r"^\['2',\s*'4',\s*'-2',\s*'-4']"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_3 = True
            if test_3 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555,]<br> " \
                                          "Expected output: <br>['2', '4', " \
                                          "'-2', '-4'] <br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"

    if found_6 is False:
        p_test['fail_message'] += "In your code, did not find 'when 6 key pressed' in your code " \
                                  "followed by some expected elements - setting a variable to a value " \
                                  "(to track the index or counter)," \
                                  "a repeat of some sort, and a say of some sort.<br><br>"

    p_test['fail_message'] += "<b>Be sure you are not hard-coding the number of items in the list.</b><br>" \
                              "The code has to work with lists of length 1 and 5 (and 205), not just length 4.<br>"
    if found_6 and test_1 and test_2 and test_3 and run_1 and run_2 and run_3:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def seven_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that pressing '7' key makes and says "
                      "'True' if numbers are ascending, 'False' if numbers are descending."
                      "  See instructions "
                      "from what this should look like "
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '7' key says 'True' if numbers are ascending, "
                              "'False' if numbers are descending.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '7' key does not say 'True' if numbers are ascending, "
                              "'False' if numbers are descending."
                              " <br><br>",
              "points": 0
              }
    found_7 = False
    test_1 = False
    test_2 = False
    test_3 = False
    test_4 = False
    for key in p_scripts:
        script = p_scripts[key]
        test_7_key = match_string(r"event_whenkeypressed', \s '7' .+  data_setvariableto .+ control_repeat .+ "
                                  r"looks_sayforsecs", script)
        if test_7_key['pass']:
            found_7 = True
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"numbers": [5, 2, -4, 0, ], 'new_list': [3, 1],
                                                                   })
            run_1 = do_sprite(sprite, script, True)
            match_this = r"^False"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_1 = True
            if test_1 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['5, 2, -4, 0']<br> " \
                                          "Expected output: <br>False <br><br>" \
                                          "Actual output: <br>" + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"numbers": [999, ], 'new_list': [3, 1], })
            run_2 = do_sprite(sprite, script, True)
            match_this = r"^True"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_2 = True
            if test_2 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: [999]<br> " \
                                          "Expected output: <br>True<br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"numbers": [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555, ]
                                                                   , 'new_list': [3, 1], })
            run_3 = do_sprite(sprite, script, True)
            match_this = r"^False"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_3 = True
            if test_3 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555,]<br> " \
                                          "Expected output: <br>False <br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"numbers": [1, 5, 7, 9, 15, ], 'new_list': [3, 1], })
            run_4 = do_sprite(sprite, script, True)
            match_this = r"^True"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_4 = True
            if test_4 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: [1, 5, 7, 9, 15,]<br> " \
                                          "Expected output: <br>True <br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"

    if found_7 is False:
        p_test['fail_message'] += "In your code, did not find 'when 7 key pressed' in your code " \
                                  "followed by some expected elements - setting a variable to a value " \
                                  "(to track the index or counter)," \
                                  "a repeat of some sort, and a say of some sort.<br><br>"

    p_test['fail_message'] += "<b>Be sure you are not hard-coding the number of items in the list.</b><br>" \
                              "The code has to work with lists of length 1 and 5 (and 205), not just length 4.<br>"
    if found_7 and test_1 and test_2 and test_3 and test_4 and run_1 and run_2 and run_3 and run_4:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def eight_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that pressing '8' key takes a list number1, a second list number2,"
                      "adds them together to make new_list, and says new_list."
                      "  See instructions "
                      "from what this should look like "
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '8' key takes a list number1, a second list number2,"
                              "adds them together to make new_list, and says new_list.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '8' key does not takes a list number1, a second list number2,"
                              "adds them together to make new_list, and says new_list.<br>"
                              " <br><br>",
              "points": 0
              }
    found_8 = False
    test_1 = False
    test_2 = False
    test_3 = False
    test_4 = False
    for key in p_scripts:
        script = p_scripts[key]
        test_8_key = match_string(r"event_whenkeypressed', \s '8' .+  data_setvariableto .+ control_repeat .+ "
                                  r"looks_sayforsecs", script)
        if test_8_key['pass']:
            found_8 = True
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"numbers1": [5, 2, -4, 0, ],
                                                                   "numbers2": [1, 2, 3, -4, ],
                                                                   'new_list': [3, 1],
                                                                   })
            run_1 = do_sprite(sprite, script, True)
            match_this = r"^\['6',\s*'4',\s*'-1',\s*'-4']"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_1 = True
            if test_1 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list numbers1: [5, 2, -4, 0]<br> "\
                                          "Input list numbers2: [1, 2, 3, -4, ]<br>" \
                                          "Expected output new_list: <br>['6', '4', '-1', '-4'] <br><br>" \
                                          "Actual output: <br>" + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"numbers1": [44, 44, 44, 0, ],
                                                                   "numbers2": [-100],
                                                                   'new_list': [3, 1],
                                                                   })
            run_2 = do_sprite(sprite, script, True)
            match_this = r"^$"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_2 = True
            if test_2 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list numbers1: [44, 44, 44, 0]<br> "\
                                          "Input list numbers2: [-100]<br>" \
                                          "Expected output: <br><br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"numbers1": [44, 44, 44, 0, ],
                                                                   "numbers2": [-100, 100, 200, 300],
                                                                   'new_list': [3, 1],
                                                                   })
            run_3 = do_sprite(sprite, script, True)
            match_this = r"^\['-56',\s*'144',\s*'244',\s*'300']"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_3 = True
            if test_3 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] +=  "Input list numbers1: [44, 44, 44, 0]<br> "\
                                          "Input list numbers2: [-100, 100, 200, 300]<br>" \
                                          "Expected output: <br>['-56', '144', '244', '300']<br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"

    if found_8 is False:
        p_test['fail_message'] += "In your code, did not find 'when 8 key pressed' in your code " \
                                  "followed by some expected elements - setting a variable to a value " \
                                  "(to track the index or counter)," \
                                  "a repeat of some sort, and a say of some sort.<br><br>"

    p_test['fail_message'] += "<b>Be sure you are not hard-coding the number of items in the list.</b><br>" \
                              "The code has to work with lists of length 1 and 5 (and 205), not just length 4.<br>"
    if found_8 and test_1 and test_2 and test_3 and run_1 and run_2 and run_3:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test
