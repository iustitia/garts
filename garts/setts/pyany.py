import yaml

STATIC_ROOT = '/static/'

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/germanarticles/garts/db',
        'USER': 'iustitia'
    }
}

with open('/home/germanarticles/garts/garts/setts/key.yaml', 'r') as y:
    doc = yaml.load(y)

SECRET_KEY = doc['key']