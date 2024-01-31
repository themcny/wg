import subprocess
from flask import Flask
from utils import *

app = Flask(__name__)

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
