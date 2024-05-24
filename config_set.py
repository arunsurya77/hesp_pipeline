import os
import fileinput

def replace_first_line(directory, prefix, new_first_line):
    for filename in os.listdir(directory):
        if filename.startswith(prefix):
            filepath = os.path.join(directory, filename)
            with fileinput.FileInput(filepath, inplace=True) as file:
                for i, line in enumerate(file):
                    if i == 0:
                        print(new_first_line.strip(), end='\n')
                    else:
                        print(line, end='')

input_directory = input("Enter the directory path: ")
prefix = input("Enter the prefix: ")
new_first_line = input("Enter the new first line: ")

replace_first_line(input_directory, prefix, new_first_line)
