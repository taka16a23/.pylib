#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: strpointer.py 298 2015-01-29 00:24:54Z t1 $
# $Revision: 298 $
# $Date: 2015-01-29 09:24:54 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:24:54 +0900 (Thu, 29 Jan 2015) $

r"""strpointer -- DESCRIPTION

"""


class StringPointer(object):
    r"""StringPointer

    StringPointer is a object.
    Responsibility:
    """
    def __init__(self, string, index=0):
        r"""

        @Arguments:
        - `string`:
        - `index`:
        """
        self._string = string
        self._index = None
        self.setindex(index)

    def getpoint(self, ):
        r"""SUMMARY

        getpoint()

        @Return:

        @Error:
        """
        if len(self._string) <= self._index or self._index < 0:
            return None
        return self._string[self._index]

    def getremain(self, ):
        r"""SUMMARY

        getremain()

        @Return:

        @Error:
        """
        return self._string[self._index:]

    def getindex(self, ):
        r"""SUMMARY

        getindex()

        @Return:

        @Error:
        """
        return self._index

    def hasright(self, ):
        r"""SUMMARY

        hasright()

        @Return:

        @Error:
        """
        return self._index + 1 < len(self._string)

    def setindex(self, index):
        r"""SUMMARY

        setindex(index)

        @Arguments:
        - `index`:

        @Return:

        @Error:
        """
        if not isinstance(index, int):
            # TODO: (Atami) [2014/10/28]
            raise TypeError()
        self._index = index

    def __nonzero__(self):
        return len(self._string) <= self._index + 1

    def __add__(self, other):
        if isinstance(other, int):
            return self.__class__(self._string, self._index + other)
        if isinstance(other, str):
            return self.__class__(self._string + other, self._index)
        # TODO: (Atami) [2014/10/28]
        raise TypeError()

    def __iadd__(self, other):
        if isinstance(other, int):
            self.setindex(self._index + other)
            return self
        if isinstance(other, str):
            self._string += other
            return self
        raise TypeError()

    def __sub__(self, other):
        if isinstance(other, int):
            return self.__class__(self._string, self._index - other)
        raise TypeError()

    def __isub__(self, other):
        if isinstance(other, int):
            self.setindex(self._index - other)
            return self
        raise TypeError()

    def __mul__(self, other):
        if isinstance(other, int):
            return self.__class__(self._string, self._index * other)
        raise TypeError()

    def __imul__(self, other):
        if isinstance(other, int):
            self.setindex(self._index * other)
            return self
        raise TypeError()

    def __div__(self, other):
        if isinstance(other, int):
            return self.__class__(self._string, self._index / other)
        raise TypeError()

    def __idiv__(self, other):
        if isinstance(other, int):
            self.setindex(self._index / other)
            return self

    def __lshift__(self, other):
        return self - other

    def __rshift__(self, other):
        return self + other

    def __ilshift__(self, other):
        self.setindex(self._index - other)
        return self

    def __irshift__(self, other):
        self.setindex(self._index + other)
        return self

    def __int__(self):
        return self._index

    def __long__(self):
        return long(int(self))

    def __len__(self):
        return len(self._string)

    def __getitem__(self, key):
        return self._string[key]

    def __setitem__(self, key, val):
        self._string[key] = val

    def __delitem__(self, key):
        del self._string[key]
        if len(self) < self._index:
            self._index -= 1

    def __contains__(self, elm):
        return elm in self._string

    def __iter__(self):
        return self

    def __repr__(self):
        return (
            '{0.__class__.__name__}("{0._string}", index={0._index}, on="{1}")'
            .format(self, self.getpoint()))

    def next(self, ):
        if len(self) < self._index:
            raise StopIteration()
        char = self._string[self._index]
        self._index += 1
        return char



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# strpointer.py ends here
