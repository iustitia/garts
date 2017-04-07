"""
Django settings for garts project.

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.utils.translation import ugettext_lazy as _
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import yaml

#if os.environ['HOME'] == '/home/iustitia':
#    from .setts.dev import *
#elif os.environ['HOME'] == '/home/germanarticles':
#    from .setts.pyany import *
#else:
#    from .setts.prod import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open(os.path.join(BASE_DIR, 'garts', 'key.yaml'), 'r') as y:
    doc = yaml.load(y)

ALLOWED_HOSTS = doc['ALLOWED_HOSTS']
DEBUG = doc['DEBUG']

STATIC_URL = doc['STATIC_URL']
MEDIA_URL = doc['MEDIA_URL']

ENV_PATH = os.path.abspath(os.path.dirname(__file__))

STATIC_ROOT = os.path.join(ENV_PATH, doc['STATIC_ROOT'])
MEDIA_ROOT = os.path.join(ENV_PATH, doc['MEDIA_ROOT'])

DATABASES = {
    'default': {
        'ENGINE': doc['DB_ENGINE'],
        'NAME': doc.get('DB_NAME') or os.path.join(ENV_PATH, doc.get('DB_SQLITENAME')),
        'USER': doc['DB_USER'],
        'PASSWORD': doc.get('PASSWORD'),
        'HOST': doc.get('DB_HOST'),
        'PORT': doc.get('PORT')
    }
}
SECRET_KEY = doc['key']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'wordbrowser',
    'lesson',
    'home',
    'quiz',
    'multichoice',
    'true_false',
    'essay'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'garts.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n'
            ],
        },
    },
]

WSGI_APPLICATION = 'garts.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'pl-pl'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en', _('English')),
    ('pl', _('Polish')),
)

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

LOGIN_REDIRECT_URL = '/'

if not DEBUG:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True