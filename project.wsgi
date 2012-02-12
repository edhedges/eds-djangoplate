import os
import sys

from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
sys.path = ['/home/edhedges/webapps/django/edhedges', '/home/edhedges/webapps/django/lib/python2.7'] + sys.path
application = WSGIHandler()
