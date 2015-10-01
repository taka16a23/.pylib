#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""warppointer -- a parts of xcb2

WarpPointer

src-window: WINDOW or None
dst-window: WINDOW or None
src-x, src-y: INT16
src-width, src-height: CARD16
dst-x, dst-y: INT16

Errors: Window

If dst-window is None, this request moves the pointer by offsets [dst-x, dst-y]
relative to the current position of the pointer. If dst-window is a window, this
request moves the pointer to [dst-x, dst-y] relative to dst-window's
origin. However, if src-window is not None, the move only takes place if
src-window contains the pointer and the pointer is contained in the specified
rectangle of src-window.

The src-x and src-y coordinates are relative to src-window's origin. If
src-height is zero, it is replaced with the current height of src-window minus
src-y. If src-width is zero, it is replaced with the current width of src-window
minus src-x.

This request cannot be used to move the pointer outside the confine-to window of
an active pointer grab. An attempt will only move the pointer as far as the
closest edge of the confine-to window.

This request will generate events just as if the user had instantaneously moved
the pointer.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['WarpPointer', 'WarpPointerChecked', ]


class WarpPointerAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xIIhhHHhh'
    code = 41

    def _getbinary(self, src_window, dst_window, src_x, src_y,
                src_width, src_height, dst_x, dst_y):
        buf = _StringIO()
        buf.write(_pack(self.fmt, src_window, dst_window, src_x, src_y,
                src_width, src_height, dst_x, dst_y))
        return buf.getvalue()

    def __call__(self, src_window, dst_window, src_x, src_y,
                src_width, src_height, dst_x, dst_y):
        """Request WarpPointer X protocol.

        @Arguments:
        - `src_window`:
        - `dst_window`:
        - `src_x`:
        - `src_y`:
        - `src_width`:
        - `src_height`:
        - `dst_x`:
        - `dst_y`:

        @Return:
        VoidCookie

        @Error:
        BadWindow
        """
        return self.request(
            self._getbinary(src_window, dst_window, src_x, src_y,
                            src_width, src_height, dst_x, dst_y))


class WarpPointer(WarpPointerAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(src_window, dst_window, src_x, src_y,
                src_width, src_height, dst_x, dst_y)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class WarpPointerChecked(WarpPointerAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(src_window, dst_window, src_x, src_y,
                src_width, src_height, dst_x, dst_y)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# warppointer.py ends here
