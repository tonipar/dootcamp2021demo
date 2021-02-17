import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('postgres://vngcxkkositxnz:b0f8bcc67d165b475ae44b0861f4e167b9540af9cbc5d5cef2935cd6e47b45ea@ec2-54-155-87-214.eu-west-1.compute.amazonaws.com:5432/df8ke85t4qi1s6') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False