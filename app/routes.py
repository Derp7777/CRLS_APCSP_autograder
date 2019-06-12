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
            elif request.form['lab'] == '2.051a':
                return redirect(url_for('feedback_2051a', filename=filename))
            elif request.form['lab'] == '2.051b':
                return redirect(url_for('feedback_2051b', filename=filename))
            elif request.form['lab'] == '3.011':
                return redirect(url_for('feedback_3011', filename=filename))
            elif request.form['lab'] == '3.020':
                return redirect(url_for('feedback_3020', filename=filename))
            elif request.form['lab'] == '3.026':
                return redirect(url_for('feedback_3026', filename=filename))
            elif request.form['lab'] == '4.011':
                return redirect(url_for('feedback_4011', filename=filename))
            elif request.form['lab'] == '4.021':
                return redirect(url_for('feedback_4021', filename=filename))
            elif request.form['lab'] == '4.022':
                return redirect(url_for('feedback_4022', filename=filename))
            elif request.form['lab'] == '4.025':
                return redirect(url_for('feedback_4025', filename=filename))
            elif request.form['lab'] == '4.031':
                return redirect(url_for('feedback_4031', filename=filename))
            elif request.form['lab'] == '4.036':
                return redirect(url_for('feedback_4036', filename=filename))
            elif request.form['lab'] == '6.011':
                return redirect(url_for('feedback_6011', filename=filename))
            elif request.form['lab'] == '6.021':
                return redirect(url_for('feedback_6021', filename=filename))
            elif request.form['lab'] == '6.031':
                return redirect(url_for('feedback_6031', filename=filename))
            elif request.form['lab'] == '6.041':
                return redirect(url_for('feedback_6041', filename=filename))
            elif request.form['lab'] == '7.021':
                return redirect(url_for('feedback_7021', filename=filename))
            elif request.form['lab'] == '7.031':
                return redirect(url_for('feedback_7031', filename=filename))
            elif request.form['lab'] == '7.034':
                return redirect(url_for('feedback_7034', filename=filename))
    form = UploadForm()
    user = {'username': 'CRLS Scholar!!!'}
    return render_template('index.html', title='Home', user=user, form=form)


@app.route('/feedback_1040')
def feedback_1040():

    from app.python_labs.filename_test import filename_test
    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.find_items import find_questions
    from app.python_labs.io_test import io_test
    from app.python_labs.python_1_040 import statement_variables
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 34.5, 'manually_scored': 5.5, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '1.040')
    tests.append(test_filename)

    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # Check that there are 3 input questions
        test_find_three_questions = find_questions(filename_data, 3, 5)
        test_find_three_questions['name'] += " Checking that Genie asks at least 3 questions. <br> " + \
                                             " Autograder will not continue if this test fails. <br>"
        tests.append(test_find_three_questions)
        if not test_find_three_questions['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # io test 1- a b c
            test_io_1 = io_test(filename, r'.+ a1 .+ a2 .+ a3 ', 1, points=5)
            test_io_1['name'] += "Check things are in correct order - wishing for a, b, c " +\
                                 " should print 'your wishes are a, b, and c.' <br>" \
                                 "You must have at least 1 character of some sort between your wishes.<br>"
            tests.append(test_io_1)

            # Check that there are 6 total questions (3 part 1, 3 part 2)
            test_find_six_questions = find_questions(filename_data, 6, 5)
            test_find_six_questions['name'] += " Checking that Genie asks at least 6 questions (you need 3 for" \
                                               " part 1 and 3 for part 2). <br>"
            tests.append(test_find_six_questions)

            # Check that repeated questions put into variables.
            test_input_variable = statement_variables(filename_data, 5)
            tests.append(test_input_variable)

            # io test 2 - a b c, b2, b3, b1
            test_io_2 = io_test(filename, r'.+ a1 .+ a2 .+ a3 .+ b2 .+ b3 .+ b1 ', 1, points=5)
            test_io_2['name'] += "Check things are in correct order - wishing for a, b, c, d, e, f " + \
                                 " should print 'your wishes are a, b, and c' <br>" +\
                                 " and 'your wishes are e, f, and d' <br>" \
                                 "You must have at least 1 character of some sort between your wishes.<br>"
            tests.append(test_io_2)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 7)
            tests.append(test_pep8)
            test_help = helps(filename, 2.5)
            tests.append(test_help)

            score_info['finished_scoring'] = True
            for test in tests:
                if test['pass']:
                    print(test['pass_message'])
                    score_info['score'] += test['points']
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_1060')
def feedback_1060():

    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.find_items import find_questions, find_string
    from app.python_labs.io_test import io_test_find_all, io_test
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'manually_scored': 11, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '1.060')
    tests.append(test_filename)

    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # Check that there are 5 input questions
        test_find_five_questions = find_questions(filename_data, 5, 5)
        test_find_five_questions['name'] += " Checking for at least 5 questions. <br> " + \
                                            " Autograder will not continue if this test fails. <br>"
        tests.append(test_find_five_questions)
        if not test_find_five_questions['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:

            # Check that inputs are named after part of speech
            test_find_parts_of_speech = find_string(filename_data,
                                                    r'(verb|noun|adjective|adverb|preposition|place) _* [0-9]* \s* = '
                                                    r'\s* input\(',
                                                    5, points=5)
            test_find_parts_of_speech['name'] += "Testing that variables are named after parts of speech. <br>"\
                                                 "If this test fails, rename variables to parts of speech " \
                                                 "per instructions.<br>" \
                                                 "Also note, Python variable name convention is LOWERCASE, so this " \
                                                 "test will flunk variables like 'Noun1' or 'Verb2'<br>"
            tests.append(test_find_parts_of_speech)

            # Check for at least 1 print statement
            test_find_print = find_string(filename_data, r'print \s* \(', 1, points=5)
            test_find_print['name'] += "Testing for at least one print statement. <br>"
            tests.append(test_find_print)

            # Check for less than 3 print statements
            test_find_three_print = find_string(filename_data, r'print \s \(', 3, points=5, minmax='max')
            test_find_three_print['name'] += "Testing for at maximum of three print statements. <br>"
            tests.append(test_find_three_print)

            # answer 5 questions, they should all show up in printout
            test_io_five_inputs = io_test_find_all(filename, [r'a1', r'a2', r'a3', r'b1', r'b2'], 1, points=15)
            test_io_five_inputs['name'] += 'Testing for first 5 things you answered questions to show in output.<br>' \
                                           'For example, if you typed in noun1, verb1, noun2, verb2, and adjective' \
                                           '<br> noun1, verb1, noun2, verb2, and adjective should all appear ' \
                                           'in the printout. <br>'
            tests.append(test_io_five_inputs)

            # Check for 3 punctuations
            test_puncts = io_test(filename, r'(\? | ! | \.) ', 1, points=5, occurrences=3)
            test_puncts['name'] += "Testing for at least 3 punctuations.<br>"
            tests.append(test_puncts)

            # Test second 4 inputs for correct spacing
            test_io_spacing = io_test_find_all(filename, [r'(\^ | \s+ ) a2 (\s+ | \? | \. | , | !)',
                                                          r'(\^ | \s+ ) a3 (\s+ | \? | \. | , | !)',
                                                          r'(\^ | \s+ ) b1 (\s+ | \? | \. | , | !)',
                                                          r'(\^ | \s+ ) b2 (\s+ | \? | \. | , | !)'],
                                               1, points=10)
            test_io_spacing['name'] += 'Testing for spacing.  Things you enter should have spaces or punctuations<br>' \
                                       'after them and spaces before them in the printout. <br>'
            tests.append(test_io_spacing)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 14)
            tests.append(test_pep8)
            test_help = helps(filename, 5)
            tests.append(test_help)

            score_info['finished_scoring'] = True
            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']

            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_2020')
