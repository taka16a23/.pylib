#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: unmapsubwindows.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""unmapsubwindows -- a parts of xcb2

UnmapSubwindows

window: WINDOW

Errors: Window

This request performs an UnmapWindow request on all mapped children of the
window, in bottom-to-top stacking order.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['UnmapSubwindows', 'UnmapSubwindowsChecked', ]


class UnmapSubwindowsAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xI'
    code = 11

    def _getbinary(self, window):
        buf = _StringIO()
        buf.write(_pack(self.fmt, window))
        return buf.getvalue()

    def __call__(self, window):
        """UnmapSubwindows

        @Arguments:
        - `window`: (int)

        @Return:
        VoidCookie

        @Errors:
        BadWindow
        """
        return self.request(self._getbinary(window))


class UnmapSubwindows(UnmapSubwindowsAbstract):
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


class UnmapSubwindowsChecked(UnmapSubwindowsAbstract):
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
# unmapsubwindows.py ends here
