from .base import *

DEBUG = False

ADMINS = (
    ('Joseph K', 'contact@josephkariuki.com'),
)

ALLOWED_HOSTS = ['127.0.0.1']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ['POSTGRES_USER'],
#         'PASSWORD': os.environ['POSTGRES_PASSWORD'],
#         'DATABASE': os.environ['POSTGRES_DB'],
#         'HOST': '127.0.0.1',
#         'PORT': os.environ['POSTGRES_PORT'],
#     }
# }

DATABASES['default'] = dj_database_url.config()

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

django_heroku.settings(locals())
