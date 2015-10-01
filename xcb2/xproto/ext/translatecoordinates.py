#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: translatecoordinates.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""translatecoordinates -- a parts of xcb2

TranslateCoordinates

src-window, dst-window: WINDOW
src-x, src-y: INT16

same-screen: BOOL
child: WINDOW or None
dst-x, dst-y: INT16

Errors: Window

The src-x and src-y coordinates are taken relative to src-window's origin and
are returned as dst-x and dst-y coordinates relative to dst-window's origin. If
same-screen is False, then src-window and dst-window are on different screens,
and dst-x and dst-y are zero. If the coordinates are contained in a mapped child
of dst-window, then that child is returned.

"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import TranslateCoordinatesCookie, TranslateCoordinatesReply


__all__ = ['TranslateCoordinates', 'TranslateCoordinatesUnchecked', ]


class TranslateCoordinatesAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xIIhh'
    code = 40

    def _getbinary(self, src_window, dst_window, src_x, src_y):
        buf = _StringIO()
        buf.write(_pack(self.fmt, src_window, dst_window, src_x, src_y))
        return buf.getvalue()

    def __call__(self, src_window, dst_window, src_x, src_y):
        """Request TranslateCoordinates X protocol.

        @Arguments:
        - `src_window`:
        - `dst_window`:
        - `src_x`:
        - `src_y`:

        @Return:
        TranslateCoordinatesCookie

        @Error:
        BadWindow
        """
        return self.request(self._getbinary(src_window, dst_window, src_x, src_y))


class TranslateCoordinates(TranslateCoordinatesAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(src_window, dst_window, src_x, src_y)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            TranslateCoordinatesCookie(), TranslateCoordinatesReply)


class TranslateCoordinatesUnchecked(TranslateCoordinatesAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(src_window, dst_window, src_x, src_y)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            TranslateCoordinatesCookie(), TranslateCoordinatesReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# translatecoordinates.py ends here