def feedback_2020():

    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.io_test import io_test, io_test_find_all
    from app.python_labs.find_items import find_questions, find_string
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 55, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '2.020')
    tests.append(test_filename)

    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # Check that there is 1 input questions
        test_find_question = find_questions(filename_data, 1, 5)
        test_find_question['name'] += " Checking for at least 1 question. <br> " + \
                                      " Autograder will not continue if this test fails. <br>"
        tests.append(test_find_question)
        if not test_find_question['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # Test for casting of any sort
            test_find_casting = find_string(filename_data, r'( int\( | float\( )', 1, points=5)
            test_find_casting['name'] += 'Checking that there is some casting of any sort to either integer or float.'
            tests.append(test_find_casting)

            # Test for casting of initial value to float.  Will crash with unknown errors later if casted to int.
            test_find_casting_2 = find_string(filename_data, r'float\( ', 1)
            test_find_casting_2['name'] += 'Test your program by manually running it and typing in 55.5 for your ' \
                                           'number. <br> If you  get an error<br>' \
                                           'ValueError: invalid literal for int() with base 10:<br>' \
                                           'This error means you are trying to convert a string that looks like' \
                                           ' a float into an integer.  ' \
                                           '<br> If you really want an integer you have to cast the string' \
                                           ' to a float first. <br> Or else if you are OK with float, cast to float ' \
                                           'instead of integer.<br> '
            tests.append(test_find_casting_2)
            if not test_find_casting_2['pass']:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:
                # Check that input1 is good (input / 2) 99 / 2 = 49.5
                test_io_1 = io_test(filename, '49.5', 1, points=10)
                test_io_1['name'] += "Checks that the number divides by 2 and prints out.  Input 99, " \
                                     "expected 49.5 and 49 in output. <br>"
                tests.append(test_io_1)

                # Check input2 is good (int(input / 2))
                test_io_2 = io_test(filename, '49$', 1, points=10)
                test_io_2['name'] += "Checks that the number divides by 2 and prints out the INTEGER only answer. " \
                                     " Input 99, expected 49 in output. <br>"
                tests.append(test_io_2)

                # Check input2 is good (int(input / 2))
                test_io_3 = io_test_find_all(filename, ['49.75', '49$'], 2, points=6)
                test_io_3['name'] += "Checks that the program works for non-whole inputs. " \
                                     " Input 99.5, expected 49.75 and 49 in output. <br>"
                tests.append(test_io_3)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 14)
                tests.append(test_pep8)
                test_help = helps(filename, 5)
                tests.append(test_help)

                score_info['finished_scoring'] = True
                for test in tests:
                    if test['pass']:
                        score_info['score'] += test['points']

                score_info['finished_scoring'] = True
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)


@app.route('/feedback_2032a')
def feedback_2032a():

    from app.python_labs.filename_test import filename_test
    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.find_items import find_if
    from app.python_labs.python_2_03x import python_2_032a
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 26.5, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '2.032a')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # Check for ifs
        test_ifs = find_if(filename_data, 0, 5, minmax='max')
        test_ifs['name'] += 'Testing for ifs.  There should be zero ifs in the code. <br>' \
                            'For example, print(1==1) NOT if (1 == 1): print("True") <br>' \
                            ''
        tests.append(test_ifs)

        if not test_ifs['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:

            debug_statement = 'Program asks for DC/Marvel, age, and power in that order. <br>' \
                              'DC must be capitalized.<br>'
            test_runs = python_2_032a(filename, filename_data, debug_statement=debug_statement)
            tests.append(test_runs)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 7)
            tests.append(test_pep8)
            test_help = helps(filename, 2.5)
            tests.append(test_help)

            score_info['finished_scoring'] = True
            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']

            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_2032b')
def feedback_2032b():

    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_if
    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.python_2_03x import python_2_032b
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 26.5, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '2.032b')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # Check for ifs
        test_ifs = find_if(filename_data, 0, 5, minmax='max')
        test_ifs['name'] += 'Testing for ifs.  There should be zero ifs in the code. <br>' \
                            'For example, print(1==1) NOT if (1 == 1): print("True") <br>' \
                            'If you think this should pass, control-F and search for "if" in your code'
        tests.append(test_ifs)

        # test all 8 cases
        debug_statement = 'Program asks for if you are Yuka Kinoshita, your stomach size, and money in that order <br>'\
                          'If you are failing 2 tests, read example 8 from the presentation.'
        test_runs = python_2_032b(filename, filename_data, debug_statement=debug_statement)
        tests.append(test_runs)

        # Find number of PEP8 errors and helps
        test_pep8 = pep8(filename, 7)
        tests.append(test_pep8)
        test_help = helps(filename, 2.5)
        tests.append(test_help)

        for test in tests:
            if test['pass']:
                score_info['score'] += test['points']

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_2040')
def feedback_2040():

    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.find_items import find_all_strings, find_questions, find_if, find_elif, find_else
    from app.python_labs.python_2_040 import python_2_040
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 61, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '2.040')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # Test for prize variables
        test_prizes = find_all_strings(filename_data, [r'prize1 \s* = \s* (\'|\")[a-zA-Z0-9!-\.\s]+',
                                                       r'prize2 \s* = \s* (\'|\")[a-zA-Z0-9!-\.\s]+',
                                                       r'prize3 \s* = \s* (\'|\")[a-zA-Z0-9!-\.\s]+',
                                                       r'prize4 \s* = \s* (\'|\")[a-zA-Z0-9!-\.\s]+', ], 6)
        test_prizes['name'] += "Testing for 4 variables names prize1, prize2, prize3, prize4 (not prize_1, prize_2..." \
                               " <br>"
        tests.append(test_prizes)
        if not test_prizes['pass']:
            test_prizes['fail_message'] += 'Be sure you have 4 variables called  prize1, prize2, prize3, prize4. <br>' \
                                           'Be sure to set their values to be prizes'
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            test_question = find_questions(filename_data, 1, 6)
            tests.append(test_question)
            if not test_question['pass']:
                test_question['fail_message'] += "You need to ask the user a question about which door to pick. <br>"
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:
                # test if, check for at least 1 if statement
                test_ifs = find_if(filename_data, 1, 6)
                tests.append(test_ifs)

                # test else check for at least 1 else statement
                test_else = find_else(filename_data, 1, 6)
                tests.append(test_else)

                # look for 3 elifs
                test_elif = find_elif(filename_data, 3, 6)
                tests.append(test_elif)

                test_correct_prizes = python_2_040(filename, filename_data)
                if not test_correct_prizes['pass']:
                    test_correct_prizes['fail_message'] += test_correct_prizes['debug']
                tests.append(test_correct_prizes)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 14)
                tests.append(test_pep8)
                test_help = helps(filename, 5)
                tests.append(test_help)

                for test in tests:
                    if test['pass']:
                        score_info['score'] += test['points']
                score_info['finished_scoring'] = True
                return render_template('feedback.html', user=user, tests=tests,
                                       filename=filename, score_info=score_info)


@app.route('/feedback_2051a')
def feedback_2051a():

    from app.python_labs.find_items import find_string, find_questions, find_all_strings
    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.python_2_05x import python_2_051a
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 32.5, 'manually_scored': 11, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '2.050a')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # test for a list being created with 4 items
        test_prizes = find_string(filename_data, r'prizes \s* = \s* \[ .+ , .+ , .+ , .+ \]', 1, points=5)
        test_prizes['name'] += "Testing that there is a variable prizes.  Prizes is a list with exactly 4 items.<br>" \
                               "Prizes is a named exactly 'prizes' and not something else."
        tests.append(test_prizes)
        if not test_prizes['pass']:
            test_prizes['fail_message'] += r"Looking for variable prizes that is a list with 4 items.  We name lists " \
                                           r"plural to help keep track of what is what.<br>  " \
                                           r"Looked for 'prizes \s* = \s* \[ .+ , .+ , .+ , .+ \]' " \
                                           r"in this string: <br>" + filename_data
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:

            # Check for question
            test_find_input = find_questions(filename_data, 1, 5)
            tests.append(test_find_input)

            # Test input gives output
            test_runs = python_2_051a(filename, filename_data)
            tests.append(test_runs)

            # Test efficiency
            test_efficiency = find_all_strings(filename_data, [r'prizes\[0\]', r'prizes\[1\]',
                                                               r'prizes\[2\]', r'prizes\[3\]'], 5)
            test_efficiency['name'] += "Testing efficiency.  Do NOT want to have a big if/elif/else.<br>" \
                                       "If you have a variable x which is a number of item in list," \
                                       " list[x-1] will get you the correct item.<br>" \
                                       "<br>  This technique saves a lot of lines of code over a big if/elif  " \
                                       "and scales to big numbers.  " \
                                       "<br>That is, a list with 10,000 items will need " \
                                       "just one line to print out the list item whereas with a big if/else, " \
                                       "you will need 20,000 lines of code.<br>" \
                                       " If this does not make sense, ask a neighbor or the teacher."
            if test_efficiency['pass']:
                test_efficiency['pass'] = False
                test_efficiency['points'] = 0
                test_efficiency['fail_message'] += "You want to use a variable for the list index of prizes."
            else:
                test_efficiency['pass'] = True
                test_efficiency['pass_message'] += "(actually, did NOT find prizes[0], prizes[1] prizes[2] prizes[3]"
                test_efficiency['points'] = 5
            tests.append(test_efficiency)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 7)
            tests.append(test_pep8)
            test_help = helps(filename, 2.5)
            tests.append(test_help)

            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']
            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_2051b')
