#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""abstract -- DESCRIPTION

"""


class BitFlagAbstract(object):
    r"""SUMMARY
    """
    def __init__(self, flags=0):
        r"""
        """
        self.flags = int(flags)

    def __int__(self, ):
        return int(self.flags)

    def __eq__(self, other):
        return self.flags == int(other)

    def __ne__(self, other):
        return self.flags != int(other)

    def __hash__(self, ):
        return hash(self.flags)

    def __and__(self, other):
        return self.__class__(self.flags & int(other))

    def __xor__(self, other):
        return self.__class__(self.flags ^ int(other))

    def __or__(self, other):
        return self.__class__(self.flags | int(other))

    def __lshift__(self, other):
        return self.__class__(self.flags << int(other))

    def __rshift__(self, other):
        return self.__class__(self.flags >> int(other))

    # def __invert__(self, ):
    #     return self.__class__(~self.bit)

    def __iand__(self, other):
        self.flags &= int(other)
        return self

    def __ixor__(self, other):
        self.flags ^= int(other)
        return self

    def __ior__(self, other):
        self.flags |= int(other)
        return self

    def __ilshift__(self, other):
        self.flags <<= int(other)
        return self

    def __irshift__(self, other):
        self.flags >>= int(other)
        return self

    def __nonzero__(self, ):
        return bool(self.flags)

    def __contains__(self, elt):
        return bool(self.__and__(elt))

    def __str__(self, ):
        # faster than '{0:b}'.format(8)
        # >>> timeit '{0:b}'.format(8)
        # 1000000 loops, best of 3: 1.07 µs per loop
        # >>> timeit str(bin(8))[2:]
        # 1000000 loops, best of 3: 671 ns per loop
        return str(bin(self.flags))[2:]

    def __repr__(self, ):
        return '{0.__class__.__name__}({1})'.format(self, self.flags)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# abstract.py ends here
