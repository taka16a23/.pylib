#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: doxygen.py 87 2013-11-30 07:34:05Z t1 $
# $Revision: 87 $
# $Date: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
""" doxygen -- for doxygen

$Revision: 87 $

"""


# for debug
import os as _os
import cgitb as _cgitb
from portable import DRIVE_DIR

_cgitb.enable(format='text')


__revision__ = '$Revision: 87 $'
__version__ = '0.1.0'


DOXYGEN = {}

if 'nt' == _os.name:
    DOXYGEN.update({
        'bin': 'doxygen.exe',
        'conf': _os.path.join(DRIVE_DIR, 'Dos/graphviz/doxygen.conf'),
    })
elif 'posix' == _os.name:
    DOXYGEN.update(
        {'bin': 'doxygen',
         'binpath': '/usr/bin/doxygen',
         'conf': _os.path.expanduser('~/.emacs.d/data_e/doxygen.conf'),
        })

def test():
    "Test function."
    pass


if __name__ == '__main__':
    test()


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# doxygen.py ends here
