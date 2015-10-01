#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""bell -- a parts of xcb2

Bell

percent: INT8

Errors: Value

This request rings the bell on the keyboard at a volume relative to the base
volume for the keyboard, if possible. Percent can range from -100 to 100
inclusive (or a Value error results). The volume at which the bell is rung when
percent is nonnegative is:

	base - [(base * percent) / 100] + percent
When percent is negative, it is:

	base + [(base * percent) / 100]
SetPointerMapping

map: LISTofCARD8

status: { Success, Busy}

Errors: Value

This request sets the mapping of the pointer. Elements of the list are indexed
starting from one. The length of the list must be the same as GetPointerMapping
would return (or a Value error results). The index is a core button number, and
the element of the list defines the effective number.

A zero element disables a button. Elements are not restricted in value by the
number of physical buttons, but no two elements can have the same nonzero value
(or a Value error results).

If any of the buttons to be altered are logically in the down state, the status
reply is Busy, and the mapping is not changed.

This request generates a MappingNotify event on a Success status.

    def test(self, percent):
        buf = _StringIO()
        buf.write(_pack(self.formt, percent)) # self.formt = '=xb2x'
        return self.request(buf.getvalue())

>>> import xcb2
>>> c=xcb2.connect()
>>> timeit c.core.Bell(2)
10000 loops, best of 3: 233 µs per loop

>>> timeit c.core.Bell.test(2)
1000 loops, best of 3: 873 µs per loop

    def test2(self, percent):
        buf = ''
        buf += self._head
        buf += _pack(self.fmt, percent)
        buf += self._tail
        return self.request(buf)

>>> timeit c.core.Bell.test2(2)
10000 loops, best of 3: 240 µs per loop

"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['Bell', 'BellChecked', ]


class BellAbstract(CoreMethodAbstract):
    r"""
    """
    _head = _pack('=x')
    _tail = _pack('2x')
    fmt = 'b'
    code = 104

    def _getbinary(self, percent):
        buf = _StringIO()
        buf.write(self._head)
        buf.write(_pack(self.fmt, percent))
        buf.write(self._tail)
        return buf.getvalue()

    def __call__(self, percent):
        """Request Bell X protocol.

        @Arguments:
        - `percent`: (int) -100 to 100

        @Return:
        VoidCookie

        @Error:
        BadValue
        """
        return self.request(self._getbinary(percent))


class Bell(BellAbstract):

    def request(self, binary):
        r"""SUMMARY

        @Arguments:
        - `binary`:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class BellChecked(BellAbstract):

    def request(self, binary):
        r"""SUMMARY

        @Arguments:
        - `binary`:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# bell.py ends here
