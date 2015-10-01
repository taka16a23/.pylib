#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: recolorcursor.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""recolorcursor -- a parts of xcb2

RecolorCursor

cursor: CURSOR
fore-red, fore-green, fore-blue: CARD16
back-red, back-green, back-blue: CARD16

Errors: Cursor

This request changes the color of a cursor. If the cursor is being displayed on
a screen, the change is visible immediately.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['RecolorCursor', 'RecolorCursorChecked', ]


class RecolorCursorAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xIHHHHHH'
    code = 96

    def _getbinary(self, cursor, fore_red, fore_green, fore_blue, back_red,
                back_green, back_blue):
        buf = _StringIO()
        buf.write(_pack(self.fmt, cursor, fore_red, fore_green, fore_blue,
                        back_red, back_green, back_blue))
        return buf.getvalue()

    def __call__(self, cursor, fore_red, fore_green, fore_blue, back_red,
                 back_green, back_blue):
        """Request RecolorCursor X protocol.

        @Arguments:
        - `cursor`:
        - `fore_red`:
        - `fore_green`:
        - `fore_blue`:
        - `back_red`:
        - `back_green`:
        - `back_blue`:

        @Return:
        VoidCookie

        @Error:
        BadCursor
        """
        return self.request(
            self._getbinary(cursor, fore_red, fore_green, fore_blue, back_red,
                back_green, back_blue))


class RecolorCursor(RecolorCursorAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cursor, fore_red, fore_green, fore_blue, back_red,
                back_green, back_blue)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class RecolorCursorChecked(RecolorCursorAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cursor, fore_red, fore_green, fore_blue, back_red,
                back_green, back_blue)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# recolorcursor.py ends here
