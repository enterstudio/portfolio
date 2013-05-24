from .base import *
import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['dev.indratech.net']

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'mv845jh5498gfhKHGBN6hnuyN'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'portfolio_db',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'portfolio',
        'PASSWORD': 'e5DfDf37djhvVBsT5r6Ye',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

