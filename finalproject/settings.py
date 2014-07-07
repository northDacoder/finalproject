"""
Django settings for finalproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/Users/northDacoder/Desktop/Dropbox/finalproject/developer_app/static/'
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4#kaw@@_(0ys%qt_9^u2qp0f&h4dhd1975fjesjwkl)=$o7&%w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

#SOME_SECRET_KEY = os.environ["SOME_SECRET_KEY"]


# from django.core.exceptions import ImproperlyConfigured
#
# def get_env_variable(var_name):
#     """
#     :param var_name: Get the environment variable or return exception """
#     try:
#         return os.environ[var_name]
#     except KeyError:
#         error_mes = "Set the $s environment variable" % var_name
#         raise ImproperlyConfigured(error_msg)



ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'developer_app',
    'company_app',
    'registration',
    'tastypie',
    'tastypie_swagger',
    'south',
)



MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'finalproject.urls'

WSGI_APPLICATION = 'finalproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgres_psycopg2',
        'NAME': 'finalproject',
    }
}



TASTYPIE_DEFAULT_FORMATS = ['json']

TASTYPIE_DATETIME_FORMATTING = 'iso-8601'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

ACCOUNT_ACTIVATION_DAYS = 7

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_MEDIA = '/media/'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/Users/northDacoder/Desktop/Dropbox/finalproject/media/'


TASTYPIE_SWAGGER_API_MODULE = "tastypie_tutorial.urls.v1_api"

LOGIN_REDIRECT_URL = '/#/developers'


try:
    from local_settings import *
except ImportError:
    pass
