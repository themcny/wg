import os
import subprocess
from flask import Flask

work_dir = os.environ["WORK_DIR"]

app = Flask(__name__)

@app.route("/")
def ls(path=None):
    result = subprocess.run(['ls', work_dir], capture_output=True, text=True)
    return "Result: " + result.stdout

@app.route("/<path>")
def get(path=None):
    path = work_dir + path + "/"
    print("path: ", path)
    result = subprocess.run(['ls', path], capture_output=True, text=True)
    print("err: ", result.stderr)
    return "Result: " + result.stdout
