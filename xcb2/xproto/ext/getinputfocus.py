#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: getinputfocus.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""getinputfocus -- a parts of xcb2

GetInputFocus

focus: WINDOW or PointerRoot or None
revert-to: { Parent, PointerRoot, None}

This request returns the current focus state.
"""
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto.wcookie import WrapGetInputFocusCookie
from xcb2.xproto import GetInputFocusCookie, GetInputFocusReply


__all__ = ['GetInputFocus', 'GetInputFocusUnchecked', ]


class GetInputFocusAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """
    _binary = _pack('=xx2x')
    fmt = '=xx2x'
    code = 43

    def _getbinary(self, ):
        return self._binary

    def __call__(self, ):
        """Request GetInputFocus X protocol.

        @Return:
        GetInputFocusCookie
        """
        return WrapGetInputFocusCookie(
            self._connection, self.request(self._getbinary()))


class GetInputFocus(GetInputFocusAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request()

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            GetInputFocusCookie(), GetInputFocusReply)


class GetInputFocusUnchecked(GetInputFocusAbstract):
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
            GetInputFocusCookie(), GetInputFocusReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# getinputfocus.py ends here
