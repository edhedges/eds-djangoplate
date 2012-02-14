from fabric.api import *

env.hosts = ['edhedges.webfactional.com']
env.user = 'edhedges'
env.django_dir = '/home/edhedges/webapps/django_projects/'
env.static_dir = '/home/edhedges/webapps/static/'

def prepare():
    """
    Prepares webfaction host.
    """
    run('mkdir -p /home/edhedges/lib/python2.7/')
    run('easy_install pip')
    run('pip install virtualenv')
    run('pip install virtualenvwrapper')
    run('mkdir -p /home/edhedges/virtualenvs')

def deploy(project_name):
    """
    Deploys the django project.
    """
    run('mkproject %s --no-site-packages' % project_name)
    with cd(env.django_dir + '%s' % project_name):
        run('git init')
        run('git pull edhedges@bitbucket.org:edhedges/%s.git master' % project_name)
        run('mv %s.wsgi ../' % project_name)
        run('pip install -r requirements.txt')
        run('python manage.py new_secret')
        run('python manage.py syncdb')
        run('mv static/* %s' % env.static_dir)
    run(env.django_dir + 'apache2/bin/restart')

def migrate_specific():
    """
    Migrates the specified app.
    """
    run('python manage.py migrate')

def restart_apache():
    """
    Restarts the apache2 instance.
    """
    run(env.django_dir + 'apache2/bin/restart')

def build_migration(app):
    """ 
    Builds a migration for the specified app. 
    """
    run('python manage.py schemamigration %s'  % app)

def migrate_specific(app):
    """
    Migrates the specified app.
    """
    run('python manage.py migrate %s' % app)

