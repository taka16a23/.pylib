#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""mapwindow -- a parts of xcb2

MapWindow

window: WINDOW

Errors: Window

If the window is already mapped, this request has no effect.

If the override-redirect attribute of the window is False and some other client
has selected SubstructureRedirect on the parent, then a MapRequest event is
generated, but the window remains unmapped. Otherwise, the window is mapped, and
a MapNotify event is generated.

If the window is now viewable and its contents have been discarded, the window
is tiled with its background (if no background is defined, the existing screen
contents are not altered), and zero or more exposure events are generated. If a
backing-store has been maintained while the window was unmapped, no exposure
events are generated. If a backing-store will now be maintained, a full-window
exposure is always generated. Otherwise, only visible regions may be
reported. Similar tiling and exposure take place for any newly viewable
inferiors.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['MapWindow', 'MapWindowChecked', ]


class MapWindowAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """
    _head = _pack('=xx2x')
    fmt = 'I'
    code = 8

    def _getbinary(self, window):
        buf = _StringIO()
        buf.write(self._head)
        buf.write(_pack(self.fmt, window))
        return buf.getvalue()

    def __call__(self, window):
        """MapWindow X protocol request.

        @Arguments:
        - `window`: (int)

        @Return:
        VoidCookie

        @Error:
        BadWindow
        """
        return self.request(self._getbinary(window))


class MapWindow(MapWindowAbstract):
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


class MapWindowChecked(MapWindowAbstract):
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
# mapwindow.py ends here
