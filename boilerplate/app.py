from .database import init_db

from flask import Flask
from flask_graphql import GraphQLView

from .settings import DevConfig
from .schema import schema


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)
    register_extensions(app)
    register_rule(app)

    return app


def register_extensions(app):
    init_db(app)


def register_rule(app):
    app.add_url_rule(
        "/graphql",
        view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True),
    )
