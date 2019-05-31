# Input parameters: lab i.e. 3.026 (string)
#                   test number (1,2,3,4)
# Output: Dictionary of test_list_created
# This module runs tests


def function_test(p_lab, p_test_number):
    import delegator
    import re

    p_test_function = {"name": "Testing calling functions, test " + str(p_test_number),
                       "pass": True,
                       "pass_message": "Pass! Test number " + str(p_test_number) + " gave expected result. <br>",
                       "fail_message": "Fail. Test number " + str(p_test_number) + " gave unexpected result. <br>",
                       }

    cmd = 'python3 /tmp/' + str(p_lab) + '.test.py testAutograde.test_' + str(p_test_number) + " 2>&1 "

    c = delegator.run(cmd)

    error = re.search('Error', c.out, re.X | re.M | re.S)
    failed_assertion = re.search('AssertionError', c.out, re.X | re.M | re.S)
    OK = re.search('^OK$', c.out, re.X | re.M | re.S)

    formatted_cout = re.sub(r"\n", "<br>", c.out)
    if failed_assertion:
        p_test_function['pass'] = False
        p_test_function['fail_message'] += "Function ran but gave the wrong result. <br>"
        p_test_function['fail_message'] += formatted_cout + "<br>"
    elif error:
        p_test_function['pass'] = False
        p_test_function['fail_message'] += "Function didn't run at all.  Check for coding errors. <br>"
        p_test_function['fail_message'] += formatted_cout + "<br>"


    return p_test_function