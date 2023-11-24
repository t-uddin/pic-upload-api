from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

import service

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def upload():
    if request.method == "GET":
        return "Working"

@main.route('/upload/', methods=['POST'])
def upload():
    if request.method == "POST":
        # get request params
        if "user_file" not in request.files:
            return "No user_file key in request.files"

        file = request.files["user_file"]

        if file.filename == "":
            return "Please select a file"

        # call service
        if file:
            file.filename = secure_filename(file.filename)
            output = service.upload_file(file, "pics-tu")
            return str(output)

        else:
            return "No file"
