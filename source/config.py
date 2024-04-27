"""
This module loads configurations from the file.
"""

# Import standard modules.
import os
import json
import socket

def read(path):
    """
    Read JSON content from the file and returns it
    as a JSON object.
    """
    conf = {}
    filepath = os.path.join(os.path.dirname(__file__),path)
    with open(filepath,'r',encoding="utf-8") as file:
        conf = json.loads(file.read())
    return conf


# Load app configurations.
appconf = read('conf/app.conf')

# Construct system configurations.
_uname = os.uname()
_loadavg = os.getloadavg()
sysconf = {
    'OS':{
        'Name': _uname.sysname,
        'Release': _uname.release,
        'Version': _uname.version,
        'Machine Type': _uname.machine
    },
    'Host':{
        'Name': _uname.nodename,
        'IP': socket.gethostbyname(_uname.nodename)
    },
    'Process':{
        'Process ID': os.getpid(),
        'Parent Process ID': os.getppid(),
        'User ID': os.getuid(),
        'Group ID': os.getgid()
    },
    'Load Avg': {
        '1 min': _loadavg[0],
        '5 min': _loadavg[1],
        '15 min': _loadavg[2]
    },
    'CPU':{
        'Number of CPUs': os.cpu_count()
    }
}
