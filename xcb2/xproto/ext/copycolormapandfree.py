#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: copycolormapandfree.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""copycolormapandfree -- a parts of xcb2

CopyColormapAndFree

mid, src-cmap: COLORMAP

Errors: Alloc, Colormap, IDChoice

This request creates a colormap of the same visual type and for the same screen
as src-cmap, and it associates identifier mid with it. It also moves all of the
client's existing allocations from src-cmap to the new colormap with their color
values intact and their read-only or writable characteristics intact, and it
frees those entries in src-cmap. Color values in other entries in the new
colormap are undefined. If src-cmap was created by the client with alloc All
(see CreateColormap request), then the new colormap is also created with alloc
All, all color values for all entries are copied from src-cmap, and then all
entries in src-cmap are freed. If src-cmap was not created by the client with
alloc All, then the allocations to be moved are all those pixels and planes that
have been allocated by the client using either AllocColor, AllocNamedColor,
AllocColorCells, or AllocColorPlanes and that have not been freed since they
were allocated.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['CopyColormapAndFree', 'CopyColormapAndFreeChecked', ]


class CopyColormapAndFreeAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xII'
    code = 80

    def _getbinary(self, mid, src_cmap):
        buf = _StringIO()
        buf.write(_pack(self.fmt, mid, src_cmap))
        return buf.getvalue()

    def __call__(self, mid, src_cmap):
        """Request CopyColormapAndFree X protocol.

        @Arguments:
        - `mid`:
        - `src_cmap`:

        @Return:
        VoidCookie

        @Error:
        BadAlloc, BadColormap, BadIDChoice
        """
        return self.request(self._getbinary(mid, src_cmap))


class CopyColormapAndFree(CopyColormapAndFreeAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(mid, src_cmap)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class CopyColormapAndFreeChecked(CopyColormapAndFreeAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(mid, src_cmap)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# copycolormapandfree.py ends here
