#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""error -- part a keymap

"""

import sys as _sys
import os as _os

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'


class UnpackError(StandardError):
    r"""Unpack Exception."""

    def __init__(self, klass):
        super(UnpackError, self).__init__(klass)
        self._klass = klass

    def __str__(self, ):
        return self._klass.message


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# error.py ends here
