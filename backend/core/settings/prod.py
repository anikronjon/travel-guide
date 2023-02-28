import os
from .base import *

DEBUG = False


ALLOWED_HOSTS = ['anikronjon.us', 'anikronjon.com', '127.0.0.1', 'localhost']


ADMINS = [
    ('Anik Ronjon', 'anikronjon@gmail.com'),
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': '5432',
    }
}


# Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
