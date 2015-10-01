#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: modifiers.py 277 2015-01-28 23:57:11Z t1 $
# $Revision: 277 $
# $Date: 2015-01-29 08:57:11 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 08:57:11 +0900 (Thu, 29 Jan 2015) $

r"""modifiers -- DESCRIPTION

"""
from struct import pack as _pack

from userint import UserInt
from wxcb.protocol.xproto.define import NamedModifierMask


class Modifiers(UserInt):
    r"""Modifiers

    Modifiers is a UserInt.
    Responsibility:
    """

    def pack(self, ):
        r"""Convert state to C short structs.

        @Return:
        (str)

        pack()

        >>> Modifiers(1).pack()
        '\x01\x00'
        """
        return _pack('H', self)

    def clear(self, ):
        r"""Clear state to 0.

        @Return:
        None

        clear()

        >>> mod = Modifiers(1)
        >>> mod.clear()
        >>> mod == Modifiers(0)
        True
        """
        self.set(0)

    def add(self, mod):
        r"""SUMMARY

        add(mod)

        @Arguments:
        - `mod`:

        @Return:

        @Error:
        """
        self._value |= mod

    def remove(self, mod):
        r"""SUMMARY

        remove(mod)

        @Arguments:
        - `mod`:

        @Return:

        @Error:
        """
        self._value ^= mod

    def isflaged(self, mod):
        r"""SUMMARY

        isflaged(mod)

        @Arguments:
        - `mod`:

        @Return:

        @Error:
        """
        return (self._value & mod) != 0

    def __iter__(self):
        yield self.__class__(0)
        for mod in NamedModifierMask:
            if (self & mod) != 0:
                yield self.__class__(mod)
        raise StopIteration()

    def __repr__(self, ):
        return '{0.__class__.__name__}({1}, "{2:b}", {3})'.format(
            self, int(self), int(self),
            [str(NamedModifierMask(mod)).split('.')[1] for mod in self if mod])

    def __str__(self, ):
        return '{0:b}'.format(self._value)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# modifiers.py ends here
