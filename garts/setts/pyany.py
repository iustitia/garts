import yaml

STATIC_ROOT = '/static/'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db',
        'USER': 'iustitia'
    }
}

with open('home/germanarticles/garts/setts/key.yaml', 'r') as y:
    doc = yaml.load(y)

SECRET_KEY = doc['key']