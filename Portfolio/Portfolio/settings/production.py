from .base import *
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'portfolio',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'portfolio',
        'PASSWORD': 'e5Df#Df3^7dT5&6r6Y*e',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ['SECRETKEY']