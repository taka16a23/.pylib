#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: sortdict.py 146 2014-04-12 09:38:34Z t1 $
# $Revision: 146 $
# $Date: 2014-04-12 18:38:34 +0900 (Sat, 12 Apr 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-04-12 18:38:34 +0900 (Sat, 12 Apr 2014) $

r"""sortdict -- DESCRIPTION

"""
from collections import OrderedDict
import sys as _sys
import os as _os

from pythonutils import OrderedDict

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 146 $'
__version__ = '0.1.0'


class SortedDict(OrderedDict):
    r"""SUMMARY
    """

    def __init__(self, init_val=(), strict=False):
        r"""

        @Arguments:
        - `iargs`:
        - `kwargs`:
        """
        OrderedDict.__init__(self, init_val, strict)
        self.sort(key=lambda key: self[key])

    def __setitem__(self, key, val):
        super(SortedDict, self).__setitem__(key, val)
        self.sort(key=lambda key: self[key])


class ValueSortedDict(OrderedDict):
    r"""SUMMARY
    """

    def __init__(self, init_val=(), strict=False):
        r"""

        @Arguments:
        - `iargs`:
        - `kwargs`:
        """
        OrderedDict.__init__(self, init_val, strict)
        self.sort()

    def sort(self, *args, **kwargs):
        r"""SUMMARY

        sort(*args, **kwargs)

        @Arguments:
        - `args`:
        - `kwargs`:

        @Return:
        """
        super(ValueSortedDict, self).sort(key=lambda key: self[key])

    def __setitem__(self, key, val):
        super(ValueSortedDict, self).__setitem__(key, val)
        self.sort()


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sortdict.py ends here
