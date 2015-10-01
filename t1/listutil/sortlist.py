#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: sortlist.py 237 2014-11-28 17:01:54Z t1 $
# $Revision: 237 $
# $Date: 2014-11-29 02:01:54 +0900 (Sat, 29 Nov 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-11-29 02:01:54 +0900 (Sat, 29 Nov 2014) $

r"""sortlist -- DESCRIPTION

"""
# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 237 $'
__version__ = '0.1.0'


class SortedList(list):
    r"""SUMMARY
    """

    def __init__(self, iterable=[]):
        r"""SUMMARY

        __init__(value=None)

        @Arguments:
        - `value`:

        @Return:
        """
        list.__init__(self, iterable)
        self.sort()

    def __setitem__(self, i, item):
        super(SortedList, self).__setitem__(i, item)
        self.sort()

    def __delitem__(self, i):
        super(SortedList, self).__delitem__(i)
        self.sort()

    def __setslice__(self, i, j, other):
        super(SortedList, self).__setslice__(i, j, other)
        self.sort()

    def __add__(self, other):
        return self.__class__(super(SortedList, self).__add__(other))

    def __radd__(self, other):
        return self.__class__(super(SortedList, self).__radd__(other))

    def __iadd__(self, other):
        super(SortedList, self).__iadd__(other)
        self.sort()
        return self

    def __mul__(self, n):
        return self.__class__(super(SortedList, self).__mul__(n))

    def __imul__(self, n):
        super(SortedList, self).__imul__(n)
        self.sort()
        return self

    def append(self, item):
        super(SortedList, self).append(item)
        self.sort()

    def insert(self, i, item):
        super(SortedList, self).insert(i, item)
        self.sort()

    def pop(self, i=-1):
        result = super(SortedList, self).pop(i)
        self.sort()
        return result

    def remove(self, item):
        super(SortedList, self).remove(item)
        self.sort()

    def extend(self, other):
        super(SortedList, self).extend(other)
        self.sort()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sortlist.py ends here
