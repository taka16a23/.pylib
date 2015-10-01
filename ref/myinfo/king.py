#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: king.py 87 2013-11-30 07:34:05Z t1 $
# $Revision: 87 $
# $Date: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
r""" king -- king server info

$Revision: 87 $

"""

import sys as _sys
from ref.myinfo import KAGI, KAGIMD5


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 87 $'
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
