#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: enable_disable.py 87 2013-11-30 07:34:05Z t1 $
# $Revision: 87 $
# $Date: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
r""" enable_disable -- enable disable decorator

$Revision: 87 $

"""

import sys as _sys

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 87 $'
__version__ = '0.1.0'


def unchanged(func):
    "This decorator doesn't add any behavior"
    return func

def disabled(func):
    "This decorator disables the provided function, and does nothing"
    def empty_func(*args,**kargs):
        pass
    return empty_func

# define this as equivalent to unchanged, for nice symmetry with disabled
enabled = unchanged


def _test():
    r"""Test function."""
    #
    # Sample use
    #

    GLOBAL_ENABLE_FLAG = True

    state = enabled if GLOBAL_ENABLE_FLAG else disabled
    @state
    def special_function_foo():
        print "function was enabled"


    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# enable_disable.py ends here
