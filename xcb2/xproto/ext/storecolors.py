#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""storecolors -- a parts of xcb2

StoreColors

cmap: COLORMAP
items: LISTofCOLORITEM
where:
COLORITEM:	[pixel: CARD32
 	 do-red, do-green, do-blue: BOOL
 	 red, green, blue: CARD16]

Errors: Access, Colormap, Value

This request changes the colormap entries of the specified pixels. The do-red,
do-green, and do-blue fields indicate which components should actually be
changed. If the colormap is an installed map for its screen, the changes are
visible immediately.

All specified pixels that are allocated writable in cmap (by any client) are
changed, even if one or more pixels produce an error. A Value error is generated
if a specified pixel is not a valid index into cmap, and an Access error is
generated if a specified pixel is unallocated or is allocated read-only. If more
than one pixel is in error, it is arbitrary as to which pixel is reported.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie, Iterator
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['StoreColors', 'StoreColorsChecked', ]


class StoreColorsAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xI'
    code = 89

    def _getbinary(self, cmap, items_len, items):
        buf = _StringIO()
        buf.write(_pack(self.fmt, cmap))
        for elt in Iterator(items, 5, 'items', True):
            buf.write(_pack('=IHHHBx', *elt))
        return buf.getvalue()

    def __call__(self, cmap, items_len, items):
        """Request StoreColors X protocol.

        @Arguments:
        - `cmap`:
        - `items_len`:
        - `items`:

        @Return:
        VoidCookie

        @Error:
        BadAccess, BadColormap, BadValue
        """
        return self.request(self._getbinary(cmap, items_len, items))


class StoreColors(StoreColorsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cmap, items_len, items)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class StoreColorsChecked(StoreColorsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cmap, items_len, items)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# storecolors.py ends here
