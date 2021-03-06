#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""nt_agent -- SSH key agent for WindowsNT
"""

import os as _os
from time import sleep
from getpass import getpass

from portable import P_INTERNET
from pywinauto import application


__version__ = "0.1.1"

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


PAGEANT = _os.path.join(P_INTERNET, 'putty\\PAGEANT.EXE')

def add_keys(key):
    """summary
    """
    passwd = getpass('Enter private key password: ')
    cmd = PAGEANT + ' ' + key
    app = application.Application().start_(cmd)
    dialog = app[u'Pageant: Enter Passphrase']
    dialog.Edit1.SetText(passwd)
    del passwd
    dialog.Button1.Click()
    # if has error like not match password
    # then close dialog
    sleep(1.5)
    if dialog.Exists():
        dialog.Button2.Click()


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# nt_agent.py ends here
