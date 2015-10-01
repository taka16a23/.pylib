#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""cleararea -- a parts of xcb2

ClearArea

window: WINDOW
x, y: INT16
width, height: CARD16
exposures: BOOL

Errors: Match, Value, Window

The x and y coordinates are relative to the window's origin and specify the
upper-left corner of the rectangle. If width is zero, it is replaced with the
current width of the window minus x. If height is zero, it is replaced with the
current height of the window minus y. If the window has a defined background
tile, the rectangle is tiled with a plane-mask of all ones and function of Copy
and a subwindow-mode of ClipByChildren. If the window has background None, the
contents of the window are not changed. In either case, if exposures is True,
then one or more exposure events are generated for regions of the rectangle that
are either visible or are being retained in a backing store.

It is a Match error to use an InputOnly window in this request.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['ClearArea', 'ClearAreaChecked', ]


class ClearAreaAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xIhhHH'
    code = 61

    def _getbinary(self, exposures, window, x, y, width, height):
        buf = _StringIO()
        buf.write(_pack(self.fmt, exposures, window, x, y, width, height))
        return buf.getvalue()


    def __call__(self, exposures, window, x, y, width, height):
        """Request ClearArea X protocol.

        @Arguments:
        - `exposures`:
        - `window`:
        - `x`:
        - `y`:
        - `width`:
        - `height`:

        @Return:
        VoidCookie

        @Error:
        BadMatch, BadValue, BadWindow
        """
        return self.request(
            self._getbinary(exposures, window, x, y, width, height))


class ClearArea(ClearAreaAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(exposures, window, x, y, width, height)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class ClearAreaChecked(ClearAreaAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(exposures, window, x, y, width, height)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# cleararea.py ends here
