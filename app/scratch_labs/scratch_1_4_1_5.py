def min_two_sprites(p_json, p_points):
    """
    Checks that there are at least two sprites in the code
    :param p_json: json data from file, which is the code of the scratch file. (dict)
    :param p_points: number of points this is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch import count_sprites
    num_sprites = count_sprites(p_json)
    p_test = {"name": "Checking that there is at least two sprites (" + str(p_points) + " points)<br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "We found at least two sprites in the code!<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Code does not have at least two sprites.<br>",
              "points": 0
              }
    if num_sprites >= 2:
        p_test['points'] += p_points
    else:
        p_test['pass'] = False
        p_test['fail_message'] += "Found this many sprites: " + str(num_sprites)
    return p_test


def show_and_hide(p_json, p_points):
    """
    Checks that there is a sprite that hides and shoes
    :param p_json: json data from file, which is the code of the scratch file. (dict)
    :param p_points: number of points this is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that there is hiding and showing of sprites going on (" + str(p_points) + " points)<br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "We found hiding and showing of sprites!<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Code does not have hiding and showing of sprites.<br>",
              "points": 0
              }
    test_show = match_string(r'looks_show', p_json)
    if test_show['pass'] is False:
        p_test['fail_message'] += test_show['fail_message']
    test_hide = match_string(r'looks_hide', p_json)
    if test_hide['pass'] is False:
        p_test['fail_message'] += test_hide['fail_message']
    if test_show['pass'] and test_hide['pass']:
        p_test['points'] += p_points
    else:
        p_test['pass'] = False
    return p_test
