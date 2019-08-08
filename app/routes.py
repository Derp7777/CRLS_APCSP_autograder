from flask import render_template, url_for, request, redirect, flash
from app import app
from app.forms import UploadForm, UploadScratchForm, UploadDocLinkForm
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
            if request.form['lab'] in ['1.040', '1.060', '2.020', '2.032a', '2.032b', '2.040', '2.050a', '2.050b',
                                       '3.011', '3.020', '3.026', '4.011', '4.021', '4.022', '4.025', '4.031',
                                       '4.036', '6.011', '6.021', '6.031', '6.041', '7.021', '7.031', '7.034', ]:
                return redirect(url_for('feedback_' + request.form['lab'].replace(".", ""), filename=filename))

    form = UploadForm()
    user = {'username': 'CRLS Scholar!!!'}
    return render_template('index.html', title='Home', user=user, form=form)


@app.route('/scratch', methods=['GET', 'POST'])
def scratch():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Please select a file')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        if not allowed_file(file.filename):
            flash('This type of file not allowed.  Only files ending in .sb3.'
                  '  In particular, Google doc and text files are not allowed.'
                  'You have to turn in a Scratch 3 file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash(file.filename + ' uploaded')
            if request.form['lab'] in ['1.3', '1.4_1.5', '1.x_family_migration_story', '2.2',
                                       '2.4_alternate', '2.5_alternate',
                                       '2.6', '3.2_alternate', '3.3_3.4_alternate', '4.2_alternate',
                                       '4.3a_alternate', '4.3b_alternate', '4.4', 'karel1', 'karel2a', 'karel2b',
                                       'karel3a', 'karel3b', 'karel3c', 'karel3d',
                                       ]:
                return redirect(url_for('scratch_feedback_' + request.form['lab'].replace(".", ""), filename=filename))

    form = UploadScratchForm()
    user = {'username': 'CRLS Scratch Scholar!!'}
    return render_template('index.html', title='Home', user=user, form=form)


@app.route('/docs', methods=['GET', 'POST'])
def docs():
    from app.docs_labs.docs import get_google_drive_id
    if request.method == 'POST':
        form = UploadDocLinkForm()
        link = get_google_drive_id(form.link.data)
        return redirect(url_for('docs_feedback_' + request.form['lab'].replace(".", ""), link=link))
    form = UploadDocLinkForm()
    user = {'username': 'CRLS Intro to CS-IT1/ APCSP Scholar!!'}
    return render_template('index.html', title='Home', user=user, form=form)


@app.route('/docs/binary_practice')
def docs_feedback_binary_practice():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'manually_scored': 71, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)
    print(text)
    test1a = exact_answer('question 1a', [r'1a .+? tabledata \s* 0011 .+ tabledata \s*? 3 [^a-z] '], text, points=2)
    test1b = exact_answer('question 1b', [r'1b .+? tabledata \s* 0100 .+ tabledata \s*?  4 [^a-z]'], text, points=2)
    test1c = exact_answer('question 1c', [r'1c .+? tabledata \s* 0101 .+ tabledata \s*? 5 [^a-z]'], text, points=2)
    test1d = exact_answer('question 1d', [r'1d .+? tabledata \s* 0110 .+ tabledata \s*? 6 [^a-z]'], text, points=2)
    test1e = exact_answer('question 1e', [r'1e .+? tabledata \s* 0111 .+ tabledata \s*?  7 [^a-z]'], text, points=2)
    test1f = exact_answer('question 1f', [r'1f .+? tabledata \s* 1000 .+ tabledata \s*?  8 [^a-z]'], text, points=2)
    test1g = exact_answer('question 1g', [r'1g .+? tabledata \s* 1001 .+ tabledata \s*?  9 [^a-z]'], text, points=2)
    test1h = exact_answer('question 1h', [r'1h .+? tabledata \s* 1010 .+ tabledata \s*?  10 [^a-z]'], text, points=2)
    test1i = exact_answer('question 1i', [r'1i .+? tabledata \s* 1011 .+ tabledata \s*?  11 [^a-z]'], text, points=2)
    test1j = exact_answer('question 1j', [r'1j .+? tabledata \s* 1100 .+ tabledata \s*?  12 [^a-z]'], text, points=2)
    test1k = exact_answer('question 1k', [r'1k .+? tabledata \s* 1101 .+ tabledata \s*?  13 [^a-z]'], text, points=2)
    test1l = exact_answer('question 1l', [r'1l .+? tabledata \s* 1110 .+ tabledata \s*?  14 [^a-z]'], text, points=2)
    test1m = exact_answer('question 1m', [r'1m .+? tabledata \s* 1111 .+ tabledata \s*?  15 [^a-z]'], text, points=2)
    test2a = exact_answer('question 2a', [r'2a. .+? tabledata \s* 0000 \s 0100 .+ tabledata \s* 4'], text, points=2)
    test2b = exact_answer('question 2b', [r'2b. .+? tabledata \s* 0000 \s 1000 .+ tabledata \s* 8'], text, points=2)
    test2c = exact_answer('question 2c', [r'2c. .+? tabledata \s* 0001 \s 0000 .+ tabledata \s* 16'], text, points=2)
    test2d = exact_answer('question 2d', [r'2d. .+? tabledata \s* 0010 \s 0000 .+ tabledata \s* 32'], text, points=2)
    test2e = exact_answer('question 2e', [r'2e. .+? tabledata \s* 0100 \s 0000 .+ tabledata \s* 64'], text, points=2)
    test2f = exact_answer('question 2f',
                          [r'2f. .+? tabledata \s* 1000 \s 0000 .+? tabledata \s* 128 .+? conversion \s practice'],
                          text, points=2)
    test3a = exact_answer('question 3a', [r'3a. .+? tabledata \s* 100 .+ tabledata \s* 5 .+? 3h'], text, points=2)
    test3b = exact_answer('question 3b', [r'3b. .+? tabledata \s* 111 .+ tabledata \s* 7 .+? 3i'], text, points=2)
    test3c = exact_answer('question 3c', [r'3c. .+? tabledata \s* 1101 .+ tabledata \s* 13 .+? 3j'], text, points=2)
    test3d = exact_answer('question 3d', [r'3d. .+? tabledata \s* 0011\s1111 .+ tabledata \s* 63 .+? 3k'],
                          text, points=2)
    test3e = exact_answer('question 3e', [r'3e. .+? tabledata \s* 0100 \s 0000 .+ tabledata \s* 64 '],
                          text, points=2)
    test3f = exact_answer('question 3f', [r'3f. .+? tabledata \s* 1010 \s 1010 .+ tabledata \s* 170'], text, points=2)
    test3g = exact_answer('question 3g', [r'3g. .+? tabledata \s* 1111 \s 1111 .+ tabledata \s* 255'], text, points=2)
    test3h = exact_answer('question 3h', [r'3h. .+? tabledata \s* 0*? 101 .+ tabledata \s* 5 .+? 3b'], text, points=2)
    test3i = exact_answer('question 3i', [r'3i. .+? tabledata \s* 0*? 1\s* 0001.+ tabledata \s* 17'], text, points=2)
    test3j = exact_answer('question 3j', [r'3j. .+? tabledata \s* 0*? 11\s*1111 .+ tabledata \s* 63'], text, points=2)
    test3k = exact_answer('question 3k', [r'3k. .+? tabledata \s* 0*? 100 \s* 0000 .+ tabledata \s* 128'], text, points=2)
    test3l = exact_answer('question 3l', [r'3l. .+? tabledata \s* 0*? 111 \s* 1111 .+ tabledata \s* 127'], text, points=2)
    test3m = exact_answer('question 3m', [r'3m. .+? tabledata \s* 0*? 1 \s* 0000 \s* 0000.+ tabledata \s* 256'],
                          text, points=2)
    test3n = exact_answer('question 3n', [r'3n. .+? tabledata \s* 0*? 10 \s* 0000 \s* 0010 .+ tabledata \s* 514'],
                          text, points=2)
    test4 = keyword_and_length('question 4', [r'[a-zA-Z]+'], text,
                               search_string=r'4. \s there .+? tabledata (.+) 5. .+? many', min_length=10, points=1)
    test5 = keyword_and_length('question 5', [r'[0-9]+'], text,
                               search_string=r'5. \s how .+? tabledata (.+) 6. .+? cartoon', min_length=7, points=1)
    test6 = keyword_and_length('question 6', [r'[0-9]+'], text,
                               search_string=r'6. \s most .+? tabledata (.+) .+? cartoon', min_length=7, points=1)
    tests.extend([test1a, test1b, test1c, test1d, test1e, test1f, test1g, test1h, test1i, test1j, test1k, test1l,
                  test1m, test2a, test2b, test2c, test2d, test2e, test2f, test3a, test3b, test3c, test3d, test3e,
                  test3f, test3g, test3h, test3i, test3j, test3k, test3l, test3m, test3n, test4, test5, test6])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/black_and_white_pixelation')
def docs_feedback_black_and_white_pixelation():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 22, 'manually_scored': 73, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('question 1', [r'1 .+? tabledata \s* aaa \s* inlineobject .+ 2.'], text, points=1)
    test2a = exact_answer('question 2a', [r'2a .+? tabledata \s* aaa \s* inlineobject .+ 2b.'], text, points=1)
    test2b = exact_answer('question 2b', [r'2b .+? tabledata \s [0-9]+ .+? questions'], text, points=1)
    test3a = exact_answer('question 3a', [r'3a. .+? tabledata \s* 255 .+? 255 .+ 3b.'], text, points=5)
    test3b = keyword_and_length('question 3b', [r'[a-z]+'], text,
                               search_string=r'3b.+? tabledata (.+) .+? 3c.', min_length=7, points=1)
    test3c = exact_answer('question 3c', [r'3c. .+? tabledata \s* 65 .+? 041 .+ 3d.'], text, points=5)
    test3d = keyword_and_length('question 3d', [r'[a-z]+'], text,
                                search_string=r'3d.+? tabledata (.+) .+? 3e.', min_length=7, points=1)
    test3e = exact_answer('question 3e', [r'3e. .+? tabledata \s* (1|17) .+ 3f.'], text, points=5)
    test3f = keyword_and_length('question 3f', [r'[a-z]+'], text,
                                search_string=r'3f.+? tabledata (.+) .+? 4.', min_length=7, points=1)
    test4 = keyword_and_length('question 4', [r'[a-z]+'], text,
                                search_string=r'4.+? tabledata (.+) .+? $', min_length=10, points=1)
    tests.extend([test1a, test2a, test2b, test3a, test3b, test3c, test3d, test3e, test3f, test4])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/encoding_color_images')
def docs_feedback_encoding_color_images():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 13, 'manually_scored': 39, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1 = exact_answer('question 1', [r'1\. .+? tabledata \s* \d .+? step \s 2:'], text, points=1)
    test2 = exact_answer('question 2', [r'2\. .+? tabledata \s* \d .+? step \s 3:'], text, points=1)
    test3 = exact_answer('question 3', [r'3\. .+? tabledata \s* \d .+? questions'], text, points=1)
    test4a = exact_answer('question 4a', [r'4a\. .+? tabledata \s* \d .+?4b'], text, points=1)
    test4b = keyword_and_length('question 4b', [r'[a-z]+'], text,
                               search_string=r'4b.+? tabledata (.+) .+? 5a', min_length=7, points=1)
    test5a = exact_answer('question 5a', [r'5a\. .+? tabledata \s* 64 .+?5b'], text, points=5)
    test5b = keyword_and_length('question 5b', [r'[a-z]+'], text,
                                search_string=r'5b\. .+? tabledata (.+?) 6\.', min_length=7, points=1)
    test6 = keyword_and_length('question 6', [r'[a-z]+'], text,
                                search_string=r'6\. .+? tabledata (.+?)  7\.', min_length=7, points=1)
    test7 = keyword_and_length('question 7', [r'[a-z]+'], text,
                               search_string=r'7\. .+? tabledata (.+?)  $', min_length=10, points=1)
    tests.extend([test1, test2, test3, test4a, test4b, test5a, test5b, test6, test7])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/docs_feedback_encryption_1')
