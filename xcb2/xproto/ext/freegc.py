#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: freegc.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""freegc -- a parts of xcb2

FreeGC

gc: GCONTEXT

Errors: GContext

This request deletes the association between the resource ID and the gcontext
and destroys the gcontext.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['FreeGC', 'FreeGCChecked', ]


class FreeGCAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xI'
    code = 60

    def _getbinary(self, gc):
        buf = _StringIO()
        buf.write(_pack(self.fmt, gc))
        return buf.getvalue()

    def __call__(self, gc):
        """Request FreeGC X protocol.

        @Arguments:
        - `gc`:

        @Return:
        VoidCookie

        @Error:
        BadGContext
        """
        return self.request(self._getbinary(gc))


class FreeGC(FreeGCAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(gc)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class FreeGCChecked(FreeGCAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(gc)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# freegc.py ends here
