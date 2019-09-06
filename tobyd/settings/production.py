import os
from .base import *
# import dj_database_url

SECRET_KEY = os.environ['SECRET_KEY']

SESSION_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

DEBUG = False

# DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['tobyd.net', '198.211.109.134', 'localhost']

# Run manage.py check --deploy

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True

X_FRAME_OPTIONS = 'DENY'

CSRF_COOKIE_SECURE = True

# SSL settings (for when i organise certificate):

SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 120
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
        'HOST': 'localhost',
        'PORT': '',
    }
}

try:
    from .local import *
except ImportError:
    pass
