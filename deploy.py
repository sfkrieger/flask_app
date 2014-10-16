import os
from fabric.operations import run
from fabric.state import env

#Host name and usernme for ssh
env.host_string = '54.186.247.5:22'
env.user = 'ubuntu'

#if you're doing this through commandline, must do KEY_LOCATION=$(pwd)/newkey.pem
try:
    env.key_filename = os.environ['KEY_NAME']
except KeyError:
    print 'You must set KEY_NAME to be the path to private key file.'
    exit(1)

#get into the right directory and pull the files
run("cd ~/repo && git pull")

#activate virtual environment
run(". ~/Virtualenvs/flaskenv/bin/activate && "
    "pip install -r ~/repo/requirements.txt")


run("sudo /etc/init.d/gunicorn restart")
#todo: missing migration