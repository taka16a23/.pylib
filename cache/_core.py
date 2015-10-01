#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: _core.py 87 2013-11-30 07:34:05Z t1 $
# $Revision: 87 $
# $Date: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
r""" _core -- Abstract Cache.

$Revision: 87 $

"""

import sys as _sys
from time import time as _time

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 87 $'
__version__ = '0.1.0'


class Cache(object):
    r"""
    """

    def __init__(self, duration=60):
        r"""

        Arguments:
        - `duration`:
        """
        self._duration = duration
        self._cached_time = 0
        self._cache = None

    def _set_cache(self, value):
        r"""SUMMARY

        @Return:
        """
        self._set_cached_time()
        self._cache = value

    def _get_cache(self):
        r"""SUMMARY

        @Return:
        """
        return self._cache

    def _set_cached_time(self):
        r"""SUMMARY

        @Return:
        """
        self._cached_time = _time()

    def _isneed_cache(self):
        r"""SUMMARY

        @Return:
        """
        return (self._cached_time + self._duration) < _time()


def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _core.py ends here
