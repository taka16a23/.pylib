#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: unmapwindow.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""unmapwindow -- a parts of xcb2

UnmapWindow

window: WINDOW

Errors: Window

If the window is already unmapped, this request has no effect. Otherwise, the
window is unmapped, and an UnmapNotify event is generated. Normal exposure
processing on formerly obscured windows is performed.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['UnmapWindow', 'UnmapWindowChecked', ]


class UnmapWindowAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xI'
    code = 10

    def _getbinary(self, window):
        buf = _StringIO()
        buf.write(_pack(self.fmt, window))
        return buf.getvalue()

    def __call__(self, window):
        """Request UnmapWindow X protocol.

        @Arguments:
        - `window`:

        @Return:
        VoidCookie

        @Error:
        BadWindow
        """
        return self.request(self._getbinary(window))


class UnmapWindow(UnmapWindowAbstract):
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


class UnmapWindowChecked(UnmapWindowAbstract):
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
# unmapwindow.py ends here
