import django_heroku
import dj_database_url
from .base import *

DEBUG = False

ADMINS = (
    ('Joseph K', 'contact@josephkariuki.com'),
)

ALLOWED_HOSTS = ['.herokuapp.com', 'localhost', '127.0.0.1']

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

django_heroku.settings(locals())
