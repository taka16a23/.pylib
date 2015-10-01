#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: freecolors.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""freecolors -- a parts of xcb2

FreeColors

cmap: COLORMAP
pixels: LISTofCARD32
plane-mask: CARD32

Errors: Access, Colormap, Value

The plane-mask should not have any bits in common with any of the pixels. The
set of all pixels is produced by ORing together subsets of plane-mask with the
pixels. The request frees all of these pixels that were allocated by the client
(using AllocColor, AllocNamedColor, AllocColorCells, and AllocColorPlanes). Note
that freeing an individual pixel obtained from AllocColorPlanes may not actually
allow it to be reused until all of its related pixels are also freed. Similarly,
a read-only entry is not actually freed until it has been freed by all clients,
and if a client allocates the same read-only entry multiple times, it must free
the entry that many times before the entry is actually freed.

All specified pixels that are allocated by the client in cmap are freed, even if
one or more pixels produce an error. A Value error is generated if a specified
pixel is not a valid index into cmap. An Access error is generated if a
specified pixel is not allocated by the client (that is, is unallocated or is
only allocated by another client) or if the colormap was created with all
entries writable (using an alloc value of All in CreateColormap). If more than
one pixel is in error, it is arbitrary as to which pixel is reported.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['FreeColors', 'FreeColorsChecked', ]


class FreeColorsAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xII'
    code = 88

    def _getbinary(self, cmap, plane_mask, pixels_len, pixels):
        buf = _StringIO()
        buf.write(_pack(self.fmt, cmap, plane_mask, pixels_len))
        buf.write(str(buffer(_array('I', pixels))))
        return buf.getvalue()

    def __call__(self, cmap, plane_mask, pixels_len, pixels):
        """Request FreeColors X protocol.

        @Arguments:
        - `cmap`:
        - `plane_mask`:
        - `pixels_len`:
        - `pixels`:

        @Return:
        VoidCookie

        @Error:
        BadAccess, BadColormap, BadValue
        """
        return self.request(self._getbinary(cmap, plane_mask, pixels_len, pixels))


class FreeColors(FreeColorsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cmap, plane_mask, pixels_len, pixels)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class FreeColorsChecked(FreeColorsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cmap, plane_mask, pixels_len, pixels)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# freecolors.py ends here