def feedback_2051b():

    from app.python_labs.find_items import find_if, find_questions, find_list, find_elif, find_else
    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.python_2_05x import python_2_051b_1
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 32.5, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '2.051b')
    tests.append(test_filename)
    if not test_filename['pass'] is True:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # test for a list being created with 4 items
        test_lcs = find_list(filename_data, num_items=4, list_name='learning_communities', points=3)
        tests.append(test_lcs)
        if not test_lcs['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # Read in the python file to filename_data
            filename_data = read_file_contents(filename)

            test_scores = find_list(filename_data, num_items=4, list_name='scores', points=3)
            test_scores['name'] += "All items should be initially all zero (which we do not check right now).<br>"
            tests.append(test_scores)
            if not test_scores['pass']:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:
                test_question = find_questions(filename_data, 1, 1)
                if not test_question['pass']:
                    test_question['fail_message'] += "You need to ask the user a question about which " \
                                                     "LC to vote for. <br>"
                tests.append(test_question)

                # test if, check for at least 1 if statement
                test_if = find_if(filename_data, 1, 1)
                tests.append(test_if)

                # test else check for at least 1 else statement
                test_else = find_else(filename_data, 1, 4)
                tests.append(test_else)

                # test elif check for at least 3
                test_elif = find_elif(filename_data, 3, 1)
                tests.append(test_elif)

                # Try C C R L S, should get 2, 1, 1, 1
                test_1_io = python_2_051b_1(filename, 5)
                tests.append(test_1_io)

                # Try C R L S blah blah blah, should get 1, 1, 1, 1
                test_2_io = python_2_051b_1(filename, 5)
                tests.append(test_2_io)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 7)
                tests.append(test_pep8)
                test_help = helps(filename, 2.5)
                tests.append(test_help)

                for test in tests:
                    if test['pass']:
                        score_info['score'] += test['points']

                score_info['finished_scoring'] = True
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)


@app.route('/feedback_3011')
def feedback_3011():

    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.find_items import find_string, find_questions, find_all_strings, find_list, find_random
    from app.python_labs.python_3_011 import python_3_011
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 64, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '3.011')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # test for a list being created with 6 items
        test_houses = find_list(filename_data, num_items=6, list_name='houses', points=10)
        tests.append(test_houses)
        if not test_houses['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # Asks a question, but that is ignore
            test_question = find_questions(filename_data, 1, 5)
            if not test_question['pass']:
                test_question['fail_message'] += "You need to ask the user a question to try to influence the hat. <br>"
            tests.append(test_question)

            # test for importing random
            test_random = find_random(filename_data, 5)
            tests.append(test_random)
            if not test_random['pass']:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:
                # test for importing randint
                test_randint = find_random(filename_data, 5, randint=True)
                tests.append(test_randint)

                # Check for at least 1 print statement
                test_find_print = find_string(filename_data, r'print\s*\(', 1, points=5)
                test_find_print['name'] += "Testing for at least one print statement. <br>"
                if test_find_print['pass']:
                    score_info['score'] += 5
                tests.append(test_find_print)

                # Test efficiency
                test_efficiency = find_all_strings(filename_data, [r'houses\[0\]', r'houses\[1\]',
                                                                   r'houses\[2\]', r'houses\[3\]'], 5)
                test_efficiency['name'] += "Testing efficiency.  Do NOT want to have a big if/elif/else.<br>" \
                                           "If you have a variable x which is a number of item in list," \
                                           " list[x-1] will get you the correct item.<br>" \
                                           "<br>  This technique saves a lot of lines of code over a big if/elif  " \
                                           "and scales to big numbers.  " \
                                           "<br>That is, a list with 10,000 items will need " \
                                           "just one line to print out the list item whereas with a big if/else, " \
                                           "you will need 20,000 lines of code.<br>" \
                                           " If this does not make sense, ask a neighbor or the teacher."
                if test_efficiency['pass']:
                    test_efficiency['pass'] = False
                    test_efficiency['fail_message'] += "You want to use a variable for the list index of houses."
                else:
                    test_efficiency['pass'] = True
                    test_efficiency[
                        'pass_message'] += "(actually, did NOT find houses[0], houses[1] houses[2] houses[3]"
                if test_efficiency['pass']:
                    score_info['score'] += 5
                tests.append(test_efficiency)

                test_runs = python_3_011(filename, filename_data)
                if test_runs['pass']:
                    score_info['score'] += 10
                tests.append(test_runs)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 14)
            tests.append(test_pep8)
            test_help = helps(filename, 5)
            tests.append(test_help)

            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_3020')
def feedback_3020():

    from app.python_labs.find_items import find_function, function_called, find_string
    from app.python_labs.function_test import extract_all_functions, extract_single_function, \
        function_test, create_testing_file
    from app.python_labs.python_3_020 import ten_runs, check_random
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 61, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '3.020')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        test_find_function_1 = find_function(filename, 'birthday_song', 1, 4)
        if test_find_function_1['pass']:
            score_info['score'] += 4
        tests.append(test_find_function_1)

        # Only continue if you have a birthday_song_function
        if not test_find_function_1['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:

            # Check that function is called once
            test_birthday_song_run = function_called(filename, 'birthday_song', 1, 4)
            if test_birthday_song_run['pass']:
                score_info['score'] += 4
            tests.append(test_birthday_song_run)

            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)

            # function test 1
            test_function_1 = function_test('3.020', 1, 5)
            test_function_1['name'] += " (prints out 'birthday' somewhere) "
            if test_function_1['pass']:
                score_info['score'] += 4
            tests.append(test_function_1)

            # function test 2
            test_function_2 = function_test('3.020', 2, 5)
            test_function_2['name'] += " (prints out input parameter somewhere) "
            if test_function_2['pass']:
                score_info['score'] += 5
            tests.append(test_function_2)

            # function test 3
            test_function_3 = function_test('3.020', 3, 8)
            test_function_3['name'] += " (output looks good) "
            if test_function_3['pass']:
                score_info['score'] += 8
            tests.append(test_function_3)

            test_find_function_2 = find_function(filename, 'pick_card', 0, 4)
            if test_find_function_2['pass']:
                score_info['score'] += 4
            tests.append(test_find_function_2)

            # Only continue if you have a birthday_song_function
            if not test_find_function_2['pass']:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:

                cards_function = extract_single_function(filename, 'pick_card')

                test_find_cards = find_string(cards_function, r"\s+ cards \s* = \s* \[ .+ , .+ , .+ , .* \]", 1, 2)
                test_find_cards['name'] += ("<h5 style=\"color:blue;\">Looking for a variable named cards that"
                                            " is a list"
                                            " with at least 4 items."
                                            "<br>This variable must be inside "
                                            "find_cards function.</p><br>")
                if test_find_cards['pass']:
                    score_info['score'] += 2
                tests.append(test_find_cards)

                test_find_suits = find_string(cards_function, r"\s+ suits \s* = \s* \[ .+ , .+ , .+ , .+ \]", 1, 2)
                test_find_suits['name'] += (
                    "<h5 style=\"color:blue;\">Looking for a variable named suits that is a list"
                    " with 4 items."
                    "<br>This variable must be inside "
                    "find_cards function.</p><br>")
                if test_find_suits['pass']:
                    score_info['score'] += 2
                tests.append(test_find_suits)

                # function test 4
                test_function_4 = function_test('3.020', 4, 5)
                test_function_4['name'] += " (function picks 1 card) "
                if test_function_4['pass']:
                    score_info['score'] += 5
                tests.append(test_function_4)

                # Check that function is called once
                test_pick_card_run = function_called(filename, 'pick_card', 1, 5)
                if test_pick_card_run['pass']:
                    score_info['score'] += 4
                tests.append(test_pick_card_run)

                # Check that random is random
                test_random = check_random(filename)
                if test_random['pass']:
                    score_info['score'] += 4
                tests.append(test_random)

                # check that pick_card prints out 10 cards (looks for 'of' 10x)
                test_run_ten_cards = ten_runs(filename)
                if test_run_ten_cards['pass']:
                    score_info['score'] += 4
                tests.append(test_run_ten_cards)

                # Find number of PEP8 errors
                pep8_max_points = 14
                test_pep8 = pep8(filename, pep8_max_points)
                if test_pep8['pass'] is False:
                    score_info['score'] += max(0, int(pep8_max_points) - test_pep8['pep8_errors'])
                tests.append(test_pep8)

                # Check for help comment
                help_points = 5
                test_help = helps(filename, help_points)
                if test_help['pass'] is True:
                    score_info['score'] += help_points
                tests.append(test_help)

                score_info['finished_scoring'] = True
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)


