#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""freecolormap -- a parts of xcb2

FreeColormap

cmap: COLORMAP

Errors: Colormap

This request deletes the association between the resource ID and the colormap
and frees the colormap storage. If the colormap is an installed map for a
screen, it is uninstalled (see UninstallColormap request). If the colormap is
defined as the colormap for a window (by means of CreateWindow or
ChangeWindowAttributes), the colormap for the window is changed to None, and a
ColormapNotify event is generated. The protocol does not define the colors
displayed for a window with a colormap of None.

This request has no effect on a default colormap for a screen.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['FreeColormap', 'FreeColormapChecked', ]


class FreeColormapAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xI'
    code = 79

    def _getbinary(self, cmap):
        buf = _StringIO()
        buf.write(_pack(self.fmt, cmap))
        return buf.getvalue()

    def __call__(self, cmap):
        """Request FreeColormap X protocol.

        @Arguments:
        - `cmap`:

        @Return:
        VoidCookie

        @Error:
        BadColormap
        """
        return self.request(self._getbinary(cmap))


class FreeColormap(FreeColormapAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cmap)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class FreeColormapChecked(FreeColormapAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cmap)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# freecolormap.py ends here
