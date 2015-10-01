#!/usr/bin/env python
# -*- coding: utf-8 -*-
r""" enable_disable -- enable disable decorator


"""

import sys as _sys

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


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