@app.route('/feedback_3026')
def feedback_3026():

    from app.python_labs.filename_test import filename_test
    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.find_items import find_string, find_function, function_called
    from app.python_labs.function_test import function_test, create_testing_file, extract_all_functions
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 44.5, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '3.026')
    tests.append(test_filename)
    if test_filename['pass'] is True:

        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # Check for function return_min
        test_find_function = find_function(filename, 'return_min', 1, 5)
        if test_find_function['pass']:
            score_info['score'] += 5
        tests.append(test_find_function)

        # Only continue if you have a return_min_function
        if test_find_function['pass']:

            # Check that function is called 1x
            test_function_run = function_called(filename, 'return_min', 1, 5)
            if test_function_run['pass']:
                score_info['score'] += 5
            tests.append(test_function_run)

            # find string return (return in the function)
            test_return = find_string(filename_data, r'return \s .+', 1, 5)
            extra_string = " (There is a return in the code)"
            test_return["name"] += extra_string
            test_return["pass_message"] += extra_string
            test_return["fail_message"] += extra_string
            if test_return['pass'] is True:
                score_info['score'] += 5
            tests.append(test_return)

            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)

            # function test 1
            test_function_1 = function_test('3.026', 1, 5)
            test_function_1['name'] += " (return_min with list [-1, 3, 5, 99] returns -1) "
            if test_function_1['pass']:
                score_info['score'] += 5
            tests.append(test_function_1)

            # function test 2
            test_function_2 = function_test('3.026', 2, 5)
            test_function_2['name'] += " (return_min with list [-1, 3, 5, -99] returns -99) "
            if test_function_1['pass']:
                score_info['score'] += 5
            tests.append(test_function_2)

            # function test 3
            test_function_3 = function_test('3.026', 3, 5)
            test_function_3['name'] += " (return_min with list [5] returns 5) "
            if test_function_1['pass']:
                score_info['score'] += 5
            tests.append(test_function_3)

            # function test 4
            test_function_4 = function_test('3.026', 4, 5)
            test_function_4['name'] += " (return_min with list [5, 4, 99, -11, 44, -241, -444, -999, 888, -2] " \
                                       "returns -444) "
            if test_function_1['pass']:
                score_info['score'] += 5
            tests.append(test_function_4)

            # Find number of PEP8 errors
            pep8_max_points = 7
            test_pep8 = pep8(filename, pep8_max_points)
            if test_pep8['pass'] is False:
                score_info['score'] += max(0, int(pep8_max_points) - test_pep8['pep8_errors'])
            tests.append(test_pep8)

            # Check for help comment
            help_points = 2.5
            test_help = helps(filename, help_points)
            if test_help['pass'] is True:
                score_info['score'] += help_points
            tests.append(test_help)

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)

        else:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_4011')
