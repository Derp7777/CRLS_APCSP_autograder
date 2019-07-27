def songs_list(p_json, p_points):
    """
     verifies the 3 lists are there
     :param p_json: json of scratch file (dict)
     :param p_points: points this is worth (int)
     :return: a test dictionary
     """
    from app.scratch_labs.scratch import find_list
    p_test = {"name": "Checking that there is list that exists: songs "
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "The list songs exists .<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The list songs does not exist.<br>"
                              "The lists must be named EXACTLY CORRECT with no caps and the 's' at the end.<br>"
                              "An 's' at the end tells you that it is plural (lists are potentially plural) and "
                              "this is a good trick to help you keep track of things.<br>",
              "points": 0
              }

    find_names = find_list(p_json, 'songs', 5)
    if find_names['pass']:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def songs_list_min_items(p_json, p_points):
    """
     verifies min number of items
     :param p_json: json of scratch file (dict)
     :param p_points: points this is worth (int)
     :return: a test dictionary
     """
    from app.scratch_labs.scratch import find_list
    p_test = {"name": "Checking that there is list songs with minimum 6 items"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "The list songs exists with minimum 6 items .<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The list songs does not have 6 or more items.",
              "points": 0
              }

    find_songs_items = find_list(p_json, 'songs', 5,  min_items=6)
    if find_songs_items['pass']:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def one_looks_ok(p_scripts, p_points):
    """
      :param p_scripts: json data from file, which is the code of the scratch file. (dict)
      :param p_points: Number of points this test is worth (int)
      :return: The test dictionary
      """
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that pressing '1' key looks approximately correct"
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '1' key looks approximately correct.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '1' key does not look approximately correct. <br>",
              "points": 0
              }

    press = '1'
    found_key = False
    for key in p_scripts:
        script = p_scripts[key]
        test_found_1 = match_string(r"event_whenkeypressed', \s '1'", script)
        if test_found_1['pass']:
            found_key = True
            test_setvar = match_string(r"event_whenkeypressed', \s '1' .+  data_setvariableto", script)
            test_repeat = match_string(r"event_whenkeypressed', \s '1' .+  control_repeat", script)
            test_looksay = match_string(r"event_whenkeypressed', \s '1' .+ looks_sayforsecs", script)
    if found_key is False:
        p_test['fail_message'] += "Did not find 'when " + press + " key is pressed ' <br>"
    else:
        if test_setvar['pass'] is False:
            p_test['fail_message'] += "Did not find any example of setting a variable after key is pressed.  You" \
                                      "will need a counter variable of some sort to loop through the list.<br>"
        if test_repeat['pass'] is False:
            p_test['fail_message'] += "You need to loop through the list multiple times. " \
                                      " Need a repeat (or better, repeat until)" \
                                      " of some sort ' <br>"
        if test_looksay['pass'] is False:
            p_test['fail_message'] += "You need to say the song when you get to it.  Needs a 'say for XXX seconds' " \
                                      "block.<br>"

        if found_key and test_setvar['pass'] and test_repeat['pass'] and test_looksay['pass']:
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
        test_found_key = match_string(r"event_whenkeypressed', \s '2'", script)
        if test_found_key['pass']:
            found_key = True
            test_setvar = match_string(r"event_whenkeypressed', \s '2' .+  data_setvariableto", script)
            test_repeat = match_string(r"event_whenkeypressed', \s '2' .+  control_repeat", script)
            test_looksay = match_string(r"event_whenkeypressed', \s '2' .+ looks_sayforsecs", script)
    if found_key is False:
        p_test['fail_message'] += "Did not find 'when " + press + " key is pressed ' <br>"
    else:
        if test_setvar['pass'] is False:
            p_test['fail_message'] += "Did not find any example of setting a variable after key is pressed.  You" \
                                      "will need a counter variable of some sort to loop through the list.<br>"
        if test_repeat['pass'] is False:
            p_test['fail_message'] += "You need to loop through the list multiple times. " \
                                      " Need a repeat (or better, repeat until)" \
                                      " of some sort ' <br>"
        if test_looksay['pass'] is False:
            p_test['fail_message'] += "You need to say the song when you get to it.  Needs a 'say for XXX seconds' " \
                                      "block.<br>"

        if found_key and test_setvar['pass'] and test_repeat['pass'] and test_looksay['pass']:
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
                              "Pressing '3' key looks approximately correct.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '3' key does not look approximately correct. <br>",
              "points": 0
              }

    press = '3'
    found_key = False
    for key in p_scripts:
        script = p_scripts[key]
        test_found_key = match_string(r"event_whenkeypressed', \s '3'", script)
        if test_found_key['pass']:
            found_key = True
            test_setvar = match_string(r"event_whenkeypressed', \s '3' .+  data_setvariableto", script)
            test_repeat = match_string(r"event_whenkeypressed', \s '3' .+  control_repeat", script)
            test_looksay = match_string(r"event_whenkeypressed', \s '3' .+ looks_sayforsecs", script)
    if found_key is False:
        p_test['fail_message'] += "Did not find 'when " + press + " key is pressed ' <br>"
    else:
        if test_setvar['pass'] is False:
            p_test['fail_message'] += "Did not find any example of setting a variable after key is pressed.  You" \
                                      "will need a counter variable of some sort to loop through the list.<br>"
        if test_repeat['pass'] is False:
            p_test['fail_message'] += "You need to loop through the list multiple times. " \
                                      " Need a repeat (or better, repeat until)" \
                                      " of some sort ' <br>"
        if test_looksay['pass'] is False:
            p_test['fail_message'] += "You need to say the song when you get to it.  Needs a 'say for XXX seconds' " \
                                      "block.<br>"

        if found_key and test_setvar['pass'] and test_repeat['pass'] and test_looksay['pass']:
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
        test_found_key = match_string(r"event_whenkeypressed', \s '4'", script)
        if test_found_key['pass']:
            found_key = True
            test_setvar = match_string(r"event_whenkeypressed', \s '4' .+  data_setvariableto", script)
            test_repeat = match_string(r"event_whenkeypressed', \s '4' .+  control_repeat", script)
            test_looksay = match_string(r"event_whenkeypressed', \s '4' .+ looks_sayforsecs", script)
    if found_key is False:
        p_test['fail_message'] += "Did not find 'when " + press + " key is pressed ' <br>"
    else:
        if test_setvar['pass'] is False:
            p_test['fail_message'] += "Did not find any example of setting a variable after key is pressed.  You" \
                                      "will need a counter variable of some sort to loop through the list.<br>"
        if test_repeat['pass'] is False:
            p_test['fail_message'] += "You need to loop through the list multiple times. " \
                                      " Need a repeat (or better, repeat until)" \
                                      " of some sort ' <br>"
        if test_looksay['pass'] is False:
            p_test['fail_message'] += "You need to say the song when you get to it.  Needs a 'say for XXX seconds' " \
                                      "block.<br>"

        if found_key and test_setvar['pass'] and test_repeat['pass'] and test_looksay['pass']:
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
        test_found_key = match_string(r"event_whenkeypressed', \s '5'", script)
        if test_found_key['pass']:
            found_key = True
            test_setvar = match_string(r"event_whenkeypressed', \s '5' .+  data_setvariableto", script)
            test_repeat = match_string(r"event_whenkeypressed', \s '5' .+  control_repeat", script)
            test_looksay = match_string(r"event_whenkeypressed', \s '5' .+ looks_sayforsecs", script)
    if found_key is False:
        p_test['fail_message'] += "Did not find 'when " + press + " key is pressed ' <br>"
    else:
        if test_setvar['pass'] is False:
            p_test['fail_message'] += "Did not find any example of setting a variable after key is pressed.  You" \
                                      "will need a counter variable of some sort to loop through the list.<br>"
        if test_repeat['pass'] is False:
            p_test['fail_message'] += "You need to loop through the list multiple times. " \
                                      " Need a repeat (or better, repeat until)" \
                                      " of some sort ' <br>"
        if test_looksay['pass'] is False:
            p_test['fail_message'] += "You need to say the song when you get to it.  Needs a 'say for XXX seconds' " \
                                      "block.<br>"

        if found_key and test_setvar['pass'] and test_repeat['pass'] and test_looksay['pass']:
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
    p_test = {"name": "Checking that pressing '1' key welcomes each name individually.  See instructions "
                      "from what this should look like "
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '1' key welcomes each name individually.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '1' key does not welcome each name individually. <br><br>",
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
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['Brahms op 118 no 1',
                                                                             'Brahms op 118 no 2',
                                                                             'Brahms op 118 no 3',
                                                                             'Brahms op 118 no 4',
                                                                             'Brahms op 118 no 5',
                                                                             'Brahms op 118 no 6', ]
                                                                   })
            run_1 = do_sprite(sprite, script, True)
            match_this = r"^Brahms\sop\s118\sno\s1\nBrahms\sop\s118\sno\s2\nBrahms\sop\s118\sno\s3\nBrahms\sop\s" \
                         r"118\sno\s4\nBrahms\sop\s118\sno\s5\nBrahms\sop\s118\sno\s6\n"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_1 = True
            if test_1 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['Brahms op 118 no 1','Brahms op 118 no 2','Brahms op 118 no 3'," \
                                          "'Brahms op 118 no 4', 'Brahms op 118 no 5','Brahms op 118 no 6']<br> " \
                                          "Expected output: <br>Brahms op 118 no 1 <br>Brahms op 118 no 2 <br>" \
                                          "Brahms op 118 no 3 <br>Brahms op 118 no 4<br>Brahms op 118 no 5<br>" \
                                          "Brahms op 118 no 6 <br><br>" \
                                          "Actual output: <br>" + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['In da club', ]})
            run_2 = do_sprite(sprite, script, True)
            match_this = r"^In\sda\sclub\n"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_2 = True
            if test_2 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['In da club']<br> " \
                                          "Expected output: <br>In da club <br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['Baby one more time',
                                                                             'Oops I did it again',
                                                                             'Lucky', ]
                                                                   })
            run_3 = do_sprite(sprite, script, True)
            match_this = r"^Baby\sone\smore\stime\nOops\sI\sdid\sit\sagain\nLucky"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_3 = True
            if test_3 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['Baby one more time','Oops I did it again','Lucky']<br> " \
                                          "Expected output: <br>Baby one more time<br>Oops I did it again<br>Lucky" \
                                          "<br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"

    if found_1 is False:
        p_test['fail_message'] += "In your code, did not find 'when 1 key pressed' in your code " \
                                  "followed by some expected elements - setting a variable to a value " \
                                  "(to track the index or counter)," \
                                  "a repeat of some sort, and a say of some sort.<br><br>"

    p_test['fail_message'] += "<b>Be sure you are not hard-coding the number of items in the list.</b><br>" \
                              "The code has to work with lists of length 1 and 5 (and 205), not just length 6.<br>"
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
    p_test = {"name": "Checking that pressing '2' key welcomes each name individually.  See instructions "
                      "from what this should look like "
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '2' key welcomes each name individually.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '2' key does not welcome each name individually. <br><br>",
              "points": 0
              }
    found_2 = False
    test_1 = False
    test_2 = False
    test_3 = False

    for key in p_scripts:
        script = p_scripts[key]
        test_1_key = match_string(r"event_whenkeypressed', \s '2' .+  data_setvariableto .+ control_repeat .+ "
                                  r"looks_sayforsecs", script)
        if test_1_key['pass']:
            found_2 = True
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['Brahms op 118 no 1',
                                                                             'Brahms op 118 no 2',
                                                                             'Brahms op 118 no 3',
                                                                             'Brahms op 118 no 4',
                                                                             'Brahms op 118 no 5',
                                                                             'Brahms op 118 no 6', ]
                                                                   })
            run_1 = do_sprite(sprite, script, True)
            match_this = r"^Brahms\sop\s118\sno\s1\nBrahms\sop\s118\sno\s3\nBrahms\sop\s118\sno\s5\n"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_1 = True
            if test_1 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['Brahms op 118 no 1','Brahms op 118 no 2','Brahms op 118 no 3'," \
                                          "'Brahms op 118 no 4', 'Brahms op 118 no 5','Brahms op 118 no 6']<br> " \
                                          "Expected output: <br>Brahms op 118 no 1 <br>" \
                                          "Brahms op 118 no 3 <br>Brahms op 118 no 5<br><br>" \
                                          "Actual output: <br>" + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['In da club', ]})
            run_2 = do_sprite(sprite, script, True)
            match_this = r"^In\sda\sclub\n"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_2 = True
            if test_2 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['In da club']<br> " \
                                          "Expected output: <br>In da club <br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['Baby one more time',
                                                                             'Oops I did it again',
                                                                             'Lucky', ]
                                                                   })
            run_3 = do_sprite(sprite, script, True)
            match_this = r"^Baby\sone\smore\stime\nLucky"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_3 = True
            if test_3 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['Baby one more time','Oops I did it again','Lucky']<br> " \
                                          "Expected output: <br>Baby one more time<br>Lucky " \
                                          "<br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"

    if found_2 is False:
        p_test['fail_message'] += "In your code, did not find 'when 2 key pressed' in your code " \
                                  "followed by some expected elements - setting a variable to a value " \
                                  "(to track the index or counter)," \
                                  "a repeat of some sort, and a say of some sort.<br><br>"

    p_test['fail_message'] += "<b>Be sure you are not hard-coding the number of items in the list.</b><br>" \
                              "The code has to work with lists of length 1 and 5 (and 205), not just length 6.<br>"
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
    p_test = {"name": "Checking that pressing '3' key welcomes each name individually.  See instructions "
                      "from what this should look like "
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '3' key welcomes each name individually.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '3' key does not welcome each name individually. <br><br>",
              "points": 0
              }
    found_3 = False
    test_1 = False
    test_2 = False
    test_3 = False

    for key in p_scripts:
        script = p_scripts[key]
        test_1_key = match_string(r"event_whenkeypressed', \s '3' .+  data_setvariableto .+ control_repeat .+ "
                                  r"looks_sayforsecs", script)
        if test_1_key['pass']:
            found_3 = True
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['Brahms op 118 no 1',
                                                                             'Brahms op 118 no 2',
                                                                             'Brahms op 118 no 3',
                                                                             'Brahms op 118 no 4',
                                                                             'Brahms op 118 no 5',
                                                                             'Brahms op 118 no 6', ]
                                                                   })
            run_1 = do_sprite(sprite, script, True)
            match_this = r"^Brahms\sop\s118\sno\s6\nBrahms\sop\s118\sno\s5\nBrahms\sop\s118\sno\s4\n" \
                         r"Brahms\sop\s118\sno\s3\nBrahms\sop\s118\sno\s2\nBrahms\sop\s118\sno\s1"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_1 = True
            if test_1 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['Brahms op 118 no 1','Brahms op 118 no 2','Brahms op 118 no 3'," \
                                          "'Brahms op 118 no 4', 'Brahms op 118 no 5','Brahms op 118 no 6']<br> " \
                                          "Expected output: <br>Brahms op 118 no 6 <br>Brahms op 118 no 5 <br>" \
                                          "Brahms op 118 no 4<br>" \
                                          "Brahms op 118 no 3 <br>Brahms op 118 no 2<br>Brahms op 118 no 1<br><br>" \
                                          "Actual output: <br>" + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['In da club', ]})
            run_2 = do_sprite(sprite, script, True)
            match_this = r"^In\sda\sclub\n"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_2 = True
            if test_2 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['In da club']<br> " \
                                          "Expected output: <br>In da club <br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['Baby one more time',
                                                                             'Oops I did it again',
                                                                             'Lucky', ]
                                                                   })
            run_3 = do_sprite(sprite, script, True)
            match_this = r"^Lucky\nOops\sI\sdid\sit\sagain\nBaby\sone\smore\stime\n"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_3 = True
            if test_3 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['Baby one more time','Oops I did it again','Lucky']<br> " \
                                          "Expected output: <br>Lucky <br>Oops I did it again<br>" \
                                          "Baby one more time<br>" \
                                          "<br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"

    if found_3 is False:
        p_test['fail_message'] += "In your code, did not find 'when 3 key pressed' in your code " \
                                  "followed by some expected elements - setting a variable to a value " \
                                  "(to track the index or counter)," \
                                  "a repeat of some sort, and a say of some sort.<br><br>"

    p_test['fail_message'] += "<b>Be sure you are not hard-coding the number of items in the list.</b><br>" \
                              "The code has to work with lists of length 1 and 5 (and 205), not just length 6.<br>"
    if found_3 and test_1 and test_2 and test_3 and run_1 and run_2 and run_3:
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
    p_test = {"name": "Checking that pressing '5' key welcomes each name individually.  See instructions "
                      "from what this should look like "
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '5' key welcomes each name individually.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '5' key does not welcome each name individually. <br><br>",
              "points": 0
              }
    found_5 = False
    test_1 = False
    test_2 = False
    test_3 = False

    for key in p_scripts:
        script = p_scripts[key]
        test_1_key = match_string(r"event_whenkeypressed', \s '5' .+  data_setvariableto .+ control_repeat .+ "
                                  r"looks_sayforsecs", script)
        if test_1_key['pass']:
            found_5 = True
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['Brahms op 118 no 1',
                                                                             'Brahms op 118 no 2',
                                                                             'Brahms op 118 no 3',
                                                                             'Brahms op 118 no 4',
                                                                             'Brahms op 118 no 5',
                                                                             'Brahms op 118 no 6', ]
                                                                   })
            run_1 = do_sprite(sprite, script, True)
            match_this = r"^Brahms\sop\s118\sno\s6\nBrahms\sop\s118\sno\s5\nBrahms\sop\s118\sno\s4\n" \
                         r"Brahms\sop\s118\sno\s3\nBrahms\sop\s118\sno\s2\nBrahms\sop\s118\sno\s1"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_1 = True
            if test_1 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['Brahms op 118 no 1','Brahms op 118 no 2','Brahms op 118 no 3'," \
                                          "'Brahms op 118 no 4', 'Brahms op 118 no 5','Brahms op 118 no 6']<br> " \
                                          "Expected output: <br>Brahms op 118 no 1 Brahms op 118 no 2 " \
                                          "Brahms op 118 no 3 Brahms op 118 no 4 Brahms op 118 no 5" \
                                          "Brahms op 118 no 6 <br><br>" \
                                          "Actual output: <br>" + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['In da club', ]})
            run_2 = do_sprite(sprite, script, True)
            match_this = r"^In\sda\sclub\n"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_2 = True
            if test_2 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['In da club']<br> " \
                                          "Expected output: <br>In da club <br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['Baby one more time',
                                                                             'Oops I did it again',
                                                                             'Lucky', ]
                                                                   })
            run_3 = do_sprite(sprite, script, True)
            match_this = r"^Lucky\nOops\sI\sdid\sit\sagain\nBaby\sone\smore\stime\n"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_3 = True
            if test_3 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['Baby one more time','Oops I did it again','Lucky']<br> " \
                                          "Expected output: <br>Baby one more time Oops I did it again Lucky<br>" \
                                          "<br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"

    if found_5 is False:
        p_test['fail_message'] += "In your code, did not find 'when 5 key pressed' in your code " \
                                  "followed by some expected elements - setting a variable to a value " \
                                  "(to track the index or counter)," \
                                  "a repeat of some sort, and a say of some sort.<br><br>"

    p_test['fail_message'] += "<b>Be sure you are not hard-coding the number of items in the list.</b><br>" \
                              "The code has to work with lists of length 1 and 5 (and 205), not just length 6.<br>"
    if found_5 and test_1 and test_2 and test_3 and run_1 and run_2 and run_3:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test
