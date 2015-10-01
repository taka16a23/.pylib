#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""imagetext8 -- a parts of xcb2

ImageText8

drawable: DRAWABLE
gc: GCONTEXT
x, y: INT16
string: STRING8

Errors: Drawable, GContext, Match

The x and y coordinates are relative to the drawable's origin and specify the
baseline starting position (the initial character origin). The effect is first
to fill a destination rectangle with the background pixel defined in gc and then
to paint the text with the foreground pixel. The upper-left corner of the filled
rectangle is at:

	[x, y - font-ascent]
the width is:

	overall-width
and the height is:

	font-ascent + font-descent
The overall-width, font-ascent, and font-descent are as they would be returned
by a QueryTextExtents call using gc and string.

The function and fill-style defined in gc are ignored for this request. The
effective function is Copy, and the effective fill-style Solid.

For fonts defined with 2-byte matrix indexing, each STRING8 byte is interpreted
as a byte2 value of a CHAR2B with a byte1 value of zero.

GC components: plane-mask, foreground, background, font, subwindow-mode,
clip-x-origin, clip-y-origin, clip-mask
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['ImageText8', 'ImageText8Checked', ]


class ImageText8Abstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xIIhh'
    code = 76

    def _getbinary(self, string_len, drawable, gc, x, y, string):
        buf = _StringIO()
        buf.write(_pack(self.fmt, string_len, drawable, gc, x, y))
        buf.write(str(buffer(_array('b', string))))
        return buf.getvalue()

    def __call__(self, string_len, drawable, gc, x, y, string):
        """Request ImageText8 X protocol.

        @Arguments:
        - `string_len`:
        - `drawable`:
        - `gc`:
        - `x`:
        - `y`:
        - `string`:

        @Return:
        VoidCookie

        @Error:
        BadDrawable, BadGContext, BadMatch
        """
        return self.request(
            self._getbinary(string_len, drawable, gc, x, y, string))


class ImageText8(ImageText8Abstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(string_len, drawable, gc, x, y, string)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class ImageText8Checked(ImageText8Abstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(string_len, drawable, gc, x, y)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# imagetext8.py ends here
