def read_file_contents(p_filename):
    """ This function reads in contents of a file.
    Input: filename (string).
    Output: Filename contents (string)
    """
    with open(p_filename, 'r', encoding='utf8') as myfile:
        p_filename_data = myfile.read()
    return p_filename_data


if __name__ == '__main__':
    print("yes")
    asdf = read_file_contents('/tmp/abc.py')
    print(asdf)
