#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""userint -- DESCRIPTION

"""


class UserInt(object):
    """Class UserInt
    """
    # Attributes:
    def __init__(self, value=0):
        r"""

        @Arguments:
        - `value`:
        """
        self._value = None
        self.set(value)

    # Operations
    def get(self):
        """get

        @Return: int

        get()
        """
        return self._value

    def set(self, value):
        """set

        @Arguments:
        - `value`:

        @Return: None

        @Error: TypeError, ValueError

        set(0)
        """
        self._value = int(value)

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
        if isinstance(value, (UserInt, )):
            return int(value)
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
        # if isinstance(other, (int, self.__class__)):
        #     return self._value == int(other)
        # return False
        return self._value == self.__cast(other)

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self._value)

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

    def __pow__(self, other):
        return self.__class__(self._value ** self.__cast(other))

    def __rpow__(self, other):
        return other ** int(self)

    def __ipow__(self, other):
        self.set(self._value ** self.__cast(other))
        return self

    def __and__(self, other):
        return self.__class__(self._value & self.__cast(other))

    def __rand__(self, other):
        return other & int(self)

    def __iand__(self, other):
        self.set(self._value & self.__cast(other))
        return self

    def __xor__(self, other):
        return self.__class__(self._value ^ self.__cast(other))

    def __rxor__(self, other):
        return other ^ int(self)

    def __ixor__(self, other):
        self.set(self._value ^ self.__cast(other))
        return self

    def __or__(self, other):
        return self.__class__(self._value | self.__cast(other))

    def __ror__(self, other):
        return other | int(self)

    def __ior__(self, other):
        self.set(self._value | self.__cast(other))
        return self

    def __lshift__(self, other):
        return self.__class__(self._value << self.__cast(other))

    def __rlshift__(self, other):
        return other << int(self)

    def __ilshift__(self, other):
        self.set(self._value << self.__cast(other))
        return self

    def __rshift__(self, other):
        return self.__class__(self._value >> self.__cast(other))

    def __rrshift__(self, other):
        return other >> int(self)

    def __irshift__(self, other):
        self.set(self._value >> self.__cast(other))
        return self

    def __pos__(self):
        self.set(+self._value)
        return self

    def __neg__(self, ):
        self.set(-self._value)
        return self

    def __invert__(self, ):
        self.set(~self._value)
        return self

    def __int__(self):
        return self._value

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
# userint.py ends here