def feedback_4011():

    import re
    from app.python_labs.function_test import function_test, extract_single_function,\
        extract_all_functions, create_testing_file
    from app.python_labs.find_items import find_function, find_loop, function_called
    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.011')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        # Check for function
        test_find_function = find_function(filename, 'could_it_be_a_martian_word', 1, 5)
        if test_find_function['pass']:
            score_info['score'] += 5
        tests.append(test_find_function)

        if not test_find_function['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            extract_all_functions(filename)
            function_data = extract_single_function(filename, 'could_it_be_a_martian_word')
            create_testing_file(filename)
            filename_data = read_file_contents(filename)

            # Check for a loop of some sort (for or while)
            test_loop = find_loop(function_data, 5)
            test_loop['name'] += "Testing there is a loop in the could_it_be_a_martian_word function.<br>"
            if test_loop['pass']:
                score_info['score'] += 5
            tests.append(test_loop)

            # Check that function is called 3x
            test_function_run = function_called(filename, 'could_it_be_a_martian_word', 3, 5)
            if test_function_run['pass']:
                score_info['score'] += 5
            tests.append(test_function_run)

            test_function_1 = function_test('4.011', 1, 10)
            test_function_1['name'] += " (could_it_be_a_martian_word with 'bcdefgijnpqrstuvwxyz' returns []) "
            if test_function_1['pass']:
                score_info['score'] += 10
            tests.append(test_function_1)

            test_function_2 = function_test('4.011', 2, 10)
            test_function_2['name'] += " (could_it_be_a_martian_word with 'ba' returns ['a']) "
            if test_function_2['pass']:
                score_info['score'] += 10
            tests.append(test_function_2)

            test_function_3 = function_test('4.011', 3, 10)
            test_function_3['name'] += " (could_it_be_a_martian_word with 'baa' returns ['a']) "
            if test_function_3['pass']:
                score_info['score'] += 10
            tests.append(test_function_3)

            matches = len(re.findall(r"[^l]if \s", filename_data, re.X | re.M | re.S))
            test_ifs = {"name": "Testing that code is efficient, not too many if if if (5 points)",
                        "pass": True,
                        "pass_message": "Pass! Code appears to be efficient<br>",
                        "fail_message": "Fail. Code is not efficient! if if if is not the way to go<br>",
                        "score": 5
                        }
            if matches > 3:
                test_ifs['pass'] = False
                test_ifs['score'] = 0
            else:
                score_info['score'] += 5
            tests.append(test_ifs)

            # Find number of PEP8 errors
            pep8_max_points = 14
            test_pep8 = pep8(filename, pep8_max_points)
            if test_pep8['pass'] is False:
                score_info['score'] += max(0, int(pep8_max_points) - test_pep8['pep8_errors'])
            tests.append(test_pep8)

            # Check for help comment
            help_points = 5
            test_help = helps(filename, help_points)
            if test_help['pass'] is True:
                score_info['score'] += help_points
            tests.append(test_help)

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_4021')
def feedback_4021():

    from app.python_labs.find_items import find_function, function_called, find_loop
    from app.python_labs.function_test import function_test, extract_all_functions, \
        extract_single_function, create_testing_file
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 34.5,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.021')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Check for function the_rock_says
        test_find_function = find_function(filename, 'the_rock_says', 1, 5)
        tests.append(test_find_function)
        if not test_find_function['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            score_info['score'] += 5

            # Check that function is called 3x
            test_function_run = function_called(filename, 'the_rock_says', 3, 5)
            if test_function_run['pass']:
                score_info['score'] += 5
            tests.append(test_function_run)

            # extract functions and create python test file
            extract_all_functions(filename)
            function_data = extract_single_function(filename, 'the_rock_says')
            create_testing_file(filename)

            # Check for a loop of some sort (for or while)
            test_loop = find_loop(function_data, 5)
            test_loop['name'] += "Testing there is a loop in the could_it_be_a_martian_word function.<br>"
            if test_loop['pass']:
                score_info['score'] += 5
            tests.append(test_loop)

            # test1 for the_rock_says
            test_function_1 = function_test('4.021', 1, 5)
            test_function_1['name'] += " (Testing calling the_rock_says with list ['eggs', 'apple'] returns a list " \
                                       "['The Rock says eggs', 'The Rock says apple']) "
            if test_function_1['pass']:
                score_info['score'] += 5
            tests.append(test_function_1)

            # test2 for the_rock_says
            test_function_2 = function_test('4.021', 1, 5)
            test_function_2['name'] += " (Testing calling the_rock_says withlist ['eggs', 'smell'] returns " \
                                       "['The Rock says eggs', 'Do you smell what The Rock is cooking']" \
                                       "['The Rock says eggs', 'The Rock says apple']) <br> "
            if test_function_2['pass']:
                score_info['score'] += 5
            tests.append(test_function_2)

            # test3 for the_rock_says
            test_function_3 = function_test('4.021', 1, 5)
            test_function_3['name'] += " (Testing calling the_rock_says with list ['smog', 'smells', 'smashmouth'] " \
                                       "returns ['Do you smell what The Rock is cooking', " \
                                       "'Do you smellell what The Rock is cooking', " \
                                       "'Do you smellellellellellellell what The Rock is cooking'] <br> "
            if test_function_3['pass']:
                score_info['score'] += 5
            tests.append(test_function_3)

            # Find number of PEP8 errors
            pep8_max_points = 7
            test_pep8 = pep8(filename, pep8_max_points)
            if test_pep8['pass'] is False:
                score_info['score'] += max(0, int(pep8_max_points) - test_pep8['pep8_errors'])
            tests.append(test_pep8)

            # Check for help comment
            help_points = 2.5
            test_help = helps(filename, help_points)
            if test_help['pass'] is True:
                score_info['score'] += help_points
            tests.append(test_help)

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_4022')
def feedback_4022():
    from app.python_labs.find_items import find_function, function_called, find_loop
    from app.python_labs.function_test import function_test, extract_all_functions, \
        extract_single_function, create_testing_file
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 34.5,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.022')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Check for function the_rock_says
        test_find_function = find_function(filename, 'bad_lossy_compression', 1, 5)
        tests.append(test_find_function)
        if not test_find_function['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            score_info['score'] += 5
        # Only continue if you have a bad_lossy_compression function
        if test_find_function['pass']:

            # Check that function is called 3x
            test_function_run = function_called(filename, 'bad_lossy_compression', 3, 5)
            if test_function_run['pass']:
                score_info['score'] += 5
            tests.append(test_function_run)

            # extract functions and create python test file
            extract_all_functions(filename)
            function_data = extract_single_function(filename, 'bad_lossy_compression')
            create_testing_file(filename)

            # Check for a loop of some sort (for or while)
            test_loop = find_loop(function_data, 5)
            test_loop['name'] += "Testing there is a loop in the bad_lossy_compression function.<br>"
            if test_loop['pass']:
                score_info['score'] += 5
            tests.append(test_loop)

            # test1
            test_function_1 = function_test('4.022', 1, 5)
            test_function_1['name'] += " (Testing calling bad_lossy_compression with 'The rain in spain falls mainly" \
                                       " in the plain' returns 'The ain n spin flls ainl in he pain') "
            if test_function_1['pass']:
                score_info['score'] += 5
            tests.append(test_function_1)

            # test2 for the_rock_says
            test_function_2 = function_test('4.022', 2, 5)
            test_function_2['name'] += " (Testing calling bad_lossy_compression with " \
                                       "'I am sick and tired of these darned snakes on this darned plane'" \
                                       " returns 'I a sik ad tredof hes danedsnaes n tis arnd pane' <br> "
            if test_function_2['pass']:
                score_info['score'] += 5
            tests.append(test_function_2)

            # test3 for the_rock_says
            test_function_3 = function_test('4.022', 3, 5)
            test_function_3['name'] += "Testing calling bad_lossy_compression with 'Madness?!?!?!?!" \
                                       " THIS IS SPARTA!!!!'" \
                                       " returns 'Madess!?!!?!THI ISSPATA!!!' <br> "
            if test_function_3['pass']:
                score_info['score'] += 5
            tests.append(test_function_3)

            # Find number of PEP8 errors
            pep8_max_points = 7
            test_pep8 = pep8(filename, pep8_max_points)
            if test_pep8['pass'] is False:
                score_info['score'] += max(0, int(pep8_max_points) - test_pep8['pep8_errors'])
            tests.append(test_pep8)

            # Check for help comment
            help_points = 2.5
            test_help = helps(filename, help_points)
            if test_help['pass'] is True:
                score_info['score'] += help_points
            tests.append(test_help)

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)

    
@app.route('/feedback_4025')
def feedback_4025():
    import re
    import delegator

    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.function_test import extract_single_function, extract_all_functions, create_testing_file
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 64,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.025')
    tests.append(test_filename)
    if test_filename['pass'] is True:

        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)

        # test1 for serena game
        cmd = 'python3 /tmp/4.025.test.py testAutograde.test_serena_1 2>&1 |grep -i fail |wc -l'
        c = delegator.run(cmd)
        failures = int(c.out)
        test_serena_1 = {"name": "Checking the game function. (10 points)",
                         "pass": True,
                         "pass_message": "Pass. Actual win percentages over 1000 tests match the predicted win percentages. ",
                         "fail_message": "Fail.  Actual win percentages over 1000 tests do NOT match the predicted win percentages.<br> "
                         " Check out your code and try again.",
        }
        if failures > 0:
            test_serena_1['pass'] = False
        else:
            score_info['score'] += 10
        tests.append(test_serena_1)
            
        # test2 for serena play_tournament prints tournmaent
        cmd = 'python3 /tmp/4.025.test.py testAutograde.test_serena_2 2>&1 |grep -i fail |wc -l'
        c = delegator.run(cmd)
        failures = int(c.out)
        test_serena_2 =  {"name": "Testing play_tournament function.  If I input 'Wimbledon', it should print 'Wimbledon' somewhere. (2.5 points)",
                          "pass": True,
                          "pass_message": "Pass.  If I input 'Wimbledon', it should print 'Wimbledon' somewhere."
                          "Note, this 'pass' is subject to manual review.",
                          "fail_message": "Fail.  If I input 'Wimbledon', it should print 'Wimbledon' somewhere.<br>"
                          "Please check the play_tournament function prints.<br>",
        }
        if failures > 0:
            test_serena_2['pass'] = False
        else:
            score_info['score'] += 2.5
        tests.append(test_serena_2)

        # test3 for serena play tournament prints win
        cmd = 'python3 /tmp/4.025.test.py testAutograde.test_serena_3 2>&1 |grep -i fail |wc -l'
        c = delegator.run(cmd)
        failures = int(c.out)
        test_serena_3 =  {"name": "Testing play_tournament function.  If I input a high enough winning percentage,  "
                                  "it should print 'Win' somewhere (5 points)",
                          "pass": True,
                          "pass_message": "Pass.  If I input a high enough winning percentage, "
                                          "it should print 'Win' somewhere.<br>"
                                          "Note, this 'pass' is subject to manual review.",
                          "fail_message": "Fail.  If I input a high enough winning percentage, "
                                          "it should print 'Win' somewhere<br>"
                                          "Please check the play_tournament function prints.<br>",
                          }
        if failures > 0:
            test_serena_3['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_serena_3)

        # Test that play_tournamnet has a loop
        test_play_tournament_loop =  {"name": "Testing play_tournament function.  Should have a loop somewhere. (2.5 points)",
                                      "pass": True,
                                      "pass_message": "Pass. play_tournament function has a loop somewhere. "
                                                      "Note, this 'pass' is subject to manual review.",
                                      "fail_message": "Fail.   play_tournament function does not have loop somewhere."
                                                      "It needs a loop to play multiple games in case of win",
                                      }
        play_tournament = extract_single_function(filename, 'play_tournament')
        match = re.search('(for|while)', play_tournament)
        if match:
            score_info['score'] += 2.5
        else:
            test_play_tournament_loop['pass'] = False            
        tests.append(test_play_tournament_loop)

        # test4 for serena data_analysis
        cmd = 'python3 /tmp/4.025.test.py testAutograde.test_serena_4 2>&1 |grep -i fail |wc -l'
        c = delegator.run(cmd)
        failures = int(c.out)
        test_serena_4 =  {"name": "Testing data_analysis function.(5 points) ",
                          "pass": True,
                          "pass_message": "Pass.  data_analysis prints correct numbers given an input. ",
                          "fail_message": "Fail.  data_analysis prints in correct numbers given an input.<br>"
                                          "Input was list [25, 50, 75], and num_simulations = 100<br>"
                                          "Please check the data_analysis function prints correct values.<br>",
                          }
        if failures > 0:
            test_serena_4['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_serena_4)

        # full run, percentage is 1.0
        filename_output = filename + '.out'
        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/4.025-1.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running Serena Williams program')
        cmd = "grep '%' " + filename_output + ' | grep -i Wimbledon  '
        c = delegator.run(cmd)
        line = c.out
        test_win_all = {"name": "Testing that Wimbledon win % is correct, given win% of 1.0 (10 points)",
                        "pass": True,
                        "pass_message": "Pass!  Wimbledon win % is correct, givyen win% of 1.0.",
                        "fail_message": "Fail.   Wimbledon win % is NOT correct, given win% of 1.0.<br>"
                                        "Looking for the word 'Wimbledon' and a '%'.  Looks for the percent of times times she wins.<br>"
                                        "check your run to verify that the output is correct and she wins the correct % of times, <br>"
                                        "given a win % of 1.0.  Assumes the characters '%' and 'Wimbledon' do not show up anywhere else in output."
                                        "<br> ",
                        }
        flash(line)
        match = re.search('([.0-9]*)%', line)
        if match:
            percent = float(match.group(1))
            if percent > 101.0 or percent < 99.0: 
                test_win_all['pass'] = False            
            else:
                score_info['score'] += 10
        else:
            test_win_all['pass'] = False            
        tests.append(test_win_all)

        # full run, percentage is .75
        filename_output = filename + '.out2'
        cmd = 'python3 ' + filename + ' < /home/ewu/CRLS_APCSP_autograder/var/4.025-2.in > ' \
              + filename_output
        c = delegator.run(cmd)
        if c.err:
            flash('bad! You have an error somewhere in running Serena Williams program' + cmd)
        cmd = "grep '%' " + filename_output + ' | grep -i Wimbledon  '
        c = delegator.run(cmd)
        line = c.out
        test_win_some = {"name": "Testing that Wimbledon win % is correct, given win% of 0.75 (10 points)",
                         "pass": True,
                         "pass_message": "Pass!  Wimbledon win % is correct, given win% of 0.75.",
                         "fail_message": "Fail.   Wimbledon win % is NOT correct, given win% of 0.75.<br>"
                                         "Looking for the word 'Wimbledon' and a '%'.  Looks for the percent of"
                                         " times times she wins.<br>"
                                         "check your run to verify that the output is correct and she wins the "
                                         "correct % of times, <br>"
                                         "given a win 0.75.  Assumes the characters '%' and 'Wimbledon' do not "
                                         "show up anywhere else in output."
                                         "<br> ",
                         }
        match = re.search('([.0-9]*)%', line)
        if match:
            percent = float(match.group(1))
            if percent > 14.5 or percent < 12.5:
                test_win_some['pass'] = False
            else:
                score_info['score'] += 10
        else:
            test_win_some['pass'] = False            
        tests.append(test_win_some)

        # Find number of PEP8 errors
        pep8_max_points = 14
        test_pep8 = pep8(filename, pep8_max_points)
        if test_pep8['pass'] is False:
            score_info['score'] += max(0, int(pep8_max_points) - test_pep8['pep8_errors'])
        tests.append(test_pep8)

        # Check for help comment
        help_points = 5
        test_help = helps(filename, help_points)
        if test_help['pass'] is True:
            score_info['score'] += help_points
        tests.append(test_help)

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)    
    else:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_6_011')
def feedback_6011():

    import re
    from app.python_labs.function_test import function_test
    from app.python_labs.function_test import extract_all_functions, create_testing_file
    from app.python_labs.find_items import find_function
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test
    from app.python_labs.read_file_contents import read_file_contents

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '6.011')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        test_find_function = find_function(filename, 'bob_kraft_translator', 2, 5)
        tests.append(test_find_function)
        if not test_find_function['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            score_info['score'] += 5

            # Test for dictionary with 3+ items
            filename_data = read_file_contents(filename)

            search_object = re.search(r"{ .+ : .+ , .+ : .+ , .+ : .+ }", filename_data, re.X | re.M | re.S)
            test_dictionary = {"name": "Testing that there is a dictionary with 3+ key/value pairs(10 points)",
                               "pass": True,
                               "pass_message": "Pass! "
                                               "Submitted file looks like it has a dictionary with 3+ key/value pairs.",
                               "fail_message": "Fail. Submitted file does not look like it has a dictionary with 3+ "
                                               "key/value pairs. ",
                               }

            if not search_object:
                test_dictionary['pass'] = False
            else:
                score_info['score'] += 10
            tests.append(test_dictionary)

            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)

            test_function_1 = function_test('6.011', 1, 10)
            test_function_1['name'] += " (Sent in dictionary  {'wth': 'What the heck'}, search for 'wth', " \
                                       "returned 'what the heck') <br>"
            if test_function_1['pass']:
                score_info['score'] += 10
            tests.append(test_function_1)

            test_function_2 = function_test('6.011', 2, 10)
            test_function_2['name'] += " (Sent in dictionary  {'wth': 'What the heck', 'aymm': 'Ay yo my man',}, " \
                                       "looking for aymm, should receive 'Ay yo my man'. <br>"
            if test_function_2['pass']:
                score_info['score'] += 10
            tests.append(test_function_2)

            test_function_3 = function_test('6.011', 3, 10)
            test_function_3['name'] += " (Sent in dictionary  {'wth': 'What the heck','aymm': 'Ay yo my man',}, " \
                                       "asdfasdf, received something with 'do not know''. <br>"
            if test_function_3['pass']:
                score_info['score'] += 10
            tests.append(test_function_3)

            # Check for 3 ifs on different lines
            matches = len(re.findall(r"[^l]if \s", filename_data, re.X | re.M | re.S))
            test_ifs = {"name": "Testing that code is efficient, not too many if if if (5 points)",
                        "pass": True,
                        "pass_message": "Pass! Code appears to be efficient<br>",
                        "fail_message": "Fail. Code is not efficient! if if if is not the way to go<br>",
                        "score": 5
                        }
            if matches > 3:
                test_ifs['pass'] = False
                test_ifs['score'] = 0
            else:
                score_info['score'] += 5
            tests.append(test_ifs)

            # Find number of PEP8 errors
            pep8_max_points = 14
            test_pep8 = pep8(filename, pep8_max_points)
            score_info['score'] += max(0, int(pep8_max_points) - test_pep8['pep8_errors'])
            tests.append(test_pep8)

            # Check for help comment
            help_points = 5
            test_help = helps(filename, help_points)
            if test_help['pass'] is True:
                score_info['score'] += help_points
            tests.append(test_help)

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_6_021')
def feedback_6021():
    import re

    from app.python_labs.find_items import find_function, function_called
    from app.python_labs.function_test import extract_all_functions, extract_single_function, \
        create_testing_file, function_test
    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '6.021')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)
        martinez_function = extract_single_function(filename, 'martinez_dictionary')
        extract_all_functions(filename)
        create_testing_file(filename)

        test_find_function = find_function(filename, 'martinez_dictionary', 1, 5)
        if test_find_function['pass']:
            score_info['score'] += 5
        tests.append(test_find_function)

        # Check that function is called
        test_function_run = function_called(filename, 'martinez_dictionary', 3, 5)
        if test_function_run['pass']:
            score_info['score'] += 5
        tests.append(test_function_run)

        # extract martinez_dictionary functions and look for dictionary
        test_martinez_dictionary_dictionary = {"name": "Testing that martinez_dictionary function has a blank"
                                                       " dictionary to initialize(5 points)",
                                               "pass": True,
                                               "pass_message": "Pass.  martinez_dictionary function has a blank "
                                                               "dictionary to initialize.  <br>",
                                               "fail_message": "Fail.  martinez_dictionary function does not have a"
                                                               " blank dictionary in it to initialize. <br>"
                                               }
        martinez_function = extract_single_function(filename, 'martinez_dictionary')
        search_object = re.search(r"{  }", martinez_function, re.X | re.M | re.S)
        if search_object:
            score_info['score'] += 5
        else:
            test_martinez_dictionary_dictionary['pass'] = False
        tests.append(test_martinez_dictionary_dictionary)

        # Martinez test 1
        test_function_1 = function_test('6.021', 1, 10)
        test_function_1['name'] += "Test for martinez_list, ['Goku', 'Goku', 'Goku', 'Goku', 'Goku'], expect back" \
                                   "{'Goku': 500}' <br>"
        if test_function_1['pass']:
            score_info['score'] += 10
        tests.append(test_function_1)

        # Martinez test 2
        test_function_2 = function_test('6.021', 2, 10)
        test_function_2['name'] += "Test for martinez_list, " \
                                   "['Goku', 'Goku', 'Trunks', 'Vegeta', 'Vegeta', 'Krillan', 'Goku'], expect back" \
                                   "{'Goku': 300, 'Trunks': 100, 'Vegeta':200, 'Krillan':100}' <br>"
        if test_function_2['pass']:
            score_info['score'] += 10
        tests.append(test_function_2)

        test_find_function = find_function(filename, 'data_generator', 2, 5)
        tests.append(test_find_function)
        if not test_find_function['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            score_info['score'] += 5
            tests.append(test_find_function)

            # Martinez test 3
            test_function_3 = function_test('6.021', 3, 5)
            test_function_3['name'] += "Checking data_generator, send in " \
                                       "['Brolly', 'Goku', 'Gohan', 'Piccolo', 'Vegeta' ] twice, " \
                                       "The two lists should be different (test of random)  <br>"
            if test_function_3['pass']:
                score_info['score'] += 5
            tests.append(test_function_3)

            # Martinez test 4
            test_function_4 = function_test('6.021', 2, 10)
            test_function_4['name'] += "Checking data_generator, send in " \
                                       "['Brolly', 'Goku', 'Gohan', 'Piccolo', 'Vegeta' ]  " \
                                       "n=100, they should all show up once at least}' <br>"
            if test_function_4['pass']:
                score_info['score'] += 5
            tests.append(test_function_4)

            # Find number of PEP8 errors
            pep8_max_points = 14
            test_pep8 = pep8(filename, pep8_max_points)
            if test_pep8['pass'] is False:
                score_info['score'] += max(0, int(pep8_max_points) - test_pep8['pep8_errors'])
            tests.append(test_pep8)

            # Check for help comment
            help_points = 5
            test_help = helps(filename, help_points)
            if test_help['pass'] is True:
                score_info['score'] += help_points
            tests.append(test_help)

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_6_031')
def feedback_6031():
    import re
    import delegator

    from app.python_labs.function_test import extract_all_functions, function_test, create_testing_file
    from app.python_labs.find_items import find_function
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test
    from app.python_labs.read_file_contents import read_file_contents
    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '6.031')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        filename_data = read_file_contents(filename)

        search_object = re.search(r"{ \s* }", filename_data, re.X | re.M | re.S)
        test_dictionary = {"name": "Testing that there is an empty dictionary(5 points)",
                           "pass": True,
                           "pass_message": "Pass! "
                                           "Submitted file looks like it has an empty dictionary ",
                           "fail_message": "Fail. Submitted file does not look like it has an empty dictionary",
                           }
        if not search_object:
            test_dictionary['pass'] = False
        else:
            score_info['score'] += 5
        tests.append(test_dictionary)

        # Check for function add with 2 inputs
        test_find_function = find_function(filename, 'add', 2, 5)
        tests.append(test_find_function)
        if not test_find_function['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            score_info['score'] += 5

            extract_all_functions(filename)
            create_testing_file(filename)

            # function test 1
            test_function_1 = function_test('6.031', 1, 5)
            test_function_1['name'] += "Checking mcglathery_dictionary 1.  " \
                                       "Adding 'fire' and 'charmander' , expect output {'fire':'charmander'} <br>"
            if test_function_1['pass']:
                score_info['score'] += 5
            tests.append(test_function_1)

            # function test 2
            test_function_2 = function_test('6.031', 2, 10)
            test_function_2['name'] += "Checking mcglathery_dictionary 2.  Adding 'ice' and 'iceperson2' to " \
                                       "{'fire':['charmander'], 'ice':['iceperson']}." \
                                       " Expect output {['fire':['charmander'], 'ice':['iceperson','iceperson2']} <br>"
            if test_function_2['pass']:
                score_info['score'] += 10
            tests.append(test_function_2)

            # Check for function add with 2 inputs
            test_find_function = find_function(filename, 'get', 2, 5)
            tests.append(test_find_function)
            if not test_find_function['pass']:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:
                score_info['score'] += 5

                # function test 3
                test_function_3 = function_test('6.031', 3, 5)
                test_function_3['name'] += "Checking mcglathery_dictionary 3.  testing get function with input  " \
                                           "{'fire':['charmander']} expecting something with 'fire'  <br>"
                if test_function_3['pass']:
                    score_info['score'] += 5
                tests.append(test_function_3)

                # function test 3
                test_function_4 = function_test('6.031', 3, 10)
                test_function_4['name'] += "Checking mcglathery_dictionary 4.  testing get function with input  " \
                                           "{'fire':['charmander','fireperson'} expecting something" \
                                           "with 'fire' and 'fireperson   <br>"
                if test_function_4['pass']:
                    score_info['score'] += 10
                tests.append(test_function_4)

                # Check for a loop of some sort (for or while)
                cmd = 'grep -E "for|while"  ' + filename + ' | wc -l  '
                c = delegator.run(cmd)
                loop = int(c.out)
                test_loop = {"name": "Testing that program has a loop. (5 points)",
                             "pass": True,
                             "pass_message": "Pass.  Testing that program has a loop.  <br>",
                             "fail_message": "Fail.  Testing that program has a loop "
                                             "(assume a while or for means you have a loop) <br>"
                                             "The program needs a while or a for. <br>"
                                             "Fix code and resubmit. <br>",
                             }
                if loop == 0:
                    test_loop['pass'] = False
                else:
                    score_info['score'] += 5
                tests.append(test_loop)

                # Find number of PEP8 errors
                pep8_max_points = 14
                test_pep8 = pep8(filename, pep8_max_points)
                if test_pep8['pass'] is False:
                    score_info['score'] += max(0, int(pep8_max_points) - test_pep8['pep8_errors'])
                tests.append(test_pep8)

                # Check for help comment
                help_points = 5
                test_help = helps(filename, help_points)
                if test_help['pass'] is True:
                    score_info['score'] += help_points
                tests.append(test_help)
                score_info['finished_scoring'] = True

                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)


