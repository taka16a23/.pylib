#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: grabserver.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""grabserver -- a parts of xcb2

GrabServer

This request disables processing of requests and close-downs on all connections
other than the one this request arrived on.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['GrabServer', 'GrabServerChecked', ]


class GrabServerAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2x'
    code = 36

    def _getbinary(self, ):
        buf = _StringIO()
        buf.write(_pack(self.fmt, ))
        return buf.getvalue()

    def __call__(self, ):
        """Request GrabServer X protocol.

        @Return:
        VoidCookie
        """
        return self.request(self._getbinary())


class GrabServer(GrabServerAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request()

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class GrabServerChecked(GrabServerAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request()

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# grabserver.py ends here
