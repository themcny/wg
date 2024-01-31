import subprocess
from errors import *
from flask import Flask, jsonify
from utils import *


def create_app(path_to_files):
    app = Flask(__name__)

    @app.route("/")
    @app.route("/<path:params>")
    def get_files(params=''):
        path = set_work_dir(path_to_files) + params

        result = parse_file_information(path)
        response_json = {
            "content_type": "application/json",
            "data": {
                "files": result
            },
            "message": "File system accessed sucessfully",
            "success": True
        }
        return jsonify(response_json), 200

    @app.errorhandler(APIError)
    def handle_exception(e):
        """Return JSON instead of HTML for HTTP errors."""
        response_json = {
            "content_type": "application/json",
            "data": {
                "error_message": e.message
            },
            "message": "An error occured.",
            "success": False
        }
        return jsonify(response_json), 400

    return app
