#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: polypoint.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""polypoint -- a parts of xcb2

PolyPoint

drawable: DRAWABLE
gc: GCONTEXT
coordinate-mode: { Origin, Previous}
points: LISTofPOINT

Errors: Drawable, GContext, Match, Value

This request combines the foreground pixel in gc with the pixel at each point in
the drawable. The points are drawn in the order listed.

The first point is always relative to the drawable's origin. The rest are
relative either to that origin or the previous point, depending on the
coordinate-mode.

GC components: function, plane-mask, foreground, subwindow-mode, clip-x-origin,
clip-y-origin, clip-mask
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['PolyPoint', 'PolyPointChecked', ]


class PolyPointAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xII'
    code = 64

    def _getbinary(self, coordinate_mode, drawable, gc, points_len, points):
        buf = _StringIO()
        buf.write(_pack(self.fmt, coordinate_mode, drawable, gc,
                        points_len, points))
        return buf.getvalue()

    def __call__(self, coordinate_mode, drawable, gc, points_len, points):
        """Request PolyPoint X protocol.

        @Arguments:
        - `coordinate_mode`:
        - `drawable`:
        - `gc`:
        - `points_len`:
        - `points`:

        @Return:
        VoidCookie

        @Error:
        BadDrawable, BadGContext, BadMatch, BadValue
        """
        return self.request(
            self._getbinary(coordinate_mode, drawable, gc, points_len, points))


class PolyPoint(PolyPointAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(coordinate_mode, drawable, gc, points_len, points)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class PolyPointChecked(PolyPointAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(coordinate_mode, drawable, gc, points_len, points)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# polypoint.py ends here
