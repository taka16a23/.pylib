#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""putimage -- a parts of xcb2

PutImage

drawable: DRAWABLE
gc: GCONTEXT
depth: CARD8
width, height: CARD16
dst-x, dst-y: INT16
left-pad: CARD8
format: { Bitmap, XYPixmap, ZPixmap}
data: LISTofBYTE

Errors: Drawable, GContext, Match, Value

This request combines an image with a rectangle of the drawable. The dst-x and
dst-y coordinates are relative to the drawable's origin.

If Bitmap format is used, then depth must be one (or a Match error results), and
the image must be in XY format. The foreground pixel in gc defines the source
for bits set to 1 in the image, and the background pixel defines the source for
the bits set to 0.

For XYPixmap and ZPixmap, the depth must match the depth of the drawable (or a
Match error results). For XYPixmap, the image must be sent in XY format. For
ZPixmap, the image must be sent in the Z format defined for the given depth.

The left-pad must be zero for ZPixmap format (or a Match error results). For
Bitmap and XYPixmap format, left-pad must be less than bitmap-scanline-pad as
given in the server connection setup information (or a Match error results). The
first left-pad bits in every scanline are to be ignored by the server. The
actual image begins that many bits into the data. The width argument defines the
width of the actual image and does not include left-pad.

GC components: function, plane-mask, subwindow-mode, clip-x-origin,
clip-y-origin, clip-mask

GC mode-dependent components: foreground, background
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['PutImage', 'PutImageChecked', ]


class PutImageAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xIIHHhhBB2x'
    code = 72

    def _getbinary(self, format, drawable, gc, width, height,
                dst_x, dst_y, left_pad, depth, data_len, data):
        buf = _StringIO()
        buf.write(_pack(self.fmt, format, drawable, gc, width, height,
                dst_x, dst_y, left_pad, depth, data_len))
        buf.write(str(buffer(_array('B', data))))
        return buf.getvalue()

    def __call__(self, format, drawable, gc, width, height,
                dst_x, dst_y, left_pad, depth, data_len, data):
        """Request PutImage X protocol.

        @Arguments:
        - `format`:
        - `drawable`:
        - `gc`:
        - `width`:
        - `height`:
        - `dst_x`:
        - `dst_y`:
        - `left_pad`:
        - `depth`:
        - `data_len`:
        - `data`:

        @Return:
        VoidCookie

        @Error:
        BadDrawable, BadGContext, BadMatch, BadValue
        """
        return self.request(self._getbinary(format, drawable, gc, width, height,
                dst_x, dst_y, left_pad, depth, data_len, data))


class PutImage(PutImageAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(format, drawable, gc, width, height,
                dst_x, dst_y, left_pad, depth, data_len, data)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class PutImageChecked(PutImageAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(format, drawable, gc, width, height,
                dst_x, dst_y, left_pad, depth, data_len, data)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# putimage.py ends here
