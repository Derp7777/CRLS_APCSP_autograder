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




def two_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that pressing '2' key says every other song.  See instructions "
                      "from what this should look like "
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '2' key says every other song.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '2' key does not say every other song. <br><br>",
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
    p_test = {"name": "Checking that pressing '3' key says the songs in reverse playlist order.  See instructions "
                      "from what this should look like "
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '3' key says the songs in reverse playlist order.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '3' key does not say the songs in reverse playlist order. <br><br>",
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


def four_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that pressing '4' key skips the first two and last two songs but says the others."
                      "  See instructions "
                      "from what this should look like "
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '4' key skips the first two and last two songs but says the others.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '4' key does not skip the first two and last two songs but says the "
                              "others. <br><br>",
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
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['Brahms op 118 no 1',
                                                                             'Brahms op 118 no 2',
                                                                             'Brahms op 118 no 3',
                                                                             'Brahms op 118 no 4',
                                                                             'Brahms op 118 no 5',
                                                                             'Brahms op 118 no 6', ]
                                                                   })
            run_1 = do_sprite(sprite, script, True)
            match_this = r"^Brahms\sop\s118\sno\s3\nBrahms\sop\s" \
                         r"118\sno\s4"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_1 = True
            if test_1 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['Brahms op 118 no 1','Brahms op 118 no 2','Brahms op 118 no 3'," \
                                          "'Brahms op 118 no 4', 'Brahms op 118 no 5','Brahms op 118 no 6']<br> " \
                                          "Expected output: <br>" \
                                          "Brahms op 118 no 3 <br>Brahms op 118 no 4<br><br>" \
                                          "Actual output: <br>" + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['In da club', ]})
            run_2 = do_sprite(sprite, script, True)
            match_this = r"^$"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_2 = True
            if test_2 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['In da club']<br> " \
                                          "Expected output: <br><br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['Baby one more time',
                                                                             'Oops I did it again',
                                                                             'Lucky', 'Humble', 'i']
                                                                   })
            run_3 = do_sprite(sprite, script, True)
            match_this = r"^Lucky"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_3 = True
            if test_3 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['Baby one more time','Oops I did it again','Lucky', 'Humble', " \
                                          "'i']<br> " \
                                          "Expected output: <br>Lucky" \
                                          "<br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"

    if found_4 is False:
        p_test['fail_message'] += "In your code, did not find 'when 1 key pressed' in your code " \
                                  "followed by some expected elements - setting a variable to a value " \
                                  "(to track the index or counter)," \
                                  "a repeat of some sort, and a say of some sort.<br><br>"

    p_test['fail_message'] += "<b>Be sure you are not hard-coding the number of items in the list.</b><br>" \
                              "The code has to work with lists of length 1 and 5 (and 205), not just length 6.<br>"
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
    p_test = {"name": "Checking that pressing '5' key says all songs at once.  See instructions "
                      "from what this should look like "
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '5' key says all songs at once.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '5' key does not say all songs at once. <br><br>",
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
            match_this = r"^s*Brahms\sop\s118\sno\s1\sBrahms\sop\s118\sno\s2\sBrahms\sop\s118\sno\s3\s" \
                         r"Brahms\sop\s118\sno\s4\sBrahms\sop\s118\sno\s5\sBrahms\sop\s118\sno\s6"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_1 = True
            if test_1 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['Brahms op 118 no 1','Brahms op 118 no 2','Brahms op 118 no 3'," \
                                          "'Brahms op 118 no 4', 'Brahms op 118 no 5','Brahms op 118 no 6']<br> " \
                                          "Expected output: <br>Brahms op 118 no 1 Brahms op 118 no 2 " \
                                          "Brahms op 118 no 3 Brahms op 118 no 4 Brahms op 118 no 5 " \
                                          "Brahms op 118 no 6 <br><br>" \
                                          "Actual output: <br>" + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['In da club', ]})
            run_2 = do_sprite(sprite, script, True)
            match_this = r"^\s*In\sda\sclub\n"
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
            match_this = r"^\s*Baby\sone\smore\stime\sOops\sI\sdid\sit\sagain\sLucky"
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


def tester(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "testing<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '1' key welcomes each name individually.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '1' key does not welcome each name individually. <br><br>",
              "points": 0
              }
    # assume just one
    for key in p_scripts:
        script = p_scripts[key]
        sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['Brahms op 118 no 1',
                                                                         'Brahms op 118 no 2',
                                                                         'Brahms op 118 no 3',
                                                                         'Brahms op 118 no 4',
                                                                         'Brahms op 118 no 5',
                                                                         'Brahms op 118 no 6', ]
                                                               })
        run_1 = do_sprite(sprite, script, True)

    if True:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def oneb_looks_ok(p_scripts, p_points):
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
            test_if = match_string(r"event_whenkeypressed', \s '1' .+ control_if", script)
            test_length = match_string(r"event_whenkeypressed', \s '1' .+ operator_length", script)
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
        if test_if['pass'] is False:
            p_test['fail_message'] += "You need an 'if' of some sort to test to see if your song is > 10 characters" \
                                      ".<br>"
        if test_length['pass'] is False:
            p_test['fail_message'] += "You need an green 'length' test to see if your song is > 10 characters" \
                                      ".<br>"
        if found_key and test_setvar['pass'] and test_repeat['pass'] and test_looksay['pass'] and \
                test_if['pass'] and test_length['pass']:
            p_test['pass'] = True
            p_test['points'] += p_points
    return p_test


