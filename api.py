import os
import subprocess
from flask import Flask

# currently trailing slash needed in WORK_DIR variable when set in env
work_dir = os.environ["WORK_DIR"]
print("WORK_DIR: ", work_dir)

app = Flask(__name__)

@app.route("/<path:params>")
def ls(params):
    path = work_dir + params
    print("path: ", path)

    file_contents = subprocess.run(['cat', path], capture_output=True, text=True)
    print("file_contents err: ", file_contents.stderr)

    if file_contents.stderr:
        path = path + "/"
        result = subprocess.run(['ls', path], capture_output=True, text=True)
    else:
        result = file_contents

    print("err: ", result.stderr)
    return "Result: " + result.stdout
