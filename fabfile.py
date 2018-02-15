from fabric.api import *

env.hosts = ['ubuntu@193.112.103.91']
env.password = 'HHcZI9sNndLrXut4'

def test():
	run('ls -l /tmp')