def oneb_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that pressing '1' key says songs with 10+ characters.  See instructions "
                      "from what this should look like "
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '1' key says songs with 10+ characters.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '1' key does not says songs with 10+ characters. <br><br>",
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
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['Chantaje', 'Whenever wherever',
                                                                             'She Wolf', 'Runaway', 'Jesus Walks',
                                                                             'Blood on the Leaves',
                                                                             "Can't tell me nothing", ]
                                                                   })
            run_1 = do_sprite(sprite, script, True)
            match_this = r"^Whenever\swherever\nJesus\sWalks\nBlood\son\sthe\sLeaves\nCant\stell\sme\snothing"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_1 = True
            if test_1 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list:['Chantaje', 'Whenever wherever',  'She Wolf', 'Runaway', " \
                                          "'Jesus Walks','Blood on the Leaves'" \
                                          "Can't tell me nothing] <br> " \
                                          "Expected output: <br>Whenever wherever <br>Jesus Walks <br>" \
                                          "Blood on the Leaves <br>Can't tell me nothing<br><br>" \
                                          "Actual output: <br>" + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['In da club', ]})
            run_2 = do_sprite(sprite, script, True)
            match_this = r"^"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_2 = True
            if test_2 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['In da club']<br> " \
                                          "Expected output: <br><br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['Baby one more time',
                                                                             'Oops I did it again',
                                                                             'Lucky', ]
                                                                   })
            run_3 = do_sprite(sprite, script, True)
            match_this = r"^Baby\sone\smore\stime\nOops\sI\sdid\sit\sagain"
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


def twob_looks_ok(p_scripts, p_points):
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
            test_if = match_string(r"event_whenkeypressed', \s '2' .+ control_if", script)
            test_letter = match_string(r"event_whenkeypressed', \s '2' .+ operator_letter_of", script)

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
        if test_if['pass'] is False:
            p_test['fail_message'] += "You need an 'if' of some sort to test to see if your song starts with 'c'" \
                                      ".<br>"
        if test_letter['pass'] is False:
            p_test['fail_message'] += "You need an green 'letter of' test to see if your song starts with 'c'" \
                                      ".<br>"

        if found_key and test_setvar['pass'] and test_repeat['pass'] and test_looksay['pass'] and \
                test_if['pass'] and test_letter['pass']:
            p_test['pass'] = True
            p_test['points'] += p_points
    return p_test


