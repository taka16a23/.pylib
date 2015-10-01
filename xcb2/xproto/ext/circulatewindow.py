#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""circulatewindow -- a parts of xcb2

CirculateWindow

window: WINDOW
direction: { RaiseLowest, LowerHighest}

Errors: Value, Window

If some other client has selected SubstructureRedirect on the window, then a
CirculateRequest event is generated, and no further processing is
performed. Otherwise, the following is performed, and then a CirculateNotify
event is generated if the window is actually restacked.

For RaiseLowest, CirculateWindow raises the lowest mapped child (if any) that is
occluded by another child to the top of the stack. For LowerHighest,
CirculateWindow lowers the highest mapped child (if any) that occludes another
child to the bottom of the stack. Exposure processing is performed on formerly
obscured windows.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['CirculateWindow', 'CirculateWindowChecked', ]


class CirculateWindowAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xI'
    code = 14

    def _getbinary(self, direction, window):
        buf = _StringIO()
        buf.write(_pack(self.fmt, direction, window))
        return buf.getvalue()


    def __call__(self, direction, window):
        """CirculateWindow

        @Arguments:
        - `direction`:
        - `window`:

        @Return:
        VoidCookie

        @Error:
        BadValue, BadWindow
        """
        return self.request(self._getbinary(direction, window))


class CirculateWindow(CirculateWindowAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(direction, window)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class CirculateWindowChecked(CirculateWindowAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(direction, window)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# circulatewindow.py ends here
