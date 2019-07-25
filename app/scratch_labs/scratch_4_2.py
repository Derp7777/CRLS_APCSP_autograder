def find_all_lists(p_json, p_points):
    """
    verifies the 3 lists are there
    :param p_json: json of scratch file (dict)
    :param p_points: points this is worth (int)
    :return: a test dictionary
    """
    from app.scratch_labs.scratch import find_list
    p_test = {"name": "Checking that there are three lists that exist: ice_creams, dry_toppings, wet_toppings "
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "The lists ice_creams, dry_toppings, wet_toppings exist .<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The lists ice_creams, dry_toppings, wet_toppings do not all exist.<br>"
                              "The lists must be named EXACTLY CORRECT with no caps and the 's' at the end.<br>"
                              "An 's' at the end tells you that it is plural (lists are potentially plural) and "
                              "this is a good trick to help you keep track of things.<br>",
              "points": 0
              }
    find_ice_creams = find_list(p_json, 'ice_creams', 5)
    if find_ice_creams['pass'] is False:
        p_test['fail_message'] += 'Did not find ice_creams1 list in your code.<br>'
    find_wet_toppings = find_list(p_json, 'wet_toppings', 5)
    if find_wet_toppings['pass'] is False:
        p_test['fail_message'] += 'Did not find wet_toppings1 list in your code.<br>'
    find_dry_toppings = find_list(p_json, 'dry_toppings', 5)
    if find_dry_toppings['pass'] is False:
        p_test['fail_message'] += 'Did not find dry_toppings1 list in your code.<br>'
    if find_ice_creams['pass'] and find_wet_toppings['pass'] and find_dry_toppings['pass']:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def find_all_lists_min_items(p_json, p_points):
    """
    verifies the 3 lists are there with minium number of items
    :param p_json: json of scratch file (dict)
    :param p_points: points this is worth (int)
    :return: a test dictionary
    """
    from app.scratch_labs.scratch import find_list
    p_test = {"name": "Checking three lists have minimum 3 items each"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "The lists ice_creams, dry_toppings, wet_toppings all have 3+ items .<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The lists ice_creams, dry_toppings, wet_toppings do not all have 3+ items.<br>",
              "points": 0
              }
    find_ice_creams = find_list(p_json, 'ice_creams', 5, min_items=3)
    if find_ice_creams['pass'] is False:
        p_test['fail_message'] += 'ice_creams list needs at least 3 items.<br>'
    find_wet_toppings = find_list(p_json, 'wet_toppings', 5, min_items=3)
    if find_wet_toppings['pass'] is False:
        p_test['fail_message'] += 'wet_toppings list needs at least 3 items.<br>'
    find_dry_toppings = find_list(p_json, 'dry_toppings', 5, min_items=3)
    if find_dry_toppings['pass'] is False:
        p_test['fail_message'] += 'dry_toppings list needs at least 3 items.<br>'
    if find_ice_creams['pass'] and find_wet_toppings['pass'] and find_dry_toppings['pass']:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def find_smash_in(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch import procedure_exists
    p_test = {"name": "Checking that there is a custom block called 'smash_in'"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a custom block called 'smash_in'.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not a custom block called 'smash_in'."
                              "<br>"
                              "The script must be named EXACTLY smash_in.<br>"
                              "Capitalization and using the underscore matter.<br>"
                              "smash_in should have zero input parameters.<br>",
              "points": 0
              }
    test_procedure = procedure_exists('smash_in', p_scripts)
    if test_procedure:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def find_sundae_and_fancy_sundae(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch import procedure_exists
    p_test = {"name": "Checking that there is a custom block called 'sundae' AND custom block called 'fancy_sundae"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a custom block called 'sundae' and a custom block called 'fancy_sundae'.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not a custom block called 'sundae' or a custom block called 'fancy_sundae' "
                              "or both. <br>"
                              "The scripts must be named EXACTLY 'sundae' and 'fancy_sundae'.<br>"
                              "Capitalization and using the underscore matter.<br>"
                              "Both should have zero input parameters.<br>",
              "points": 0
              }
    test_procedure_1 = procedure_exists('sundae', p_scripts)
    test_procedure_2 = procedure_exists('fancy_sundae', p_scripts)
    if test_procedure_1 and test_procedure_2:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def smash_in_works_random(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string

    p_test = {"name": "Checking that the smash_in custom block works.  Input list of ice creams and 5 dry toppings.<br>"
                      "Expect to see all 10 items when I do 150 runs."
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "The smash_in custom block  works.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The smash_in custom block  does not appear to work.<br>"
                              "Are you randomly picking an item from each list?<br>"
                              "Are you using the correct random number range? It should be from 1 to length of "
                              "list.<br>"
                              "Be sure length of LIST (maroon color) not length of WORD (green color).<br>",
              "points": 0
              }
    smash_in_1 = True
    if 'smash_in' in p_scripts.keys():
        sprite = brickLayer(0, 0, 0, pendown=False, variables={"ice_creams":
                                                                   ['ice_1', 'ice_2', 'ice_3', 'ice_4', 'ice_5', ],
                                                               'dry_toppings':
                                                                   ['dry_1', 'dry_2', 'dry_3', 'dry_4', 'dry_5', ]})
        script = p_scripts['smash_in']
        for _ in range(150):
            smash_in_1 = do_sprite(sprite, script, True)
        print("VALHALLA {}".format(sprite.say_history))
        test_1 = match_string(r'ice_1', sprite.say_history)
        test_2 = match_string(r'ice_2', sprite.say_history)
        test_3 = match_string(r'ice_3', sprite.say_history)
        test_4 = match_string(r'ice_4', sprite.say_history)
        test_5 = match_string(r'ice_5', sprite.say_history)
        test_6 = match_string(r'dry_1', sprite.say_history)
        test_7 = match_string(r'dry_2', sprite.say_history)
        test_8 = match_string(r'dry_3', sprite.say_history)
        test_9 = match_string(r'dry_4', sprite.say_history)
        test_10 = match_string(r'dry_5', sprite.say_history)

        if test_1['pass'] is False:
            p_test['fail_message'] += "Called custom block 'smash_in' 100x.  Expected to see ice_1 in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history
        if test_2['pass'] is False:
            p_test['fail_message'] += "Called custom block 'smash_in' 100x.  Expected to see ice_2 in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history
        if test_3['pass'] is False:
            p_test['fail_message'] += "Called custom block 'smash_in' 100x.  Expected to see ice_3 in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history
        if test_4['pass'] is False:
            p_test['fail_message'] += "Called custom block 'smash_in' 100x.  Expected to see ice_4 in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history
        if test_5['pass'] is False:
            p_test['fail_message'] += "Called custom block 'smash_in' 100x.  Expected to see ice_5 in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history
        if test_6['pass'] is False:
            p_test['fail_message'] += "Called custom block 'smash_in' 100x.  Expected to see dry_1 in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history
        if test_7['pass'] is False:
            p_test['fail_message'] += "Called custom block 'smash_in' 100x.  Expected to see dry_2 in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history
        if test_8['pass'] is False:
            p_test['fail_message'] += "Called custom block 'smash_in' 100x.  Expected to see dry_3 in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history
        if test_9['pass'] is False:
            p_test['fail_message'] += "Called custom block 'smash_in' 100x.  Expected to see dry_4 in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history
        if test_10['pass'] is False:
            p_test['fail_message'] += "Called custom block 'smash_in' 100x.  Expected to see dry_5 in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history

        if test_1['pass'] and test_2['pass'] and test_3['pass'] and test_4['pass'] and test_5['pass'] and \
                test_6['pass'] and test_7['pass'] and test_8['pass'] and test_9['pass'] and \
                test_10['pass'] and smash_in_1:
            p_test['pass'] = True
            p_test['points'] += p_points
    return p_test


def smash_in_works_spacing(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string

    p_test = {"name": "Checking that the smash_in custom block works.  Input list of 1 ice creams and 1 dry toppings."
                      "<br>"
                      "Expect to see  'ice_1 dry_1' in that order with the space."
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "The smash_in custom block  works.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The smash_in custom block does not appear to work.<br>"
                              "Did you join in an extra space between ice cream and dry topping?",
              "points": 0
              }
    smash_in_1 = True
    if 'smash_in' in p_scripts.keys():
        sprite = brickLayer(0, 0, 0, pendown=False, variables={"ice_creams":
                                                                   ['ice_1', ],
                                                               'dry_toppings':
                                                                   ['dry_1', ]})
        script = p_scripts['smash_in']
        for _ in range(1):
            smash_in_1 = do_sprite(sprite, script, True)
        print("VALHALLA {}".format(sprite.say_history))
        test_1 = match_string(r'ice_1 \s dry_1', sprite.say_history)
        if test_1['pass'] is False:
            p_test['fail_message'] += "Called custom block 'smash_in' 1x.  Expected to see 'ice_1 dry1' " \
                                      "in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history + "<br>" \
                                                                                            "Did you remember to join" \
                                                                                            " a space?<br>"

        if test_1['pass'] and smash_in_1:
            p_test['pass'] = True
            p_test['points'] += p_points
    return p_test


def sundae_fancy_sundae_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string

    p_test = {"name": "Checking that the sundae and fancy_sundae custom blocks works.  "
                      "For both Input list of ice creams and 5 dry toppings.<br>"
                      "Expect to see all 10 items when I do 150 runs.<br>"
                      "Also expect to see correct spacing"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "The sundae and fancy_sundae custom blocks work.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The sundae and fancy_sundae custom blocks do not appear to work.<br>"
                              "Are you randomly picking an item from each list?<br>"
                              "Are you using the correct random number range? It should be from 1 to length of "
                              "list.<br>"
                              "Be sure length of LIST (maroon color) not length of WORD (green color).<br>"
                              "Do you have a space between your items?  Be sure to 'join' a space"
                              "in addition to the items",
              "points": 0
              }
    smash_in_1 = True
    if 'sundae' in p_scripts.keys():
        sprite = brickLayer(0, 0, 0, pendown=False, variables={"ice_creams":
                                                                   ['ice_1', 'ice_2', 'ice_3', 'ice_4', 'ice_5', ],
                                                               'wet_toppings':
                                                                   ['dry_1', 'dry_2', 'dry_3', 'dry_4', 'dry_5', ]})
        script = p_scripts['sundae']
        for _ in range(150):
            smash_in_1 = do_sprite(sprite, script, True)
        print("VALHALLA {}".format(sprite.say_history))
        test_1 = match_string(r'ice_1', sprite.say_history)
        test_2 = match_string(r'ice_2', sprite.say_history)
        test_3 = match_string(r'ice_3', sprite.say_history)
        test_4 = match_string(r'ice_4', sprite.say_history)
        test_5 = match_string(r'ice_5', sprite.say_history)
        test_6 = match_string(r'dry_1', sprite.say_history)
        test_7 = match_string(r'dry_2', sprite.say_history)
        test_8 = match_string(r'dry_3', sprite.say_history)
        test_9 = match_string(r'dry_4', sprite.say_history)
        test_10 = match_string(r'dry_5', sprite.say_history)

        if test_1['pass'] is False:
            p_test['fail_message'] += "Called custom block 'sundae' 100x.  Expected to see ice_1 in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history
        if test_2['pass'] is False:
            p_test['fail_message'] += "Called custom block 'sundae' 100x.  Expected to see ice_2 in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history
        if test_3['pass'] is False:
            p_test['fail_message'] += "Called custom block 'sundae' 100x.  Expected to see ice_3 in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history
        if test_4['pass'] is False:
            p_test['fail_message'] += "Called custom block 'sundae' 100x.  Expected to see ice_4 in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history
        if test_5['pass'] is False:
            p_test['fail_message'] += "Called custom block 'sundae' 100x.  Expected to see ice_5 in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history
        if test_6['pass'] is False:
            p_test['fail_message'] += "Called custom block 'sundae' 100x.  Expected to see dry_1 in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history
        if test_7['pass'] is False:
            p_test['fail_message'] += "Called custom block 'sundae' 100x.  Expected to see dry_2 in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history
        if test_8['pass'] is False:
            p_test['fail_message'] += "Called custom block 'sundae' 100x.  Expected to see dry_3 in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history
        if test_9['pass'] is False:
            p_test['fail_message'] += "Called custom block 'sundae' 100x.  Expected to see dry_4 in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history
        if test_10['pass'] is False:
            p_test['fail_message'] += "Called custom block 'sundae' 100x.  Expected to see dry_5 in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history





        if test_1['pass'] and test_2['pass'] and test_3['pass'] and test_4['pass'] and test_5['pass'] and \
                test_6['pass'] and test_7['pass'] and test_8['pass'] and test_9['pass'] and \
                test_10['pass'] and smash_in_1:
            p_test['pass'] = True
            p_test['points'] += p_points
    return p_test


def add_icecreams_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string

    p_test = {"name": "Checking that pressing 'i' adds an ice cream to the ice_creams list.  Use add, not insert."
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing 'i' adds an ice cream to the ice_creams list..<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing 'i' does not appear to add an ice cream to the ice_creams list. "
                              "does not appear to work.<br>",
              "points": 0
              }
    add_1 = True
    sprite = brickLayer(0, 0, 0, pendown=False, variables={"ice_creams":
                                                                   ['ice_1', 'ice_2', 'ice_3', 'ice_4', 'ice_5', ],
                                                           'dry_toppings':
                                                                   ['dry_1', 'dry_2', 'dry_3', 'dry_4', 'dry_5', ],
                                                           'sensing_answer': ['meat']
                                                           })

    for key in p_scripts:
        script = p_scripts[key]
        test_i = match_string(r"event_whenkeypressed', \s 'i'", script)
        if test_i['pass']:
            print('xxxx {} '.format(script))
            add_1 = do_sprite(sprite, script, True)

    #if test_1['pass'] is False:
    #        p_test['fail_message'] += "Called custom block 'smash_in' 100x.  Expected to see ice_1 in the results" \
                                   #   " but did not.  Got this:<br>" + sprite.say_history

    # if test_1['pass'] and  add_1:
    #         p_test['pass'] = True
    #         p_test['points'] += p_points
    return p_test