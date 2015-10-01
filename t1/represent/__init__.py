#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from inspect import getmembers

from dotavoider import ListDotAvoider


__version__ = "0.1.0"

__all__ = [ '' ]

class ReprPublic(object):
    r"""SUMMARY
    """

    def __repr__(self, ):
        fmt = '{0}={1}'.format
        lis, append = ListDotAvoider().append
        for name, value in getmembers(self):
            if not name.startswith(('_')) and value is not None:
                append(fmt(name, value))
        return '{0.__class__.__name__}({1})'.format(self, ', '.join(lis))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