def twob_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that pressing '2' key says songs starting with c.  See instructions "
                      "from what this should look like "
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '2' key says songs starting with c.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '2' key does not say songs starting with c. <br>"
                              "In your Scratch code, be sure to check for LOWERCASE c.<br><br>",
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
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['Chantaje', 'Whenever wherever',
                                                                             'She Wolf', 'Runaway', 'Jesus Walks',
                                                                             'Blood on the Leaves',
                                                                             "Can't tell me nothing", ]
                                                                   })
            run_1 = do_sprite(sprite, script, True)
            match_this = r"^Chantaje\nCant\stell\sme\snothing"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_1 = True
            if test_1 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list:['Chantaje', 'Whenever wherever',  'She Wolf', 'Runaway', " \
                                          "'Jesus Walks','Blood on the Leaves'" \
                                          "Can't tell me nothing] <br> " \
                                          "Expected output: <br>Chantaje <br>Cant tell me nothing <br><br>" \
                                          "Actual output: <br>" + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['In da club', ]})
            run_2 = do_sprite(sprite, script, True)
            match_this = r"^"
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
                                                                             'Lucky', 'Crazy you drive me']
                                                                   })
            run_3 = do_sprite(sprite, script, True)
            match_this = r"^Crazy\syou\sdrive\sme"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_3 = True
            if test_3 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['Baby one more time','Oops I did it again','Lucky', " \
                                          "'Crazy (you drive me)']<br> " \
                                          "Expected output: <br>Crazy you drive me" \
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


def threeb_looks_ok(p_scripts, p_points):
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
            test_if = match_string(r"event_whenkeypressed', \s '3' .+ control_if", script)
            test_letter = match_string(r"event_whenkeypressed', \s '3' .+ operator_letter_of", script)

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
        if test_if['pass'] is False:
            p_test['fail_message'] += "You need an 'if' of some sort to test to see if your song starts with 'c'" \
                                      ".<br>"
        if test_letter['pass'] is False:
            p_test['fail_message'] += "You need an green 'letter of' test to see if your song starts with 'c'" \
                                      ".<br>"

        if found_key and test_setvar['pass'] and test_repeat['pass'] and test_looksay['pass'] and \
                test_if['pass'] and test_letter['pass']:
            p_test['pass'] = True
            p_test['points'] += p_points
    return p_test


def threeb_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that pressing '3' key says songs ending with 'y'.  See instructions "
                      "from what this should look like "
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '3' key says songs  ending with 'y'.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '3' key does not say songs ending with 'y'. <br>"
                              "In your Scratch code, be sure to check for LOWERCASE y.<br><br>",
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
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['Chantaje', 'Whenever wherever',
                                                                             'She Wolf', 'Runaway', 'Jesus Walks',
                                                                             'Blood on the Leaves',
                                                                             "Can't tell me nothing", ]
                                                                   })
            run_1 = do_sprite(sprite, script, True)
            match_this = r"^Runaway"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_1 = True
            if test_1 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list:['Chantaje', 'Whenever wherever',  'She Wolf', 'Runaway', " \
                                          "'Jesus Walks','Blood on the Leaves'" \
                                          "Can't tell me nothing] <br> " \
                                          "Expected output: <br>Runaway <br><br>" \
                                          "Actual output: <br>" + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['In da club', ]})
            run_2 = do_sprite(sprite, script, True)
            match_this = r"^"
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
                                                                             'Lucky', 'You drive me Crazy']
                                                                   })
            run_3 = do_sprite(sprite, script, True)
            match_this = r"^Lucky\nYou\sdrive\sme\sCrazy"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_3 = True
            if test_3 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['Baby one more time','Oops I did it again','Lucky', " \
                                          "'Crazy (you drive me)']<br> " \
                                          "Expected output: <br>You drive me Crazy" \
                                          "<br><br>" \
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


