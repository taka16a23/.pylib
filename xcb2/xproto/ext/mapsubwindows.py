#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""mapsubwindows -- a parts of xcb2

MapSubwindows

window: WINDOW

Errors: Window

This request performs a MapWindow request on all unmapped children of the
window, in top-to-bottom stacking order.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['MapSubwindows', 'MapSubwindowsChecked', ]


class MapSubwindowsAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xI'
    code = 9

    def _getbinary(self, window):
        buf = _StringIO()
        buf.write(_pack(self.fmt, window))
        return buf.getvalue()

    def __call__(self, window):
        """Request MapSubwindows X protocol.

        @Arguments:
        - `window`: (int)

        @Return:
        VoidCookie

        @Error:
        BadWindow
        """
        return self.request(self._getbinary(window))


class MapSubwindows(MapSubwindowsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(window)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class MapSubwindowsChecked(MapSubwindowsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(window)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# mapsubwindows.py ends here
