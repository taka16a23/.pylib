#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""xfe -- xfe reference

"""

import sys as _sys
import os as _os

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'


NAME = 'xfe'
BIN = 'xfe'
BINPATH = '/usr/bin/xfe'


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# xfe.py ends here
