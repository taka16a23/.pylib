#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""getgeometry -- a parts of xcb2

GetGeometry

drawable: DRAWABLE

root: WINDOW
depth: CARD8
x, y: INT16
width, height, border-width: CARD16

Errors: Drawable

This request returns the root and current geometry of the drawable. The depth is
the number of bits per pixel for the object. The x, y, and border-width will
always be zero for pixmaps. For a window, the x and y coordinates specify the
upper-left outer corner of the window relative to its parent's origin, and the
width and height specify the inside size, not including the border.

It is legal to pass an InputOnly window as a drawable to this request.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import GetGeometryCookie, GetGeometryReply
from xcb2.xproto.wcookie import WrapGetGeometryCookie


__all__ = ['GetGeometry', 'GetGeometryUnchecked', ]


class GetGeometryAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """
    _head = _pack('=xx2x')
    fmt = 'I'
    code = 14

    def _getbinary(self, drawable):
        buf = _StringIO()
        buf.write(self._head)
        buf.write(_pack(self.fmt, drawable))
        return buf.getvalue()

    def __call__(self, drawable):
        """Request GetGeometry X protocol.

        @Arguments:
        - `drawable`: (int)

        @Return:
        WrapGetGeometryCookie

        @Error:
        BadDrawable
        """
        return WrapGetGeometryCookie(
            self._connection, self.request(self._getbinary(drawable)))


class GetGeometry(GetGeometryAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(drawable)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            GetGeometryCookie(), GetGeometryReply)


class GetGeometryUnchecked(GetGeometryAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(drawable)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            GetGeometryCookie(), GetGeometryReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# getgeometry.py ends here
