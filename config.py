import os

basedir = os.path.abspath(os.path.dirname(__file__))

HEADERS = {'Access-Control-Allow-Origin': '*'}


class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'xxx-xxxx-xxxx-xxxx'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
