# Input: a filename (string)
# Output: filename contents (string)


def read_file_contents(p_filename):
    with open(p_filename, 'r', encoding='utf8') as myfile:
        p_filename_data = myfile.read()
    return p_filename_data
