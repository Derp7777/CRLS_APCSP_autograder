# Inputs: p_filename, filename to extract functions from
#         p_points, number of points this is worth.
# Output: none
# This module extracts all functions from a python file and puts them in a file outputfile.functions.py

def extract_all_functions(orig_file):
    import re
    outfile_name = orig_file.replace('.py', '.functions.py')
    outfile = open(outfile_name, 'w')
    with open(orig_file, 'r', encoding='utf8') as infile:
        line = True
        while line:
            line = infile.readline()
            start_def = re.search("^(def|class) \s+ .+ " , line,  re.X | re.M | re.S)
            if start_def:
                outfile.write(line)
                in_function = True
                while in_function:
                    line = infile.readline()
                    end_of_function = re.search("^[a-zA-Z]", line, re.X | re.M | re.S)
                    new_function = re.search("^(def|class) \s+ .+ " , line,  re.X | re.M | re.S)

                    if end_of_function and not new_function:
                        in_function = False
                        start_def = False
                    elif end_of_function and new_function:
                        in_function = True
                        start_def = True
                        outfile.write(line)

                    else:
                        outfile.write(line)