def docs_feedback_encryption_1():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 16, 'manually_scored': 34, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)
    print(text)
    test1a = keyword_and_length('question 1a', ['\s*26!\s*', '\ss*4\.[0-9]+ .+ 26\s*', '\s* 26 \s* factorial',
                                                '\s*26\s*x\s*25\s*x\s*24'], text,
                                search_string=r'1a. .+? tabledata (.+) 1b', min_length=1, points=5)
    test1b = keyword_and_length('question 1b', [r'[a-zA-Z]+'], text,
                                search_string=r'1b. .+? tabledata (.+) 2a', min_length=10, points=1)
    test2a = keyword_and_length('question 2a', [r'[a-zA-Z]+'], text,
                                search_string=r'2a. .+? tabledata (.+) 2b', min_length=10, points=1)
    test2b = keyword_and_length('question 2b', [r'\s* 1\.6[0-9]+ .+ 25'], text,
                                search_string=r'2b. .+? tabledata (.+) 2c', min_length=1, points=5)
    test2c = keyword_and_length('question 2c', [r'[a-zA-Z]+'], text,
                                search_string=r'2c. .+? tabledata (.+) 3a', min_length=94, points=1)
    test3a = keyword_and_length('question 3a', [r'[a-zA-Z]+'], text,
                                search_string=r'3a. .+? tabledata (.+) 3b', min_length=10, points=1)
    test3b = keyword_and_length('question 3b', [r'[a-zA-Z]+'], text,
                                search_string=r'3b. .+? tabledata (.+) 4a', min_length=10, points=1)
    test4a = keyword_and_length('question 4a', [r'[a-zA-Z]+'], text,
                                search_string=r'4a. .+? tabledata (.+) 4b', min_length=8, points=1)
    test4b = keyword_and_length('question 4b', [r'[a-zA-Z]+'], text,
                                search_string=r'4b. .+? tabledata (.+) $', min_length=8, points=1)
    tests.extend([test1a, test1b, test2a, test2b, test2c, test3a, test3b, test4a, test4b, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/docs_feedback_encryption_2')
def docs_feedback_encryption_2():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 24, 'manually_scored': 26 , 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)
    print(text)
    test1a = keyword_and_length('question 1a', [r'[^\s]+'], text,
                                search_string=r'1a. .+? tabledata .+? tabledata (.+) tabledata .+? 1b', min_length=1,
                                points=3)
    test1b = keyword_and_length('question 1b', [r'[^\s]+'], text,
                                search_string=r'1b. .+? tabledata .+? tabledata (.+) tabledata .+? 1c', min_length=1,
                                points=3)
    test1c = keyword_and_length('question 1c', [r'[^\s]+'], text,
                                search_string=r'1c. .+? tabledata .+? tabledata (.+) tabledata .+? 1d', min_length=1,
                                points=3)
    test1d = keyword_and_length('question 1d', [r'[^\s]+'], text,
                                search_string=r'1d. .+? tabledata .+? tabledata (.+) tabledata .+? 1e', min_length=1,
                                points=3)
    test1e = keyword_and_length('question 1e', [r'[^\s]+'], text,
                                search_string=r'1e. .+? tabledata .+? tabledata (.+) Thought', min_length=1,
                                points=3)
    test2a = keyword_and_length('question 2a', [r'[a-zA-Z]+'], text,
                                search_string=r'2a. .+? tabledata (.+) 2b', min_length=10, points=1)
    test2b = keyword_and_length('question 2b', [r'[a-zA-Z]+'], text,
                                search_string=r'2b. .+? tabledata (.+) 3a', min_length=10, points=1)
    test3a = keyword_and_length('question 3a', [r'[a-zA-Z]+'], text,
                                search_string=r'3a. .+? tabledata (.+) 4a', min_length=10, points=1)
    test4a = keyword_and_length('question 4a', [r'no'], text,
                                search_string=r'4a. .+? tabledata (.+) 4b', min_length=1, points=5)
    test4b = keyword_and_length('question 4b', [r'[a-zA-Z]+'], text,
                                search_string=r'4b. .+? tabledata (.+) $', min_length=10, points=1)
    tests.extend([test1a, test1b, test1c, test1d, test1e, test2a, test2b, test3a, test4a, test4b, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/docs_feedback_encryption_3')
def docs_feedback_encryption_3():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 13, 'manually_scored': 37, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)
    print(text)
    test1a = keyword_and_length('question 1a', [r'[a-zA-Z]+'], text,
                                search_string=r'1a. .+? tabledata (.+) 2a.', min_length=10,
                                points=1)
    test2a = keyword_and_length('question 2a', [r'[a-zA-Z]+'], text,
                                search_string=r'2a. .+? tabledata (.+) 3a.', min_length=10,
                                points=1)
    test3a = keyword_and_length('question 3a', [r'[a-zA-Z]+'], text,
                                search_string=r'3a. .+? tabledata (.+) 4a', min_length=7, points=1)

    test4a = keyword_and_length('question 4a', [r'[a-zA-Z]'], text,
                                search_string=r'4a. .+? tabledata (.+) 4b', min_length=7, points=1)
    test4b = keyword_and_length('question 4b', [r'\s*secur'], text,
                                search_string=r'4b. .+? tabledata (.+) 5', min_length=1, points=5)
    test5a = keyword_and_length('question 5a', [r'[a-zA-Z]+'], text,
                                search_string=r'5a. .+? tabledata (.+) 6a', min_length=8, points=1)
    test6a = keyword_and_length('question 6a', [r'[a-zA-Z]+'], text,
                                search_string=r'6a. .+? tabledata (.+) 6b', min_length=7, points=1)
    test6b = keyword_and_length('question 6b', [r'[a-zA-Z]+'], text,
                                search_string=r'6b. .+? tabledata (.+) 6c', min_length=7, points=1)
    test6c = keyword_and_length('question 6c', [r'[a-zA-Z]+'], text,
                                search_string=r'6c. .+? tabledata (.+) $', min_length=7, points=1)

    tests.extend([test1a, test2a, test3a, test4a, test4b, test5a, test6a, test6b, test6c ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/docs_feedback_encryption_4')
def docs_feedback_encryption_4():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 20, 'manually_scored': 30, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)
    print(text)
    test1a = keyword_and_length('question 1a', [r'5\s*s'], text,
                                search_string=r'1a. .+? tabledata (.+) 2a.', min_length=1,
                                points=10)
    test2a = keyword_and_length('question 2a', [r'2\s*d'], text,
                                search_string=r'2a. .+? tabledata (.+) 2b.', min_length=1,
                                points=5)
    test2b = keyword_and_length('question 2b', [r'[a-zA-Z]+'], text,
                                search_string=r'2b. .+? tabledata (.+) 3a', min_length=10, points=1)
    test3a = keyword_and_length('question 3a', [r'[a-zA-Z]+'], text,
                                search_string=r'3a. .+? tabledata (.+) 3b', min_length=2, points=1)
    test3b = keyword_and_length('question 3b', [r'[a-zA-Z]+'], text,
                                search_string=r'3b. .+? tabledata (.+) 4a', min_length=8, points=1)

    test4a = keyword_and_length('question 4a', [r'[a-zA-Z]'], text,
                                search_string=r'4a. .+? tabledata (.+) 5a', min_length=1, points=1)
    test5a = keyword_and_length('question 5a', [r'[a-zA-Z]+'], text,
                                search_string=r'5a. .+? tabledata (.+) $', min_length=10, points=1)
    tests.extend([test1a, test2a, test2b, test3a, test3b, test4a, test5a, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/hardware_esd_formfactors_cards')
def docs_feedback_hardware_esd_formfactors_cards():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 29, 'manually_scored': 71, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)
    print(text)
    test1a = exact_answer('question 1a', [r'1a .+? tabledata \s*  electr .+ static .+ discharg .+ 1b'], text, points=5)
    test1b = keyword_and_length('question 1b', [r'[a-zA-Z]+'], text,
                                search_string=r'1b. .+? tabledata (.+) 1c.', min_length=7, points=1)
    test1c1 = exact_answer('question 1c-1', [r'1c. .+? tabledata .+ touch .+ side .+ 2.'], text, points=4)
    test1c2 = exact_answer('question 1c-2', [r'1c. .+? tabledata .+ (wrist|strap|brac) .+ 2.'], text, points=3)
    test1c3 = exact_answer('question 1c-3', [r'1c. .+? tabledata .+ (mat|rug) .+ 2.'], text, points=3)
    test2a = exact_answer('question 2a', [r'2a. .+? tabledata .+ small .+ form .+ factor .+ 2b.',
                                          r'2a. .+? tabledata .+ micro .+ 2b.',
                                          r'2a. .+? tabledata .+ tower.+ 2b.',
                                          r'2a. .+? tabledata .+ rack.+ 2b.'], text, points=3, required=2)
    test2b = exact_answer('question 2b', [r'2b. .+? tabledata .+ [a-zA-Z] .+ pci'], text, points=1)
    test3a = exact_answer('question 3a', [r'3a. .+? tabledata .+ inlineobject .+ 3b'], text, points=1)
    test3b = exact_answer('question 3b', [r'3b. .+? tabledata .+ [a-zA-Z] .+ pci'], text, points=1)
    test4a = keyword_and_length('question 4a', [r'[a-zA-Z]+'], text,
                                search_string=r'4a. .+? tabledata (.+) 4b', min_length=7, points=1)
    test4b = exact_answer('question 4b', [r'4b. .+? tabledata .+ (1|16) .+ 4c'], text, points=5)
    test4c = keyword_and_length('question 4c', [r'[a-zA-Z]+'], text,
                                search_string=r'4c. .+? tabledata (.+) How', min_length=15, points=1)
    tests.extend([test1a, test1b, test1c1, test1c2, test1c3, test2a, test2b, test3a, test3b, test4a, test4b, test4c])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/hex_minilab')
def docs_feedback_hex_minilab():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 16, 'manually_scored': 0, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)
    print(text)
    test1a = exact_answer('question 1a', [r'1a .+? tabledata \s* 5.+ tabledata \s*? 3 [^a-z] '], text, points=2)
    test1b = exact_answer('question 1b', [r'1b .+? tabledata \s* c .+ tabledata \s*?  12 [^a-z]'], text, points=2)
    test1c = exact_answer('question 1c', [r'1c .+? tabledata \s* a4 .+ tabledata \s*? 164 [^a-z]'], text, points=2)
    test1d = exact_answer('question 1d', [r'1d .+? tabledata \s* 2f .+ tabledata \s*? 47 [^a-z]'], text, points=2)
    test2a = exact_answer('question 2a', [r'2a. .+? tabledata \s* 1f .+ tabledata \s* 31'], text, points=2)
    test2b = exact_answer('question 2b', [r'2b. .+? tabledata \s* 8 .+ tabledata \s* 8'], text, points=2)
    test2c = exact_answer('question 2c', [r'2c. .+? tabledata \s* 51 .+ tabledata \s* 81'], text, points=2)
    test2d = exact_answer('question 2d', [r'2d. .+? tabledata \s* FF .+ tabledata \s* 255'], text, points=2)

    tests.extend([test1a, test1b, test1c, test1d, test2a, test2b, test2c, test2d, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/docs_ip_addressing_dns')
def docs_feedback_ip_addressing_dns():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 22, 'manually_scored': 28, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)
    print(text)
    test1 = keyword_and_length('question 1a', [r'(standard|rule)'], text,
                                search_string=r'1. .+? tabledata (.+) 2a.', min_length=5,
                                points=5)
    test2a = keyword_and_length('question 2a', [r'[a-zA-Z]+'], text,
                                search_string=r'2a. .+? tabledata (.+) 2b.', min_length=1,
                                points=1)
    test2b = keyword_and_length('question 2b', [r'[a-zA-Z]+'], text,
                                search_string=r'2b. .+? tabledata (.+) 3a', min_length=7, points=1)
    test3a = keyword_and_length('question 3a', [r'32'], text,
                                search_string=r'3a. .+? tabledata (.+) 3b', min_length=1, points=5)
    test3b = keyword_and_length('question 3b', [r'4\s*billion', '2 .+32', '4,*294,*967,*296'], text,
                                search_string=r'3b. .+? tabledata (.+) 4a', min_length=1, points=5)

    test4a = keyword_and_length('question 4a', [r'[a-zA-Z]'], text,
                                search_string=r'4a. .+? tabledata (.+) 4b', min_length=7, points=1)
    test4b = keyword_and_length('question 4b', [r'[a-zA-Z]'], text,
                                search_string=r'4b. .+? tabledata (.+) 5', min_length=7, points=1)
    test5 = keyword_and_length('question 5', [r'[a-zA-Z]+'], text,
                                search_string=r'5. .+? tabledata (.+) 6', min_length=6, points=1)
    test6 = keyword_and_length('question 6', [r'[a-zA-Z]+'], text,
                                search_string=r'6. .+? tabledata (.+) 7', min_length=10, points=1)
    test7 = keyword_and_length('question 7', [r'[a-zA-Z]+'], text,
                                search_string=r'7. .+? tabledata (.+) 8', min_length=5, points=1)
    tests.extend([test1, test2a, test2b, test3a, test3b, test4a, test4b, test5, test6, test7,  ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/python_1020')
def docs_feedback_python_1020():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 39, 'manually_scored': 10, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('question 1 expected', [r'\s1a\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 1b\.\n'],
                          text, points=0.5)
    test1b = exact_answer('question 1 actual', [r'\s1b\. \n+ tabledata \s 9 .+ tabledata \s 1c\.\n'],
                          text, points=0.5)
    test1c = exact_answer('question 1 difference',
                          [r'\s1c\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s print .+ 2a\.'],
                          text, points=0.5)
    test2a = exact_answer('question 2 expected', [r'\s2a\. \n+ tabledata \s [\.a-zA-Z0-9] .+ tabledata \s 2b\.\n'],
                          text, points=0.5)
    test2b = exact_answer('question 2 actual', [r'\s2b\. \n+ tabledata \s 0*\.6+ .+ tabledata \s 2c\.\n'],
                          text, points=0.5)
    test2c = exact_answer('question 2 difference',
                          [r'\s2c\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s print .+ 3a\.'],
                          text, points=0.5)
    test3a = exact_answer('question 3 expected', [r'\s3a\. \n+ tabledata \s [\.a-zA-Z0-9] .+ tabledata \s 3b\.\n'],
                          text, points=0.5)
    test3b = exact_answer('question 3 actual', [r'\s3b\. \n+ tabledata \s 3\.0 .+ tabledata \s 3c\.\n'],
                          text, points=0.5)
    test3c = exact_answer('question 3 difference',
                          [r'\s3c\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s print .+ 4a\.'],
                          text, points=0.5)
    test4a = exact_answer('question 4 expected', [r'\s4a\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 4b\.\n'],
                          text, points=0.5)
    test4b = exact_answer('question 4 actual', [r'\s4b\. \n+ tabledata \s 50 .+ tabledata \s 4c\.\n'],
                          text, points=0.5)
    test4c = exact_answer('question 4 difference',
                          [r'\s4c\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s print .+ 5a\.'],
                          text, points=0.5)
    test5a = exact_answer('question 5 expected', [r'\s5a\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 5b\.\n'],
                          text, points=0.5)
    test5b = exact_answer('question 5 actual', [r'\s5b\. \n+ tabledata \s 2\.0 .+ tabledata \s 5c\.\n'],
                          text, points=0.5)
    test5c = exact_answer('question 5 difference',
                          [r'\s5c\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s print .+ 6a\.'],
                          text, points=0.5)
    test6a = exact_answer('question 6 expected', [r'\s6a\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 6b\.\n'],
                          text, points=0.5)
    test6b = exact_answer('question 6 actual', [r'\s6b\. \n+ tabledata \s 1\.0 .+ tabledata \s 6c\.\n'],
                          text, points=0.5)
    test6c = exact_answer('question 6 difference',
                          [r'\s6c\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s print .+ section'],
                          text, points=0.5)
    test7a = exact_answer('question 7 expected', [r'\s7a\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 7b\.\n'],
                          text, points=0.5)
    test7b = exact_answer('question 7 actual', [r'\s7b\. \n+ tabledata \s error .+ tabledata \s 7c\.\n'],
                          text, points=0.5)
    test7c = exact_answer('question 7 difference',
                          [r'\s7c\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s print .+ 8a\.'],
                          text, points=0.5)
    test8a = exact_answer('question 8 expected', [r'\s8a\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 8b\.\n'],
                          text, points=0.5)
    test8b = exact_answer('question 8 actual', [r'\s8b\. \n+ tabledata \s a .+ tabledata \s 8c\.\n'],
                          text, points=0.5)
    test8c = exact_answer('question 8 difference',
                          [r'\s8c\. \n+ tabledata \s [a-zA-Z0-9] .+? section'],
                          text, points=0.5)
    test9a = exact_answer('question 9 expected', [r'\s9a\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 9b\.\n'],
                          text, points=0.5)
    test9b = exact_answer('question 9 actual', [r'\s9b\. \n+ tabledata \s a \s* \+ \s* b .+ tabledata \s 9c\.\n'],
                          text, points=0.5)
    test9c = exact_answer('question 9 difference',
                          [r'\s9c\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s print .+ 10a\.\n'],
                          text, points=0.5)
    test10a = exact_answer('question 10 expected', [r'\s10a\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 10b\.\n'],
                          text, points=0.5)
    test10b = exact_answer('question 10 actual', [r'\s10b\. \n+ tabledata \s ab .+ tabledata \s 10c\.\n'],
                          text, points=0.5)
    test10c = exact_answer('question 10 difference', [r'\s10c\. \n+ tabledata \s [a-zA-Z0-9] .+ section'],
                          text, points=0.5)
    test11a = exact_answer('question 11 expected', [r'\s11a\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 11b\.\n'],
                           text, points=0.5)
    test11b = exact_answer('question 11 actual', [r'\s11b\. \n+ tabledata \s error .+ tabledata \s 11c\.\n'],
                           text, points=0.5)
    test11c = exact_answer('question 11 difference',
                           [r'\s11c\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s print .+ 12a\.\n'],
                           text, points=0.5)
    test12a = exact_answer('question 12 expected', [r'\s12a\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 12b\.\n'],
                           text, points=0.5)
    test12b = exact_answer('question 12 actual', [r'\s12b\. \n+ tabledata \s aa .+ tabledata \s 12c\.\n'],
                           text, points=0.5)
    test12c = exact_answer('question 12 difference',
                           [r'\s12c\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s .+ part'],
                           text, points=0.5)
    test13a = exact_answer('question 13 expected datatype',
                           [r'\s13a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 13b\.\n'],
                           text, points=0.5)
    test14a = exact_answer('question 14 expected datatype',
                           [r'\s14a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 14b\.\n'],
                           text, points=0.5)
    test15a = exact_answer('question 15 expected datatype',
                           [r'\s15a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 15b\.\n'],
                           text, points=0.5)
    test16a = exact_answer('question 16 expected datatype',
                           [r'\s16a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 16b\.\n'],
                           text, points=0.5)
    test17a = exact_answer('question 17 expected datatype',
                           [r'\s17a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 17b\.\n'],
                           text, points=0.5)
    test18a = exact_answer('question 18 expected datatype',
                           [r'\s18a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 18b\.\n'],
                           text, points=0.5)
    test19a = exact_answer('question 19 expected datatype',
                           [r'\s19a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 19b\.\n'],
                           text, points=0.5)
    test20a = exact_answer('question 20 expected datatype',
                           [r'\s20a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 20b\.\n'],
                           text, points=0.5)
    test21a = exact_answer('question 21 expected datatype',
                           [r'\s21a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 21b\.\n'],
                           text, points=0.5)
    test22a = exact_answer('question 22 expected datatype',
                           [r'\s22a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 22b\.\n'],
                           text, points=0.5)
    test23a = exact_answer('question 23 expected datatype',
                           [r'\s23a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 23b\.\n'],
                           text, points=0.5)
    test24a = exact_answer('question 24 expected datatype',
                           [r'\s24a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 24b\.\n'],
                           text, points=0.5)
    test25a = exact_answer('question 25 expected datatype',
                           [r'\s25a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 25b\.\n'],
                           text, points=0.5)
    test26a = exact_answer('question 26 expected datatype',
                           [r'\s26a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 26b\.\n'],
                           text, points=0.5)
    test13b = exact_answer('question 13 expected', [r'\s13b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 13c\.\n'],
                           text, points=0.5)
    test14b = exact_answer('question 14 expected', [r'\s14b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 14c\.\n'],
                           text, points=0.5)
    test15b = exact_answer('question 15 expected', [r'\s15b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 15c\.\n'],
                           text, points=0.5)
    test16b = exact_answer('question 16 expected', [r'\s16b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 16c\.\n'],
                           text, points=0.5)
    test17b = exact_answer('question 17 expected', [r'\s17b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 17c\.\n'],
                           text, points=0.5)
    test18b = exact_answer('question 18 expected', [r'\s18b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 18c\.\n'],
                           text, points=0.5)
    test19b = exact_answer('question 19 expected', [r'\s19b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 19c\.\n'],
                           text, points=0.5)
    test20b = exact_answer('question 20 expected', [r'\s20b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 20c\.\n'],
                           text, points=0.5)
    test21b = exact_answer('question 21 expected', [r'\s21b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 21c\.\n'],
                           text, points=0.5)
    test22b = exact_answer('question 22 expected', [r'\s22b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 22c\.\n'],
                           text, points=0.5)
    test23b = exact_answer('question 23 expected', [r'\s23b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 23c\.\n'],
                           text, points=0.5)
    test24b = exact_answer('question 24 expected', [r'\s24b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 24c\.\n'],
                           text, points=0.5)
    test25b = exact_answer('question 25 expected', [r'\s25b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 25c\.\n'],
                           text, points=0.5)
    test26b = exact_answer('question 26 expected', [r'\s26b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 26c\.\n'],
                           text, points=0.5)
    test13c = exact_answer('question 13 actual',
                           [r'\s13c\. \n+ tabledata \s  5\.0 .+? tabledata \s 14a\.\n'],
                           text, points=0.5)
    test14c = exact_answer('question 14 actual',
                           [r'\s14c\. \n+ tabledata \s  0 .+? tabledata \s 15a\.\n'],
                           text, points=0.5)
    test15c = exact_answer('question 15 actual',
                           [r'\s15c\. \n+ tabledata \s  8 .+? tabledata \s 16a\.\n'],
                           text, points=0.5)
    test16c = exact_answer('question 16 actual',
                           [r'\s16c\. \n+ tabledata \s  21 .+? tabledata \s 17a\.\n'],
                           text, points=0.5)
    test17c = exact_answer('question 17 actual',
                           [r'\s17c\. \n+ tabledata \s  17 .+? tabledata \s 18a\.\n'],
                           text, points=0.5)
    test18c = exact_answer('question 18 actual',
                           [r'\s18c\. \n+ tabledata \s  ab123 .+? tabledata \s 19a\.\n'],
                           text, points=0.5)
    test19c = exact_answer('question 19 actual',
                           [r'\s19c\. \n+ tabledata \s  error .+? tabledata \s 20a\.\n'],
                           text, points=0.5)
    test20c = exact_answer('question 20 actual',
                           [r'\s20c\. \n+ tabledata \s  abcd .+? tabledata \s 21a\.\n'],
                           text, points=0.5)
    test21c = exact_answer('question 21 actual',
                           [r'\s21c\. \n+ tabledata \s  abcabc .+? tabledata \s 22a\.\n'],
                           text, points=0.5)
    test22c = exact_answer('question 22 actual',
                           [r'\s22c\. \n+ tabledata \s 11222 .+? tabledata \s 23a\.\n'],
                           text, points=0.5)
    test23c = exact_answer('question 23 actual',
                           [r'\s23c\. \n+ tabledata \s error .+? tabledata \s 24a\.\n'],
                           text, points=0.5)
    test24c = exact_answer('question 24 actual',
                           [r'\s24c\. \n+ tabledata \s error .+? tabledata \s 25a\.\n'],
                           text, points=0.5)
    test25c = exact_answer('question 25 actual',
                           [r'\s25c\. \n+ tabledata \s error .+? tabledata \s 26a\.\n'],
                           text, points=0.5)
    test26c = exact_answer('question 26 actual',
                           [r'\s26c\. \n+ tabledata \s error .+? $'],
                           text, points=0.5)
    tests.extend([test1a, test1b, test1c, test2a, test2b, test2c, test3a, test3b, test3c, test4a, test4b, test4c,
                  test5a, test5b, test5c, test6a, test6b, test6c, test7a, test7b, test7c, test8a, test8b, test8c,
                  test9a, test9b, test9c, test10a, test10b, test10c, test11a, test11b, test11c,
                  test12a, test12b, test12c, test13a, test13b, test13c, test14a, test14b, test14c, test15a, test15b,
                  test15c, test16a, test16b, test16c, test17a, test17b, test17c, test18a, test18b, test18c, test19a,
                  test19b, test19c, test20a, test20b, test20c, test21a, test21b, test21c, test22a, test22b, test22c,
                  test23a, test23b, test23c, test24a, test24b, test24c, test25a,
                  test25b, test25c, test26a, test26b, test26c, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/python_1030')
def docs_feedback_python_1030():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 29.5, 'manually_scored': 8, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('question 1a expected',
                         [r'\s1a\. \n+ tabledata \s [a-zA-Z\.0-9] .+? tabledata \s 1b\.\n'],
                         text, points=0.5)
    test2a = exact_answer('question 2a expected',
                         [r'\s2a\. \n+ tabledata \s [a-zA-Z\.0-9] .+? tabledata \s 2b\.\n'],
                         text, points=0.5)
    test3a = exact_answer('question 3a expected',
                         [r'\s3a\. \n+ tabledata \s [a-zA-Z\.0-9] .+? tabledata \s 3b\.\n'],
                         text, points=0.5)
    test4a = exact_answer('question 4a expected',
                         [r'\s4a\. \n+ tabledata \s [a-zA-Z\.0-9] .+? tabledata \s 4b\.\n'],
                         text, points=0.5)
    test5a = exact_answer('question 5a expected',
                         [r'\s5a\. \n+ tabledata \s [a-zA-Z\.0-9] .+? tabledata \s 5b\.\n'],
                         text, points=0.5)
    test1b = exact_answer('question 1b actual', [r'\s1b\. \n+ tabledata \s  1 .+? tabledata \s 1c\.\n'],
                          text, points=0.5)
    test2b = exact_answer('question 2b actual', [r'\s2b\. \n+ tabledata \s  1 .+? tabledata \s 2c\.\n'],
                          text, points=0.5)
    test3b = exact_answer('question 3b actual', [r'\s3b\. \n+ tabledata \s  3 .+? tabledata \s 3c\.\n'],
                          text, points=0.5)
    test4b = exact_answer('question 4b actual', [r'\s4b\. \n+ tabledata \s  12 .+? tabledata \s 4c\.\n'],
                          text, points=0.5)
    test5b = exact_answer('question 5b actual',
                          [r'\s5b\. \n+ tabledata \s  this \s is \s a \s sentence\. .+? tabledata \s 5c\.\n'],
                          text, points=0.5)
    test1c = exact_answer('question 1c different', [r'\s1c\. \n+ tabledata \s [a-zA-Z0-9\.] .+? tabledata \s 2a\.\n'],
                          text, points=0.5)
    test2c = exact_answer('question 2c different', [r'\s2c\. \n+ tabledata \s [a-zA-Z0-9\.] .+? tabledata \s 3a\.\n'],
                          text, points=0.5)
    test3c = exact_answer('question 3c different', [r'\s3c\. \n+ tabledata \s [a-zA-Z0-9\.] .+? tabledata \s 4a\.\n'],
                          text, points=0.5)
    test4c = exact_answer('question 4c different', [r'\s4c\. \n+ tabledata \s [a-zA-Z0-9\.] .+? tabledata \s 5a\.\n'],
                          text, points=0.5)
    test5c = exact_answer('question 5c different', [r'\s5c\. \n+ tabledata \s [a-zA-Z0-9\.] .+? part'],
                          text, points=0.5)
    test6a = exact_answer('question 6a', [r'\s6a\. .+? \n+ tabledata \s dogs \s are \s really \s cool .+? 6b\.'],
                          text, points=5)
    test7a = exact_answer('question 7a', [r'\s7a\. .+? \n+ tabledata \s error .+? 7b\.'],
                          text, points=5)
    test6b = keyword_and_length('question 6b', [r'[a-zA-Z]+'], text,
                                search_string=r'\s6b\. .+? tabledata (.+) 7a\.', min_length=5, points=1)
    test7b = keyword_and_length('question 7b', [r'[a-zA-Z]+'], text,
                                search_string=r'\s7b\. .+? tabledata (.+) 8\.', min_length=5, points=1)
    test8a = keyword_and_length('question 8a', [r'number \s* = \s* 100'], text,
                                search_string=r'\s8\. .+? tabledata (.+) create\sa\svariable', min_length=5, points=2.5)
    test8b = keyword_and_length('question 8b', [r'print \s* \(number\)'], text,
                                search_string=r'\s8\. .+? tabledata (.+) create\sa\svariable', min_length=5, points=2.5)
    test8c = keyword_and_length('question 8c', [r'number2 .+? 100'], text,
                                search_string=r'\s8\. .+? tabledata (.+) create\sa\svariable', min_length=5, points=2.5)
    test8d = keyword_and_length('question 8d', [r'print \s* \(number2\)'], text,
                                search_string=r'\s8\. .+? tabledata (.+) create\sa\svariable', min_length=5, points=2.5)


    tests.extend([test1a, test1b, test1c, test2a, test2b, test2c, test3a, test3b, test3c, test4a, test4b, test4c,
                  test5a, test5b, test5c, test6a, test6b, test7a, test7b, test8a, test8b, test8c, test8d])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/docs_routers_and_redundancy')
def docs_feedback_routers_and_redundancy():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 11, 'manually_scored': 39, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)
    print(text)
    test1 = keyword_and_length('question 1', [r'[a-zA-Z]+'], text,
                               search_string=r'1. .+? tabledata (.+) 2.', min_length=1,
                               points=1)
    test2 = keyword_and_length('question 2', [r'[a-zA-Z]+'], text,
                               search_string=r'2. .+? tabledata (.+) 3.', min_length=5,
                               points=1)
    test3 = keyword_and_length('question 3', [r'[a-zA-Z]+'], text,
                               search_string=r'3. .+? tabledata (.+) 4.', min_length=1,
                               points=1)
    test4 = keyword_and_length('question 4', [r'[a-zA-Z]+'], text,
                               search_string=r'4. .+? tabledata (.+) Find', min_length=10,
                               points=1)
    test5 = keyword_and_length('question 5', [r'[a-zA-Z]+'], text,
                               search_string=r'5. .+? tabledata (.+) 6.', min_length=1,
                               points=1)
    test6 = keyword_and_length('question 6', [r'[a-zA-Z]+'], text,
                               search_string=r'6. .+? tabledata (.+) 7.', min_length=10,
                               points=1)
    test7 = keyword_and_length('question 7', [r'[a-zA-Z]+'], text,
                               search_string=r'7. .+? tabledata (.+) 8.', min_length=5,
                               points=1)
    test8 = keyword_and_length('question 8', [r'[a-zA-Z]+'], text,
                               search_string=r'8. .+? tabledata (.+) 9.', min_length=5,
                               points=1)
    test9 = keyword_and_length('question 9', [r'[a-zA-Z]+'], text,
                               search_string=r'9. .+? tabledata (.+) 10a.', min_length=5,
                               points=1)
    test10a = keyword_and_length('question 10a', [r'[a-zA-Z]+'], text,
                                 search_string=r'10a. .+? tabledata (.+) 10b.', min_length=5,
                                 points=1)
    test10b = keyword_and_length('question 10b', [r'[a-zA-Z]+'], text,
                                 search_string=r'10b. .+? tabledata (.+) $', min_length=10,
                                 points=1)

    tests.extend([test1, test2, test3, test4, test5, test6, test7, test8, test9, test10a, test10b])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/docs_feedback_scratch_25_alternate')
def docs_feedback_scratch_25_alternate():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 12, 'manually_scored': 0, 'finished_scoring': True}

    print(request.args)
    link = request.args['link']
    text = get_text(link)
    print(text)
    test1a = exact_answer('question 1a', [r'1a .+? tabledata \s*  (true|True|t|T) \s* tabledata \s 1b'], text, points=1)
    test1b = exact_answer('question 1b', [r'1b .+? tabledata \s*  (false|False|f|F) \s* tabledata \s 1c'], text, points=1)
    test1c = exact_answer('question 1c', [r'1c .+? tabledata \s*  (true|True|t|T) \s* tabledata \s 1d'], text, points=1)
    test1d = exact_answer('question 1d', [r'1d .+? tabledata \s*  (true|True|t|T) \s* Fill '], text, points=1)
    test2a = exact_answer('question 2a', [r'2a .+? tabledata \s*  (true|True|t|T) \s* tabledata \s 2b'], text, points=1)
    test2b = exact_answer('question 2b', [r'2b .+? tabledata \s*  (false|False|f|F) \s* tabledata \s 2c'], text, points=1)
    test2c = exact_answer('question 2c', [r'2c .+? tabledata \s*  (true|True|t|T) \s* tabledata \s 2d'], text, points=1)
    test2d = exact_answer('question 2d', [r'2d .+? tabledata \s*  (false|False|f|F) \s* Fill '], text, points=1)
    test3a = exact_answer('question 2a', [r'3a .+? tabledata \s*  (false|False|f|F) \s* tabledata \s 3b'], text, points=1)
    test3b = exact_answer('question 2b', [r'3b .+? tabledata \s*  (true|True|t|T) \s* tabledata \s 3c'], text, points=1)
    test3c = exact_answer('question 2c', [r'3c .+? tabledata \s*  (true|True|t|T) \s* tabledata \s 3d'], text, points=1)
    test3d = exact_answer('question 2d', [r'3d .+? tabledata \s*  (true|True|t|T) \s*  '], text, points=1)

    tests.extend([test1a, test1b, test1c, test1d, test2a, test2b, test2c, test2d, test3a, test3b, test3c, test3d])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/docs_feedback_scratch_12')
def docs_feedback_scratch_12():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 38, 'manually_scored': 12, 'finished_scoring': True}

    print(request.args)
    link = request.args['link']
    text = get_text(link)
    print(text)
    test1b2 = exact_answer('question 1 b2', [r'b\.AAA\sINLINEOBJECT\ntabledata?\s*looks?'], text, points=1)
    test1b3 = keyword_and_length('question 1 b3', ['say', 'seconds', 'time', 'text', 'bubble'], text,
                                 search_string=r'b\.AAA\sINLINEOBJECT\n .+? tabledata?\s* (.+?)tabledata',  points=1)
    test1c2 = exact_answer('question 1 c2', [r'c\.AAA\sINLINEOBJECT\ntabledata?\s*sound?'], text, points=1)
    test1c3 = keyword_and_length('question 1 c3', ['play', 'sound', 'meow'], text,
                                 search_string=r'c\.AAA\sINLINEOBJECT\n .+? tabledata?\s* (.+?)tabledata',  points=1)
    test1d2 = exact_answer('question 1 d2', [r'd\.AAA\sINLINEOBJECT\ntabledata?\s*looks?'], text, points=1)
    test1d3 = keyword_and_length('question 1 d3', ['costume', 'switch', 'look'], text,
                                 search_string=r'd\.AAA\sINLINEOBJECT\n .+? tabledata?\s* (.+?)tabledata',  points=1)
    test1e2 = exact_answer('question 1 e2', [r'e\.AAA\sINLINEOBJECT\ntabledata?\s*motion?'], text, points=1)
    test1e3 = keyword_and_length('question 1 e3', ['move', 'glide', 'location', 'smooth', 'slow'], text,
                                 search_string=r'e\.AAA\sINLINEOBJECT\n .+? tabledata?\s* (.+?)tabledata',  points=1)
    test1f2 = exact_answer('question 1 f2', [r'f\.AAA\sINLINEOBJECT\ntabledata?\s*looks?'], text, points=1)
    test1f3 = keyword_and_length('question 1 f3', ['size', 'change', 'size',], text,
                                 search_string=r'f\.AAA\sINLINEOBJECT\n .+? tabledata?\s* (.+?)tabledata', points=1)
    test1g2 = exact_answer('question 1 g2', [r'g\.AAA\sINLINEOBJECT\ntabledata?\s*control?'], text, points=1)
    test1g3 = keyword_and_length('question 1 g3', ['repeat', 'control', ], text,
                                 search_string=r'g\.AAA\sINLINEOBJECT\n .+? tabledata?\s* (.+?)tabledata', points=1)
    test1h2 = exact_answer('question 1 h2', [r'h\.AAA\sINLINEOBJECT\ntabledata?\s*looks?'], text, points=1)
    test1h3 = keyword_and_length('question 1 h3', ['color', 'sprite', 'change', ], text,
                                 search_string=r'h\.AAA\sINLINEOBJECT\n .+? tabledata?\s* (.+?)tabledata', points=1)
    test1i2 = exact_answer('question 1 i2', [r'i\.AAA\sINLINEOBJECT\ntabledata?\s*motion?'], text, points=1)
    test1i3 = keyword_and_length('question 1 i3', ['move', 'go', 'location', ], text,
                                 search_string=r'i\.AAA\sINLINEOBJECT\n .+? tabledata?\s* (.+?)tabledata', points=1)
    test1j2 = exact_answer('question 1 j2', [r'j\.AAA\sINLINEOBJECT\n.+?tabledata?\s*pen?'], text, points=1)
    test1j3 = keyword_and_length('question 1 j3', ['pen', 'change', 'size', ], text,
                                 search_string=r'j\.AAA\sINLINEOBJECT\n .+? tabledata?\s* (.+?)tabledata\sk', points=1)
    test1k2 = exact_answer('question 1 k2', [r'k\.AAA\sINLINEOBJECT\ntabledata?\s*pen?'], text, points=1)
    test1k3 = keyword_and_length('question 1 k3', ['pen', 'change', 'color', 'set'], text,
                                 search_string=r'k\.AAA\sINLINEOBJECT\n .+? tabledata?\s* (.+?)tabledata\sl', points=1)
    test1l2 = exact_answer('question 1 l2', [r'l\.AAA\sINLINEOBJECT\ntabledata?\s*motion?'], text, points=1)
    test1l3 = keyword_and_length('question 1 l3', ['point', 'sprite', 'mouse'], text,
                                 search_string=r'l\.AAA\sINLINEOBJECT\n .+? tabledata?\s* (.+?)2', points=1)
    test2a = keyword_and_length('question 2a', ['motion', 'move', 'moving', 'category', 'speed', 'way', 'blocks',
                                                'glide', 'turn', 'go', 'set', 'sprite'], text,
                                search_string=r'tabledata\sa\.\sWhat\sdo\sthe\sblocks\sin\sthe\s'
                                              r'Motion\scategory\sdo\?\s+You\smay\swant\sto\sgive\ssome\sexamples\sof\s'
                                              r'what\syou\scan\sdo\.\ntabledata (.+?) tabledata',
                                points=4, min_matches=2)
    test2b = keyword_and_length('question 2b', ['look', 'appearance', 'effect', 'talk', 'say', 'disappear',
                                                'category', 'blocks',
                                                'set', 'sprite'], text,
                                search_string=r'tabledata\sb\.\sWhat\sdo\sthe\sblocks\sin\sthe\s'
                                              r'Looks\scategory\sdo\?\s+You\smay\swant\sto\sgive\ssome\sexamples\sof\s'
                                              r'what\syou\scan\sdo\.\ntabledata (.+?) tabledata',
                                points=4, min_matches=2)
    test2c = keyword_and_length('question 2c', ['noise', 'sound', 'music', 'effect', 'cat', 'meow',
                                                'category', 'blocks',
                                                'set', 'sprite'], text,
                                search_string=r'tabledata\sc\.\sWhat\sdo\sthe\sblocks\sin\sthe\s'
                                              r'Sound\scategory\sdo\?\s+You\smay\swant\sto\sgive\ssome\sexamples\sof\s'
                                              r'what\syou\scan\sdo\.\ntabledata (.+?) tabledata',
                                points=4, min_matches=2)
    test2d = keyword_and_length('question 2d', ['tools', 'pen', 'thickness', 'color', 'size', 'erase', 'clear', 'draw'
                                                'sprite'], text,
                                search_string=r'tabledata\sd\.\sWhat\sdo\sthe\sblocks\sin\sthe\s'
                                              r'Pen\scategory\sdo\?\s+You\smay\swant\sto\sgive\ssome\sexamples\sof\s'
                                              r'what\syou\scan\sdo\.\ntabledata (.+)',
                                points=4, min_matches=2)
    tests.extend([test1b2, test1b3, test1c2, test1c3, test1d2, test1d3, test1e2, test1e3, test1f2, test1f3, test1g2,
                  test1g3, test1h2, test1h3, test1i2, test1i3, test1j2, test1j3, test1k2, test1k3, test1l2, test1l3,
                  test2a, test2b, test2c, test2d])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/docs_feedback_privacy_policies')
def docs_feedback_privacy_policies():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 11, 'manually_scored': 39, 'finished_scoring': True}

    print(request.args)
    link = request.args['link']
    text = get_text(link)
    test_website = keyword_and_length('Website?', [r'[a-zA-Z]+'], text,
                                      search_string=r'Your\swebsite\: .+? tabledata (.+) What', min_length=4, points=1)
    test1a = keyword_and_length('question 1a', [r'[a-zA-Z]+'], text,
                                search_string=r'1a. .+? tabledata (.+) 1b', min_length=4, points=1)
    test1b = keyword_and_length('question 1b', [r'[a-zA-Z]+'], text,
                                search_string=r'1b. .+? tabledata (.+) 2a', min_length=4, points=1)
    test2a = keyword_and_length('question 2a', [r'[a-zA-Z]+'], text,
                                search_string=r'2a. .+? tabledata (.+) 2b', min_length=4, points=1)
    test2b = keyword_and_length('question 2b', [r'[a-zA-Z]+'], text,
                                search_string=r'2b. .+? tabledata (.+) 3a', min_length=4, points=1)
    test3a = keyword_and_length('question 3a', [r'[a-zA-Z]+'], text,
                                search_string=r'3a. .+? tabledata (.+) 3b', min_length=4, points=1)
    test3b = keyword_and_length('question 3b', [r'[a-zA-Z]+'], text,
                                search_string=r'3b. .+? tabledata (.+) 4a', min_length=4, points=1)
    test4a = keyword_and_length('question 4a', [r'[a-zA-Z]+'], text,
                                search_string=r'4a. .+? tabledata (.+) 4b', min_length=4, points=1)
    test4b = keyword_and_length('question 4b', [r'[a-zA-Z]+'], text,
                                search_string=r'4b. .+? tabledata (.+) 5a', min_length=4, points=1)
    test5a = keyword_and_length('question 5a', [r'[0-4]+'], text,
                                search_string=r'5a. .+? tabledata  (.+?) tabledata ', min_length=1, points=1)
    test5b = keyword_and_length('question 5b', [r'[a-zA-Z]+'], text,
                                search_string=r'5b. .+? tabledata (.+) Verify', min_length=10, points=1)
    tests.extend([test_website, test1a, test1b, test2a, test2b, test3a, test3b, test4a, test4b, test5a, test5b])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/docs_feedback_research_yourself')
def docs_feedback_research_yourself():
    from app.docs_labs.docs import get_text, keyword_and_length

    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 5, 'manually_scored': 39, 'finished_scoring': True}

    print(request.args)
    link = request.args['link']
    text = get_text(link)
    print(text)
    test_info = keyword_and_length('Info', [r'[a-zA-Z]+'], text,
                                   search_string=r'Where\syou\sfound\sit\ntabledata (.+?) tabledata', min_length=4,
                                   points=1)
    test_where = keyword_and_length('Where you found it', [r'[a-zA-Z]+'], text,
                                    search_string=r'Where\syou\sfound\sit\ntabledata .+? tabledata (.+?) 2a',
                                    min_length=4, points=1)
    test2a = keyword_and_length('2a connect the dots', [r'[a-zA-Z]+'], text,
                                search_string=r'2a. .+? tabledata (.+) 3a', min_length=4, points=1)
    test3a = keyword_and_length('3a biggest threat to security', [r'[a-zA-Z]+'], text,
                                search_string=r'3a. .+? tabledata (.+) 3b', min_length=4, points=1)
    test3b = keyword_and_length('3b Why do you think so', [r'[a-zA-Z]+'], text,
                                search_string=r'3b. .+? tabledata (.+) ', min_length=4, points=1)
    tests.extend([test_info, test_where, test2a, test3a, test3b])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/scratch/scratch_feedback_13')
def scratch_feedback_13():
    from app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help, arrange_blocks
    from app.scratch_labs.scratch_1_3 import press_zero, press_one, press_two, press_four, press_five

    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 65, 'manually_scored': 15, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = scratch_filename_test(filename, '1.3')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        scripts = arrange_blocks(json_data)
        test_zero = press_zero(scripts, 10)
        tests.append(test_zero)
        if test_zero['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            test_one = press_one(scripts, 10)
            tests.append(test_one)
            test_two = press_two(scripts, 10)
            tests.append(test_two)
            test_four = press_four(scripts, 15)
            tests.append(test_four)
            test_five = press_five(scripts, 15)
            tests.append(test_five)
            test_help = find_help(json_data, 5)
            tests.append(test_help)
            score_info['finished_scoring'] = True
            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/scratch/scratch_feedback_14_15')
def scratch_feedback_14_15():
    from app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help, arrange_blocks, \
        match_string, every_sprite_green_flag, every_sprite_broadcast_and_receive
    from app.scratch_labs.scratch_1_4_1_5 import min_two_sprites, show_and_hide
    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 45, 'manually_scored': 35, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = scratch_filename_test(filename, '1.4_1.5')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        scripts = arrange_blocks(json_data)
        test_num_sprites = min_two_sprites(json_data, 5)
        tests.append(test_num_sprites)
        test_green_flag = every_sprite_green_flag(json_data, 5)
        tests.append(test_green_flag)
        test_broadcast_receive = every_sprite_broadcast_and_receive(json_data, 10)
        tests.append(test_broadcast_receive)
        if test_broadcast_receive['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            test_find_move = match_string(r'motion_movesteps', scripts, points=5)
            if test_find_move['pass'] is False:
                test_find_move['fail_message'] += 'At least one of the sprites should move. <br>'
            tests.append(test_find_move)
            test_find_rotate = match_string(r'(motion_turnleft|motion_turnright)', scripts, points=5)
            if test_find_rotate['pass'] is False:
                test_find_rotate['fail_message'] += 'At least one of the sprites should rotate. <br>'
            tests.append(test_find_rotate)
            test_change_costume = match_string(r'(looks_nextcostume|looks_switchcostumeto)', scripts, points=5)
            if test_change_costume['pass'] is False:
                test_change_costume['fail_message'] += 'At least one of the sprites should change a costume. <br>'
            tests.append(test_change_costume)
            test_show_and_hide = show_and_hide(scripts, 5)
            tests.append(test_show_and_hide)

            test_help = find_help(json_data, 5)
            tests.append(test_help)
            score_info['finished_scoring'] = True
            for test in tests:
                if test['pass']:
                        score_info['score'] += test['points']
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/scratch/scratch_feedback_1x_family_migration_story')
def scratch_feedback_1x_family_migration_story():
    from app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help, arrange_blocks, \
        match_string, every_sprite_green_flag, every_sprite_broadcast_and_receive
    from app.scratch_labs.scratch_1_4_1_5 import min_two_sprites, show_and_hide
    from app.scratch_labs.scratch_1x_family_migration_story import min_two_stages
    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 40, 'manually_scored': 40, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = scratch_filename_test(filename, '1.x_family_migration_story')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        scripts = arrange_blocks(json_data)
        test_num_sprites = min_two_sprites(json_data, 5)
        tests.append(test_num_sprites)
        test_green_flag = every_sprite_green_flag(json_data, 4)
        tests.append(test_green_flag)
        test_broadcast_receive = every_sprite_broadcast_and_receive(json_data, 5)
        tests.append(test_broadcast_receive)
        if test_broadcast_receive['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            test_find_move = match_string(r'motion_movesteps', scripts, points=4)
            if test_find_move['pass'] is False:
                test_find_move['fail_message'] += 'At least one of the sprites should move. <br>'
            tests.append(test_find_move)
            test_find_rotate = match_string(r'(motion_turnleft|motion_turnright)', scripts, points=4)
            if test_find_rotate['pass'] is False:
                test_find_rotate['fail_message'] += 'At least one of the sprites should rotate. <br>'
            tests.append(test_find_rotate)
            test_change_costume = match_string(r'(looks_nextcostume|looks_switchcostumeto)', scripts, points=4)
            if test_change_costume['pass'] is False:
                test_change_costume['fail_message'] += 'At least one of the sprites should change a costume. <br>'
            tests.append(test_change_costume)
            test_show_and_hide = show_and_hide(scripts, 4)
            tests.append(test_show_and_hide)
            test_change_stage = min_two_stages(json_data, 5)
            tests.append(test_change_stage)
            test_help = find_help(json_data, 5)
            tests.append(test_help)
            score_info['finished_scoring'] = True
            for test in tests:
                if test['pass']:
                        score_info['score'] += test['points']
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/scratch/scratch_feedback_22')
def scratch_feedback_22():
    from app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help, arrange_blocks,\
         arrange_blocks_v2
    from app.scratch_labs.scratch_2_2 import press_zero, press_one, press_two, press_three, press_four

    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 70, 'manually_scored': 10, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = scratch_filename_test(filename, '2.2')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        scripts = arrange_blocks_v2(json_data)
        print("scripts {}".format(scripts))
        test_zero = press_zero(scripts, 15)
        tests.append(test_zero)
        if test_zero['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            test_one = press_one(scripts, 10)
            tests.append(test_one)
            test_two = press_two(scripts, 10)
            tests.append(test_two)
            test_three = press_three(scripts, 15)
            tests.append(test_three)
            test_four = press_four(scripts, 15)
            tests.append(test_four)
            test_help = find_help(json_data, 5)
            tests.append(test_help)
            score_info['finished_scoring'] = True
            for test in tests:
                if test['pass']:
                        score_info['score'] += test['points']
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/scratch/scratch_feedback_24_alternate')
def scratch_feedback_24_alternate():
    from app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help,\
        find_variable, find_question, find_set_variable, arrange_blocks_v2, match_string
    from app.scratch_labs.scratch_2_4_alternate import green_flag, test_color_change, one_question, two_question, \
        name_variable_x4, color_variables
    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 70, 'manually_scored': 10, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = scratch_filename_test(filename, '2.4_alternate')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        scripts = arrange_blocks_v2(json_data)
        print("scripts {}".format(scripts))
        test_question = find_question(json_data, 'name', 5)
        tests.append(test_question)
        test_name = find_variable(json_data, 'name', 5)
        tests.append(test_name)
        if test_name['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            test_flag = green_flag(scripts, 5)
            tests.append(test_flag)
            test_name_variable = find_set_variable(json_data, 'name', 'answer', points=5)
            tests.append(test_name_variable)
            test_question_color = find_question(json_data, 'color', 5)
            tests.append(test_question_color)
            test_color = find_variable(json_data, 'color', 5)
            tests.append(test_color)
            test_color_variable = color_variables(scripts, 5)
            tests.append(test_color_variable)
            test_stage = test_color_change(scripts, 5)
            tests.append(test_stage)
            test_q1 = one_question(scripts, 10)
            tests.append(test_q1)
            test_q2 = two_question(scripts, 10)
            tests.append(test_q2)
            test_name_usage = name_variable_x4(scripts, 5)
            tests.append(test_name_usage)
            test_help = find_help(json_data, 5)
            tests.append(test_help)
            score_info['finished_scoring'] = True
            for test in tests:
                if test['pass']:
                        score_info['score'] += test['points']
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/scratch/scratch_feedback_25_alternate')
def scratch_feedback_25_alternate():
    from app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help, \
         find_question, arrange_blocks_v2
    from app.scratch_labs.scratch_2_4_alternate import green_flag
    from app.scratch_labs.scratch_2_5_alternate import test_prizes, test_prizes_defined, any_conditional, four_prizes, \
        no_if_if, find_else
    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 46, 'manually_scored': 10, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = scratch_filename_test(filename, '2.5_alternate')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        scripts = arrange_blocks_v2(json_data)
        print("scripts {}".format(scripts))
        test_question = find_question(json_data, 'door', 6)
        tests.append(test_question)
        test_prize_variables = test_prizes(json_data, 5)
        tests.append(test_prize_variables)
        if test_prize_variables['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            test_prize_values = test_prizes_defined(scripts, 5)
            tests.append(test_prize_values)
            test_flag = green_flag(scripts, 5)
            tests.append(test_flag)
            test_conditional = any_conditional(scripts, 5)
            tests.append(test_conditional)
            test_four = four_prizes(scripts, 5)
            tests.append(test_four)
            test_efficient = no_if_if(scripts, 5)
            tests.append(test_efficient)
            test_else = find_else(scripts, 5)
            tests.append(test_else)
            test_help = find_help(json_data, 5)
            tests.append(test_help)
            score_info['finished_scoring'] = True
            for test in tests:
                if test['pass']:
                        score_info['score'] += test['points']
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/scratch/scratch_feedback_26')
def scratch_feedback_26():
    from app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help, \
         arrange_blocks_v2
    from app.scratch_labs.scratch_2_6 import green_flag, test_top_1, test_fall, test_hit_ground, test_random_x, \
        platform_or_ground
    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 70, 'manually_scored': 10, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = scratch_filename_test(filename, '2.6')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        scripts = arrange_blocks_v2(json_data)
        print("scripts {}".format(scripts))
        test_flag = green_flag(scripts, 15)
        tests.append(test_flag)
        test_top_1 = test_top_1(scripts, 10)
        tests.append(test_top_1)
        if test_top_1['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            test_falling = test_fall(scripts, 10)
            tests.append(test_falling)
            test_ground = test_hit_ground(scripts, 20)
            tests.append(test_ground)
            test_x = test_random_x(scripts, 5)
            tests.append(test_x)
            test_both = platform_or_ground(scripts, 5)
            tests.append(test_both)
            test_help = find_help(json_data, 5)
            tests.append(test_help)

            score_info['finished_scoring'] = True
            for test in tests:
                if test['pass']:
                        score_info['score'] += test['points']
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/scratch/scratch_feedback_32_alternate')
def scratch_feedback_32_alternate():
    from app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help, arrange_blocks_v2
    from app.scratch_labs.scratch_3_2_alternate import press_zero, press_one, press_two, press_three, press_four, \
        find_make_triangle, find_happy_birthday, make_triangle_works, happy_birthday_works
    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 50, 'manually_scored': 10, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = scratch_filename_test(filename, '3.2_alternate')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        scripts = arrange_blocks_v2(json_data)
        test_zero = press_zero(json_data, 5)
        tests.append(test_zero)
        if test_zero['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            test_one = press_one(scripts, 5)
            tests.append(test_one)
            test_two = press_two(scripts, 5)
            tests.append(test_two)
            test_procedure_triangle = find_make_triangle(scripts, 5)
            tests.append(test_procedure_triangle)
            test_triangle_works = make_triangle_works(scripts, 5)
            tests.append(test_triangle_works)
            test_press_three = press_three(scripts, 5)
            tests.append(test_press_three)
            test_find_happy_birthday = find_happy_birthday(scripts, 5)
            tests.append(test_find_happy_birthday)
            test_happy_birthday_works = happy_birthday_works(scripts, 5)
            tests.append(test_happy_birthday_works)
            test_press_four = press_four(scripts, 5)
            tests.append(test_press_four)
            test_find_help = find_help(json_data, 5)
            tests.append(test_find_help)
            score_info['finished_scoring'] = True
            for test in tests:
                if test['pass']:
                        score_info['score'] += test['points']
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/scratch/scratch_feedback_33_34_alternate')
def scratch_feedback_33_34_alternate():
    from app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help, arrange_blocks_v2
    from app.scratch_labs.scratch_3_3_3_4_alternate import find_day_of_week, day_of_week_works, if_ifelse, \
        find_min, find_between, min_works, minif_ifelse, between_works_equal, between_works_unequal
    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 70, 'manually_scored': 10, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = scratch_filename_test(filename, '3.3_3.4_alternate')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        scripts = arrange_blocks_v2(json_data)
        print('scripts')
        for key in scripts:
                print("key {}  script {} ".format(key, scripts[key]))
        test_find_day_of_week = find_day_of_week(scripts, 5)
        tests.append(test_find_day_of_week)
        test_day_of_week_works = day_of_week_works(scripts, 5)
        tests.append(test_day_of_week_works)
        test_if_ifelse = if_ifelse(scripts, 5)
        tests.append(test_if_ifelse)
        test_find_min = find_min(scripts, 5)
        tests.append(test_find_min)
        test_min_works = min_works(scripts, 15)
        tests.append(test_min_works)
        test_minif_ifelse = minif_ifelse(scripts, 5)
        tests.append(test_minif_ifelse)
        test_find_between = find_between(scripts, 5)
        tests.append(test_find_between)
        test_between_works_equal = between_works_equal(scripts, 10)
        tests.append(test_between_works_equal)
        test_between_works_unequal = between_works_unequal(scripts, 10)
        tests.append(test_between_works_unequal)
        test_help = find_help(json_data, 5)
        tests.append(test_help)
        score_info['finished_scoring'] = True
        for test in tests:
            if test['pass']:
                    score_info['score'] += test['points']
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/scratch/scratch_feedback_42_alternate')
def scratch_feedback_42_alternate():
    from app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help, arrange_blocks_v2
    from app.scratch_labs.scratch_4_2 import find_all_lists, find_all_lists_min_items, find_smash_in, \
        find_sundae_and_fancy_sundae, smash_in_works_random, smash_in_works_spacing, sundae_fancy_sundae_works,\
        add_icecreams_works, add_dry_toppings_and_wet_toppings_works, delete_two_questions, delete_works
    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 70, 'manually_scored': 10, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = scratch_filename_test(filename, '4.2_alternate')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        scripts = arrange_blocks_v2(json_data)
        test_find_all_lists = find_all_lists(json_data, 5)
        tests.append(test_find_all_lists)
        test_find_all_lists_min_items = find_all_lists_min_items(json_data, 5)
        tests.append(test_find_all_lists_min_items)
        test_find_smash_in = find_smash_in(scripts, 5)
        tests.append(test_find_smash_in)
        test_find_sundae_and_fancy_sundae = find_sundae_and_fancy_sundae(scripts, 5)
        tests.append(test_find_sundae_and_fancy_sundae)
        test_smash_in_works_random = smash_in_works_random(scripts, 5)
        tests.append(test_smash_in_works_random)
        test_smash_in_works_spacing = smash_in_works_spacing(scripts, 5)
        tests.append(test_smash_in_works_spacing)
        test_sundae_fancy_sundae_works = sundae_fancy_sundae_works(scripts, 5)
        tests.append(test_sundae_fancy_sundae_works)
        test_add_icecream_works = add_icecreams_works(scripts, 5)
        tests.append(test_add_icecream_works)
        test_add_dry_toppings_and_wet_toppings_works = add_dry_toppings_and_wet_toppings_works(scripts, 10)
        tests.append(test_add_dry_toppings_and_wet_toppings_works)
        test_delete_two_questions = delete_two_questions(scripts, 5)
        tests.append(test_delete_two_questions)
        test_delete_works = delete_works(scripts, 10)
        tests.append(test_delete_works)
        for key in scripts:
                print("key {}  script {} ".format(key, scripts[key]))
        test_help = find_help(json_data, 5)
        tests.append(test_help)
        score_info['finished_scoring'] = True
        for test in tests:
            if test['pass']:
                    score_info['score'] += test['points']
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/scratch/scratch_feedback_43a_alternate')
def scratch_feedback_43a_alternate():
    from app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help, \
        arrange_blocks_v2, free_points
    from app.scratch_labs.scratch_4_3 import one_works, songs_list, songs_list_min_items, one_looks_ok, two_looks_ok, \
        three_looks_ok, four_looks_ok, five_looks_ok, two_works, three_works, four_works, five_works, tester
    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 70, 'manually_scored': 10, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = scratch_filename_test(filename, '4.3a_alternate')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        scripts = arrange_blocks_v2(json_data)
        for key in scripts:
            print("key {}  script {} ".format(key, scripts[key]))
        test_songs_list = songs_list(json_data, 5)
        tests.append(test_songs_list)
        test_songs_list_min_items = songs_list_min_items(json_data, 5)
        tests.append(test_songs_list_min_items)

        if test_songs_list_min_items['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            free_points = free_points(5)
            tests.append(free_points)
            test_one_looks_ok = one_looks_ok(scripts, 5)
            tests.append(test_one_looks_ok)
            test_one_works = one_works(scripts, 5)
            tests.append(test_one_works)
            test_two_looks_ok = two_looks_ok(scripts, 5)
            tests.append(test_two_looks_ok)
            test_two_works = two_works(scripts, 5)
            tests.append(test_two_works)
            test_three_looks_ok = three_looks_ok(scripts, 5)
            tests.append(test_three_looks_ok)
            test_three_works = three_works(scripts, 5)
            tests.append(test_three_works)
            test_four_looks_ok = four_looks_ok(scripts, 5)
            tests.append(test_four_looks_ok)
            test_four_works = four_works(scripts, 5)
            tests.append(test_four_works)
            test_five_looks_ok = five_looks_ok(scripts, 5)
            tests.append(test_five_looks_ok)
            test_five_works = five_works(scripts, 5)
            tests.append(test_five_works)
            test_help = find_help(json_data, 5)
            tests.append(test_help)
            score_info['finished_scoring'] = True
            for test in tests:
                if test['pass']:
                        score_info['score'] += test['points']
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/scratch/scratch_feedback_43b_alternate')
def scratch_feedback_43b_alternate():
    from app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help, \
        arrange_blocks_v2, free_points
    from app.scratch_labs.scratch_4_3 import oneb_works, songs_list, songs_list_min_items, oneb_looks_ok, \
        twob_looks_ok, \
        threeb_looks_ok,  twob_works, threeb_works, fourb_works, fiveb_works, tester
    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 45, 'manually_scored': 10, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = scratch_filename_test(filename, '4.3b_alternate')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        scripts = arrange_blocks_v2(json_data)
        for key in scripts:
            print("key {}  script {} ".format(key, scripts[key]))
        test_songs_list = songs_list(json_data, 5)
        tests.append(test_songs_list)
        test_songs_list_min_items = songs_list_min_items(json_data, 5)
        tests.append(test_songs_list_min_items)

        if test_songs_list_min_items['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            test_oneb_looks_ok = oneb_looks_ok(scripts, 5)
            tests.append(test_oneb_looks_ok)
            test_oneb_works = oneb_works(scripts, 5)
            tests.append(test_oneb_works)
            test_twob_looks_ok = twob_looks_ok(scripts, 5)
            tests.append(test_twob_looks_ok)
            test_twob_works = twob_works(scripts, 5)
            tests.append(test_twob_works)
            test_threeb_looks_ok = threeb_looks_ok(scripts, 5)
            tests.append(test_threeb_looks_ok)
            test_threeb_works = threeb_works(scripts, 5)
            tests.append(test_threeb_works)
            test_fourb_works = fourb_works(scripts, 5)
            tests.append(test_fourb_works)
            test_fiveb_works = fiveb_works(scripts, 5)
            tests.append(test_fiveb_works)
            test_help = find_help(json_data, 5)
            tests.append(test_help)
            score_info['finished_scoring'] = True
            for test in tests:
                if test['pass']:
                        score_info['score'] += test['points']
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/scratch/scratch_feedback_44')
def scratch_feedback_44():
    from app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help, \
        arrange_blocks_v2
    from app.scratch_labs.scratch_4_4 import numbers_list, numbers_list_min_items, two_looks_ok, one_works, two_works, \
        three_looks_ok, three_works, four_looks_ok, four_works, five_looks_ok, five_works, six_looks_ok, six_works, \
        seven_works, eight_works
    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 70, 'manually_scored': 10, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = scratch_filename_test(filename, '4.4')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        scripts = arrange_blocks_v2(json_data)
        for key in scripts:
            print("key {}  script {} ".format(key, scripts[key]))
        test_numbers_list = numbers_list(json_data, 5)
        tests.append(test_numbers_list)
        test_numbers_list_min_items = numbers_list_min_items(json_data, 5)
        tests.append(test_numbers_list_min_items)

        if test_numbers_list_min_items['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            test_one_works = one_works(scripts, 5)
            tests.append(test_one_works)
            test_two_looks_ok = two_looks_ok(scripts, 5)
            tests.append(test_two_looks_ok)
            test_two_works = two_works(scripts, 5)
            tests.append(test_two_works)
            test_three_looks_ok = three_looks_ok(scripts, 5)
            tests.append(test_three_looks_ok)
            test_three_works = three_works(scripts, 5)
            tests.append(test_three_works)
            test_four_looks_ok = four_looks_ok(scripts, 5)
            tests.append(test_four_looks_ok)
            test_four_works = four_works(scripts, 5)
            tests.append(test_four_works)
            test_five_looks_ok = five_looks_ok(scripts, 5)
            tests.append(test_five_looks_ok)
            test_five_works = five_works(scripts, 5)
            tests.append(test_five_works)
            test_six_looks_ok = six_looks_ok(scripts, 5)
            tests.append(test_six_looks_ok)
            test_six_works = six_works(scripts, 5)
            tests.append(test_six_works)
            test_seven_works = seven_works(scripts, 5)
            tests.append(test_seven_works)
            test_eight_works = eight_works(scripts, 5)
            tests.append(test_eight_works)
            test_help = find_help(json_data, 5)
            tests.append(test_help)
            score_info['finished_scoring'] = True
            for test in tests:
                if test['pass']:
                        score_info['score'] += test['points']
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/scratch/karel1')
def scratch_feedback_karel1():
    from app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help, \
        match_string, every_sprite_green_flag, every_sprite_broadcast_and_receive
    from app.scratch_labs.karel import extract_coder_json, arrange_karel_blocks, karel1a, find_turnright
    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 45, 'manually_scored': 0, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = scratch_filename_test(filename, 'karel1')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        coder_json = extract_coder_json(json_data)
        [moves, user_blocks, repeat_scripts] = arrange_karel_blocks(coder_json)
        test_turnright = find_turnright(user_blocks, 5)
        tests.append(test_turnright)
        test_karel = karel1a(moves, 35)
        tests.append(test_karel)
        test_help = find_help(json_data, 5)
        tests.append(test_help)
        score_info['finished_scoring'] = True
        for test in tests:
            if test['pass']:
                    score_info['score'] += test['points']
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/scratch/karel2a')
def scratch_feedback_karel2a():
    from app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help
    from app.scratch_labs.karel import extract_coder_json, arrange_karel_blocks, find_turnright, find_repeatfive, \
        karel2a
    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 45, 'manually_scored': 0, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = scratch_filename_test(filename, 'karel2a')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        coder_json = extract_coder_json(json_data)
        [moves, user_blocks, repeat_scripts] = arrange_karel_blocks(coder_json)
        test_turnright = find_turnright(user_blocks, 5)
        tests.append(test_turnright)
        test_repeatfive = find_repeatfive(user_blocks, 5)
        tests.append(test_repeatfive)
        test_karel = karel2a(moves, 30)
        tests.append(test_karel)

        test_help = find_help(json_data, 5)
        tests.append(test_help)
        score_info['finished_scoring'] = True
        for test in tests:
            if test['pass']:
                    score_info['score'] += test['points']
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/scratch/karel2b')
def scratch_feedback_karel2b():
    from app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help
    from app.scratch_labs.karel import extract_coder_json, arrange_karel_blocks, find_turnright, find_repeatfour, \
        karel2b
    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 45, 'manually_scored': 0, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = scratch_filename_test(filename, 'karel2b')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        coder_json = extract_coder_json(json_data)
        [moves, user_blocks, repeat_scripts] = arrange_karel_blocks(coder_json)
        test_turnright = find_turnright(user_blocks, 5)
        tests.append(test_turnright)
        test_repeatfour = find_repeatfour(user_blocks, 5)
        tests.append(test_repeatfour)
        test_karel = karel2b(moves, 30)
        tests.append(test_karel)

        test_help = find_help(json_data, 5)
        tests.append(test_help)
        score_info['finished_scoring'] = True
        for test in tests:
            if test['pass']:
                    score_info['score'] += test['points']
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/scratch/karel3a')
def scratch_feedback_karel3a():
    from app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help
    from app.scratch_labs.karel import extract_coder_json, arrange_karel_blocks, find_turnright,  \
        karel3a_1, karel3a_2, karel_final_spot
    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 45, 'manually_scored': 0, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = scratch_filename_test(filename, 'karel3a')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        coder_json = extract_coder_json(json_data)
        [moves, user_blocks, repeat_scripts] = arrange_karel_blocks(coder_json)
        test_turnright = find_turnright(user_blocks, 5)
        tests.append(test_turnright)
        test_karel = karel3a_1(moves, 15)
        tests.append(test_karel)
        test_karel_2 = karel3a_2(moves, 17.5)
        tests.append(test_karel_2)
        test_final_spot = karel_final_spot(moves, 2.5)
        tests.append(test_final_spot)

        test_help = find_help(json_data, 5)
        tests.append(test_help)
        score_info['finished_scoring'] = True
        for test in tests:
            if test['pass']:
                    score_info['score'] += test['points']
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/scratch/karel3b')
def scratch_feedback_karel3b():
    from app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help
    from app.scratch_labs.karel import extract_coder_json, arrange_karel_blocks, find_turnright,  \
        karel3b_1, karel3b_2, karel_final_spot
    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 45, 'manually_scored': 0, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = scratch_filename_test(filename, 'karel3b')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        coder_json = extract_coder_json(json_data)
        [moves, user_blocks, repeat_scripts] = arrange_karel_blocks(coder_json)
        test_turnright = find_turnright(user_blocks, 5)
        tests.append(test_turnright)
        test_karel = karel3b_1(moves, 15)
        tests.append(test_karel)
        test_karel_2 = karel3b_2(moves, 17.5)
        tests.append(test_karel_2)
        test_final_spot = karel_final_spot(moves, 2.5)
        tests.append(test_final_spot)

        test_help = find_help(json_data, 5)
        tests.append(test_help)
        score_info['finished_scoring'] = True
        for test in tests:
            if test['pass']:
                    score_info['score'] += test['points']
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/scratch/karel3c')
def scratch_feedback_karel3c():
    from app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help
    from app.scratch_labs.karel import extract_coder_json, arrange_karel_blocks, find_turnright,  \
        karel3c_1, karel3c_2, karel_final_spot
    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 45, 'manually_scored': 0, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = scratch_filename_test(filename, 'karel3c')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        coder_json = extract_coder_json(json_data)
        [moves, user_blocks, repeat_scripts] = arrange_karel_blocks(coder_json)
        test_turnright = find_turnright(user_blocks, 5)
        tests.append(test_turnright)
        test_karel = karel3c_1(moves, 15)
        tests.append(test_karel)
        test_karel_2 = karel3c_2(moves, 17.5)
        tests.append(test_karel_2)
        test_final_spot = karel_final_spot(moves, 2.5)
        tests.append(test_final_spot)

        test_help = find_help(json_data, 5)
        tests.append(test_help)
        score_info['finished_scoring'] = True
        for test in tests:
            if test['pass']:
                    score_info['score'] += test['points']
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/scratch/karel3d')
def scratch_feedback_karel3d():
    from app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help
    from app.scratch_labs.karel import extract_coder_json, arrange_karel_blocks, find_turnright,  \
        karel3d_1, karel3d_2
    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 45, 'manually_scored': 0, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = scratch_filename_test(filename, 'karel3d')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        coder_json = extract_coder_json(json_data)
        [moves, user_blocks, repeat_scripts] = arrange_karel_blocks(coder_json)
        test_turnright = find_turnright(user_blocks, 5)
        tests.append(test_turnright)
        test_karel = karel3d_1(moves, 17.5)
        tests.append(test_karel)
        test_karel_2 = karel3d_2(moves, 17.5)
        tests.append(test_karel_2)

        test_help = find_help(json_data, 5)
        tests.append(test_help)
        score_info['finished_scoring'] = True
        for test in tests:
            if test['pass']:
                    score_info['score'] += test['points']
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


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
    from app.python_labs.find_items import find_questions, find_list, find_random, find_print
    from app.python_labs.python_3_011 import python_3_011_2, python_3_011_1
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
                test_find_print = find_print(filename_data, 1, 5)
                tests.append(test_find_print)

                # Test efficiency
                test_efficiency = python_3_011_1(filename_data, 5)
                tests.append(test_efficiency)

                test_runs = python_3_011_2(filename, filename_data, 10)
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

    from app.python_labs.find_items import find_function, function_called, find_list
    from app.python_labs.filename_test import filename_test
    from app.python_labs.function_test import extract_all_functions, extract_single_function, run_unit_test, \
        create_testing_file
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8
    from app.python_labs.python_3_020 import ten_runs, check_random

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '3.020')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_find_function_1 = find_function(filename, 'birthday_song', 1, points=4)
        tests.append(test_find_function_1)

        # Only continue if you have a birthday_song_function
        if not test_find_function_1['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # Check that function is called once
            test_birthday_song_run = function_called(filename, 'birthday_song', 1, points=4)
            tests.append(test_birthday_song_run)

            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)

            # function test 1
            test_function_1 = run_unit_test('3.020', 1, 4)
            test_function_1['name'] += " (prints out 'birthday' somewhere) "
            tests.append(test_function_1)

            # function test 2
            test_function_2 = run_unit_test('3.020', 2, 5)
            test_function_2['name'] += " (prints out input parameter somewhere) "
            tests.append(test_function_2)

            # function test 3
            test_function_3 = run_unit_test('3.020', 3, 8)
            test_function_3['name'] += " (output looks good) "
            tests.append(test_function_3)

            test_find_function_2 = find_function(filename, 'pick_card', 0, points=4)
            tests.append(test_find_function_2)

            # Only continue if you have a birthday_song_function
            if not test_find_function_2['pass']:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:

                cards_function = extract_single_function(filename, 'pick_card')

                test_find_cards = find_list(cards_function, num_items=4, list_name='cards', points=2)
                tests.append(test_find_cards)

                test_find_suits = find_list(cards_function, num_items=4, list_name='suits', points=2)
                tests.append(test_find_suits)

                # function test 4
                test_function_4 = run_unit_test('3.020', 4, 5)
                test_function_4['name'] += " (function picks 1 card) "
                tests.append(test_function_4)

                # Check that function is called once
                test_pick_card_run = function_called(filename, 'pick_card', 1, points=4)
                tests.append(test_pick_card_run)

                # Check that random is random
                test_random = check_random(filename)
                tests.append(test_random)

                # check that pick_card prints out 10 cards (looks for 'of' 10x)
                test_run_ten_cards = ten_runs(filename)
                tests.append(test_run_ten_cards)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 14)
                tests.append(test_pep8)
                test_help = helps(filename, 5)
                tests.append(test_help)

                for test in tests:
                    if test['pass']:
                        score_info['score'] += test['points']
                score_info['finished_scoring'] = True
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)


@app.route('/feedback_3026')
def feedback_3026():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_string, find_function, function_called, find_loop
    from app.python_labs.function_test import run_unit_test, create_testing_file, extract_all_functions, \
        extract_single_function
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 44.5, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '3.026')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Check for function return_min
        test_find_function = find_function(filename, 'return_min', 1, points=5)
        tests.append(test_find_function)

        # Only continue if you have a return_min_function
        if test_find_function['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            return_min_function = extract_single_function(filename, 'return_min')

            # Check that function is called 1x
            test_function_run = function_called(filename, 'return_min', 1, points=5)
            tests.append(test_function_run)

            # find string return (return in the function)
            test_return = find_string(return_min_function, r'return \s .+', 1, points=2.5)
            test_return["name"] += " (There is a return in the function)"
            test_return["fail_message"] += " (There is a return in the function)"
            tests.append(test_return)

            # find loop in function
            test_loop = find_loop(return_min_function, 2.5)
            test_loop["name"] += " (There is a loop in the code)"
            test_loop["fail_message"] += " (There is a loop in the function)"
            tests.append(test_loop)

            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)

            # function test 1
            test_function_1 = run_unit_test('3.026', 1, 5)
            test_function_1['name'] += " (return_min with list [-1, 3, 5, 99] returns -1) "
            tests.append(test_function_1)

            # function test 2
            test_function_2 = run_unit_test('3.026', 2, 5)
            test_function_2['name'] += " (return_min with list [-1, 3, 5, -99] returns -99) "
            tests.append(test_function_2)

            # function test 3
            test_function_3 = run_unit_test('3.026', 3, 5)
            test_function_3['name'] += " (return_min with list [5] returns 5) "
            tests.append(test_function_3)

            # function test 4
            test_function_4 = run_unit_test('3.026', 4, 5)
            test_function_4['name'] += " (return_min with list [5, 4, 99, -11, 44, -241, -444, -999, 888, -2] " \
                                       "returns -444) "
            tests.append(test_function_4)

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


@app.route('/feedback_4011')
def feedback_4011():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_function, find_loop, function_called, find_if
    from app.python_labs.function_test import run_unit_test, extract_single_function,\
        extract_all_functions, create_testing_file
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.011')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        # Check for function
        test_find_function = find_function(filename, 'could_it_be_a_martian_word', 1, points=5)
        tests.append(test_find_function)

        if test_find_function['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            extract_all_functions(filename)
            function_data = extract_single_function(filename, 'could_it_be_a_martian_word')
            create_testing_file(filename)

            # Check for a loop of some sort (for or while)
            test_loop = find_loop(function_data, 5)
            test_loop['name'] += "Testing there is a loop in the could_it_be_a_martian_word function.<br>"
            tests.append(test_loop)

            if test_loop['pass'] is False:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:
                # Check that function is called 3x
                test_function_run = function_called(filename, 'could_it_be_a_martian_word', 3, points=5)
                tests.append(test_function_run)

                test_function_1 = run_unit_test('4.011', 1, 10)
                test_function_1['name'] += " (could_it_be_a_martian_word with 'bcdefgijnpqrstuvwxyz' returns []) "
                tests.append(test_function_1)

                test_function_2 = run_unit_test('4.011', 2, 10)
                test_function_2['name'] += " (could_it_be_a_martian_word with 'ba' returns ['a']) "
                tests.append(test_function_2)

                test_function_3 = run_unit_test('4.011', 3, 10)
                test_function_3['name'] += " (could_it_be_a_martian_word with 'baa' returns ['a']) "
                tests.append(test_function_3)

                test_ifs = find_if(function_data, 3, 5, minmax='max')
                tests.append(test_ifs)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 14)
                tests.append(test_pep8)
                test_help = helps(filename, 5)
                tests.append(test_help)

                for test in tests:
                    if test['pass']:
                        score_info['score'] += test['points']
                score_info['finished_scoring'] = True
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)


@app.route('/feedback_4021')
def feedback_4021():
    from app.python_labs.find_items import find_function, function_called, find_loop
    from app.python_labs.filename_test import filename_test
    from app.python_labs.function_test import run_unit_test, extract_all_functions, extract_single_function, \
        create_testing_file
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 37,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.021')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Check for function the_rock_says
        test_find_function = find_function(filename, 'the_rock_says', 1, points=5)
        tests.append(test_find_function)
        if test_find_function['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)
            function_data = extract_single_function(filename, 'the_rock_says')

            # Check for a loop of some sort (for or while)
            test_loop = find_loop(function_data, 2.5)
            test_loop['name'] += "Testing there is a loop in the the_rock_says function.<br>"
            tests.append(test_loop)

            if test_loop['pass'] is False:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:
                # Check that function is called 3x
                test_function_run = function_called(filename, 'the_rock_says', 3, points=5)

                tests.append(test_function_run)

                # test1 for the_rock_says
                test_function_1 = run_unit_test('4.021', 1, 5)
                test_function_1['name'] += " (Testing calling the_rock_says with list ['eggs', 'apple'] returns a " \
                                           "list ['The Rock says eggs', 'The Rock says apple']) "
                tests.append(test_function_1)

                # test2 for the_rock_says
                test_function_2 = run_unit_test('4.021', 2, 5)
                test_function_2['name'] += " (Testing calling the_rock_says withlist ['eggs', 'smell'] returns " \
                                           "['The Rock says eggs', 'Do you smell what The Rock is cooking']" \
                                           "['The Rock says eggs', 'The Rock says apple']) <br> "
                tests.append(test_function_2)

                # test3 for the_rock_says
                test_function_3 = run_unit_test('4.021', 3, 5)
                test_function_3['name'] += " (Testing calling the_rock_says with list " \
                                           "['smog', 'smells', 'smashmouth'] returns ['Do you smell what The Rock is" \
                                           " cooking', " \
                                           "'Do you smellell what The Rock is cooking', " \
                                           "'Do you smellellellellellellell what The Rock is cooking'] <br> "
                tests.append(test_function_3)

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


@app.route('/feedback_4022')
def feedback_4022():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_function, function_called, find_loop
    from app.python_labs.function_test import run_unit_test, extract_all_functions, \
        extract_single_function, create_testing_file
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 37,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.022')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Check for function
        test_find_function = find_function(filename, 'bad_lossy_compression', 1, points=5)
        tests.append(test_find_function)
        if test_find_function['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # extract functions and create python test file
            extract_all_functions(filename)
            function_data = extract_single_function(filename, 'bad_lossy_compression')
            create_testing_file(filename)

            # Check for a loop of some sort (for or while)
            test_loop = find_loop(function_data, 2.5)
            test_loop['name'] += "Testing there is a loop in the bad_lossy_compression function.<br>"
            tests.append(test_loop)

            if test_loop['pass'] is False:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:
                # Check that function is called 3x
                test_function_run = function_called(filename, 'bad_lossy_compression', 3, points=5)
                tests.append(test_function_run)

                # test1
                test_function_1 = run_unit_test('4.022', 1, 5)
                test_function_1['name'] += " (Testing calling bad_lossy_compression with 'The rain in spain falls " \
                                           "mainly in the plain' returns 'The ain n spin flls ainl in he pain') "
                tests.append(test_function_1)

                # test2 for the_rock_says
                test_function_2 = run_unit_test('4.022', 2, 5)
                test_function_2['name'] += " (Testing calling bad_lossy_compression with " \
                                           "'I am sick and tired of these darned snakes on this darned plane'" \
                                           " returns 'I a sik ad tredof hes danedsnaes n tis arnd pane' <br> "
                tests.append(test_function_2)

                # test3 for the_rock_says
                test_function_3 = run_unit_test('4.022', 3, 5)
                test_function_3['name'] += "Testing calling bad_lossy_compression with 'Madness?!?!?!?!" \
                                           " THIS IS SPARTA!!!!'" \
                                           " returns 'Madess!?!!?!THI ISSPATA!!!' <br> "
                tests.append(test_function_3)

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

    
@app.route('/feedback_4025')
def feedback_4025():

    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_loop, find_string
    from app.python_labs.function_test import extract_all_functions, create_testing_file, extract_single_function, \
        run_unit_test
    from app.python_labs.python_4_025 import win_all, win_most

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 114,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.025')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)
        play_tournament_function = extract_single_function(filename, 'play_tournament')

        test_function_1 = run_unit_test('4.025', 1, 15)
        test_function_1['name'] += " Testing game function - 1000 runs should give between 730 and 780 wins " \
                                   "(10 points) "
        tests.append(test_function_1)

        if test_function_1['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:

            test_loop = find_loop(play_tournament_function, 5)
            test_loop['name'] += " Testing for loop in play_tournament function.<br>"
            tests.append(test_loop)

            test_function_2 = run_unit_test('4.025', 2, 5)
            test_function_2['name'] += " Testing play_tournament function.  If I call play_tournament with " \
                                       "input parameters (0.75, 'Wimbledon'), play_tournament  should " \
                                       "print 'Wimbledon' somewhere (2.5 points).<br>"
            tests.append(test_function_2)

            test_function_3 = run_unit_test('4.025', 3, 5)
            test_function_3['name'] += " Testing play_tournament function.  If I call play_tournament with " \
                                       "input parameters (1.0, 'Wimbledon'), Serena should win this tournament" \
                                       "(5 points).<br>"
            tests.append(test_function_3)

            test_function_4 = run_unit_test('4.025', 4, 10)
            test_function_4['name'] += " Testing play_season function.  If I call play_season enough times," \
                                       "Serena should win US open most, followed by Wimbledon, followed by French " \
                                       "open (10 points).<br>"
            tests.append(test_function_4)

            test_function_5 = run_unit_test('4.025', 5, 10)
            test_function_5['name'] += " Testing data_analysis function, looking to see if correct percentages are " \
                                       "printed (10 points).<br>"
            tests.append(test_function_5)

            run_simulation_function = extract_single_function(filename, 'run_simulation')
            test_run_sim = find_loop(run_simulation_function, 5)
            test_run_sim['name'] = "Looking for loop in the run_simulation function (5 points).<br>"
            tests.append(test_run_sim)

            test_run_sim_data_analysis = find_string(run_simulation_function, r'\s*data_analysis\(', 1, points=5)
            test_run_sim_data_analysis['name'] = "Checking that run_simulation calls data_analysis (5 points).<br>"
            tests.append(test_run_sim_data_analysis)

            test_function_6 = run_unit_test('4.025', 6, 5)
            test_function_6['name'] = " Testing run_simulation function, verifying that if you call it with" \
                                      "p_num_simulations of 300, the printout shows 300 runs. <br>" \
                                      " Requires a working data_analysis (5 points).<br>"
            tests.append(test_function_6)

            # IO tests
            test_io_1 = win_all(filename)
            tests.append(test_io_1)

            test_io_2 = win_most(filename)
            tests.append(test_io_2)

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


@app.route('/feedback_6_011')
def feedback_6011():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_function, find_elif, find_dictionary
    from app.python_labs.function_test import extract_all_functions, create_testing_file, run_unit_test
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8
    from app.python_labs.read_file_contents import read_file_contents

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '6.011')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        test_find_function = find_function(filename, 'bob_kraft_translator', 2, points=5)
        tests.append(test_find_function)
        if not test_find_function['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:

            # Test for dictionary with 3+ items
            filename_data = read_file_contents(filename)

            test_dictionary = find_dictionary(filename_data, num_items=3, points=10)
            tests.append(test_dictionary)

            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)

            test_function_1 = run_unit_test('6.011', 1, 10)
            test_function_1['name'] += " (Sent in dictionary  {'wth': 'What the heck'}, search for 'wth', " \
                                       "returned 'what the heck') <br>"
            tests.append(test_function_1)

            test_function_2 = run_unit_test('6.011', 2, 10)
            test_function_2['name'] += " (Sent in dictionary  {'wth': 'What the heck', 'aymm': 'Ay yo my man',}, " \
                                       "looking for aymm, should receive 'Ay yo my man'. <br>"
            tests.append(test_function_2)

            test_function_3 = run_unit_test('6.011', 3, 10)
            test_function_3['name'] += " (Sent in dictionary  {'wth': 'What the heck','aymm': 'Ay yo my man',}, " \
                                       "asdfasdf, received something with 'do not know''. <br>"
            tests.append(test_function_3)

            # Check for 3 ifs on different lines
            test_elifs = find_elif(filename_data, 3, 5, minmax='max')
            tests.append(test_elifs)

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


@app.route('/feedback_6_021')
def feedback_6021():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_function, function_called, find_dictionary
    from app.python_labs.function_test import extract_all_functions, extract_single_function, \
        create_testing_file, run_unit_test
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '6.021')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        extract_all_functions(filename)
        create_testing_file(filename)

        test_find_function = find_function(filename, 'martinez_dictionary', 1, points=5)
        tests.append(test_find_function)

        # Check that function is called 3x
        test_function_run = function_called(filename, 'martinez_dictionary', 3, points=5)
        tests.append(test_function_run)

        # extract martinez_dictionary functions and look for dictionary
        martinez_function = extract_single_function(filename, 'martinez_dictionary')
        test_dictionary = find_dictionary(martinez_function, num_items=0, points=5)
        tests.append(test_dictionary)

        # Martinez test 1
        test_function_1 = run_unit_test('6.021', 1, 10)
        tests.append(test_function_1)

        # Martinez test 2
        test_function_2 = run_unit_test('6.021', 2, 10)
        tests.append(test_function_2)

        test_find_function = find_function(filename, 'data_generator', 2, points=5)
        tests.append(test_find_function)
        if test_find_function['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # Martinez test 3
            test_function_3 = run_unit_test('6.021', 3, 5)
            tests.append(test_function_3)

            # Martinez test 4
            test_function_4 = run_unit_test('6.021', 4, 5)
            tests.append(test_function_4)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 14)
            tests.append(test_pep8)
            test_help = helps(filename, 5)
            tests.append(test_help)

            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']
                flash(test['name'])
                flash(score_info['score'])

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_6_031')
def feedback_6031():
    from app.python_labs.function_test import extract_all_functions, run_unit_test, create_testing_file
    from app.python_labs.find_items import find_function, find_loop, find_dictionary
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
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        filename_data = read_file_contents(filename)

        test_dictionary = find_dictionary(filename_data, num_items=0, points=5)
        tests.append(test_dictionary)
        if test_dictionary['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:

            # Check for function add with 3 inputs
            test_find_function = find_function(filename, 'add', 3, points=5)
            tests.append(test_find_function)
            if test_find_function['pass'] is False:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:

                extract_all_functions(filename)
                create_testing_file(filename)

                # function test 1
                test_function_1 = run_unit_test('6.031', 1, 5)
                tests.append(test_function_1)

                # function test 2
                test_function_2 = run_unit_test('6.031', 2, 10)
                tests.append(test_function_2)

                # Check for function add with 2 inputs
                test_find_function = find_function(filename, 'get', 2, points=5)
                tests.append(test_find_function)
                if test_find_function['pass'] is False:
                    return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                           score_info=score_info)
                else:
                    # function test 3
                    test_function_3 = run_unit_test('6.031', 3, 5)
                    tests.append(test_function_3)

                    # function test 3
                    test_function_4 = run_unit_test('6.031', 4, 10)
                    tests.append(test_function_4)

                    # Check for a loop of some sort (for or while)
                    test_loop = find_loop(filename_data, 5)
                    tests.append(test_loop)

                    # Find number of PEP8 errors and helps
                    test_pep8 = pep8(filename, 14)
                    tests.append(test_pep8)
                    test_help = helps(filename, 5)
                    tests.append(test_help)

                    for test in tests:
                        if test['pass']:
                            score_info['score'] += test['points']

                    score_info['finished_scoring'] = True
                    return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                           score_info=score_info)


@app.route('/feedback_6_041')
def feedback_6041():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_function, find_string
    from app.python_labs.function_test import extract_all_functions, create_testing_file, run_unit_test
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8
    from app.python_labs.python_6_041 import five_loop
    from app.python_labs.read_file_contents import read_file_contents

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '6.041')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        filename_data = read_file_contents(filename)

        # Check for function add with 1 inputs
        test_find_function = find_function(filename, 'item_list_to_dictionary', 1, points=5)
        tests.append(test_find_function)
        if test_find_function['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)

            # function test 1
            test_function_1 = run_unit_test('6.041', 1, 10)
            tests.append(test_function_1)

            # Check for function 1 inputs
            test_find_function_2 = find_function(filename, 'min_item', 1, points=5)
            tests.append(test_find_function_2)

            # unit test 2
            test_function_2 = run_unit_test('6.041', 2, 20)
            tests.append(test_function_2)

            # Check that removes, just look for del or pop
            test_removal = find_string(filename_data, r"\.pop\( | del", 1, points=5)
            tests.append(test_removal)

            # Check that it's run 5x
            test_five_times = five_loop(filename_data)
            tests.append(test_five_times)

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


@app.route('/feedback_7_021')
def feedback_7021():
    from app.python_labs.find_items import find_class, find_function, function_called, object_created
    from app.python_labs.function_test import extract_all_functions, create_testing_file, run_unit_test
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '7.021')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        # Check for class Collectible
        test_class = find_class(filename, 'Collectible', 'object', points=5)
        tests.append(test_class)

        if test_class['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:

            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)

            # function test 2
            test_function_1 = run_unit_test('7.021', 1, 15)
            tests.append(test_function_1)

            # Check for function existence
            test_find_function = find_function(filename, 'collectible_printer', 1, points=5)
            tests.append(test_find_function)

            # test 2
            test_function_2 = run_unit_test('7.021', 2, 5)
            tests.append(test_function_2)

            # test 3
            test_function_3 = run_unit_test('7.021', 3, 10)
            tests.append(test_function_3)

            # Check for all objects
            test_objects = object_created(filename, 'Collectible', 3, points=5)
            tests.append(test_objects)

            # Check that function is called
            test_function_run = function_called(filename, 'collectible_printer', 1, points=5)
            tests.append(test_function_run)

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


@app.route('/feedback_7_031')
def feedback_7031():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.function_test import extract_all_functions, create_testing_file, run_unit_test
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 34.5, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '7.031')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)

        # unit test 1
        test_function_1 = run_unit_test('7.031', 1, 5)
        tests.append(test_function_1)

        # unit test 2
        test_function_2 = run_unit_test('7.031', 2, 10)
        tests.append(test_function_2)

        # unit test 3
        test_function_3 = run_unit_test('7.031', 3, 10)
        tests.append(test_function_3)

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


@app.route('/feedback_7_034')
def feedback_7034():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.function_test import extract_all_functions, create_testing_file, run_unit_test
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 34.5,  'manually_scored': 11, 'finished_scoring': False}

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
        unit_test_1 = run_unit_test('7.034', 1, 5)
        tests.append(unit_test_1)

        # unit test 2
        unit_test_2 = run_unit_test('7.034', 2, 5)
        tests.append(unit_test_2)

        # unit test 3
        unit_test_3 = run_unit_test('7.034', 3, 5)
        tests.append(unit_test_3)

        # unit test 4
        unit_test_4 = run_unit_test('7.034', 4, 5)
        tests.append(unit_test_4)

        # unit test 5
        unit_test_5 = run_unit_test('7.034', 5, 5)
        tests.append(unit_test_5)

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


@app.route('/feedback_4031')
def feedback_4031():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.function_test import create_testing_file, extract_all_functions, run_unit_test
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8
    from app.python_labs.python_4_03x import python_4_031_double_loops, python_4_031_good_prints

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.031')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)

        # unit test 1
        unit_test_1 = run_unit_test('4.031', 1, 2.5)
        tests.append(unit_test_1)

        # unit test 2
        unit_test_2 = run_unit_test('4.031', 2, 2.5)
        tests.append(unit_test_2)

        # unit test 3
        unit_test_3 = run_unit_test('4.031', 3, 2.5)
        tests.append(unit_test_3)

        # unit test 4
        unit_test_4 = run_unit_test('4.031', 4, 5)
        tests.append(unit_test_4)

        # unit test 5
        unit_test_5 = run_unit_test('4.031', 5, 5)
        tests.append(unit_test_5)

        # unit test 6
        unit_test_6 = run_unit_test('4.031', 6, 5)
        tests.append(unit_test_6)

        # unit test 7
        unit_test_7 = run_unit_test('4.031', 7, 5)
        tests.append(unit_test_7)

        # unit test 8
        unit_test_8 = run_unit_test('4.031', 8, 7.5)
        tests.append(unit_test_8)

        # Check for double loops
        test_loop = python_4_031_double_loops(filename)
        tests.append(test_loop)

        # Check for double loops
        test_prints = python_4_031_good_prints(filename)
        tests.append(test_prints)

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

    
@app.route('/feedback_4036')
def feedback_4036():
    from app.python_labs.find_items import find_function
    from app.python_labs.function_test import extract_all_functions, create_testing_file, run_unit_test
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 89,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.036')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        # Check for function existence
        test_find_function = find_function(filename, 'fried_chicken_problem_1', 2, points=5)
        tests.append(test_find_function)

        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)

        # unit test 1
        unit_test_1 = run_unit_test('4.036', 1, 10)
        tests.append(unit_test_1)

        # unit test 2
        unit_test_2 = run_unit_test('4.036', 2, 10)
        tests.append(unit_test_2)

        # Check for function existence
        test_find_function = find_function(filename, 'fried_chicken_problem_2', 2, points=5)
        tests.append(test_find_function)

        # unit test 3
        unit_test_3 = run_unit_test('4.036', 3, 10)
        tests.append(unit_test_3)

        # unit test 4
        unit_test_4 = run_unit_test('4.036', 4, 10)
        tests.append(unit_test_4)

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
