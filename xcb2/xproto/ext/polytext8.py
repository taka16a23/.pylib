#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""polytext8 -- a parts of xcb2

PolyText8

drawable: DRAWABLE
gc: GCONTEXT
x, y: INT16
items: LISTofTEXTITEM8
where:
TEXTITEM8:	 TEXTELT8 or FONT
TEXTELT8:	 [delta: INT8
string: STRING8]

Errors: Drawable, Font, GContext, Match

The x and y coordinates are relative to the drawable's origin and specify the
baseline starting position (the initial character origin). Each text item is
processed in turn. A font item causes the font to be stored in gc and to be used
for subsequent text. Switching among fonts does not affect the next character
origin. A text element delta specifies an additional change in the position
along the x axis before the string is drawn; the delta is always added to the
character origin. Each character image, as defined by the font in gc, is treated
as an additional mask for a fill operation on the drawable.

All contained FONTs are always transmitted most significant byte first.

If a Font error is generated for an item, the previous items may have been
drawn.

For fonts defined with 2-byte matrix indexing, each STRING8 byte is interpreted
as a byte2 value of a CHAR2B with a byte1 value of zero.

GC components: function, plane-mask, fill-style, font, subwindow-mode,
clip-x-origin, clip-y-origin, clip-mask

GC mode-dependent components: foreground, background, tile, stipple,
tile-stipple-x-origin, tile-stipple-y-origin
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['PolyText8', 'PolyText8Checked', ]


class PolyText8Abstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xIIhh'
    code = 74

    def _getbinary(self, drawable, gc, x, y, items_len, items):
        buf = _StringIO()
        buf.write(_pack(self.fmt, drawable, gc, x, y, items_len))
        buf.write(str(buffer(_array('B', items))))
        return buf.getvalue()

    def __call__(self, drawable, gc, x, y, items_len, items):
        """Request PolyText8 X protocol.

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


class PolyText8(PolyText8Abstract):
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


class PolyText8Checked(PolyText8Abstract):
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
# polytext8.py ends here
