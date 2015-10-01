#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 100 2014-01-18 08:53:13Z t1 $
# $Revision: 100 $
# $Date: 2014-01-18 17:53:13 +0900 (Sat, 18 Jan 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-01-18 17:53:13 +0900 (Sat, 18 Jan 2014) $

r"""Name: __init__.py


"""
from predicate import isint

__revision__ = "$Revision: 100 $"
__version__ = "0.1.0"

__all__ = [ '' ]


class CountError(StandardError):
    r"""
    """
    pass


class Counter(object):
    r"""
    """

    def __init__(self, max_, init=0, exceptclass=CountError):
        r"""

        @Arguments:
        - `max_`:
        - `init`:
        - `exceptclass`:
        """
        if not isint(max_):
            raise ValueError('max_ must be integer. given {}'
                             .format(type(max_)))
        if not isint(init):
            raise ValueError('init must be integer. given {}'
                             .format(type(init)))
        self._max = max_
        self._init = init
        self.current = self._init
        self._exceptclass = exceptclass

    def __call__(self, ):
        self.count()

    def __repr__(self, ):
        return str(self.current)

    def count(self, add=1):
        r"""SUMMARY

        count()

        @Return:
        """
        self.current += add
        if self._max <= self.current:
            raise self._exceptclass()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
