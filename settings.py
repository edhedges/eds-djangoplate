#Settings file for django projects

"""
This gets the host whether it is webfaction or just local development.
"""
import socket, os, sys

def contains(str, substr):
    if str.find(substr) != -1:
        return True
    else:
        return False

if contains(socket.gethostname(), 'webfaction'):
    LIVEHOST = True
else:
    LIVEHOST = False

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

"""
Settings for production
"""
if LIVEHOST:
    DEBUG = False
    TEMPLATE_DEBUG = DEBUG

    #Database configuration
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',       # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'xxx',                              # Or path to database file if using sqlite3.
            'USER': 'xxx',                              # Not used with sqlite3.
            'PASSWORD': 'xxx',                          # Not used with sqlite3.
            'HOST': '',                                 # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                                 # Set to empty string for default. Not used with sqlite3.
        }
    }

    #Email configuration
    EMAIL_HOST = 'smtp.webfaction.com'
    EMAIL_HOST_USER = 'xxx'
    EMAIL_HOST_PASSWORD = 'xxx'

    #Development url conf
    ROOT_URLCONF = 'urls'

    # Absolute filesystem path to the directory that will hold user-uploaded files.
    # Example: "/home/media/media.lawrence.com/media/"
    MEDIA_ROOT = ''

    # URL that handles the media served from MEDIA_ROOT. Make sure to use a
    # trailing slash.
    # Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
    MEDIA_URL = ''

    # Absolute path to the directory static files should be collected to.
    # Don't put anything in this directory yourself; store your static files
    # in apps' "static/" subdirectories and in STATICFILES_DIRS.
    # Example: "/home/media/media.lawrence.com/static/"
    STATIC_ROOT = '/home/edhedges/webapps/static/'

    # URL prefix for static files.
    # Example: "http://media.lawrence.com/static/"
    STATIC_URL = 'http://www.edhedges.com/static/'

    # Additional locations of static files
    STATICFILES_DIRS = (
        # Put strings here, like "/home/html/static" or "C:/www/django/static".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        '/home/edhedges/webapps/static/',
    )

    # URL prefix for admin static files -- CSS, JavaScript and images.
    # Make sure to use a trailing slash.
    # Examples: "http://foo.com/static/admin/", "/static/admin/".
    ADMIN_MEDIA_PREFIX = 'http://www.edhedges.com/static/admin/'

"""
Settings for development
"""
if not LIVEHOST:
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

    #Database configuration
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',         # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'dev',                                  # Or path to database file if using sqlite3.
            'USER': '',                                     # Not used with sqlite3.
            'PASSWORD': '',                                 # Not used with sqlite3.
            'HOST': '',                                     # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                                     # Set to empty string for default. Not used with sqlite3.
        }
    }

    #Development url conf
    ROOT_URLCONF = 'urls'

    #Email configuration
    #If you use this type this in terminal - python -m smtpd -n -c DebuggingServer localhost:1025
    #EMAIL_HOST = 'localhost'
    #EMAIL_PORT = 1025

    # Absolute filesystem path to the directory that will hold user-uploaded files.
    # Example: "/home/media/media.lawrence.com/media/"
    MEDIA_ROOT = ''

    # URL that handles the media served from MEDIA_ROOT. Make sure to use a
    # trailing slash.
    # Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
    MEDIA_URL = ''

    # Absolute path to the directory static files should be collected to.
    # Don't put anything in this directory yourself; store your static files
    # in apps' "static/" subdirectories and in STATICFILES_DIRS.
    # Example: "/home/media/media.lawrence.com/static/"
    STATIC_ROOT = ''

    # URL prefix for static files.
    # Example: "http://media.lawrence.com/static/"
    STATIC_URL = '/static/'
    
    # Additional locations of static files
    STATICFILES_DIRS = (
        # Put strings here, like "/home/html/static" or "C:/www/django/static".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        os.path.join(PROJECT_ROOT, 'static/'),
    )

    # URL prefix for admin static files -- CSS, JavaScript and images.
    # Make sure to use a trailing slash.
    # Examples: "http://foo.com/static/admin/", "/static/admin/".
    ADMIN_MEDIA_PREFIX = '/static/admin/'

"""
Common settings below
"""

ADMINS = (
    ('Eddie Hedges', 'edhedges@k-state.edu'),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/Regina'

LANGUAGE_CODE = 'en-us'

#Uncomment the next line and configure to use the site framework: https://docs.djangoproject.com/en/dev/ref/contrib/sites/
#SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

#Set one
SECRET_KEY = '191h_1gw1jr!$zyeqed((5)pghe62m-exv$e^!-m(q&3)ggbng'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

#May need to move this up into the if/else in the future
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates/'),
)

#Apps installed onto this project
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.admin',
    
    #Dependency apps
    #'south',
    #'fabric',

    #Sample apps included
    'apps.sample_one',
    'apps.sample_two',
    'apps.startup',

    #Add more apps when you write them!
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


