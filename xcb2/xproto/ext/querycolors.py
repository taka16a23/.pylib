#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""querycolors -- a parts of xcb2

QueryColors

cmap: COLORMAP
pixels: LISTofCARD32

colors: LISTofRGB
where:
RGB: [red, green, blue: CARD16]

Errors: Colormap, Value

This request returns the hardware-specific color values stored in cmap for the
specified pixels. The values returned for an unallocated entry are undefined. A
Value error is generated if a pixel is not a valid index into cmap. If more than
one pixel is in error, it is arbitrary as to which pixel is reported.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import QueryColorsCookie, QueryColorsReply


__all__ = ['QueryColors', 'QueryColorsUnchecked', ]


class QueryColorsAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xI'
    code = 91

    def _getbinary(self, cmap, pixels_len, pixels):
        buf = _StringIO()
        buf.write(_pack(self.fmt, cmap))
        buf.write(str(buffer(_array('I', pixels))))
        return buf.getvalue()

    def __call__(self, cmap, pixels_len, pixels):
        """Request QueryColors X protocol.

        @Arguments:
        - `cmap`:
        - `pixels_len`:
        - `pixels`:

        @Return:
        QueryColorsCookie

        @Error:
        BadColormap, BadValue
        """
        return self.request(self._getbinary(cmap, pixels_len, pixels))


class QueryColors(QueryColorsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cmap, pixels_len, pixels)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            QueryColorsCookie(), QueryColorsReply)


class QueryColorsUnchecked(QueryColorsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cmap, pixels_len, pixels)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            QueryColorsCookie(), QueryColorsReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# querycolors.py ends here
