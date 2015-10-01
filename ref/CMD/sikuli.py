#!/usr/bin/env python
# -*- coding: utf-8 -*-
r""" sikuli -- for sikuli's informations.


"""


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')

import os as _os
import subprocess as _sbp

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
