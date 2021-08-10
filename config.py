"""Class-based Flask app configuration."""
from os import environ, path
from dotenv import load_dotenv
import secrets

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))
print(basedir)

class Config:
    """Set Flask configuration vars from .env file."""

    # General Config
    SECRET_KEY = secrets.token_urlsafe(32)
    FLASK_ENV = environ.get('FLASK_ENV')
    FLASK_APP = 'wsgi.py'

    # Static Assets
    STATIC_FOLDER = environ.get('STATIC_FOLDER')
    TEMPLATES_FOLDER = environ.get('TEMPLATES_FOLDER')

    # DB Info
    MONGO_URI = environ.get('MONGO_URI')

    # ReCaptcha Info
    #RECAPTCHA_PUBLIC_KEY = environ.get('RECAPTCHA_PUB')
    #RECAPTCHA_PARAMETERS = {'size': '100%'}