def fourb_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that pressing '4' key says songs ending with 'y'.  See instructions "
                      "from what this should look like "
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '4' key says songs  ending with 'y'.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '4' key does not say songs ending with 'y'. <br>"
                              "In your Scratch code, be sure to check for LOWERCASE y.<br><br>",
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
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['Chantaje', 'Whenever wherever',
                                                                             'She Wolf', 'Runaway', 'Jesus Walks',
                                                                             'Blood on the Leaves',
                                                                             "Can't tell me nothing", ]
                                                                   })
            run_1 = do_sprite(sprite, script, True)
            match_this = r"^Chantaje\nWhenever\swherever\nShe\sWolf\nJesus\sWalks\nBlood\son\sthe\sLeaves\n" \
                         r"Cant\stell\sme\snothing"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_1 = True
            if test_1 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list:['Chantaje', 'Whenever wherever',  'She Wolf', 'Runaway', " \
                                          "'Jesus Walks','Blood on the Leaves'" \
                                          "Can't tell me nothing] <br> " \
                                          "Expected output: <br>Chantaje<br>" \
                                          "Whenever wherever<br>She Wolf<br>Jesus Walks<br>Blood on the Leaves" \
                                          "<br><br>" \
                                          "Actual output: <br>" + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['In da club', ]})
            run_2 = do_sprite(sprite, script, True)
            match_this = r"^"
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
                                                                             'Lucky', 'You drive me Crazy']
                                                                   })
            run_3 = do_sprite(sprite, script, True)
            match_this = r"^Baby\sone\smore\stime\nYou\sdrive\sme\sCrazy"
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_3 = True
            if test_3 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['Baby one more time','Oops I did it again','Lucky', " \
                                          "'(You drive me) Crazy']<br> " \
                                          "Expected output: <br>You drive me Crazy" \
                                          "<br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"

    if found_4 is False:
        p_test['fail_message'] += "In your code, did not find 'when 4 key pressed' in your code " \
                                  "followed by some expected elements - setting a variable to a value " \
                                  "(to track the index or counter)," \
                                  "a repeat of some sort, and a say of some sort.<br><br>"

    p_test['fail_message'] += "<b>Be sure you are not hard-coding the number of items in the list.</b><br>" \
                              "The code has to work with lists of length 1 and 5 (and 205), not just length 6.<br>"
    if found_4 and test_1 and test_2 and test_3 and run_1 and run_2 and run_3:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def fiveb_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that pressing '5' key says all the songs with commas and a period at the end."
                      "  See instructions "
                      "from what this should look like "
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '5' key says songs all the songs with commas and a period at the end.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '5' key does not say all the songs with commas and a period at the end. <br>"
                              "In your Scratch code, be sure to check for LOWERCASE y.<br><br>",
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
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['Chantaje', 'Whenever wherever',
                                                                             'She Wolf', 'Runaway', 'Jesus Walks',
                                                                             'Blood on the Leaves',
                                                                             "Can't tell me nothing", ]
                                                                   })
            run_1 = do_sprite(sprite, script, True)
            match_this = r"^Chantaje,\s*Whenever\swherever,\s*She\sWolf,\s*Runaway,\sJesus\sWalks," \
                         r"\s*Blood\son\sthe\sLeaves,\s*and\sCant\stell\sme\snothing\."

            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_1 = True
            if test_1 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list:['Chantaje', 'Whenever wherever',  'She Wolf', 'Runaway', " \
                                          "'Jesus Walks','Blood on the Leaves', " \
                                          "'Cant tell me nothing'] <br> " \
                                          "Expected output: <br>Chantaje, Whenever wherever, She Wolf, " \
                                          "Runaway, Jesus Walks, Blood on the Leaves, and Cant tell me nothing." \
                                          "<br><br>" \
                                          "Actual output: <br>" + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['In da club', ]})
            run_2 = do_sprite(sprite, script, True)
            match_this = r"^In\sda\sclub\."
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_2 = True
            if test_2 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['In da club']<br> " \
                                          "Expected output: <br>In da club. <br><br>" \
                                          "Actual output:<br> " + history_newlines + "<br><br>"
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"songs": ['Baby one more time',
                                                                             'Oops I did it again',
                                                                             'Lucky', 'You drive me Crazy']
                                                                   })
            run_3 = do_sprite(sprite, script, True)
            match_this = r"^Baby\sone\smore\stime,\s*Oops\sI\sdid\sit\sagain,\s*Lucky,\s*and\sYou\sdrive\sme\sCrazy\."
            matched = re.search(match_this, sprite.say_history)
            if matched:
                test_3 = True
            if test_3 is False:
                history_newlines = re.sub(r"\n", "<br>", sprite.say_history)
                p_test['fail_message'] += "Input list: ['Baby one more time','Oops I did it again','Lucky', " \
                                          "'You drive me Crazy']<br> " \
                                          "Expected output: <br>Baby one more time, Oops I did it again, Lucky, " \
                                          "and You drive me Crazy." \
                                          "<br><br>" \
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
