
print("in dev")
STATIC_ROOT = '/static/'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'py',
        'USER': 'iustitia'
    }
}