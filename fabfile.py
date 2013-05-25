''' Fabric deployment code
'''

from fabric.api import *

#env.hosts = ['dev.indratech.net']
#env.user = ['john']

def update_project():
        '''Pulls master from github, updates python and env
        '''
        with cd ('/home/john/production/portfolio'):
            sudo('git pull')
            with prefix('source /home/john/env/bin/activate'):
                # have to fix import on production.txt, change when fixed
                sudo('pip install -r requirements/base.txt')
                #run syncdb with production settings
                sudo('python Portfolio/manage.py syncdb --settings=Portfolio.settings.production')
                #South migration with production settings
                sudo('python Portfolio/manage.py migrate --settings=Portfolio.settings.production')
                #Collect static files into static root
                sudo('python Portfolio/manage.py collectstatic --settings=Portfolio.settings.production')

def restart_servers():
    '''restarts nginx an uWSGI
    '''
    sudo("service uwsgi restart")
    sudo("service nginx restart")

def deploy():
    '''Deploy project on production server
    '''
    update_project()
    restart_servers()