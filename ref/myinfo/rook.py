#!/usr/bin/env python
# -*- coding: utf-8 -*-
r""" rook -- rook router's info

"""

import sys as _sys
from ref.myinfo import KAGI, KAGIMD5

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'


HOST = 'taka16.no-ip.info'
LOCALIP = '192.168.1.1'
USER = 'root'
PORT = 12316
MAC = '00:1D:73:1A:C0:9C'
OPEN_PORT = [12317, 12318, 12319]
CLOSE_PORT = [12313, 12314, 12315]

def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# rook.py ends here
