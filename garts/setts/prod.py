import os

STATIC_ROOT = os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'static')
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'py',
        'USER': os.environ['PGUSER'],
        'PASSWORD': os.environ['PGPASSWORD']
    }
}
