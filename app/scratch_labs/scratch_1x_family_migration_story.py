def min_two_stages(p_json, p_points):
    """
    Checks that there are at least two stages in the code
    :param p_json: json data from file, which is the code of the scratch file. (dict)
    :param p_points: number of points this is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch import count_stage_changes
    num_changes = count_stage_changes(p_json)
    p_test = {"name": "Checking that there is at least two stage changes (" + str(p_points) + " points)<br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "We found at least two stage changes in the code!<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Code does not have at least two stage changes.<br>",
              "points": 0
              }
    if num_changes >= 2:
        p_test['points'] += p_points
    else:
        p_test['pass'] = False
        p_test['fail_message'] += "Found this many stage changes: " + str(num_changes)
    return p_test
