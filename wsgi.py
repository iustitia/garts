
# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys
#
## assuming your django settings file is at '/home/garts/mysite/mysite/settings.py'
## and your manage.py is is at '/home/garts/mysite/manage.py'
path = '/home/garts/garts/'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'garts.settings'

## then, for django >=1.5:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
