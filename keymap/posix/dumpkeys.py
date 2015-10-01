#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""dumpkeys -- dumpkeys command

"""
import sys as _sys
import os as _os

from abstract.singleton import Singleton

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


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
