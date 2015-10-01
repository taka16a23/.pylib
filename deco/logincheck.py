#!/usr/bin/env python
# -*- coding: utf-8 -*-
r""" logincheck -- logincheck decorator


"""

import sys as _sys

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'

# https://wiki.python.org/moin/PythonDecoratorLibrary#Access_control
class LoginCheck:
    '''
    This class checks whether a user
    has logged in properly via
    the global "check_function". If so,
    the requested routine is called.
    Otherwise, an alternative page is
    displayed via the global "alt_function"
    '''
    def __init__(self, f):
        self._f = f

    def __call__(self, *args):
        Status = check_function()
        if Status is 1:
            return self._f(*args)
        else:
            return alt_function()


def check_function():
    return test


def alt_function():
    return 'Sorry - this is the forced behaviour'


def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    @LoginCheck
    def display_members_page():
        print 'This is the members page'


    test = 0
    display_members_page()
    # Displays "Sorry - this is the forced behaviour"

    test = 1
    display_members_page()
    # Displays "This is the members page"
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# logincheck.py ends here
