
# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

path = '/home/garts/garts/'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'garts.settings'

## then, for django >=1.5:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
