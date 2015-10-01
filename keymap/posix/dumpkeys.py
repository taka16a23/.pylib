#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: dumpkeys.py 98 2014-01-11 10:09:59Z t1 $
# $Revision: 98 $
# $Date: 2014-01-11 19:09:59 +0900 (Sat, 11 Jan 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-01-11 19:09:59 +0900 (Sat, 11 Jan 2014) $

r"""dumpkeys -- dumpkeys command

"""
import sys as _sys
import os as _os

from abstract.singleton import Singleton

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 98 $'
__version__ = '0.1.0'


class DumpKeys(Singleton):
    r"""Buffering key by dumpkeys command.

    This class is Singleton.
    command line: 'dumpkeys --keys-only --separate-lines'
    and iterable like this.
    for line in DumpKeys():
        print(line)
    """
    _cmdline = 'dumpkeys --keys-only --separate-lines'

    def __init__(self, ):
        self.lines = _os.popen(self._cmdline).readlines()

    def __iter__(self, ):
        for line in self.lines:
            yield line



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# dumpkeys.py ends here
