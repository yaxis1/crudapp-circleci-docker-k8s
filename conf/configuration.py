
class Config(object):
    DEBUG = False
    TESTING = False
    DB_NAME = "Mongo_db"
    RUNNING_ON = "http://127.0.0.1/apidocs/"



class TestingConfig(Config):

    TESTING = True

