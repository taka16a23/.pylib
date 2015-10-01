#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""polytext16 -- a parts of xcb2

PolyText16

drawable: DRAWABLE
gc: GCONTEXT
x, y: INT16
items: LISTofTEXTITEM16
where:
TEXTITEM16:	 TEXTELT16 or FONT
TEXTELT16:	 [delta: INT8
string: STRING16]

Errors: Drawable, Font, GContext, Match

This request is similar to PolyText8, except 2-byte (or 16-bit) characters are
used. For fonts defined with linear indexing rather than 2-byte matrix indexing,
the server will interpret each CHAR2B as a 16-bit number that has been
transmitted most significant byte first (that is, byte1 of the CHAR2B is taken
as the most significant byte).
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['PolyText16', 'PolyText16Checked', ]


class PolyText16Abstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xIIhh'
    code = 75

    def _getbinary(self, drawable, gc, x, y, items_len, items):
        buf = _StringIO()
        buf.write(_pack(self.fmt, drawable, gc, x, y, items_len))
        buf.write(str(buffer(_array('B', items))))
        return buf.getvalue()

    def __call__(self, drawable, gc, x, y, items_len, items):
        """Request PolyText16 X protocol.

        @Arguments:
        - `drawable`:
        - `gc`:
        - `x`:
        - `y`:
        - `items_len`:
        - `items`:

        @Return:
        VoidCookie

        @Error:
        BadDrawable, BadFont, BadGContext, BadMatch
        """
        return self.request(self._getbinary(drawable, gc, x, y, items_len, items))


class PolyText16(PolyText16Abstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(drawable, gc, x, y, items_len, items)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class PolyText16Checked(PolyText16Abstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(drawable, gc, x, y, items_len, items)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# polytext16.py ends here
