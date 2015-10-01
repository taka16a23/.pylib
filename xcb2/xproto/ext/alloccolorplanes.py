#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""alloccolorplanes -- a parts of xcb2

AllocColorPlanes

cmap: COLORMAP
colors, reds, greens, blues: CARD16
contiguous: BOOL

pixels: LISTofCARD32
red-mask, green-mask, blue-mask: CARD32

Errors: Alloc, Colormap, Value

The number of colors must be positive, and the reds, greens, and blues must be
nonnegative (or a Value error results). If C colors, R reds, G greens, and B
blues are requested, then C pixels are returned, and the masks have R, G, and B
bits set, respectively. If contiguous is True, then each mask will have a
contiguous set of bits. No mask will have any bits in common with any other mask
or with any of the pixels. For DirectColor, each mask will lie within the
corresponding pixel subfield. By ORing together subsets of masks with pixels,
C*%2 sup R+G+B% distinct pixels can be produced; all of these are allocated
writable by the request. The initial RGB values of the allocated entries are
undefined. In the colormap, there are only C*%2 sup R% independent red entries,
C*%2 sup G% independent green entries, and C*%2 sup B% independent blue
entries. This is true even for PseudoColor. When the colormap entry for a pixel
value is changed using StoreColors or StoreNamedColor, the pixel is decomposed
according to the masks and the corresponding independent entries are updated.
AllocColor

cmap: COLORMAP
red, green, blue: CARD16

pixel: CARD32
red, green, blue: CARD16

Errors: Alloc, Colormap

This request allocates a read-only colormap entry corresponding to the closest
RGB values provided by the hardware. It also returns the pixel and the RGB
values actually used. Multiple clients requesting the same effective RGB values
can be assigned the same read-only entry, allowing entries to be shared.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import AllocColorPlanesCookie, AllocColorPlanesReply


__all__ = ['AllocColorPlanes', 'AllocColorPlanesUnchecked', ]


class AllocColorPlanesAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xIHHHH'
    code = 87

    def _getbinary(self, contiguous, cmap, colors, reds, greens, blues):
        r"""SUMMARY

        _getbinary(contiguous, cmap, colors, reds, greens, blues)

        @Arguments:
        - `contiguous`:
        - `cmap`:
        - `colors`:
        - `reds`:
        - `greens`:
        - `blues`:

        @Return:
        """
        buf = _StringIO()
        buf.write(_pack(self.fmt, contiguous, cmap, colors, reds, greens, blues))
        return buf.getvalue()

    def __call__(self, contiguous, cmap, colors, reds, greens, blues):
        """Request AllocColorPlanes X protocol.

        @Arguments:
        - `contiguous`:
        - `cmap`:
        - `colors`:
        - `reds`:
        - `greens`:
        - `blues`:

        @Return:
        AllocColorPlanesCookie

        @Error:
        BadAlloc, BadColormap, BadValue
        """
        return self.request(
            self._getbinary(contiguous, cmap, colors, reds, greens, blues))


class AllocColorPlanes(AllocColorPlanesAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(contiguous, cmap, colors, reds, greens, blues)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            AllocColorPlanesCookie(), AllocColorPlanesReply)


class AllocColorPlanesUnchecked(AllocColorPlanesAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(contiguous, cmap, colors, reds, greens, blues)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            AllocColorPlanesCookie(), AllocColorPlanesReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# alloccolorplanes.py ends here
