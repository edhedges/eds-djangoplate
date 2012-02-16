#fabric is awesome!
from fabric.api import *
from project import *

#Host and user information
env.hosts = ['edhedges.webfactional.com']
env.user = 'edhedges'
env.password = 'xxx'

#Home, webapps, and webfaction python paths
env.my_dir = '/home/edhedges'
env.webapps_dir = env.my_dir + '/webapps'
env.host_python_dir = env.my_dir + '/lib/python2.7'

#Level directly underneath webapps paths
env.projects_dir = env.webapps_dir + '/pyprojects'
env.static_dir = env.webapps_dir + '/static/%s' % PROJECT_ID

#Level directly under pyprojects paths
env.apache_bin = env.projects_dir + '/apache2/bin'
env.virtualenv_dir = env.projects_dir + '/virtualenvs'
env.current_project_dir = env.projects_dir + '/%s' % PROJECT_ID

#Level directly under virtualenvs
env.specific_virtualenv_dir = env.virtualenv_dir + '/%s' % PROJECT_ID

def run_local_server():
    """
    Use this command when you don't need new requirements installed or changes to the database.
    """
    local('python manage.py runserver')

def run_local():
    """
    Installs requirements, syncs the database, migrates with south, and runs the server.
    """
    local('pip install -r conf/requirements.txt')
    local('python manage.py syncdb')
    local('python manage.py migrate')
    local('python manage.py runserver')

#WRITE A FUNCTION THAT REPLACE THE httpd.conf in apache2/conf with the once in the boilerplate
#WRITE another function that does the .bashrc and .bash_profile things maybe

def set_up():
    """
    Sets up webfaction host with python2.7 directory and dependencies.
    """
    run('mkdir -p %s' % env.host_python_dir)
    run('easy_install-2.7 pip')
    run('pip-2.7 install virtualenv')
    run('pip-2.7 install virtualenvwrapper')
    run('mkdir -p %s' % env.virtualenv_dir)

def deploy():
    """
    Deploys the django project.
    """
    run('mkproject %s' % PROJECT_ID)
    with cd(env.projects_dir + '%s/' % PROJECT_ID):
        run('git init')
        run('git pull https://edhedges@bitbucket.org/edhedges/%s.git master' % PROJECT_ID)
        run('pip-2.7 install -r conf/requirements.txt')
        run('python2.7 manage.py new_secret')
        run('python2.7 manage.py syncdb')
        run('python2.7 manage.py migrate')
        run('mv static/* %s' % env.static_dir)
    with cd(env.apache_bin):
        run('./restart')
   
def destroy_all():
    """
    Destroys things created in setup and deploy. BE CAREFUL!
    """
    run('rm -rf %s' % env.host_python_dir)
    run('rm -rf %s' % env.virtualenv_dir)
    destroy_project()

def destroy_project():
    """
    Destroys the project associated with this fabfile
    """
    run('rm -rf %s' % env.current_project_dir)
    run('rm -rf %s' % env.specific_virtualenv_dir)
    run('rm -rf %s' % env.static_dir)
 
def rebuild_all():
    """
    Rebuilds entire webfaction by using destroy_all(), set_up(), and deploy()
    """
    destroy_all()
    set_up()
    deploy()

def migrate_proj(environment=None):
    """
    Migrates project.
    """
    if environment == 'local':
        local('python manage.py migrate')
    else:
        run('python2.7 manage.py migrate')

def restart_apache():
    """
    Restarts the apache2 instance.
    """
    run(env.apache_bin + '/restart')

def build_migration(app, environment=None):
    """
    Builds a migration for the specified app. 
    """
    if environment == 'local':
        local('python manage.py schemamigration %s' % app)
    else:
        run('python2.7 manage.py schemamigration %s'  % app)

def migrate_specific(app, environment=None):
    """
    Migrates the specified app.
    """
    if environment == 'local':
        local('python manage.py migrate %s' % app)
    else:
        run('python2.7 manage.py migrate %s' % app)

