from flask import Flask

from flask_mongodb.database import DB
from flask_mongodb.models.job import Job



def create_app(config):
    flask_mongodb = Flask(__name__)
    flask_mongodb.config["DEBUG"] = True
    DB.init()
    register_blueprints(flask_mongodb)
    return flask_mongodb


def register_blueprints(flask_mongodb):
    from flask_mongodb.main import bp as main_bp
    flask_mongodb.register_blueprint(main_bp)