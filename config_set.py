import os
import fileinput
import subprocess

def replace_first_line(directory, prefix, new_first_line):
    for filename in os.listdir(directory):
        if filename.startswith(prefix):
            filepath = os.path.join(directory, filename)
            with fileinput.FileInput(filepath, inplace=True) as file:
                for i, line in enumerate(file):
                    if i == 1:
                        print(new_first_line.strip(), end='\n')
                    else:
                        print(line, end='')

python_path = subprocess.check_output("pwd", shell=True).strip()
python_path = python_path.decode('utf-8')
replace_first_line('.', 'hesp.config', 'path='+python_path+'/bin/')
