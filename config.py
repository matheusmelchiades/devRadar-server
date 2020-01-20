import os
from dotenv import load_dotenv

load_dotenv('.env')


class Config():
    DEBUG = True
    TEST = True
    HOST = os.getenv('HOST', default='localhost')
    PORT = os.getenv('PORT', default='5000')
    DB_NAME = os.getenv('DB_NAME', default='test')
    DB_USERNAME = os.getenv('DB_USERNAME', default='root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', default='123456')
    DB_HOST = os.getenv('DB_HOST', default='localhost')
    DB_PORT = os.getenv('DB_PORT', default='5000')


class Development(Config):
    ENV = 'development'
    DATABASE_URL = f'mongodb://{Config.DB_USERNAME}:{Config.DB_PASSWORD}@' + \
        f'{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}'
