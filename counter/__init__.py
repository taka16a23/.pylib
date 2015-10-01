#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from predicate import isint

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
