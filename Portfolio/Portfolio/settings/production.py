from .base import *
import os
import ConfigParser

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['dev.indratech.net']

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = '/home/john/production/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = '/home/john/production/static/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

ROOT_URLCONF = 'Portfolio.urls.production'

#load config file for keys
config = ConfigParser.ConfigParser()
config.readfp(open('/home/john/key_config/keys.cfg'))

# Make this unique, and don't share it with anybody.
#SECRET_KEY = 'mv845jh5498gfhKHGBN6hnuyN'

SECRET_KEY = config.get('secret', 'key')
dbkey = config.get('db', 'key')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'portfolio_db',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'portfolio',
        'PASSWORD': dbkey,
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