@app.route('/feedback_6_041')
def feedback_6041():

    from app.python_labs.find_items import find_function, find_string
    from app.python_labs.function_test import extract_all_functions, create_testing_file, function_test
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test
    from app.python_labs.read_file_contents import read_file_contents

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 64, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '6.041')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        filename_data = read_file_contents(filename)

        # Check for function add with 2 inputs
        test_find_function = find_function(filename, 'item_list_to_dictionary', 2, 5)
        tests.append(test_find_function)
        if test_find_function['pass']:
            score_info['score'] += 5
        tests.append(test_find_function)

        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)

        # function test 1
        test_function_1 = function_test('6.041', 1, 10)
        test_function_1['name'] += "Checking that item_list_to_dictionary works.   Input " \
                                   "['fantastic spaghetti', 'fantastic spaghetti', 'garlic bread', " \
                                   "'noodles noodles', " \
                                   "'noodles noodles', 'Gooey gelato', 'fantastic spaghetti'] " \
                                   " expected {'fantastic spaghetti': 3, 'garlic bread': 1, 'noodles noodles':2," \
                                   "'Gooey gelato':1}) <br>"
        if test_function_1['pass']:
            score_info['score'] += 10
        tests.append(test_function_1)

        # Check for function add with 2 inputs
        test_find_function = find_function(filename, 'min_item', 2, 5)
        tests.append(test_find_function)
        if test_find_function['pass']:
            score_info['score'] += 5
        tests.append(test_find_function)

        # unit test 2
        test_function_2 = function_test('6.041', 1, 10)
        test_function_2['name'] += "Call min_item with input" \
                                   " {'fantastic spaghetti': 3, 'garlic bread': 1, 'noodles noodles':2, " \
                                   "'Gooey gelato':99}.<br> " \
                                   "expect output 'garlic bread'). <br>"
        if test_function_2['pass']:
            score_info['score'] += 20
        tests.append(test_function_2)
                    
        # Check that removes, just look for del or pop
        test_removal = find_string(filename_data, r"\.pop\( | del", 1, 5)
        if test_removal:
            score_info['score'] += 5
        tests.append(test_removal)

        # Find number of PEP8 errors
        pep8_max_points = 14
        test_pep8 = pep8(filename, pep8_max_points)
        if test_pep8['pass'] is False:
            score_info['score'] += max(0, int(pep8_max_points) - test_pep8['pep8_errors'])
        tests.append(test_pep8)

        # Check for help comment
        help_points = 5
        test_help = helps(filename, help_points)
        if test_help['pass'] is True:
            score_info['score'] += help_points
        tests.append(test_help)

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_7_021')
def feedback_7021():
    from app.python_labs.find_items import find_class, find_function, function_called, object_created
    from app.python_labs.function_test import extract_all_functions, create_testing_file, function_test
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '7.021')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        # Check for class Collectible
        test_class = find_class(filename, 'Collectible', 'object', 5)
        if test_class['pass']:
            score_info['score'] += 5
        tests.append(test_class)

        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)

        # function test 2
        test_function_1 = function_test('7.021', 1, 15)
        if test_function_1['pass']:
            score_info['score'] += 15
        tests.append(test_function_1)

        # Check for function existence
        test_find_function = find_function(filename, 'collectible_printer', 1, 5)
        tests.append(test_find_function)
        if test_find_function['pass']:
            score_info['score'] += 5
        tests.append(test_find_function)

        # test 2
        test_function_2 = function_test('7.021', 2, 5)
        if test_function_2['pass']:
            score_info['score'] += 5
        tests.append(test_function_2)

        # test 2
        test_function_2 = function_test('7.021', 2, 5)
        if test_function_2['pass']:
            score_info['score'] += 5
        tests.append(test_function_2)

        # test 3
        test_function_3 = function_test('7.021', 3, 10)
        if test_function_3['pass']:
            score_info['score'] += 10
        tests.append(test_function_3)

        # Check for all objects
        test_objects = object_created(filename, 'Collectible', 3, 5)
        if test_objects['pass']:
            score_info['score'] += 5
        tests.append(test_objects)

        # Check that function is called
        test_function_run = function_called(filename, 'collectible_printer', 1, 5)
        if test_function_run['pass']:
            score_info['score'] += 5
        tests.append(test_function_run)

        # Find number of PEP8 errors
        pep8_max_points = 14
        test_pep8 = pep8(filename, pep8_max_points)
        if test_pep8['pass'] is False:
            score_info['score'] += max(0, int(pep8_max_points) - test_pep8['pep8_errors'])
        tests.append(test_pep8)

        # Check for help comment
        help_points = 5
        test_help = helps(filename, help_points)
        if test_help['pass'] is True:
            score_info['score'] += help_points
        tests.append(test_help)

        score_info['finished_scoring'] = True

        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_7_031')
