#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""\
Posix_agent -- SSH key agent
"""

from contextlib import closing
from time import sleep
from getpass import getpass

import pexpect

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
