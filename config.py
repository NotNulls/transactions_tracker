import os

base_dir = os.path.abspath(os.path.dirname(__name__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "vnnOPJjnJywygy3HPcf7v0BzTqmx8lucQvxmUQW_dsY"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'postgresql:///'+ os.path.join(base_dir,'tracker.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG=True