def feedback_7031():
    from app.python_labs.function_test import extract_all_functions, create_testing_file, function_test
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 34.5, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '7.031')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)

        # unit test 1
        test_function_1 = function_test('7.031', 1, 5)
        if test_function_1['pass']:
            score_info['score'] += 5
        tests.append(test_function_1)

        # unit test 2
        test_function_2 = function_test('7.031', 1, 10)
        if test_function_2['pass']:
            score_info['score'] += 10
        tests.append(test_function_2)

        # unit test 3
        test_function_3 = function_test('7.031', 1, 10)
        if test_function_3['pass']:
            score_info['score'] += 10
        tests.append(test_function_3)

        # Find number of PEP8 errors
        pep8_max_points = 7
        test_pep8 = pep8(filename, pep8_max_points)
        if test_pep8['pass'] is False:
            score_info['score'] += max(0, int(pep8_max_points) - test_pep8['pep8_errors'])
        tests.append(test_pep8)

        # Check for help comment
        help_points = 2.5
        test_help = helps(filename, help_points)
        if test_help['pass'] is True:
            score_info['score'] += help_points
        tests.append(test_help)

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_7_034')
def feedback_7034():
    from app.python_labs.function_test import extract_all_functions, create_testing_file, function_test
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 34.5, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '7.034')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)

        # unit test 1
        unit_test_1 = function_test('7.034', 1, 5)
        if unit_test_1['pass']:
            score_info['score'] += 5
        tests.append(unit_test_1)

        # unit test 2
        unit_test_2 = function_test('7.034', 1, 5)
        if unit_test_2['pass']:
            score_info['score'] += 5
        tests.append(unit_test_2)

        # unit test 3
        unit_test_3 = function_test('7.034', 1, 5)
        if unit_test_3['pass']:
            score_info['score'] += 5
        tests.append(unit_test_3)

        # unit test 4
        unit_test_4 = function_test('7.034', 1, 5)
        if unit_test_4['pass']:
            score_info['score'] += 5
        tests.append(unit_test_4)

        # unit test 5
        unit_test_5 = function_test('7.034', 1, 5)
        if unit_test_5['pass']:
            score_info['score'] += 5
        tests.append(unit_test_5)

        # Find number of PEP8 errors
        pep8_max_points = 7
        test_pep8 = pep8(filename, pep8_max_points)
        if test_pep8['pass'] is False:
            score_info['score'] += max(0, int(pep8_max_points) - test_pep8['pep8_errors'])
        tests.append(test_pep8)

        # Check for help comment
        help_points = 2.5
        test_help = helps(filename, help_points)
        if test_help['pass'] is True:
            score_info['score'] += help_points
        tests.append(test_help)

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)    


