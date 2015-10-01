#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""getpointercontrol -- a parts of xcb2

GetPointerControl

acceleration-numerator, acceleration-denominator: CARD16
threshold: CARD16
This request returns the current acceleration and threshold for the pointer.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import GetPointerControlCookie, GetPointerControlReply


__all__ = ['GetPointerControl', 'GetPointerControlUnchecked', ]


class GetPointerControlAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2x'
    code = 106

    def _getbinary(self, ):
        buf = _StringIO()
        buf.write(_pack(self.fmt, ))
        return buf.getvalue()

    def __call__(self, ):
        """Request GetPointerControl X protocol.

        @Return:
        GetPointerControlCookie
        """
        return self.request(self._getbinary())


class GetPointerControl(GetPointerControlAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request()

        @Arguments:

        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            GetPointerControlCookie(), GetPointerControlReply)


class GetPointerControlUnchecked(GetPointerControlAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request()

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            GetPointerControlCookie(), GetPointerControlReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# getpointercontrol.py ends here
