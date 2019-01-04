from flask import render_template, url_for, request, redirect, flash

from app import app
from app.forms import UploadForm
from werkzeug.utils import secure_filename
import os


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Please select a file')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        if not allowed_file(file.filename):
            flash('This type of file not allowed.  Only files ending in .py.'
                  '  In particular, Google doc and text files are not allowed.'
                  'You have to turn in a Python file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash(file.filename + ' uploaded')
            if request.form['lab'] == '1.040':
                return redirect(url_for('feedback_1040', filename=filename))
            elif request.form['lab'] == '1.060':
                return redirect(url_for('feedback_1060', filename=filename))
            elif request.form['lab'] == '2.020':
                return redirect(url_for('feedback_2020', filename=filename))
            elif request.form['lab'] == '2.032a':
                return redirect(url_for('feedback_2032a', filename=filename))
            elif request.form['lab'] == '2.032b':
                return redirect(url_for('feedback_2032b', filename=filename))
            elif request.form['lab'] == '2.040':
                return redirect(url_for('feedback_2040', filename=filename))
            elif request.form['lab'] == '2.050a':
                return redirect(url_for('feedback_2050a', filename=filename))
            elif request.form['lab'] == '2.050b':
                return redirect(url_for('feedback_2050b', filename=filename))
            elif request.form['lab'] == '3.011':
                return redirect(url_for('feedback_3.011', filename=filename))

            
    form = UploadForm()
    user = {'username': 'CRLS Scholar!!!'}
    return render_template('index.html', title='Home', user=user, form=form)


@app.route('/feedback_1040')
def feedback_1040():
    import re
    import subprocess
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 34.5, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2018', filename)
    find_lab = re.search('1.040', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2018_luismartinez_1.04.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2018_luismartinez_1.040.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)

        # Check for part 1 asks 3 questions
        cmd = 'grep "input" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        inputs = int(c.out)
        test_inputs_1 = {"name": "Testing for at genie asking at least 3 questions (first part of lab) ( 5 points )",
                         "pass": True,
                         "pass_message": "Pass!  Genie asks at least 3 questions (first part of lab)",
                         "fail_message": "Fail.  Code does not have at least 3 inputs (first part of lab).<br>"
                                         "The Genie needs to ask for 3 wishes for the first part"
                                         "Please fix error and resubmit (other tests not run). <br>",
                         }
        if inputs < 3:
            test_inputs_1['pass'] = False
            tests.append(test_inputs_1)
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            score_info['score'] += 5
            tests.append(test_inputs_1)

            # Check that things are in correct order (a, b, c)
            filename_output = filename + '.out'
            cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/1.040.in > ' \
                  + filename_output
            c = delegator.run(cmd)
            if c.err:
                flash('bad! You have an error somewhere in running program correct order 1.040')
                flash(c.err)
            with open(filename_output, 'r') as myfile:
                outfile_data = myfile.read()

            search_object = re.search(r".+ "
                                      r"a1 "
                                      r".+ "
                                      r"a2 "
                                      r".+ "
                                      r"a3 "
                                      r".+ ",
                                      outfile_data, re.X | re.M | re.S)
            test_order_1 = {"name": "Testing that Genie answers in correct order for part 1 (5 points)",
                            "pass": True,
                            "pass_message": "Pass!  Genie appears to answer your wishes in correct order",
                            "fail_message": "Fail.  Double check that the Genie is answering in correct order. <br>"
                                            "Genie needs to reply back with the 3 wishes you asked for in a particular order. <br>"
                                            "Note: you must have a comma, period, space, or something between wishes."
                                            "Review the sample run if this isn't clear. <br>"
                            }
            if not search_object or c.err:
                test_order_1['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_order_1)

            # Check for part 2 asks 3 more questions, 6 total
            cmd = 'grep "input" ' + filename + ' | wc -l  '
            c = delegator.run(cmd)
            inputs = int(c.out)
            test_inputs_2 = {"name": "Testing for at genie asking at least 6 questions (first + second part of lab) "
                                     "(5 points)",
                             "pass": True,
                             "pass_message": "Pass!  Genie asks at least 6 questions (first + second part of lab)",
                             "fail_message": "Fail. Code does not have at least 6 inputs (first + second part of lab)."
                                             "<br>"
                                             "The Genie needs to ask for 3 wishes for the first part and 3 for the second part",
                             }
            if inputs < 6:
                test_inputs_2['pass'] = False
                tests.append(test_inputs_2)
            else:
                score_info['score'] += 5
                tests.append(test_inputs_2)

            # Check for asing variable questions
            process_grep1 = subprocess.Popen(['/bin/grep', "input([\"']", filename], stdout=subprocess.PIPE)
            process_wc = subprocess.Popen(['wc', '-l'], stdin=process_grep1.stdout, stdout=subprocess.PIPE)
            process_grep1.wait()
            process_grep1.stdout.close()
            output_string = str(process_wc.communicate()[0])
            match_object = re.search(r"([0-9]+)", output_string)
            inputs_variable = int(match_object.group())
            test_input_variable = {"name": "Testing for use of variable to sub for repeated strings in asking questions"
                                           "(5 points)",
                                   "pass": True,
                                   "pass_message": "Pass!  Genie appears to have stuck repeated strings into variables,"
                                                   " per instructions AND there are at least 6 inputs",
                                   "fail_message": "Fail.  There are over 3 inputs with single or double quotations. "
                                                   "<br>"
                                                   "Please recheck the instructions about putting repeated strings into variables. "
                                                   "This translates to -10 points deduction.<br>",
                                   }
            if inputs_variable > 4:
                test_input_variable['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_input_variable)

            # Check that things are in correct order (a, b, c, then b, c, a)

            cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/1.040.in > ' \
                  + filename_output
            c = delegator.run(cmd)

            search_object = re.search(r".+ "
                                      r"a1 "
                                      r".+ "
                                      r"a2 "
                                      r".+ "
                                      r"a3 "
                                      r".+ "
                                      r"b2 "
                                      r".+ "
                                      r"b3 "
                                      r".+ "
                                      r"b1",
                                      outfile_data, re.X | re.M | re.S)
            test_order_2 = {"name": "Testing that Genie answers in correct order for part 1 and part 2 (5 points)",
                            "pass": True,
                            "pass_message": "Pass!  Genie appears to answer your wishes in correct order for part 1 "
                                            "and part 2",
                            "fail_message": "Fail.  Double check that the Genie is answering in correct order for both "
                                            "part 1 and part 2. <br>"
                                            "wish1, wish2, and wish3 responses need to go in a particular order. <br>"
                                            "Note: you must have a comma, period, space, or something between wishes."
                                            "Review the instructions if this isn't clear. <br>"
                            }
            if not search_object or c.err:
                test_order_2['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_order_2)

            # Find number of PEP8 errors
            cmd = '/home/ewu/CRLS_APCSP_autograder/venv1/bin/pycodestyle ' + filename + ' | wc -l  '
            c = delegator.run(cmd)
            if c.err:
                flash(c.err)
            else:
                flash(c.out)
            side_errors = int(c.out)
            test_pep8 = {"name": "Testing for PEP8 warnings and errors (7 points)",
                         "pass": True,
                         "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                         "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                                                                          "This translates to -" + str(
                             side_errors) + " point(s) deduction.<br>"
                         }
            if side_errors != 0:
                test_pep8['pass'] = False
            score_info['score'] += max(0, int(7) - side_errors)
            tests.append(test_pep8)

            # Check for help comment
            cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
            c = delegator.run(cmd)
            help_comments = int(c.out)
            test_help = {"name": "Testing that you got a help and documented it as a comment (2.5 points)",
                         "pass": True,
                         "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                                         "Be sure your comment is meaningful, otherwise this can be overturned on review.",
                         "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                                         " how somebody helped you with your code.  <br>"
                                         "If you didn't have any problems, then ask somebody to check that your code"
                                         " gives correct outputs, given an input.<br>"
                                         "This translates to -5 points deduction.<br>",
                         }
            if help_comments == 0:
                test_help['pass'] = False
            else:
                score_info['score'] += 2.5
            tests.append(test_help)

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_1060')
def feedback_1060():
    import re
    import subprocess
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 59, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2018', filename)
    find_lab = re.search('1.060', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2018_luismartinez_1.06.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2018_luismartinez_1.060.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)

        # Check that asks at least 5 questions
        cmd = 'grep "input" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        inputs = int(c.out)
        test_inputs_1 = {"name": "Testing for at least 5 input questions (5 points)",
                         "pass": True,
                         "pass_message": "Pass!  Asks at least 5 inputs questions",
                         "fail_message": "Fail.  Code does not have at least 5 input questions.<br>"
                                         "The program needs to ask for 5 inputs of parts of speech"
                                         "Please fix error and resubmit (other tests not run). <br>",
                         }
        if inputs < 5:
            test_inputs_1['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_inputs_1)

        # Check that inputs are named after part of speech
        cmd = 'grep -E "verb|noun|adjective|adverb|preposition" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        parts_of_speech = int(c.out)
        test_parts_of_speech = {"name": "Testing that variables named after parts of speech (5 points)",
                                "pass": True,
                                "pass_message": "Pass!  Code asks at least 5 parts of speech in code",
                                "fail_message": "Fail.  Variables should be named after parts of speech. "
                                                "(noun, verb1, adjective, noun3, adverb10, etc...)<br>"
                                                "The program needs to ask for 5 inputs of parts of speech.<br>"
                                                "Please fix error and resubmit (other tests not run). <br>",
                                }

        if parts_of_speech < 5:
            test_parts_of_speech['pass'] = False
            tests.append(test_parts_of_speech)
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            score_info['score'] += 5
            tests.append(test_parts_of_speech)

            # Check for at least 1 print statement
            cmd = 'grep "print" ' + filename + ' | wc -l  '
            c = delegator.run(cmd)
            prints = int(c.out)
            test_one_print = {"name": "Testing for at least 1 print statement (5 points)",
                              "pass": True,
                              "pass_message": "Pass!  Asks at least 1 print statement.",
                              "fail_message": "Fail.  Code does not have at least 1 print statement.<br>"
                                              "The program needs to have print statements"
                              }
            if prints < 1:
                test_one_print['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_one_print)

            # Check for less than 3 print statement
            test_three_print = {"name": "Testing for  less than 3 print statements (5 points)",
                                "pass": True,
                                "pass_message": "Pass!  Fewer than 3 print statements.",
                                "fail_message": "Fail.  Code has more than 3 print statements.<br>"
                                                "The program should have max 3 prints"
                                }
            if prints > 3:
                test_three_print['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_three_print)

            # Check that things are in correct order.  First 5 inputs show up in output)
            filename_output = filename + '.out'
            cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/1.060.in > ' \
                  + filename_output
            c = delegator.run(cmd)
            if c.err:
                flash('bad! You have an error somewhere in running program first 5 inputs show up')
            with open(filename_output, 'r') as myfile:
                outfile_data = myfile.read()

            search_object_1 = re.search(r"a1", outfile_data, re.X | re.M | re.S)
            search_object_2 = re.search(r"a2", outfile_data, re.X | re.M | re.S)
            search_object_3 = re.search(r"a3", outfile_data, re.X | re.M | re.S)
            search_object_4 = re.search(r"b1", outfile_data, re.X | re.M | re.S)
            search_object_5 = re.search(r"b2", outfile_data, re.X | re.M | re.S)

            test_show_5 = {"name": "Testing that first 5 inputs show up in the output printout (5 points)",
                           "pass": True,
                           "pass_message": "Pass!  First 5 inputs show up in the output printout",
                           "fail_message": "Fail.  Check that first 5 inputs show up in the output printout.<br>"
                                           "For example, if you typed in noun1, verb1, noun2, verb2, and adjective<br>"
                                           "noun1, verb1, noun2, verb2, and adjective should all appear in the prinout."
                                           "<br> ",
                           }
            if search_object_1 and search_object_2 and search_object_3 and search_object_4 and search_object_5:
                score_info['score'] += 15
            else:
                test_show_5['pass'] = False
            tests.append(test_show_5)

            # Check for 3 punctuations
            filename_output = filename + '.out'
            cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/1.060.in > ' \
                  + filename_output
            c = delegator.run(cmd)
            if c.err:
                flash('bad! You have an error somewhere in running program check 3 punctuations')
            with open(filename_output, 'r') as myfile:
                outfile_data = myfile.read()

            num_periods = outfile_data.count('.')
            num_questions = outfile_data.count('?')
            num_exclamations = outfile_data.count('!')
            num_punctuations = num_periods + num_questions + num_exclamations
            test_puncts = {"name": "Testing that there are at least 3 punctuations (5 points)",
                           "pass": True,
                           "pass_message": "Pass!  There are at least 3 punctuations.",
                           "fail_message": "Fail.  Check that there are at least 3 punctuations.<br>"
                                           "Looking for at least 3 periods, questions marks, or exclamations "
                                           "<br> ",
                           }
            if num_punctuations < 3:
                test_puncts['pass'] = False
            else:
                score_info['score'] += 5

            tests.append(test_puncts)

            # Find number of PEP8 errors
            cmd = '/home/ewu/CRLS_APCSP_autograder/venv1/bin/pycodestyle ' + filename + ' | wc -l  '
            c = delegator.run(cmd)
            side_errors = int(c.out)
            test_pep8 = {"name": "Testing for PEP8 warnings and errors (14 points)",
                         "pass": True,
                         "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                         "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                                                                          "This translates to -" + str(
                             side_errors) + " point(s) deduction.<br>"
                         }
            if c.err:
                flash(c.err)
            if side_errors != 0:
                test_pep8['pass'] = False
            score_info['score'] += max(0, int(14) - side_errors)
            tests.append(test_pep8)

            # Check for help comment
            cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
            c = delegator.run(cmd)
            help_comments = int(c.out)
            test_help = {"name": "Testing that you got a help and documented it as a comment (5 points)",
                         "pass": True,
                         "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                                         "Be sure your comment is meaningful, otherwise this can be "
                                         "overturned on review.",
                         "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                                         " how somebody helped you with your code.  <br>"
                                         "If you didn't have any problems, then ask somebody to check that your code"
                                         " gives correct outputs, given an input.<br>"
                                         "This translates to -5 points deduction.<br>",
                         }
            if help_comments == 0:
                test_help['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_help)

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_2020')
def feedback_2020():
    import re
    import subprocess
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 55, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2018', filename)
    find_lab = re.search('2.020', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2018_luismartinez_1.06.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2018_luismartinez_2.020.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)

        # Check that input1 is good (input / 2)
        filename_output = filename + '.out'
        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.020-1.in > ' + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check input1')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"49.5", outfile_data, re.X | re.M | re.S)
        test_output_1 = {"name": "Testing that the number divides by 2 correctly and prints it out (15 points)",
                         "pass": True,
                         "pass_message": "Pass!  The number divides by 2 correctly and prints it out.",
                         "fail_message": "Fail.  Check that the number divides by 2 correctly and prints it out.<br>"
                                         "For example, if you input 5, it should output 2.5.<br>"
                                         "<br> ",
                         }
        if search_object:
            score_info['score'] += 15
        else:
            test_output_1['pass'] = False
        tests.append(test_output_1)

        # Check input2 is good (int(input / 2))
        search_object = re.search(r"49", outfile_data, re.X | re.M | re.S)
        test_output_2 = {"name": "Testing that the number divides by 2 correctly and prints it out INTEGER (15 points)",
                         "pass": True,
                         "pass_message": "Pass!  The number divides by 2 correctly and prints it out.",
                         "fail_message": "Fail.  Check that first 5 inputs show up in the output printout.<br>"
                                         "Check that the number divides by 2 correctly and prints it out INTEGER.<br>"
                                         "For example, if you input 5, it should output 2 <br>"
                                         " Other tests not run. They will be run after filename is fixed.<br>"
                                         "<br> ",
                         }
        if not search_object:
            test_output_2['pass'] = False
            tests.append(test_output_2)
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            tests.append(test_output_2)
            score_info['score'] += 15

            # check input3 is good (input / 2) AND (int(input/2)) for 3.5 number
            filename_output = filename + '.out'
            cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.020-2.in > ' \
                  + filename_output
            c = delegator.run(cmd)
            if c.err:
                flash('bad! You have an error somewhere in running program check input2')
            with open(filename_output, 'r') as myfile:
                outfile_data = myfile.read()

            search_object1 = re.search(r"49.75", outfile_data, re.X | re.M | re.S)
            search_object2 = re.search(r"49", outfile_data, re.X | re.M | re.S)

            test_output_3 = {"name": "Testing that it works for float numbers (6 points)",
                             "pass": True,
                             "pass_message": "Pass!  It works for float numbers",
                             "fail_message": "Fail.  Check that it works for float numbers.<br>"
                                             "For example, if you typed in 3.5, it should output 1.75 and 1"
                                             "<br> ",
                             }
            if search_object1 and search_object2:
                score_info['score'] += 6
            else:
                test_output_2['pass'] = False
            tests.append(test_output_3)

            # Find number of PEP8 errors
            cmd = 'pycodestyle ' + filename + ' | wc -l  '
            c = delegator.run(cmd)
            side_errors = int(c.out)
            test_pep8 = {"name": "Testing for PEP8 warnings and errors (14 points)",
                         "pass": True,
                         "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                         "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                                                                          "This translates to -" + str(
                             side_errors) + " point(s) deduction.<br>"
                         }
            if side_errors != 0:
                test_pep8['pass'] = False
            score_info['score'] += max(0, int(14) - side_errors)
            tests.append(test_pep8)

            # Check for help comment
            cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
            c = delegator.run(cmd)
            help_comments = int(c.out)
            test_help = {"name": "Testing that you got a help and documented it as a comment (5 points)",
                         "pass": True,
                         "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                                         "Be sure your comment is meaningful, otherwise this can be "
                                         "overturned on review.",
                         "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                                         " how somebody helped you with your code.  <br>"
                                         "If you didn't have any problems, then ask somebody to check that your code"
                                         " gives correct outputs, given an input.<br>"
                                         "This translates to -5 points deduction.<br>",
                         }
            if help_comments == 0:
                test_help['pass'] = False
            else:
                score_info['score'] += 5
            tests.append(test_help)

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_2032a')
def feedback_2032a():
    import re
    import subprocess
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 22.5, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2018', filename)
    find_lab = re.search('2.032a', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2018_luismartinez_2.032a.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2018_luismartinez_2.032a.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)

        # Check for ifs
        cmd = 'grep "if" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        ifs = int(c.out)

        test_ifs = {"name": "Checking for zero if statements (5 points)",
                    "pass": True,
                    "pass_message": "Pass!  Zero if statements",
                    "fail_message": "Fail.  Code should not have any if statements.<br>"
                                    "For example, print(1==1) NOT if (1 == 1): print('True') <br>"
                                    "Review instructions or ask teacher for more details<br> ",
                    }
        if ifs == 0:
            score_info['score'] += 5
        else:
            test_ifs['pass'] = False
        tests.append(test_ifs)

        # test all 8 cases
        filename_output = filename + '.out'
        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032a-1.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-1')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()
        eight_cases_score = 0

        search_object = re.search(r"False", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032a-2.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-2')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"False", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032a-3.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-3')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"True", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032a-4.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-4')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"False", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032a-5.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-5')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"False", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032a-6.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-6')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"False", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032a-7.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-7')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"False", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032a-8.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-8')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"False", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        test_eight_tests = {"name": "Testing that all 8 test cases work (8 points)",
                            "pass": True,
                            "pass_message": "Pass!  All 8 test cases work",
                            "fail_message": "Fail.  Check your 8 test cases.<br>"
                                            "Please review the table that is after the 2.032a program run "
                                            "in your assignment <br> "
                                            "As part of this assignment, you should have populated that table.<br>"
                                            "You should test your code with the data from this table.<br>"
                                            "You need to figure out which ones, we do not tell you",
                            }

        if eight_cases_score != 8:
            test_eight_tests['pass'] = False
        if c.err:
            test_eight_tests['pass'] = False
            eight_cases_score = 0 
        score_info['score'] += eight_cases_score
        tests.append(test_eight_tests)

        # Find number of PEP8 errors
        cmd = 'pycodestyle ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        side_errors = int(c.out)
        test_pep8 = {"name": "Testing for PEP8 warnings and errors (7 points)",
                     "pass": True,
                     "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                     "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                                                                      "This translates to -" + str(
                         side_errors) + " point(s) deduction.<br>"
                     }
        if side_errors != 0:
            test_pep8['pass'] = False
        score_info['score'] += max(0, int(7) - side_errors)
        tests.append(test_pep8)

        # Check for help comment
        cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
        c = delegator.run(cmd)
        help_comments = int(c.out)
        test_help = {"name": "Testing that you got a help and documented it as a comment (2.5 points)",
                     "pass": True,
                     "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                                     "Be sure your comment is meaningful, otherwise this can be "
                                     "overturned on review.",
                     "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                                     " how somebody helped you with your code.  <br>"
                                     "If you didn't have any problems, then ask somebody to check that your code"
                                     " gives correct outputs, given an input.<br>"
                                     "This translates to -5 points deduction.<br>",
                     }
        if help_comments == 0:
            test_help['pass'] = False
        else:
            score_info['score'] += 2.5
        tests.append(test_help)

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_2032b')
def feedback_2032b():
    import re
    import subprocess
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 22.5, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2018', filename)
    find_lab = re.search('2.032b', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2018_luismartinez_2.032b.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2018_luismartinez_2.032b.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)

        # Check for ifs
        cmd = 'grep "if" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        ifs = int(c.out)

        test_ifs = {"name": "Checking for zero if statements (5 points)",
                    "pass": True,
                    "pass_message": "Pass!  Zero if statements",
                    "fail_message": "Fail.  Code should not have any if statements.<br>"
                                    "For example, print(1==1) NOT if (1 == 1): print('True') <br>"
                                    "Review instructions or ask teacher for more details<br> ",
                    }
        if ifs == 0:
            score_info['score'] += 5
        else:
            test_ifs['pass'] = False
        tests.append(test_ifs)

        # test all 8 cases
        filename_output = filename + '.out'
        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032b-1.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-1')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()
        eight_cases_score = 0

        search_object = re.search(r"True", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032b-2.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-2')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"False", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032b-3.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-3')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"True", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032b-4.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-4')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"False", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032b-5.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-5')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"True", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032b-6.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-6')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"False", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032b-7.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-7')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"False", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/2.032b-8.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running program check 2.032-8')
        with open(filename_output, 'r') as myfile:
            outfile_data = myfile.read()

        search_object = re.search(r"False", outfile_data, re.X | re.M | re.S)
        if search_object:
            eight_cases_score += 1

        test_eight_tests = {"name": "Testing that all 8 test cases work (8 points)",
                            "pass": True,
                            "pass_message": "Pass!  All 8 test cases work",
                            "fail_message": "Fail.  Check your 8 test cases.<br>"
                                            "Please review the table that is after the 2.032b program run "
                                            "in your assignment <br> "
                                            "As part of this assignment, you should have populated that table.<br>"
                                            "You should test your code with the data from this table.<br>"
                                            "You need to figure out which ones, we do not tell you",
                            }

        if eight_cases_score != 8:
            test_eight_tests['pass'] = False
        if c.err:
            test_eight_tests['pass'] = False
            eight_cases_score = 0 

        score_info['score'] += eight_cases_score
        tests.append(test_eight_tests)

        # Find number of PEP8 errors
        cmd = 'pycodestyle ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        side_errors = int(c.out)
        test_pep8 = {"name": "Testing for PEP8 warnings and errors (7 points)",
                     "pass": True,
                     "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                     "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                                                                      "This translates to -" + str(
                         side_errors) + " point(s) deduction.<br>"
                     }
        if side_errors != 0:
            test_pep8['pass'] = False
        score_info['score'] += max(0, int(7) - side_errors)
        tests.append(test_pep8)

        # Check for help comment
        cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
        c = delegator.run(cmd)
        help_comments = int(c.out)
        test_help = {"name": "Testing that you got a help and documented it as a comment (2.5 points)",
                     "pass": True,
                     "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                                     "Be sure your comment is meaningful, otherwise this can be "
                                     "overturned on review.",
                     "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                                     " how somebody helped you with your code.  <br>"
                                     "If you didn't have any problems, then ask somebody to check that your code"
                                     " gives correct outputs, given an input.<br>"
                                     "This translates to -5 points deduction.<br>",
                     }
        if help_comments == 0:
            test_help['pass'] = False
        else:
            score_info['score'] += 2.5
        tests.append(test_help)

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_2040')
def feedback_2040():
    import re
    import subprocess
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 46, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2018', filename)
    find_lab = re.search('2.040', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2018_luismartinez_2.032b.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2018_luismartinez_2.040.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)

        # Check for equals, aka variable assignment
        cmd = 'grep "=" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        equals = int(c.out)

        test_variables = {"name": "Checking for variables, need > 4 (5 points)",
                          "pass": True,
                          "pass_message": "Pass!  At least 4 equals signs assigning variables",
                          "fail_message": "Fail.  Code should assign at least 4 prizes.<br>"
                                          "For example, prize1 = 'brand new car' prize2 =..etc.. <br>"
                                          "Review instructions or ask teacher for more details<br> ",
                          }
        if equals > 4:
            score_info['score'] += 5
        else:
            test_variables['pass'] = False
        tests.append(test_variables)

        # test input
        cmd = 'grep "input" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        inputs = int(c.out)

        test_inputs = {"name": "Checking for asking use question (5 points)",
                       "pass": True,
                       "pass_message": "Pass!  At least 4 equals signs assigning variables",
                       "fail_message": "Fail. Code should ask user for a door to choose.<br>"
                       }
        if inputs >= 1:
            score_info['score'] += 5
        else:
            test_inputs['pass'] = False
        tests.append(test_inputs)

        # test if
        cmd = 'grep "if" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        ifs = int(c.out)

        test_ifs = {"name": "Checking for at least one if(5 points)",
                    "pass": True,
                    "pass_message": "Pass!  At least 1 if in code",
                    "fail_message": "Fail. Code should use an if to help decide what to print <br>"
                                    " depending on what door was chosen"
                    }
        if ifs >= 1:
            score_info['score'] += 5
        else:
            test_ifs['pass'] = False
        tests.append(test_ifs)

        # test else
        cmd = 'grep "^else" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        elses = int(c.out)

        test_elses = {"name": "Checking for at least one else at beginning of line(5 points)",
                      "pass": True,
                      "pass_message": "Pass!  At least one else in code at beginning of line",
                      "fail_message": "Fail. Code should use an else in case user doesn't pick door 1-4"
                      }
        if elses >= 1:
            score_info['score'] += 6
        else:
            test_elses['pass'] = False
        tests.append(test_elses)

        # test elif
        cmd = 'grep "elif" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        elifs = int(c.out)

        test_elifs = {"name": "Checking for at least 3 elifs (6 points)",
                      "pass": True,
                      "pass_message": "Pass!  At least 3 elifs in code",
                      "fail_message": "Fail. Review the presentation for why we use elif vs if.  This question will be "
                                      "on <br> your lab understanding Google form for sure."
                      }
        if elifs >= 3:
            score_info['score'] += 6
        else:
            test_elifs['pass'] = False
        tests.append(test_elifs)

        # Find number of PEP8 errors
        cmd = 'pycodestyle ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        side_errors = int(c.out)
        test_pep8 = {"name": "Testing for PEP8 warnings and errors (7 points)",
                     "pass": True,
                     "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                     "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                                                                      "This translates to -" + str(
                         side_errors) + " point(s) deduction.<br>"
                     }
        if side_errors != 0:
            test_pep8['pass'] = False
        score_info['score'] += max(0, int(14) - side_errors)
        tests.append(test_pep8)

        # Check for help comment
        cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
        c = delegator.run(cmd)
        help_comments = int(c.out)
        test_help = {"name": "Testing that you got a help and documented it as a comment (2.5 points)",
                     "pass": True,
                     "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                                     "Be sure your comment is meaningful, otherwise this can be "
                                     "overturned on review.",
                     "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                                     " how somebody helped you with your code.  <br>"
                                     "If you didn't have any problems, then ask somebody to check that your code"
                                     " gives correct outputs, given an input.<br>"
                                     "This translates to -5 points deduction.<br>",
                     }
        if help_comments == 0:
            test_help['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_help)

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)



@app.route('/feedback_2050a')
def feedback_2050a():
    import re
    import subprocess
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 15.5, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2018', filename)
    find_lab = re.search('2.050a', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2018_luismartinez_2.050a.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2018_luismartinez_2.050a.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)

        # test for a list
        with open(filename, 'r') as myfile:
            filename_data = myfile.read()

        search_object = re.search(r".+ = .* \[ .* \]", outfile_data, re.X | re.M | re.S)

        test_list = {"name": "Testing that there is something looking like a list",
                     "pass": True,
                     "pass_message": "Pass! Submitted file looks like it has a list",
                     "fail_message": "Submitted file does not look like it has a list.",
                     }

        if not search_object:
            test_list['pass'] = False
        else:
            score_info['score'] += 3
        tests.append(test_list)


        # Check for uinput 
        cmd = 'grep "input" ' + filename + ' | grep help | wc -l  '
        c = delegator.run(cmd)
        inputs = int(c.out)
        test_input = {"name": "Testing that you got a help and documented it as a comment (2.5 points)",
                     "pass": True,
                     "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                                     "Be sure your comment is meaningful, otherwise this can be "
                                     "overturned on review.",
                     "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                                     " how somebody helped you with your code.  <br>"
                                     "If you didn't have any problems, then ask somebody to check that your code"
                                     " gives correct outputs, given an input.<br>"
                                     "This translates to -5 points deduction.<br>",
                     }
        if inputs == 0:
            test_help['pass'] = False
        else:
            score_info['score'] += 3
        tests.append(test_input)

        # Find number of PEP8 errors
        cmd = 'pycodestyle ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        side_errors = int(c.out)
        test_pep8 = {"name": "Testing for PEP8 warnings and errors (7 points)",
                     "pass": True,
                     "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                     "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                                                                      "This translates to -" + str(
                         side_errors) + " point(s) deduction.<br>"
                     }
        if side_errors != 0:
            test_pep8['pass'] = False
        score_info['score'] += max(0, int(7) - side_errors)
        tests.append(test_pep8)

        flash(score_info['score'])

        # Check for help comment
        cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
        c = delegator.run(cmd)
        help_comments = int(c.out)
        test_help = {"name": "Testing that you got a help and documented it as a comment (2.5 points)",
                     "pass": True,
                     "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                                     "Be sure your comment is meaningful, otherwise this can be "
                                     "overturned on review.",
                     "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                                     " how somebody helped you with your code.  <br>"
                                     "If you didn't have any problems, then ask somebody to check that your code"
                                     " gives correct outputs, given an input.<br>"
                                     "This translates to -5 points deduction.<br>",
                     }
        if help_comments == 0:
            test_help['pass'] = False
        else:
            score_info['score'] += 2.5
        tests.append(test_help)

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_2050b')
def feedback_2050b():
    import re
    import subprocess
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 14.5, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2018', filename)
    find_lab = re.search('2.050a', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2018_luismartinez_2.050a.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2018_luismartinez_2.050a.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)

        # test for a 2 lists
        with open(filename, 'r') as myfile:
            filename_data = myfile.read()

        search_object = re.search(r".+ = .* \[ .* \] (.|\n)*  .+ = .* \[ .* \]  ", outfile_data, re.X | re.M | re.S)

        test_twolist = {"name": "Testing that there is something looking like a 2 lists",
                        "pass": True,
                        "pass_message": "Pass! Submitted file looks like it has 2 lists",
                        "fail_message": "Submitted file does not look like it has 2 lists.",
        }

        if not search_object:
            test_twolist['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_twolist)

        # Find number of PEP8 errors
        cmd = 'pycodestyle ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        side_errors = int(c.out)
        test_pep8 = {"name": "Testing for PEP8 warnings and errors (7 points)",
                     "pass": True,
                     "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                     "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                                                                      "This translates to -" + str(
                         side_errors) + " point(s) deduction.<br>"
                     }
        if side_errors != 0:
            test_pep8['pass'] = False
        score_info['score'] += max(0, int(7) - side_errors)
        tests.append(test_pep8)

        flash(score_info['score'])

        # Check for help comment
        cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
        c = delegator.run(cmd)
        help_comments = int(c.out)
        test_help = {"name": "Testing that you got a help and documented it as a comment (2.5 points)",
                     "pass": True,
                     "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                                     "Be sure your comment is meaningful, otherwise this can be "
                                     "overturned on review.",
                     "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                                     " how somebody helped you with your code.  <br>"
                                     "If you didn't have any problems, then ask somebody to check that your code"
                                     " gives correct outputs, given an input.<br>"
                                     "This translates to -5 points deduction.<br>",
                     }
        if help_comments == 0:
            test_help['pass'] = False
        else:
            score_info['score'] += 2.5
        tests.append(test_help)

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


    
@app.route('/feedback_3011')
def feedback_3011():
    import re
    import subprocess
    import delegator

    # have same feedback for all
    # different template
    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 49, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    find_year = re.search('2018', filename)
    find_lab = re.search('3.011', filename)
    test_filename = {"name": "Testing that file is named correctly",
                     "pass": True,
                     "pass_message": "Pass! File name looks correct (i.e. something like 2018_luismartinez_3.011.py)",
                     "fail_message": "File name of submitted file does not follow required convention. "
                                     " Rename and resubmit.<br>"
                                     "File name should be like this: <br> <br>"
                                     "2018_luismartinez_3.011.py <br><br>"
                                     "File must be python file (ends in .py), not a Google doc with Python code"
                                     " copy+pasted in. <br>"
                                     " Other tests not run. They will be run after filename is fixed.<br>"
                     }

    if find_year and find_lab:
        test_filename['pass'] = True
        tests.append(test_filename)

        # test for a list
        with open(filename, 'r') as myfile:
            filename_data = myfile.read()

        search_object = re.search(r".+ = .* \[ .* \]", outfile_data, re.X | re.M | re.S)

        test_list = {"name": "Testing that there is something looking like a list",
                     "pass": True,
                     "pass_message": "Pass! Submitted file looks like it has a list",
                     "fail_message": "Submitted file does not look like it has a list.",
                     }

        if not search_object:
            test_list['pass'] = False
        else:
            score_info['score'] += 10
        tests.append(test_list)

        # test for 4+ items list
        search_object = re.search(r".+ = .* \[ .* , .* , .* , .* \]", outfile_data, re.X | re.M | re.S)

        test_four_item_list = {"name": "Testing that there is something looking like a 4+ items in list",
                               "pass": True,
                               "pass_message": "Pass! Submitted file looks like it has 4+ items in list",
                               "fail_message": "Submitted file does not look like it has 4+ items in list.",
        }

        if not search_object:
            test_four_item_list['pass'] = False
        else:
            score_info['score'] += 10
        tests.append(test_four_item_list)

        # Check for any print
        cmd = 'grep "print" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        prints = int(c.out)
        test_print = {"name": "Testing for a print of any type (5 points)",
                     "pass": True,
                     "pass_message": "Pass (for now).  You have a print statment.  <br>",
                     "fail_message": "Fail.  You do not have a print of any sort <br>",
                     }
        if help_comments == 0:
            test_print['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_print)

        # Check for any input
        cmd = 'grep "input" ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        inputs = int(c.out)
        test_input = {"name": "Testing for an input of any type (5 points)",
                     "pass": True,
                     "pass_message": "Pass (for now).  You have an input statment.  <br>",
                     "fail_message": "Fail.  You do not have an input of any sort <br>",
                     }
        if help_comments == 0:
            test_input['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_input)
        
        # Find number of PEP8 errors
        cmd = 'pycodestyle ' + filename + ' | wc -l  '
        c = delegator.run(cmd)
        side_errors = int(c.out)
        test_pep8 = {"name": "Testing for PEP8 warnings and errors (7 points)",
                     "pass": True,
                     "pass_message": "Pass! Zero PEP8 warnings or errors, congrats!",
                     "fail_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>"
                                                                      "This translates to -" + str(
                         side_errors) + " point(s) deduction.<br>"
                     }
        if side_errors != 0:
            test_pep8['pass'] = False
        score_info['score'] += max(0, int(14) - side_errors)
        tests.append(test_pep8)

        flash(score_info['score'])

        # Check for help comment
        cmd = 'grep "#" ' + filename + ' | grep help | wc -l  '
        c = delegator.run(cmd)
        help_comments = int(c.out)
        test_help = {"name": "Testing that you got a help and documented it as a comment (2.5 points)",
                     "pass": True,
                     "pass_message": "Pass (for now).  You have a comment with 'help' in it.  <br>"
                                     "Be sure your comment is meaningful, otherwise this can be "
                                     "overturned on review.",
                     "fail_message": "Fail.  Did not find a comment in your code with the word 'help' describing"
                                     " how somebody helped you with your code.  <br>"
                                     "If you didn't have any problems, then ask somebody to check that your code"
                                     " gives correct outputs, given an input.<br>"
                                     "This translates to -5 points deduction.<br>",
                     }
        if help_comments == 0:
            test_help['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_help)

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_filename['pass'] = False
        tests.append(test_filename)
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)

