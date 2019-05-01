import os


class Config(object):
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))


class ProdConfig(Config):
    ENV = 'prod'
    DEBUG = False
    DB_NAME = 'boilerplateprod'
    GRAPHQL_DATABASE_URI = 'ComingSoon'


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    DB_NAME = 'boilerplatetest'
    GRAPHQL_DATABASE_URI = 'mongodb://localhost:27017'
