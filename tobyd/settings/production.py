import os
from .base import *
# import dj_database_url

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True

# DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['tobyd.net', '198.211.109.134', '127.0.0.1']

# Run manage.py check --deploy

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True

X_FRAME_OPTIONS = 'DENY'

CSRF_COOKIE_SECURE = True

# SSL settings (for when i organise certificate):

# SECURE_SSL_REDIRECT = True

# SESSION_COOKIE_SECURE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': 'localhost',
        'PORT': '',
    }
}

try:
    from .local import *
except ImportError:
    pass
