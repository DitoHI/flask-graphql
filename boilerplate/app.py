from flask import Flask

from .settings import DevConfig
from .database import init_db


def create_app(config_object=DevConfig):
    app = Flask(__name__.split(".")[0])
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    init_db(app)
