""" Deployment of your django project.
"""

from fabric.api import *

def hello():
    print("Hello world!")

env.hosts = ['dev.indratech.net']
env.user = "moskeyombus"

def update_django_project():
    """ Updates the remote django project.
    """
    with cd('/home/moskeyombus/production/portfolio'):
        run('git pull')
        with prefix('source /home/moskeyombus/env/bin/activate'):
            run('pip install -r production.txt')
            run('python manage.py syncdb')
            run('python manage.py migrate') # if you use south
            run('python manage.py collectstatic --noinput')

def restart_webserver():
    """ Restarts remote nginx and uwsgi.
    """
    sudo("service uwsgi restart")
    sudo("/etc/init.d/nginx restart")

def deploy():
    """ Deploy Django Project.
    """
    update_django_project()
    restart_webserver()