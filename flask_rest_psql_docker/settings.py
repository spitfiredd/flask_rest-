import os
from environs import Env

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


env = Env()
env.read_env()

ENV = env.str('FLASK_ENV', default='production')
DEBUG = ENV == 'development'
SECRET_KEY = env.str('SECRET_KEY', default='super-secret')
URL_PREFIX = '/api'

#  Sqlalchemy Settings (change to postgres)
SQLALCHEMY_DATABASE_URI = env.str(
    'DATABASE_URI',
    default='sqlite:///' + os.path.join(ROOT_DIR, 'people.db')
)
SQLALCHEMY_TRACK_MODIFICATIONS = ENV == 'development'
