class BaseConfig():
    SECRET_KEY = "key"
    DEBUG = True
    TESTING = True

class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@localhost/flask_chat'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProConfig(BaseConfig):
    DEBUG = False
    TESTING = False