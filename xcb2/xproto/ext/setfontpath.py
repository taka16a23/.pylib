#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: setfontpath.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""setfontpath -- a parts of xcb2

SetFontPath

path: LISTofSTRING8

Errors: Value

This request defines the search path for font lookup. There is only one search
path per server, not one per client. The interpretation of the strings is
operating-system-dependent, but the strings are intended to specify directories
to be searched in the order listed.

Setting the path to the empty list restores the default path defined for the
server.

As a side effect of executing this request, the server is guaranteed to flush
all cached information about fonts for which there currently are no explicit
resource IDs allocated.

The meaning of an error from this request is system specific.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie, Iterator
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['SetFontPath', 'SetFontPathChecked', ]


class SetFontPathAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xH2x'
    code = 51

    def _getbinary(self, font_qty, font):
        buf = _StringIO()
        buf.write(_pack(self.fmt, font_qty))
        for elt in Iterator(font, -1, 'font', True):
            buf.write(_pack('=None', *elt))
        return buf.getvalue()

    def __call__(self, font_qty, font):
        """Request SetFontPath X protocol.

        @Arguments:
        - `font_qty`:
        - `font`:

        @Return:
        VoidCookie

        @Error:
        BadValue
        """
        return self.request(self._getbinary(font_qty, font))


class SetFontPath(SetFontPathAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(font_qty, font)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class SetFontPathChecked(SetFontPathAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(font_qty, font)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# setfontpath.py ends here
