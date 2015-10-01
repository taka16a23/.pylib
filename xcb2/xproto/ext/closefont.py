#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: closefont.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""closefont -- a parts of xcb2

CloseFont

font: FONT

Errors: Font

This request deletes the association between the resource ID and the font. The
font itself will be freed when no other resource references it.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['CloseFont', 'CloseFontChecked', ]


class CloseFontAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xI'
    code = 46

    def _getbinary(self, font):
        buf = _StringIO()
        buf.write(_pack(self.fmt, font))
        return buf.getvalue()

    def __call__(self, font):
        """Request CloseFont X protocol.

        @Arguments:
        - `font`:

        @Return:
        VoidCookie

        @Error:
        BadFont
        """
        return self.request(self._getbinary(font))


class CloseFont(CloseFontAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(font)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class CloseFontChecked(CloseFontAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(font)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# closefont.py ends here
