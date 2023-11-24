from flask import Flask, current_app, g
import mongoengine
import certifi
from environment import secret_access_key, access_key
from flask_cors import CORS, cross_origin

def create_app():
    # initiate app
    app = Flask(__name__)

    # update environment variables
    app.config['AWS_SECRET_ACCESS_KEY'] = secret_access_key
    app.config['AWS_ACCESS_KEY_ID'] = access_key

    # Allow cross-origin requests from AR app
    cors = CORS(app)

    # register blueprints
    register_blueprints(app)

    return app


def register_blueprints(app):
    from controller import main
    app.register_blueprint(main)
