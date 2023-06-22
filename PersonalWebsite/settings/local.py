from .base import *
import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

ENVIRONMENT = "development"

SECRET_KEY = env("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")

INSTALLED_APPS.insert(5, "whitenoise.runserver_nostatic")
MIDDLEWARE.insert(2, "whitenoise.middleware.WhiteNoiseMiddleware")

# Database configuration
DATABASES = {
    "default": {
        "ENGINE": env("ENGINE"),
        "NAME": env("APP_DB_NAME"),
        "USER": env("APP_DB_USER"),
        "PASSWORD": env("APP_DB_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
}

# Static and Media files
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
WHITENOISE_USE_FINDERS = True
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "mediafiles"

# Email configuration
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
