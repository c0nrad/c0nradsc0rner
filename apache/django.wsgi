
import os,sys

apache_configuration = os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)
sys.path.append('/home/djangotest/c0nradsc0rner')
sys.path.append('/home/djangotest')

os.environ['DJANGO_SETTINGS_MODULE'] = 'c0nradsc0rner.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

