#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: sikuli.py 87 2013-11-30 07:34:05Z t1 $
# $Revision: 87 $
# $Date: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
""" sikuli -- for sikuli's informations.

$Revision: 87 $

"""


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')

import os as _os
import subprocess as _sbp

__revision__ = '$Revision: 87 $'
__version__ = '0.1.0'

NAME = 'sikuli'
BIN = 'sikuli-ide'
BINPATH = '/usr/bin/sikuli-ide'
EXEPATH = _os.path.expanduser('~/sikuli')
RUNOPT = '-r'
EXEFORMAT = ' '.join((BINPATH, RUNOPT, '{0}'))

## set dictionary for .skl excutable path.
#
SKL_FILE = {}

try:
    _sklfiles = _os.listdir(EXEPATH)
except OSError:
    _sklfiles = ()

for d in _sklfiles:
    if d.endswith('.skl'):
        key = _os.path.splitext(d)[0]
        value = _os.path.join(EXEPATH, d)
        SKL_FILE.setdefault(key, value)

del _sklfiles

def sikulirun(path):
    """SUMMARY

    @Arguments:
    - `target`:

    @Return:
    """
    # _os.system(EXEFORMAT.format(path))
    return _sbp.call((BINPATH, RUNOPT, path))

def test():
    pass


if __name__ == '__main__':
    test()


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sikuli.py ends here
