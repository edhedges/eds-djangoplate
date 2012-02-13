import os
import sys
import site

from django.core.handlers.wsgi import WSGIHandler

from project import *

site.addsitedir('/home/edhedges/virtualenvs/%s/lib/python2.7/site-packages' % PROJECT_ID)

os.environ['DJANGO_SETTINGS_MODULE'] = '%s.settings' % PROJECT_ID

activate_this = os.path.expanduser('~/virtualenvs/%s/bin/activate_this.py' % PROJECT_ID)
execfile(activate_this, dict(__file__=activate_this))
	
project = '/home/edhedges/webapps/django_projects/%s/' % PROJECT_ID
workspace = os.path.dirname(project)
sys.path.append(workspace)

application = WSGIHandler()
