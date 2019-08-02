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
        p_test['fail_message'] += 'Did not find ice_creams list in your code.<br>'
    find_wet_toppings = find_list(p_json, 'wet_toppings', 5)
    if find_wet_toppings['pass'] is False:
        p_test['fail_message'] += 'Did not find wet_toppings list in your code.<br>'
    find_dry_toppings = find_list(p_json, 'dry_toppings', 5)
    if find_dry_toppings['pass'] is False:
        p_test['fail_message'] += 'Did not find dry_toppings list in your code.<br>'
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
                              "Be sure length of LIST (orange color) not length of WORD (green color).<br>",
              "points": 0
              }
    smash_in_1 = True
    if 'smash_in' in p_scripts.keys():
        sprite = brickLayer(0, 0, 0, pendown=False, variables={"ice_creams": ['ice_1', 'ice_2', 'ice_3', 'ice_4',
                                                                              'ice_5', ],
                                                               'dry_toppings': ['dry_1', 'dry_2', 'dry_3', 'dry_4',
                                                                                'dry_5', ]})
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
                              "Did you join in an extra space between ice cream and dry topping?<br>",
              "points": 0
              }
    smash_in_1 = True
    if 'smash_in' in p_scripts.keys():
        sprite = brickLayer(0, 0, 0, pendown=False, variables={"ice_creams": ['ice_1', ],
                                                               'dry_toppings': ['dry_1', ]})
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
                              "Be sure length of LIST (orange color) not length of WORD (green color).<br>"
                              "Do you have a space between your items?  Be sure to 'join' a space"
                              "in addition to the items.<br>",
              "points": 0
              }
    smash_in_1 = True
    if 'sundae' in p_scripts.keys():
        sprite = brickLayer(0, 0, 0, pendown=False, variables={"ice_creams": ['ice_1', 'ice_2', 'ice_3', 'ice_4',
                                                                              'ice_5', ],
                                                               'wet_toppings': ['wet_1', 'wet_2', 'wet_3', 'wet_4',
                                                                                'wet_5', ]})
        script = p_scripts['sundae']
        for _ in range(150):
            smash_in_1 = do_sprite(sprite, script, True)
        print("VALHALLA {}".format(sprite.say_history))
        test_1 = match_string(r'ice_1', sprite.say_history)
        test_2 = match_string(r'ice_2', sprite.say_history)
        test_3 = match_string(r'ice_3', sprite.say_history)
        test_4 = match_string(r'ice_4', sprite.say_history)
        test_5 = match_string(r'ice_5', sprite.say_history)
        test_6 = match_string(r'wet_1', sprite.say_history)
        test_7 = match_string(r'wet_2', sprite.say_history)
        test_8 = match_string(r'wet_3', sprite.say_history)
        test_9 = match_string(r'wet_4', sprite.say_history)
        test_10 = match_string(r'wet_5', sprite.say_history)

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
            p_test['fail_message'] += "Called custom block 'sundae' 100x.  Expected to see wet_1 in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history
        if test_7['pass'] is False:
            p_test['fail_message'] += "Called custom block 'sundae' 100x.  Expected to see wet_2 in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history
        if test_8['pass'] is False:
            p_test['fail_message'] += "Called custom block 'sundae' 100x.  Expected to see wet_3 in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history
        if test_9['pass'] is False:
            p_test['fail_message'] += "Called custom block 'sundae' 100x.  Expected to see wet_4 in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history
        if test_10['pass'] is False:
            p_test['fail_message'] += "Called custom block 'sundae' 100x.  Expected to see wet_5 in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history

        sprite = brickLayer(0, 0, 0, pendown=False, variables={"ice_creams": ['ice_1', ],
                                                               'wet_toppings': ['wet_1', ]})
        script = p_scripts['sundae']
        for _ in range(1):
            smash_in_1 = do_sprite(sprite, script, True)
        test_200 = match_string(r'ice_1 \s wet_1', sprite.say_history)
        if test_200['pass'] is False:
            p_test['fail_message'] += "Called custom block 'sundae' 1x.  Expected to see 'ice_1 wet_1' " \
                                      "in the results" \
                                      " but did not.  Got this:<br>" + sprite.say_history + "<br>" \
                                                                                            "Did you remember to join" \
                                                                                            " a space?<br>"

        if 'fancy_sundae' in p_scripts.keys():
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"ice_creams": ['ice_6', 'ice_7', 'ice_8', 'ice_9',
                                                                                  'ice_10', ],
                                                                   'dry_toppings': ['dry_6', 'dry_7', 'dry_8', 'dry_9',
                                                                                    'dry_10', ],
                                                                   'wet_toppings': ['wet_6', 'wet_7', 'wet_8', 'wet_9',
                                                                                    'wet_10', ],
                                                                   })
            script = p_scripts['fancy_sundae']
            for _ in range(150):
                smash_in_1 = do_sprite(sprite, script, True)
            print("VALHALLA {}".format(sprite.say_history))
            test_100 = match_string(r'ice_6', sprite.say_history)
            test_101 = match_string(r'ice_7', sprite.say_history)
            test_102 = match_string(r'ice_8', sprite.say_history)
            test_103 = match_string(r'ice_9', sprite.say_history)
            test_104 = match_string(r'ice_10', sprite.say_history)
            test_105 = match_string(r'dry_6', sprite.say_history)
            test_106 = match_string(r'dry_7', sprite.say_history)
            test_107 = match_string(r'dry_8', sprite.say_history)
            test_108 = match_string(r'dry_9', sprite.say_history)
            test_109 = match_string(r'dry_10', sprite.say_history)
            test_110 = match_string(r'wet_6', sprite.say_history)
            test_111 = match_string(r'wet_7', sprite.say_history)
            test_112 = match_string(r'wet_8', sprite.say_history)
            test_113 = match_string(r'wet_9', sprite.say_history)
            test_114 = match_string(r'wet_10', sprite.say_history)

            if test_100['pass'] is False:
                p_test['fail_message'] += "Called custom block 'fancy_sundae' 100x.  " \
                                          "Expected to see ice_6 in the results" \
                                          " but did not.  Got this:<br>" + sprite.say_history
            if test_101['pass'] is False:
                p_test['fail_message'] += "Called custom block 'fancy_sundae' 100x.  " \
                                          "Expected to see ice_7 in the results" \
                                          " but did not.  Got this:<br>" + sprite.say_history
            if test_102['pass'] is False:
                p_test['fail_message'] += "Called custom block 'fancy_sundae' 100x.  " \
                                          "Expected to see ice_8 in the results" \
                                          " but did not.  Got this:<br>" + sprite.say_history
            if test_103['pass'] is False:
                p_test['fail_message'] += "Called custom block 'fancy_sundae' 100x.  " \
                                          "Expected to see ice_9 in the results" \
                                          " but did not.  Got this:<br>" + sprite.say_history
            if test_104['pass'] is False:
                p_test['fail_message'] += "Called custom block 'fancy_sundae' 100x.  " \
                                          "Expected to see ice_10 in the results" \
                                          " but did not.  Got this:<br>" + sprite.say_history
            if test_105['pass'] is False:
                p_test['fail_message'] += "Called custom block 'fancy_sundae' 100x.  " \
                                          "Expected to see dry_6 in the results" \
                                          " but did not.  Got this:<br>" + sprite.say_history
            if test_106['pass'] is False:
                p_test['fail_message'] += "Called custom block 'fancy_sundae' 100x.  " \
                                          "Expected to see dry_7 in the results" \
                                          " but did not.  Got this:<br>" + sprite.say_history
            if test_107['pass'] is False:
                p_test['fail_message'] += "Called custom block 'fancy_sundae' 100x.  " \
                                          "Expected to see dry_8 in the results" \
                                          " but did not.  Got this:<br>" + sprite.say_history
            if test_108['pass'] is False:
                p_test['fail_message'] += "Called custom block 'fancy_sundae' 100x.  " \
                                          "Expected to see dry_9 in the results" \
                                          " but did not.  Got this:<br>" + sprite.say_history
            if test_109['pass'] is False:
                p_test['fail_message'] += "Called custom block 'fancy_sundae' 100x.  " \
                                          "Expected to see dry_10 in the results" \
                                          " but did not.  Got this:<br>" + sprite.say_history
            if test_110['pass'] is False:
                p_test['fail_message'] += "Called custom block 'fancy_sundae' 100x.  " \
                                          "Expected to see wet_6 in the results" \
                                          " but did not.  Got this:<br>" + sprite.say_history
            if test_111['pass'] is False:
                p_test['fail_message'] += "Called custom block 'fancy_sundae' 100x.  " \
                                          "Expected to see wet_7 in the results" \
                                          " but did not.  Got this:<br>" + sprite.say_history
            if test_112['pass'] is False:
                p_test['fail_message'] += "Called custom block 'fancy_sundae' 100x.  " \
                                          "Expected to see wet_8 in the results" \
                                          " but did not.  Got this:<br>" + sprite.say_history
            if test_113['pass'] is False:
                p_test['fail_message'] += "Called custom block 'fancy_sundae' 100x.  " \
                                          "Expected to see wet_9 in the results" \
                                          " but did not.  Got this:<br>" + sprite.say_history
            if test_114['pass'] is False:
                p_test['fail_message'] += "Called custom block 'fancy_sundae' 100x.  " \
                                          "Expected to see wet_10 in the results" \
                                          " but did not.  Got this:<br>" + sprite.say_history

            sprite = brickLayer(0, 0, 0, pendown=False, variables={"ice_creams": ['ice_1', ],
                                                                   "dry_toppings": ['dry_1', ],
                                                                   'wet_toppings': ['wet_1', ]
                                                                   })
            for _ in range(1):
                smash_in_1 = do_sprite(sprite, script, True)
            test_201 = match_string(r'ice_1 \s dry_1 \s wet_1', sprite.say_history)
            print("jjj say_hist {}".format(sprite.say_history))
            if test_201['pass'] is False:
                p_test['fail_message'] += "Called custom block 'fancy_sundae' 1x.  Expected to see " \
                                          "'ice_1 dry_1 wet_1'" \
                                          " " \
                                          "in the results" \
                                          " but did not.  Got this:<br>" + sprite.say_history + "<br>" \
                                                                                                "Did you remember " \
                                                                                                "to join" \
                                                                                                " a space?<br>"

            if test_1['pass'] and test_2['pass'] and test_3['pass'] and test_4['pass'] and test_5['pass'] and \
                test_6['pass'] and test_7['pass'] and test_8['pass'] and test_9['pass'] and \
                test_10['pass'] and test_100['pass'] and test_101['pass'] and test_102['pass'] and test_103['pass'] \
                    and test_104['pass'] and test_105['pass'] and test_106['pass'] and test_107['pass'] and\
                    test_108['pass'] \
                    and test_109['pass'] and test_110['pass'] and test_111['pass'] and test_112['pass'] and \
                    test_113['pass'] and test_114['pass'] and test_200['pass'] and test_201['pass'] and smash_in_1:
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
                              "Pressing 'i' adds an ice cream to the ice_creams list.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing 'i' does not appear to add an ice cream to the ice_creams list. <br>",
              "points": 0
              }
    add_1 = True
    sprite = brickLayer(0, 0, 0, pendown=False, variables={"ice_creams": ['ice_1', 'ice_2', 'ice_3', 'ice_4',
                                                                          'ice_5', ],
                                                           'dry_toppings': ['dry_1', 'dry_2', 'dry_3', 'dry_4',
                                                                            'dry_5', ],
                                                           'sensing_answer': ['meat']
                                                           })
    found_i = False
    found_new_item = False
    for key in p_scripts:
        script = p_scripts[key]
        test_i = match_string(r"event_whenkeypressed', \s 'i' .+ sensing_askandwait", script)
        if test_i['pass']:
            found_i = True
            add_1 = do_sprite(sprite, script, True)
            print("ooo is it there? {}".format(sprite.variables))
            if sprite.variables['ice_creams'][-1] == 'meat':
                found_new_item = True
    if found_i is False:
        p_test['fail_message'] += "In your code, did not find 'when i key pressed' in your code " \
                                  "followed by asking user a question<br>"
        return p_test
    if found_new_item is False:
        p_test['fail_message'] += "Tried to add 'meat' to ice_creams.  Didn't find it at end of list.<br>" \
                                  "Found this ice_creams list:<br>" + \
                                  str(sprite.variables['ice_creams'])

    if found_i and found_new_item and add_1:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def add_dry_toppings_and_wet_toppings_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string

    p_test = {"name": "Checking that pressing 'd' adds a dry topping to the dry_toppings list AND "
                      " that pressing 'w' adds a wet topping to the wet _toppings list. <br>Use add, not insert."
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing 'd' adds a dry topping to the dry_toppings list AND "
                              " pressing 'w' adds a wet topping to the wet _toppings list.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing 'd' does not add a dry topping to the dry_toppings list OR "
                              "pressing 'w' does not add a wet topping to the wet _toppings list or both <br>",
              "points": 0
              }
    add_1 = True
    sprite = brickLayer(0, 0, 0, pendown=False, variables={"ice_creams": ['ice_1', 'ice_2', 'ice_3', 'ice_4',
                                                                          'ice_5', ],
                                                           'wet_toppings': ['dry_1', 'dry_2', 'dry_3', 'dry_4',
                                                                            'dry_5', ],
                                                           'sensing_answer': ['poop']
                                                           })
    found_w = False
    found_new_item = False
    for key in p_scripts:
        script = p_scripts[key]
        test_i = match_string(r"event_whenkeypressed', \s 'w' .+ sensing_askandwait", script)
        if test_i['pass']:
            found_w = True
            add_1 = do_sprite(sprite, script, True)
            print("ooo is it there? {}".format(sprite.variables))
            if sprite.variables['wet_toppings'][-1] == 'poop':
                found_new_item = True
    if found_w is False:
        p_test['fail_message'] += "In your code, did not find 'when w key pressed' in your code " \
                                  "followed by asking user a question.<br>"
        return p_test
    if found_new_item is False:
        p_test['fail_message'] += "Tried to add 'poop' to wet_toppings.  Didn't find it at end of list.<br>" \
                                  "Found this wet_toppings list:<br>" + \
                                  str(sprite.variables['wet_toppings']) + "<br>"

    sprite = brickLayer(0, 0, 0, pendown=False, variables={"ice_creams": ['ice_1', 'ice_2', 'ice_3', 'ice_4',
                                                                          'ice_5', ],
                                                           'dry_toppings': ['dry_1', 'dry_2', 'dry_3', 'dry_4',
                                                                            'dry_5', ],
                                                           'sensing_answer': ['dried boogers']
                                                           })
    found_d = False
    found_new_dry = False
    for key in p_scripts:
        script = p_scripts[key]
        test_i = match_string(r"event_whenkeypressed', \s 'd' .+ sensing_askandwait", script)
        if test_i['pass']:
            found_d = True
            add_1 = do_sprite(sprite, script, True)
            print("ooo is it there? {}".format(sprite.variables))
            if sprite.variables['dry_toppings'][-1] == 'dried boogers':
                found_new_dry = True
    if found_d is False:
        p_test['fail_message'] += "In your code, did not find 'when d key pressed' in your code " \
                                  "followed by asking user a question.<br>"
        return p_test
    if found_new_dry is False:
        p_test['fail_message'] += "Tried to add 'dried boogers' to dry_toppings.  Didn't find it at end of list.<br>" \
                                  "Found this dry_toppings list:<br>" + \
                                  str(sprite.variables['dry_toppings']) + "<br>"
    if found_w and found_d and found_new_item and found_new_dry and add_1:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def delete_two_questions(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string

    p_test = {"name": "Checking that there are two questions asked after pressing 'x'"
                      "(" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "That there are two questions asked after pressing 'x' <br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "That there are not two questions asked after pressing 'x'."
                              "Check that you have a 'When x key is pressed' in your code.<br>"
                              "Check that you ask two questions after that - one for the list and "
                              "one for the item to delete <br>",
              "points": 0
              }
    two_questions = False
    for key in p_scripts:
        script = p_scripts[key]
        test_two_questions = match_string(r"event_whenkeypressed', \s 'x' .+ sensing_askandwait .+ sensing_askandwait",
                                          script)
        if test_two_questions:
            p_test['pass'] = True
    if p_test['pass']:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def delete_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string

    p_test = {"name": "Checking that after pressing 'x', you can delete selected item from selected list."
                      "(" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "After pressing 'x', you can delete selected item from selected list.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "After pressing 'x', deleting selected item from selected list does not work.<br>"
                              "Test tried to delete item 3 from list ice_creams<br>"
                              "Test asks which list you want to delete, then which item - "
                              " You must also ask in this order.<br>",
              "points": 0
              }
    sprite1 = brickLayer(0, 0, 0, pendown=False, variables={"ice_creams": ['ice_1', 'ice_2', 'ice_3', 'ice_4',
                                                                           'ice_5', ],
                                                            'dry_toppings': ['dry_1', 'dry_2', 'dry_3', 'dry_4',
                                                                             'dry_5', ],
                                                            'sensing_answer': ['ice_creams', '3']
                                                            })
    sprite2 = brickLayer(0, 0, 0, pendown=False, variables={"ice_creams": ['ice_1', 'ice_2', 'ice_3', 'ice_4',
                                                                           'ice_5', ],
                                                            'dry_toppings': ['dry_1', 'dry_2', 'dry_3', 'dry_4',
                                                                             'dry_5', ],
                                                            'sensing_answer': ['ice_creams', '4']
                                                            })
    sprite3 = brickLayer(0, 0, 0, pendown=False, variables={"ice_creams": ['ice_1', 'ice_2', 'ice_3', 'ice_4',
                                                                           'ice_5', ],
                                                            'dry_toppings': ['dry_1', 'dry_2', 'dry_3', 'dry_4',
                                                                             'dry_5', ],
                                                            'sensing_answer': ['dry_toppings', '1']
                                                            })
    sprite4 = brickLayer(0, 0, 0, pendown=False, variables={"ice_creams": ['ice_1', 'ice_2', 'ice_3', 'ice_4',
                                                                           'ice_5', ],
                                                            'wet_toppings': ['wet_1', 'wet_2', 'wet_3', 'wet_4',
                                                                             'wet_5', ],
                                                            'sensing_answer': ['wet_toppings', '5']
                                                            })
    test1 = False
    test2 = False
    test3 = False
    test4 = False
    for key in p_scripts:
        script = p_scripts[key]
        test_two_questions = match_string(r"event_whenkeypressed', \s 'x' .+ sensing_askandwait .+ sensing_askandwait",
                                          script)
        if test_two_questions['pass']:
            print("start of delete_works")
            print("uuu this asdfasdf{}".format(script))
            run1 = do_sprite(sprite1, script, True)
            print("post run1 sprite vars {}".format(sprite1.variables))
            if sprite1.variables['ice_creams'] == ['ice_1', 'ice_2', 'ice_4', 'ice_5', ]:
                test1 = True
            if test1 is False:
                p_test['fail_message'] += "Tried to delete item 3 from ice creams, failed.  <br>" \
                                          "Should be ['ice_1', 'ice_2', 'ice_4', 'ice_5', ].  Got this instead:<br>" \
                                          + str(sprite1.variables['ice_creams']) + "<br>"
            print("pre run2 sprite vars {}".format(sprite2.variables))
            run2 = do_sprite(sprite2, script, True)
            if sprite2.variables['ice_creams'] == ['ice_1', 'ice_2', 'ice_3', 'ice_5', ]:
                test2 = True
            if test2 is False:
                p_test['fail_message'] += "Tried to delete item 4 from ice creams, failed.  <br>" \
                                          "Should be ['ice_1', 'ice_2', 'ice_3', 'ice_5', ].  Got this instead:<br>" \
                                          + str(sprite2.variables['ice_creams']) + "<br>"
            print("post run2 sprite vars {}".format(sprite2.variables))
            run3 = do_sprite(sprite3, script, True)
            if sprite3.variables['dry_toppings'] == ['dry_2', 'dry_3', 'dry_4', 'dry_5', ]:
                test3 = True
            run4 = do_sprite(sprite4, script, True)
            if sprite4.variables['wet_toppings'] == ['wet_1', 'wet_2', 'wet_3', 'wet_4',]:
                test4 = True
        if test_two_questions['pass'] and test1 and test2 and test3 and test4 and run1 and run2 and run3 and run4:
            p_test['pass'] = True
            p_test['points'] += p_points
    return p_test
