# settings/local.py
from .base import *
import os
import ConfigParser

DEBUG = True
TEMPLATE_DEBUG = DEBUG

config = ConfigParser.ConfigParser()
config.readfp(open('/home/john/key_config/keys.cfg'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'portfolio_db',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': '5w0mpuS!',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Make this unique, and don't share it with anybody.
#SECRET_KEY = os.environ['SECRETKEY']
SECRET_KEY = config.get('secret', 'key')