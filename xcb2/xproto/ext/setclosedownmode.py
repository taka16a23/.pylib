#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: setclosedownmode.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""setclosedownmode -- a parts of xcb2

SetCloseDownMode

mode: { Destroy, RetainPermanent, RetainTemporary}

Errors: Value

This request defines what will happen to the client's resources at connection
close. A connection starts in Destroy mode. The meaning of the close-down mode
is described in section 10.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['SetCloseDownMode', 'SetCloseDownModeChecked', ]


class SetCloseDownModeAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2x'
    code = 112

    def _getbinary(self, mode):
        buf = _StringIO()
        buf.write(_pack(self.fmt, mode))
        return buf.getvalue()

    def __call__(self, mode):
        """Request SetCloseDownMode X protocol.

        @Arguments:
        - `mode`:

        @Return:
        VoidCookie

        @Error:
        BadValue
        """
        return self.request(self._getbinary(mode))


class SetCloseDownMode(SetCloseDownModeAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(mode)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class SetCloseDownModeChecked(SetCloseDownModeAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(mode)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# setclosedownmode.py ends here
