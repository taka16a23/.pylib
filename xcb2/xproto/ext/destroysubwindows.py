#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""destroysubwindows -- a parts of xcb2

DestroySubwindows

window: WINDOW
Errors: Window

This request performs a DestroyWindow request on all children of the window, in
bottom-to-top stacking order.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['DestroySubwindows', 'DestroySubwindowsChecked', ]


class DestroySubwindowsAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xI'
    code = 5

    def _getbinary(self, window):
        buf = _StringIO()
        buf.write(_pack(self.fmt, window))
        return buf.getvalue()

    def __call__(self, window):
        """DestroySubwindows

        @Arguments:
        - `window`: (int)

        @Return:
        VoidCookie

        @Error:
        BadWindow
        """
        return self.request(self._getbinary(window))


class DestroySubwindows(DestroySubwindowsAbstract):
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


class DestroySubwindowsChecked(DestroySubwindowsAbstract):
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
# destroysubwindows.py ends here
