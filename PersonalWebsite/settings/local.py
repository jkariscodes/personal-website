import os

from .base import *

DEBUG = True

DATABASES = {
    'default': env.dj_db_url("DATABASE_URL")
}

TIME_ZONE = 'Africa/Nairobi'

# Email config
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Additional static configuration
STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]
STATIC_ROOT = STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Handling images
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
