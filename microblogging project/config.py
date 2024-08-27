import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SECRET_KEY = 'you will never guess'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'mydb.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_PASSWORD_SALT = 'thisissalt'
