import yaml

STATIC_ROOT = '/static/'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'py',
        'USER': 'iustitia'
    }
}

with open('setts/key.yaml', 'r') as y:
    doc = yaml.load(y)

SECRET_KEY = doc['key']