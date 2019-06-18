def five_loop(filename_data):
    import re

    loop_range = re.search(r'in \s range \( .* [56789]', filename_data, re.X | re.M | re.S)
    while_check = re.search(r'while .+ < .+ [56789]', filename_data, re.X | re.M | re.S)
    manual_check = len(re.findall(r'min_item\(', filename_data, re.X | re.M | re.S))

    p_test = {"name": "Run min_item 5 times (5 points) <br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5> min_item ran 5 times",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Min item does not appear to have been run 5x.  Looked for one of these things<br>"
                              "for .. in range 5 (or 6, 7, 8, 9), a while loop less than 5 (or 6,7,8 or 9),"
                              " or else manually running min_item 5 times.  <br>"
                              "If you think yours  should work, try running min_item 5x a slightly different way.<br>",
              "points": 0,
              }
    if loop_range or while_check or manual_check > 5:
        p_test['points'] = 5
    else:
        p_test['pass'] = False
    return p_test
