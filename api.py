import os
import re
import subprocess
from flask import Flask

app = Flask(__name__)

def set_work_dir():
    work_dir = os.environ["WORK_DIR"]

    if not work_dir.endswith('/'):
        work_dir = work_dir + './'

    print("WORK_DIR: ", work_dir)
    return work_dir

def parse_ls_result(path):
    ls_string = subprocess.run(['ls', '-lh', path], capture_output=True, text=True).stdout
    ls_parts = ls_string.split('\n')

    file_size_regex = r'(\d+[a-zA-Z])'
    file_owner_regex = r'\s{1}\d{1}\s{1}([a-zA-Z]+)'
    file_name_regex = r'[:]\d{2}\s{1}(\w+\S{1}\w+)'
    file_type_regex = r'\d+\s{1}\w+(\W{1}\w+)$'

    file_info_dictionaries = []
    for part in ls_parts:
        if re.search(file_size_regex, part) and re.search(file_owner_regex, part) and re.search(file_name_regex, part):
            file_size = re.search(file_size_regex, part).group(1)
            file_owner = re.search(file_owner_regex, part).group(1)
            file_name = re.search(file_name_regex, part).group(1)

            file_type = ''
            if re.search(file_type_regex, part):
                file_type = re.search(file_type_regex, part).group(1)
            else:
                file_type = 'folder'
                

            file_info_dict = {
                    "file_name": file_name,
                    "file_owner": file_owner,
                    "file_size": file_size,
                    "file_type": file_type
                    }
            file_info_dictionaries.append(file_info_dict)

    print("file_info: ", file_info_dictionaries)
    return file_info_dictionaries

@app.route("/")
def get_root_ls():
    path = set_work_dir()

    file_contents = subprocess.run(['cat', path], capture_output=True, text=True)
    print("file_contents err: ", file_contents.stderr)

    if file_contents.stderr:
        path = path + "/"
        result = parse_ls_result(path)
    else:
        # TODO: return a proper JSON response with file name, file type, owner, and size
        result = file_contents.stdout

    return result

@app.route("/<path:params>")
def ls(params):
    path = set_work_dir() + params
    print("path: ", path)

    file_contents = subprocess.run(['cat', path], capture_output=True, text=True)
    print("file_contents err: ", file_contents.stderr)

    if file_contents.stderr:
        path = path + "/"
        result = parse_ls_result(path)
    else:
        # TODO: return a proper JSON response with file name, file type, owner, and size
        result = file_contents.stdout

    return result
