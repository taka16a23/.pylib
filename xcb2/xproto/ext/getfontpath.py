#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: getfontpath.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""getfontpath -- a parts of xcb2

GetFontPath

path: LISTofSTRING8
This request returns the current search path for fonts.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import GetFontPathCookie, GetFontPathReply


__all__ = ['GetFontPath', 'GetFontPathUnchecked', ]


class GetFontPathAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2x'
    code = 52

    def _getbinary(self, ):
        buf = _StringIO()
        buf.write(_pack(self.fmt, ))
        return buf.getvalue()

    def __call__(self, ):
        """Request GetFontPath X protocol.

        @Return:
        GetFontPathCookie
        """
        return self.request(self._getbinary())


class GetFontPath(GetFontPathAbstract):
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
            GetFontPathCookie(), GetFontPathReply)


class GetFontPathUnchecked(GetFontPathAbstract):
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
            GetFontPathCookie(), GetFontPathReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# getfontpath.py ends here
