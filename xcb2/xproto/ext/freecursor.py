#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""freecursor -- a parts of xcb2

"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['FreeCursor', 'FreeCursorChecked', ]


class FreeCursorAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xI'
    code = 95

    def _getbinary(self, cursor):
        buf = _StringIO()
        buf.write(_pack(self.fmt, cursor))
        return buf.getvalue()

    def __call__(self, cursor):
        """Request FreeCursor X protocol.

        @Arguments:
        - `cursor`:

        @Return:
        VoidCookie

        @Error:
        BadCursor
        """
        return self.request(self._getbinary(cursor))


class FreeCursor(FreeCursorAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cursor)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class FreeCursorChecked(FreeCursorAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cursor)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# freecursor.py ends here
