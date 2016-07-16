import os

STATIC_ROOT = os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'static')
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'py',
        'USER': os.environ['OPENSHIFT_POSTGRESQL_DB_USERNAME'],
        'PASSWORD': os.environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD'],
        'PORT': os.environ['OPENSHIFT_POSTGRESQL_DB_PORT'],
        'HOST': os.environ['OPENSHIFT_POSTGRESQL_DB_HOST']
    }
}

SECRET_KEY = os.environ['key']