#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""createcolormap -- a parts of xcb2

CreateColormap

mid: COLORMAP
visual: VISUALID
window: WINDOW
alloc: { None, All}

Errors: Alloc, IDChoice, Match, Value, Window

This request creates a colormap of the specified visual type for the screen on
which the window resides and associates the identifier mid with it. The visual
type must be one supported by the screen (or a Match error results). The initial
values of the colormap entries are undefined for classes GrayScale, PseudoColor,
and DirectColor. For StaticGray, StaticColor, and TrueColor, the entries will
have defined values, but those values are specific to the visual and are not
defined by the core protocol. For StaticGray, StaticColor, and TrueColor, alloc
must be specified as None (or a Match error results). For the other classes, if
alloc is None, the colormap initially has no allocated entries, and clients can
allocate entries.

If alloc is All, then the entire colormap is allocated writable. The initial
values of all allocated entries are undefined. For GrayScale and PseudoColor,
the effect is as if an AllocColorCells request returned all pixel values from
zero to N - 1, where N is the colormap-entries value in the specified
visual. For DirectColor, the effect is as if an AllocColorPlanes request
returned a pixel value of zero and red-mask, green-mask, and blue-mask values
containing the same bits as the corresponding masks in the specified
visual. However, in all cases, none of these entries can be freed with
FreeColors.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['CreateColormap', 'CreateColormapChecked', ]


class CreateColormapAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xIII'
    code = 78

    def _getbinary(self, alloc, mid, window, visual):
        buf = _StringIO()
        buf.write(_pack(self.fmt, alloc, mid, window, visual))
        return buf.getvalue()

    def __call__(self, alloc, mid, window, visual):
        """Request CreateColormap X protocol.

        @Arguments:
        - `alloc`:
        - `mid`:
        - `window`:
        - `visual`:

        @Return:
        VoidCookie

        @Error:
        BadAlloc, BadIDChoice, BadMatch, BadValue, BadWindow
        """
        return self.request(self._getbinary(alloc, mid, window, visual))


class CreateColormap(CreateColormapAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(alloc, mid, window, visual)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class CreateColormapChecked(CreateColormapAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(alloc, mid, window, visual)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# createcolormap.py ends here
