#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: beepmod.py 418 2015-08-07 00:25:11Z t1 $
# $Revision: 418 $
# $Date: 2015-08-07 09:25:11 +0900 (Fri, 07 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-07 09:25:11 +0900 (Fri, 07 Aug 2015) $
r""" beepmod -- load beepmod

$Revision: 418 $

"""

import os as _os
import sys as _sys
import subprocess as _sbp

try:
    import kmod
except ImportError:
    print('pip install kmod')
    print('if failed above command, do below')
    print('apt-get install libkmod-dev')
    print('pip install cython')


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 418 $'
__version__ = '0.1.0'

def load_pcspkr(force=False):
    r"""SUMMARY

    load_pcspkr()

    @Return:
    """
    kmd = kmod.Kmod()
    if force or not 'pcspkr' in (x for x, _ in kmd.list()): # list first
        kmd.modprobe('pcspkr')
    return 'pcspkr' in (x for x, _ in kmd.list())


def beep(frequency, amplitude, duration):
    """PC Beep function.

    @Arguments:
    - `frequency`:
    - `amplitude`:
    - `duration`:

    @Return:

    copied from
    http://bytes.com/topic/python/answers/25217-beeping-under-linux
    """
    sample = 8000
    half_period = int(sample / frequency / 2)
    beeps = chr(amplitude) * half_period + chr(0) * half_period
    beeps *= int(duration * frequency)
    # _os.system(' '.join(('echo', '-en', '\a', '>', '/dev/tty')))
    # s = _sbp.Popen(('echo', '-en', '\007'), stdout=_sbp.PIPE)

    with open('/dev/tty', 'w') as audio:
        audio.write('\xA0')
    # print(beeps)


def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# beepmod.py ends here
