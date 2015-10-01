#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""limitlist -- DESCRIPTION


2014/05/15: Renamed LimitList._fill to LimitList.fill,
LimitList._length to LimitList.length,

"""
# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.1'


class MaxLimitedError(StandardError):
    r"""
    """
    def __init__(self, obj=None):
        self._obj = obj or ''

    def __str__(self, ):
        return repr(self._obj)


class LimitList(list):
    r"""
    """

    def __init__(self, initlist=None, length=None):
        r"""

        @Arguments:
        - `length`:
        """
        if initlist is not None:
            list.__init__(self, initlist)
        self.length = length or len(self)
        self[:] = self[:self.length]

    def islimited(self, ):
        r"""SUMMARY

        islimited()

        @Return:
        """
        return len(self) == self.length

    def append(self, item):
        r"""SUMMARY

        append(item)

        @Arguments:
        - `item`:

        @Return:
        """
        if self.islimited():
            raise MaxLimitedError(self)
        super(LimitList, self).append(item)

    def insert(self, i, item):
        r"""SUMMARY

        insert(i, item)

        @Arguments:
        - `i`:
        - `item`:

        @Return:
        """
        if self.islimited():
            raise MaxLimitedError(self)
        super(LimitList, self).insert(i, item)

    def extend(self, other):
        r"""SUMMARY

        extend(other)

        @Arguments:
        - `other`:

        @Return:
        """
        if self.length < len(self) + len(other):
            raise MaxLimitedError(self)
        super(LimitList, self).extend(other)

    def clear(self, ):
        r"""SUMMARY

        clear()

        @Return:

        @Error:
        """
        del self[:]

    def setlength(self, i):
        r"""SUMMARY

        setlength(i)

        @Arguments:
        - `i`:

        @Return:
        """
        self.length = i
        self[:] = self[:self.length]

    def __repr__(self, ):
        fmt = '{0.__class__.__name__}({1}, length={0.length})'.format
        return fmt(self, super(LimitList, self).__repr__())

    def __add__(self, other):
        if isinstance(other, LimitList):
            length = self.length + other.length
            return self.__class__(list(self) + list(other), length=length)
        return self.__class__(list(self) + list(other), length=self.length)

    def __radd__(self, other):
        if isinstance(other, LimitList):
            length = self.length + other.length
            return self.__class__(list(other) + list(self), length=length)
        return self.__class__(list(other) + list(self), length=self.length)

    def __iadd__(self, other):
        if self.length < len(self) + len(other):
            raise MaxLimitedError()
        return super(LimitList, self).__iadd__(other)


class ListFill(LimitList):
    r"""
    """

    def __init__(self, initlist=None, length=None, fill=None):
        r"""
        """
        LimitList.__init__(self, initlist=initlist, length=length)
        self.filler = fill
        self.__fill()

    def __fill(self, ):
        r"""SUMMARY

        _fill()

        @Return:
        """
        self[:] = (list(self) + [self.filler] * self.length)[:self.length]

    def pop(self, i=-1):
        r"""SUMMARY

        pop()

        @Return:
        """
        poped = super(ListFill, self).pop(i)
        self.__fill()
        return poped

    def remove(self, item):
        r"""SUMMARY

        remove(item)

        @Arguments:
        - `item`:

        @Return:
        """
        super(ListFill, self).remove(item)
        self.__fill()

    def clear(self, ):
        r"""SUMMARY

        clear()

        @Return:
        """
        self[:] = (self.filler, ) * self.length

    def __delitem__(self, num):
        self[num] = self.filler



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# limitlist.py ends here
