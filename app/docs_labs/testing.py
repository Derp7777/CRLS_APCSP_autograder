from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

# The ID of a sample document.
#DOCUMENT_ID = '1Rl1M-bFJsbRLT8ngjsDvLbYDpAWfY2jjSNl8vUK7JWw' \

DOCUMENT_ID = '1LZfjuWRdWNRA0vysLC1J8LYnp49cL5UWk2rGrd34lPc'

# https://docs.google.com/document/d/1LZfjuWRdWNRA0vysLC1J8LYnp49cL5UWk2rGrd34lPc/edit#heading=h.gg00kbxzvzqj

def read_paragraph_element(element):
    """Returns the text in the given ParagraphElement.

        Args:
            element: a ParagraphElement from a Google Doc.
    """
    text_run = element.get('textRun')
    inlineobject = element.get('inlineObjectElement')
    if inlineobject:
        # print("BBB INLINE!!! {}".format(inlineobject))
        return "AAA INLINEOBJECT"
    if not text_run:
        return ' '
    return text_run.get('content')

# inlineObjectElement'

def read_strucutural_elements(elements):
    """Recurses through a list of Structural Elements to read a document's text where text may be
        in nested elements.

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
                    #print("tabledata {}".format(read_strucutural_elements(cell.get('content'))))

                    text += "tabledata " + read_strucutural_elements(cell.get('content'))
        elif 'inlineObjectElement' in value:
            print("YSEOIJSOIFJSEO")
        elif 'tableOfContents' in value:
            # The text in the TOC is also in a Structural Element.
            toc = value.get('tableOfContents')
            text += read_strucutural_elements(toc.get('content'))
    return text



def main():
    """Shows basic usage of the Docs API.
    Prints the title of a sample document.
    """
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
    document = service_document.documents().get(documentId=DOCUMENT_ID).execute()

    print('The title of the document is: {}'.format(document.get('title')))

    doc = service_document.documents().get(documentId=DOCUMENT_ID).execute()
    doc_content = doc.get('body').get('content')

    abc = read_strucutural_elements(doc_content)

    print(abc)


if __name__ == '__main__':
    main()
