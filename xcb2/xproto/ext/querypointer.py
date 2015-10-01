#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""querypointer -- a parts of xcb2

QueryPointer

window: WINDOW

root: WINDOW
child: WINDOW or None
same-screen: BOOL
root-x, root-y, win-x, win-y: INT16
mask: SETofKEYBUTMASK

Errors: Window

The root window the pointer is logically on and the pointer coordinates relative
to the root's origin are returned. If same-screen is False, then the pointer is
not on the same screen as the argument window, child is None, and win-x and
win-y are zero. If same-screen is True, then win-x and win-y are the pointer
coordinates relative to the argument window's origin, and child is the child
containing the pointer, if any. The current logical state of the modifier keys
and the buttons are also returned. Note that the logical state of a device (as
seen by means of the protocol) may lag the physical state if device event
processing is frozen.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import QueryPointerCookie, QueryPointerReply


__all__ = ['QueryPointer', 'QueryPointerUnchecked', ]


class QueryPointerAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xI'
    code = 38

    def _getbinary(self, window):
        buf = _StringIO()
        buf.write(_pack(self.fmt, window))
        return buf.getvalue()

    def __call__(self, window):
        """Request QueryPointer X protocol.

        @Arguments:
        - `window`:

        @Return:
        QueryPointerCookie

        @Error:
        BadWindow
        """
        return self.request(self._getbinary(window))


class QueryPointer(QueryPointerAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(window)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            QueryPointerCookie(), QueryPointerReply)


class QueryPointerUnchecked(QueryPointerAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(window)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            QueryPointerCookie(), QueryPointerReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# querypointer.py ends here
