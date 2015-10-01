#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id$
# $Revision$
# $Date$
# $Author$
# $LastChangedBy$
# $LastChangedDate$
r""" error -- wm module error

$Revision$

"""

import sys as _sys
from Xlib.error import *

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision$'
__version__ = '0.1.0'


class TimeoutError(StandardError):
    def __init__(self, count):
        r"""
        """
        self.count = count


def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# error.py ends here
