class Config():
    DEBUG = True
    TEST = True
    SERVER_NAME = '0.0.0.0:5000'


class Development(Config):
    ENV = 'development'
