#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""getscreensaver -- a parts of xcb2

GetScreenSaver

timeout, interval: CARD16
prefer-blanking: { Yes, No}
allow-exposures: { Yes, No}
This request returns the current screen-saver control values.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import GetScreenSaverCookie, GetScreenSaverReply


__all__ = ['GetScreenSaver', 'GetScreenSaverUnchecked', ]


class GetScreenSaverAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2x'
    code = 108

    def _getbinary(self, ):
        buf = _StringIO()
        buf.write(_pack(self.fmt, ))
        return buf.getvalue()

    def __call__(self, ):
        """Request GetScreenSaver X protocol.

        @Return:
        GetScreenSaverCookie
        """
        return self.request(self._getbinary())


class GetScreenSaver(GetScreenSaverAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request()

        @Arguments:

        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            GetScreenSaverCookie(), GetScreenSaverReply)


class GetScreenSaverUnchecked(GetScreenSaverAbstract):
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
            GetScreenSaverCookie(), GetScreenSaverReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# getscreensaver.py ends here
