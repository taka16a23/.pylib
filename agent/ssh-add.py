#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: ssh-add.py 83 2013-11-22 07:03:11Z t1 $
# $Revision: 83 $
# $Date: 2013-11-22 16:03:11 +0900 (Fri, 22 Nov 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-11-22 16:03:11 +0900 (Fri, 22 Nov 2013) $

r""" ssh-add -- ssh-add command

$Revision: 83 $

"""

import sys as _sys

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 83 $'
__version__ = '0.1.0'


class SSHAdd(object):
    r"""
    """

    def __init__(self, ):
        r"""
        """
        pass




def list():
    r"""SUMMARY

    list()

    @Return:
    """
    pass

def add(filename, lifetime=None):
    r"""SUMMARY

    @Arguments:
    - `filename`:
    - `lifetime`: (int) seconds

    @Return:

    add(filename)
    """
    pass

def delete(etc):
    r"""SUMMARY

    delete(etc)

    @Arguments:
    - `etc`:

    @Return:
    """
    pass

def deleteall():
    r"""SUMMARY

    deleteall()

    @Return:
    """
    pass

def lock():
    r"""SUMMARY

    lock()

    @Return:
    """
    pass

def unlock():
    r"""SUMMARY

    unlock()

    @Return:
    """
    pass





def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# ssh-add.py ends here
