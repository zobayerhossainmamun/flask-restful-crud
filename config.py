from os import path

BASE_DIR = path.abspath(path.dirname(__file__))

# config class
class Config(object):
    """set Flask configuration variables from .env file."""

    # General
    DEBUG = True
    HOST='127.0.0.1'
    PORT=3000
    SECRET_KEY='12345'

    # sqlalchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(BASE_DIR, 'db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False