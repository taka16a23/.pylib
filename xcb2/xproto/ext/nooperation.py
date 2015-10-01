#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: nooperation.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""nooperation -- a parts of xcb2

NoOperation

This request has no arguments and no results, but the request length field
allows the request to be any multiple of four bytes in length. The bytes
contained in the request are uninterpreted by the server.

This request can be used in its minimum four byte form as padding where
necessary by client libraries that find it convenient to force requests to begin
on 64-bit boundaries.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['NoOperation', 'NoOperationChecked', ]


class NoOperationAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2x'
    code = 127

    def _getbinary(self, ):
        buf = _StringIO()
        buf.write(_pack(self.fmt, ))
        return buf.getvalue()

    def __call__(self, ):
        """Request NoOperation X protocol.

        @Return:
        VoidCookie
        """
        return self.request(self._getbinary())


class NoOperation(NoOperationAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request()

        @Arguments:

        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class NoOperationChecked(NoOperationAbstract):
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
# nooperation.py ends here
