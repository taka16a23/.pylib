#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: alloccolorcells.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""alloccolorcelles -- a parts of xcb2

AllocColorCells

cmap: COLORMAP
colors, planes: CARD16
contiguous: BOOL

pixels, masks: LISTofCARD32

Errors: Alloc, Colormap, Value

The number of colors must be positive, and the number of planes must be
nonnegative (or a Value error results). If C colors and P planes are requested,
then C pixels and P masks are returned. No mask will have any bits in common
with any other mask or with any of the pixels. By ORing together masks and
pixels, C*%2 sup P% distinct pixels can be produced; all of these are allocated
writable by the request. For GrayScale or PseudoColor, each mask will have
exactly one bit set to 1; for DirectColor, each will have exactly three bits set
to 1. If contiguous is True and if all masks are ORed together, a single
contiguous set of bits will be formed for GrayScale or PseudoColor, and three
contiguous sets of bits (one within each pixel subfield) for DirectColor. The
RGB values of the allocated entries are undefined.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import AllocColorCellsCookie, AllocColorCellsReply


__all__ = ['AllocColorCells', 'AllocColorCellsUnchecked', ]


class AllocColorCellsAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xIHH'
    code = 86

    def _getbinary(self, contiguous, cmap, colors, planes):
        r"""SUMMARY

        _getbinary(contiguous, cmap, colors, planes)

        @Arguments:
        - `contiguous`:
        - `cmap`:
        - `colors`:
        - `planes`:

        @Return:
        """
        buf = _StringIO()
        buf.write(_pack(self.fmt, contiguous, cmap, colors, planes))
        return buf.getvalue()

    def __call__(self, contiguous, cmap, colors, planes):
        """Request AllocColorCells X protocol.

        @Arguments:
        - `contiguous`: 
        - `cmap`: 
        - `colors`: 
        - `planes`: 

        @Return:
        AllocColorCellsCookie

        @Error:
        BadAlloc, BadColormap, BadValue
        """
        return self.request(self._getbinary(contiguous, cmap, colors, planes))


class AllocColorCells(AllocColorCellsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(contiguous, cmap, colors, planes)

        @Arguments:
        - `contiguous`:
        - `cmap`:
        - `colors`:
        - `planes`:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            AllocColorCellsCookie(), AllocColorCellsReply)


class AllocColorCellsUnchecked(AllocColorCellsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(contiguous, cmap, colors, planes)

        @Arguments:
        - `contiguous`:
        - `cmap`:
        - `colors`:
        - `planes`:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            AllocColorCellsCookie(), AllocColorCellsReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# alloccolorcelles.py ends here
