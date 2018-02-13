#!/usr/bin/env python

# This file may be used instead of Apache mod_wsgi to run your Python
# web application with a different framework. A few examples are
# provided (cherrypi, gevent), but this file may be altered to run
# whatever framework is desired - or a completely customized service.

import imp
import os
import sys

try:
    virtenv = os.path.join(os.environ.get('OPENSHIFT_PYTHON_DIR','.'), 'virtenv')
    python_version = "python" + str(sys.version_info[0]) + "." + str(sys.version_info[1]) 
    os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib', python_version, 'site-packages')
    virtualenv = os.path.join(virtenv, 'bin','activate_this.py')
    if(sys.version_info[0] < 3):
        execfile(virtualenv, dict(__file__=virtualenv))
    else:
        exec(open(virtualenv).read(), dict(__file__=virtualenv))
                                    
except IOError:
    pass

# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
from server import Server
if __name__ == '__main__':
    #port = 9001#application.app.config['PORT']
    #ip = '0.0.0.0'#application.app.config['IP']
    HOST_NAME = os.environ.get('OPENSHIFT_APP_DNS','localhost')
    APP_NAME = os.environ.get('OPENSHIFT_APP_NAME','conveniences')
    IP = os.environ.get('OPENSHIFT_PYTHON_IP','0.0.0.0')
    PORT = int(os.environ.get('OPENSHIFT_PYTHON_PORT',8000))
    print(IP)
    print(PORT)
    Server('127.0.0.1',8080)