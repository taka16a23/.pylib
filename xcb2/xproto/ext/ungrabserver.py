#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""ungrabserver -- a parts of xcb2

UngrabServer

This request restarts processing of requests and close-downs on other
connections.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['UngrabServer', 'UngrabServerChecked', ]


class UngrabServerAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2x'
    code = 37

    def _getbinary(self, ):
        buf = _StringIO()
        buf.write(_pack(self.fmt, ))
        return buf.getvalue()

    def __call__(self, ):
        """Request UngrabServer X protocol.

        @Return:
        VoidCookie
        """
        return self.request(self._getbinary())


class UngrabServer(UngrabServerAbstract):
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


class UngrabServerChecked(UngrabServerAbstract):
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
# ungrabserver.py ends here
