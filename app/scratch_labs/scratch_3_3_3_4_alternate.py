def day_of_week_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string

    p_test = {"name": "Checking that the happy_birthday custom block with one argument works"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "The happy_birthday custom block with one argument works.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The make_triangle custom block with one argument does not appear to work."
                              "Is the input parameter named name?<br>"
                              "BE SURE INPUT PARAMETER IS NAMED name OTHERWISE THIS TEST BREAKS.<br>",
              "points": 0
              }
    if 'happy_birthday %s' in p_scripts.keys():
        sprite = brickLayer(0, 0, 0, pendown=False, variables={"day": 1})
        script = p_scripts['day_of_week %s']
        day_success_1 = do_sprite(sprite, script, True)
        print("VALHALLA {}".format(sprite.say_history))
        # test_1a = match_string(r'McGlathery', sprite.say_history)
        # test_1b = match_string(r'(birthday|Birthday|BIRTHDAY)', sprite.say_history)
        # if test_1a['pass'] is False:
        #     p_test['fail_message'] += "Didn't find the word 'McGlathery' in say output when I called custom block" \
        #                               "with input parameter 'McGlathery'<br>"
        # if test_1b['pass'] is False:
        #     p_test['fail_message'] += "Didn't find the word 'birthday', 'Birthday', or 'BIRTHDAY'" \
        #                               " in say output when I called custom block" \
        #                               "with input parameter 'McGlathery'<br>"
        # sprite = brickLayer(0, 0, 0, pendown=False, variables={"name": 'MichaelJordan'})
        # script = p_scripts['happy_birthday %s']
        # word_success_2 = do_sprite(sprite, script, True)
        # test_2a = match_string(r'MichaelJordan', sprite.say_history)
        # test_2b = match_string(r'(birthday|Birthday|BIRTHDAY)', sprite.say_history)
        # if test_2a['pass'] is False:
        #     p_test['fail_message'] += "Didn't find the word 'MichaelJordan' in say output when I called custom block " \
        #                               "with input parameter 'MichaelJordan'<br>"
        # if test_2b['pass'] is False:
        #     p_test['fail_message'] += "Didn't find the word 'birthday', 'Birthday', or 'BIRTHDAY' " \
        #                               "in say output when I called custom block " \
        #                               "with input parameter 'MichaelJordan'<br>"
        #
        # if word_success_1 and word_success_2 and test_1a['pass'] and test_1b['pass'] and test_2a['pass'] and \
        #         test_2b['pass']:
        #     p_test['pass'] = True
        #     p_test['points'] += p_points
    return p_test
