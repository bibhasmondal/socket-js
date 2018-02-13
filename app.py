import os
import sys
from server import Server
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

if __name__ == '__main__':
    HOST_NAME = os.environ.get('OPENSHIFT_APP_DNS','localhost')
    APP_NAME = os.environ.get('OPENSHIFT_APP_NAME','socketserver')
    IP = os.environ.get('OPENSHIFT_PYTHON_IP','0.0.0.0')
    PORT = int(os.environ.get('OPENSHIFT_PYTHON_PORT',8080))
    Server(IP,PORT)