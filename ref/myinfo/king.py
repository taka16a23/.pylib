#!/usr/bin/env python
# -*- coding: utf-8 -*-
r""" king -- king server info

"""

import sys as _sys
from ref.myinfo import KAGI, KAGIMD5


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'


HOST = 'localhost' # portforwarding
USER = 't1'
IP = '192.168.1.123'
PORT = 12316
MAC = '00:01:80:61:d8:47'
CRYPTED_DISK = '/dev/mapper/VG-data'
DECRYPTED_DISK_NAME = 'data_crypt'


def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# king.py ends here
