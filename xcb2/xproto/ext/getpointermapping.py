#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""getpointermapping -- a parts of xcb2

GetPointerMapping


map: LISTofCARD8
This request returns the current mapping of the pointer. Elements of the list
are indexed starting from one. The length of the list indicates the number of
physical buttons.

The nominal mapping for a pointer is the identity mapping: map[i]=i.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import GetPointerMappingCookie, GetPointerMappingReply


__all__ = ['GetPointerMapping', 'GetPointerMappingUnchecked', ]


class GetPointerMappingAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2x'
    code = 117

    def _getbinary(self, ):
        buf = _StringIO()
        buf.write(_pack(self.fmt, ))
        return buf.getvalue()

    def __call__(self, ):
        """Request GetPointerMapping X protocol.

        @Return:
        GetPointerMappingCookie
        """
        return self.request(self._getbinary())


class GetPointerMapping(GetPointerMappingAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request()

        @Arguments:

        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            GetPointerMappingCookie(), GetPointerMappingReply)


class GetPointerMappingUnchecked(GetPointerMappingAbstract):
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
            GetPointerMappingCookie(), GetPointerMappingReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# getpointermapping.py ends here
