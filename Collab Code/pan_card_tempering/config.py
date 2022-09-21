import os
from os import environ
from pickle import FALSE, TRUE
class Config(object):
    DEBUG=FALSE
    TESTING=FALSE

    basedir=os.path.abspath(os.path.dirname(__file__))


    SECRET_KEY='Pratik'

    UPLOADS='E:\Udemy courses PDF\75 machine learning Projects\Collab Code'

    SESSION_COOKIE_SECURE=TRUE
    DEFAULT_THEME=None

    class DevelopmentConfig(Config):
        DEBUG=True
        ESSION_COOKIE_SECURE=FALSE

    class DebugConfig(Config):
        DEBUG=False