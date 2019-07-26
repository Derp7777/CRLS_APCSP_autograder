def one_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that pressing '1' key welcomes each name individually.  See instructions"
                      "from what this should look like "
                      " (" + str(p_points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Pressing '1' key welcomes each name individually.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Pressing '1' key does not welcome each name individually. <br>",
              "points": 0
              }
    found_1 = False
    for key in p_scripts:
        script = p_scripts[key]
        test_1_key = match_string(r"event_whenkeypressed', \s '1' .+  data_setvariableto .+ control_repeat .+ "
                                  r"looks_sayforsecs", script)
        if test_1_key['pass']:
            found_1 = True
            sprite = brickLayer(0, 0, 0, pendown=False, variables={"names": ['GORILLA Joe', 'Emma',
                                                                             'Miguel', 'Andrea']
                                                                   })
            run_1 = do_sprite(sprite, script, True)
            print("uuuu after run1 {} {}".format(sprite.variables, sprite.say_history))

    if found_1 is False:
        p_test['fail_message'] += "In your code, did not find 'when 1 key pressed' in your code " \
                                  "followed by some expected elements - setting a variable to a value " \
                                  "(to track the index or counter)," \
                                  "a repeat of some sort, and a say of some sort<br>"
    if found_1:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test