@app.route('/feedback_4031')
def feedback_4031():
    from app.python_labs.function_test import create_testing_file, extract_all_functions, function_test
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 54, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '7.034')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)

        # unit test 1
        unit_test_1 = function_test('4.031', 1, 2.5)
        if unit_test_1['pass']:
            score_info['score'] += 2.5
        tests.append(unit_test_1)

        # unit test 2
        unit_test_2 = function_test('4.031', 2, 2.5)
        if unit_test_2['pass']:
            score_info['score'] += 2.5
        tests.append(unit_test_2)

        # unit test 3
        unit_test_3 = function_test('4.031', 3, 2.5)
        if unit_test_3['pass']:
            score_info['score'] += 2.5
        tests.append(unit_test_3)

        # unit test 4
        unit_test_4 = function_test('4.031', 4, 2.5)
        if unit_test_4['pass']:
            score_info['score'] += 5
        tests.append(unit_test_4)

        # unit test 5
        unit_test_5 = function_test('4.031', 5, 2.5)
        if unit_test_5['pass']:
            score_info['score'] += 5
        tests.append(unit_test_5)

        # unit test 6
        unit_test_6 = function_test('4.031', 6, 2.5)
        if unit_test_6['pass']:
            score_info['score'] += 5
        tests.append(unit_test_6)

        # unit test 7
        unit_test_7 = function_test('4.031', 7, 2.5)
        if unit_test_7['pass']:
            score_info['score'] += 5
        tests.append(unit_test_7)

        # unit test 8
        unit_test_8 = function_test('4.031', 8, 2.5)
        if unit_test_8['pass']:
            score_info['score'] += 7.5
        tests.append(unit_test_8)

        # Find number of PEP8 errors
        pep8_max_points = 14
        test_pep8 = pep8(filename, pep8_max_points)
        if test_pep8['pass'] is False:
            score_info['score'] += max(0, int(pep8_max_points) - test_pep8['pep8_errors'])
        tests.append(test_pep8)

        # Check for help comment
        help_points = 5
        test_help = helps(filename, help_points)
        if test_help['pass'] is True:
            score_info['score'] += help_points
        tests.append(test_help)

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)

    
@app.route('/feedback_4036')
def feedback_4036():
    from app.python_labs.find_items import find_function
    from app.python_labs.function_test import extract_all_functions, create_testing_file, function_test
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '7.034')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        # Check for function existence
        test_find_function = find_function(filename, 'fried_chicken_problem_1', 2, 5)
        tests.append(test_find_function)
        if test_find_function['pass']:
            score_info['score'] += 5
        tests.append(test_find_function)

        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)

        # unit test 1
        unit_test_1 = function_test('4.036', 1, 10)
        if unit_test_1['pass']:
            score_info['score'] += 10
        tests.append(unit_test_1)

        # unit test 2
        unit_test_2 = function_test('4.036', 2, 10)
        if unit_test_2['pass']:
            score_info['score'] += 10
        tests.append(unit_test_2)

        # Check for function existence
        test_find_function = find_function(filename, 'fried_chicken_problem_2', 2, 5)
        tests.append(test_find_function)
        if test_find_function['pass']:
            score_info['score'] += 5
        tests.append(test_find_function)

        # unit test 3
        unit_test_3 = function_test('4.036', 3, 10)
        if unit_test_3['pass']:
            score_info['score'] += 10
        tests.append(unit_test_3)

        # unit test 4
        unit_test_4 = function_test('4.036', 4, 10)
        if unit_test_4['pass']:
            score_info['score'] += 10
        tests.append(unit_test_4)

        # Find number of PEP8 errors
        pep8_max_points = 14
        test_pep8 = pep8(filename, pep8_max_points)
        if test_pep8['pass'] is False:
            score_info['score'] += max(0, int(pep8_max_points) - test_pep8['pep8_errors'])
        tests.append(test_pep8)

        # Check for help comment
        help_points = 5
        test_help = helps(filename, help_points)
        if test_help['pass'] is True:
            score_info['score'] += help_points
        tests.append(test_help)

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
