#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: posix_agent.py 80 2013-11-22 07:02:28Z t1 $
# $Revision: 80 $
# $Date: 2013-11-22 16:02:28 +0900 (Fri, 22 Nov 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-11-22 16:02:28 +0900 (Fri, 22 Nov 2013) $

r"""\
Posix_agent -- SSH key agent
"""

from contextlib import closing
from time import sleep
from getpass import getpass

import pexpect

__revision__ = '$Revision: 80 $'
__version__ = '0.1.1'

def add_keys(key, passwd=None):
    """Add ssh key to keyring."""
    if not passwd:
        passwd = getpass('Enter private key password: ')
    cmd = 'ssh-add {}'.format(key)
    with closing(pexpect.spawn(cmd)) as child:
        sleep(1)
        child.sendline(passwd)
        sleep(1) # need this
        del passwd



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# posix_agent.py ends here
