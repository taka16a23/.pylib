#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: fillpoly.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""fillpoly -- a parts of xcb2

FillPoly

drawable: DRAWABLE
gc: GCONTEXT
shape: { Complex, Nonconvex, Convex}
coordinate-mode: { Origin, Previous}
points: LISTofPOINT

Errors: Drawable, GContext, Match, Value

This request fills the region closed by the specified path. The path is closed
automatically if the last point in the list does not coincide with the first
point. No pixel of the region is drawn more than once.

The first point is always relative to the drawable's origin. The rest are
relative either to that origin or the previous point, depending on the
coordinate-mode.

The shape parameter may be used by the server to improve performance. Complex
means the path may self-intersect. Contiguous coincident points in the path are
not treated as self-intersection.

Nonconvex means the path does not self-intersect, but the shape is not wholly
convex. If known by the client, specifying Nonconvex over Complex may improve
performance. If Nonconvex is specified for a self-intersecting path, the
graphics results are undefined.

Convex means that for every pair of points inside the polygon, the line segment
connecting them does not intersect the path. If known by the client, specifying
Convex can improve performance. If Convex is specified for a path that is not
convex, the graphics results are undefined.

GC components: function, plane-mask, fill-style, fill-rule, subwindow-mode,
clip-x-origin, clip-y-origin, clip-mask

GC mode-dependent components: foreground, background, tile, stipple,
tile-stipple-x-origin, tile-stipple-y-origin
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['FillPoly', 'FillPolyChecked', ]


class FillPolyAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xIIBB2x'
    code = 2

    def _getbinary(self,
            drawable, gc, shape, coordinate_mode, points_len, points):
        buf = _StringIO()
        buf.write(_pack(self.fmt, drawable, gc, shape, coordinate_mode,
                        points_len, points))
        return buf.getvalue()

    def __call__(self, drawable, gc, shape, coordinate_mode, points_len, points):
        """Request FillPoly X protocol.

        @Arguments:
        - `drawable`:
        - `gc`:
        - `shape`:
        - `coordinate_mode`:
        - `points_len`:
        - `points`:

        @Return:
        VoidCookie

        @Error:
        BadDrawable, BadGContext, BadMatch, BadValue
        """
        return self.request(self._getbinary(
            drawable, gc, shape, coordinate_mode, points_len, points))


class FillPoly(FillPolyAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(drawable, gc, shape, coordinate_mode, points_len, points)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class FillPolyChecked(FillPolyAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(drawable, gc, shape, coordinate_mode, points_len, points)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# fillpoly.py ends here
