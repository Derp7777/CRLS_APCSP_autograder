def read_paragraph_element(element):
    """Returns the text in the given ParagraphElement.
    swiped directly from https://developers.google.com/docs/api/samples/extract-text?refresh=1
    then modified slightly for our needs
        Args:
            element: a ParagraphElement from a Google Doc.
    """
    text_run = element.get('textRun')
    inlineobject = element.get('inlineObjectElement')
    if inlineobject:
        return "AAA INLINEOBJECT"
    if not text_run:
        return ' '
    return text_run.get('content')


def read_strucutural_elements(elements):
    """Recurses through a list of Structural Elements to read a document's text where text may be
        in nested elements.
       swiped directly from https://developers.google.com/docs/api/samples/extract-text?refresh=1
       then modified slightly for our needs
        Args:
            elements: a list of Structural Elements.
    """
    text = ''
    for value in elements:
        if 'paragraph' in value:
            elements = value.get('paragraph').get('elements')
            for elem in elements:
                text += read_paragraph_element(elem)

        elif 'table' in value:
            # The text in table cells are in nested Structural Elements and tables may be
            # nested.
            table = value.get('table')
            for row in table.get('tableRows'):
                cells = row.get('tableCells')
                for cell in cells:
                    text += "tabledata " + read_strucutural_elements(cell.get('content'))
        elif 'tableOfContents' in value:
            # The text in the TOC is also in a Structural Element.
            toc = value.get('tableOfContents')
            text += read_strucutural_elements(toc.get('content'))
    return text


def get_google_drive_id(p_link):
    """
    Took this from CRLS_google_classroom_autopopulator.  Should just link it through git but maybe later
    :param p_link: link to the file
    :return:
    """
    import re

    print("aaa p_link {}".format(p_link))
    # Figure out which format it is
    format1 = re.search(r'\?id=', p_link)
    format2 = re.search(r'/d/', p_link)

    # Extract google_id from the link
    google_id = ''
    if format1:
        google_id = re.sub(r'^.+\?id=', '', p_link)
    if format2:
        google_id = re.sub(r'.+/d/', '', p_link)
        google_id = re.sub(r'/.+$', '', google_id)

    print("aaa g_id {}".format(google_id))

    return google_id


def get_text(document_id):
    """Shows basic usage of the Docs API.
    Prints the title of a sample document.
    Swiped directly from https://developers.google.com/docs/api/samples/extract-text?refresh=1
    then modified slightly for our needs
    """
    import pickle
    import os.path
    from googleapiclient.discovery import build
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request

    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

    # https://docs.google.com/document/d/1LZfjuWRdWNRA0vysLC1J8LYnp49cL5UWk2rGrd34lPc/edit#heading=h.gg00kbxzvzqj



    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service_document = build('docs', 'v1', credentials=creds)

    # Retrieve the documents contents from the Docs service.
    document = service_document.documents().get(documentId=document_id).execute()

    print('The title of the document is: {}'.format(document.get('title')))

    doc = service_document.documents().get(documentId=document_id).execute()
    doc_content = doc.get('body').get('content')

    p_doctext = read_strucutural_elements(doc_content)

    return p_doctext


def exact_answer(p_label, p_answers, p_text, *, points=0):
    """
    checks that the answer is exactly correct.
    :param p_label: the label of the problem (i.e. 3a, 3b.) (str)
    :param p_answers: The text you are searching for REGEX.  LIST, in case multiple correct answers. (list)
    :param p_text: The text you are searching (str)
    :param points: how many this is worth
    :return: 
    """
    import re
    p_test = {"name": "Checking that " + str(p_label) + " is exactly correct " + str(points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  " +\
                              str(p_label) + " appears correct!<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> " +
                              str(p_label) + " does not appear correct.  Try again.<br>"
                                             "Answers must be spelled correctly (no typos), "
                                             "but capitalization does not matter.<br>",
              "points": 0,
              }
    for answer in p_answers:
        if re.search(answer, p_text, re.X | re.M | re.S):
            p_test['pass'] = True
            break
    if p_test['pass']:
        p_test['points'] += points
    return p_test


def keyword_and_length(p_label, p_answers, p_text, *, search_string='', min_matches=1, min_length=5, points=0):
    """
    checks that the answer has x number of required keywords and a minimum word length.
    :param p_label: the label of the problem (i.e. 3a, 3b.) (str)
    :param p_answers: The words you are searching for.  LIST of allowed answers. (list)
    :param p_text: The text you are searching (str)
    :param search_string: regex for what you want to capture.  Basically search only this.
    :param min_matches: how many words of the keywords you need to match
    :param min_length: minimum length of answer
    :param points: how many this is worth
    :return:
    """
    import re
    p_test = {"name": "Checking that " + str(p_label) + " is has at least " + str(min_matches) + " words that we are "
                      "looking for, with a minimum word length of " + str(min_length) + " (" + str(points) +
                      " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  " +
                              str(p_label) + " appears to pass the test or checkoff!<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> " +
                              str(p_label) + " does not appear correct.  Try again.<br>"
                                             "keywords must be spelled correctly (no typos), "
                                             "but capitalization does not matter.<br><br>",
              "points": 0,
              }
    found_matches = 0
    pass_len = False
    pass_match = False

    final_search_string = ''
    if search_string:
        search_obj = re.search(search_string, p_text, re.X | re.M | re.S)
        if search_obj:
            final_search_string = search_obj.group(1)
    else:
        final_search_string = search_string
    final_search_string = final_search_string.lower()
    # print("aaa this is label {} final-search_string {}".format(p_label, final_search_string))
    for answer in p_answers:
        answer = answer.lower()
        # print("bbb answer {} string {}".format(answer, final_search_string))
        if re.search(answer, final_search_string, re.X | re.M | re.S):
            found_matches += 1
    if found_matches < min_matches:
        p_test['fail_message'] += "Found this many words we were looking for: " + str(found_matches) + "<br>" \
                                  "Require this many matches: " + str(min_matches) + "<br>" \
                                  "Looked in this string: <br>" + \
                                  final_search_string + "<br><br>"
    else:
        pass_match = True
    p_text_list = final_search_string.split()
    if len(p_text_list) < min_length:
        p_test['fail_message'] += 'Found answer was this many words ' + str(len(p_text_list) + 1) + "<br>" \
                                  'Require this length: ' + str(min_length) + "<br>Looked in this string: <br>" + \
                                  final_search_string + "<br><br>"
    else:
        pass_len = True
    if pass_len and pass_match:
        p_test['pass'] = True
        p_test['points'] += points
    return p_test
