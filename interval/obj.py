#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""obj -- DESCRIPTION

"""
from time import sleep as _sleep


class Interval(object):
    r"""Interval

    Interval is a object.
    Responsibility:
    """
    def __init__(self, value):
        r"""

        @Arguments:
        - `value`:
        """
        self._value = None
        self.set(value)

    def get(self, ):
        r"""SUMMARY

        get()

        @Return:

        @Error:
        """
        return self._value

    def set(self, value):
        r"""SUMMARY

        set(value)

        @Arguments:
        - `value`:

        @Return:

        @Error:
        """
        val = value
        if isinstance(val, (self.__class__, )):
            val = val.get()
        if not isinstance(val, (int, float)):
            # TODO: (Atami) [2015/01/25]
            raise TypeError()
        self._value = val

    def interval(self, ):
        r"""SUMMARY

        interval()

        @Return:

        @Error:
        """
        _sleep(self._value)

    def __call__(self, ):
        self.interval()

    def __repr__(self):
        return '{0.__class__.__name__}({0._value})'.format(self)

    def __str__(self):
        return str(self._value)

    def __cast(self, value):
        r"""SUMMARY

        __cast(value)

        @Arguments:
        - `value`:

        @Return:

        @Error:
        """
        if isinstance(value, (self.__class__, )):
            return value.get()
        return value

    def __cmp__(self, other):
        return cmp(self._value, self.__cast(other))

    def __lt__(self, other):
        return self._value < self.__cast(other)

    def __le__(self, other):
        return self._value <= self.__cast(other)

    def __gt__(self, other):
        return self._value > self.__cast(other)

    def __ge__(self, other):
        return self._value >= self.__cast(other)

    def __eq__(self, other):
        return self._value == self.__cast(other)

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(float(self))

    def __nonzero__(self):
        return bool(self._value)

    def __add__(self, other):
        return self.__class__(self._value + self.__cast(other))

    def __radd__(self, other):
        return other + int(self)

    def __iadd__(self, other):
        self.set(self._value + self.__cast(other))
        return self

    def __sub__(self, other):
        return self.__class__(self._value - self.__cast(other))

    def __rsub__(self, other):
        return other - int(self)

    def __isub__(self, other):
        self.set(self._value - self.__cast(other))
        return self

    def __mul__(self, other):
        return self.__class__(self._value * self.__cast(other))

    def __rmul__(self, other):
        return other * int(self)

    def __imul__(self, other):
        self.set(self._value * self.__cast(other))
        return self

    def __div__(self, other):
        return self.__class__(self._value / self.__cast(other))

    def __rdiv__(self, other):
        return other / int(self)

    def __idiv__(self, other):
        self.set(self._value / self.__cast(other))
        return self

    def __int__(self):
        return int(self._value)

    def __long__(self):
        return long(self._value)

    def __float__(self):
        return float(self._value)

    def __complex__(self):
        return complex(self._value)

    def __oct__(self):
        return oct(self._value)

    def __hex__(self):
        return hex(self._value)




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# obj.py ends here
