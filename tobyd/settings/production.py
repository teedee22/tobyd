import os
from .base import *
# import dj_database_url

SECRET_KEY = os.environ['SECRET_KEY']

SESSION_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

DEBUG = False


ALLOWED_HOSTS = ['tobyd.net', '198.211.109.134', 'localhost']

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

# AWS
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'https://' + '.s3.amazonaws.com/' + 'media/'

# Mail settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ['MG_HOST']
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ['MG_ADDRESS']
EMAIL_HOST_PASSWORD =os.environ['MG_PASSWORD']
EMAIL_USE_TLS = True

try:
    from .local import *
except ImportError:
    pass
