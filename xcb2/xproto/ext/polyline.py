#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""polyline -- a parts of xcb2

PolyLine

drawable: DRAWABLE
gc: GCONTEXT
coordinate-mode: { Origin, Previous}
points: LISTofPOINT

Errors: Drawable, GContext, Match, Value

This request draws lines between each pair of points (point[i], point[i+1]). The
lines are drawn in the order listed. The lines join correctly at all
intermediate points, and if the first and last points coincide, the first and
last lines also join correctly.

For any given line, no pixel is drawn more than once. If thin (zero line-width)
lines intersect, the intersecting pixels are drawn multiple times. If wide lines
intersect, the intersecting pixels are drawn only once, as though the entire
PolyLine were a single filled shape.

The first point is always relative to the drawable's origin. The rest are
relative either to that origin or the previous point, depending on the
coordinate-mode.

When either of the two lines involved in a Bevel join is neither vertical nor
horizontal, then the slope and position of the line segment defining the bevel
join edge is implementation dependent. However, the computation of the slope and
distance (relative to the join point) only depends on the line width and the
slopes of the two lines.

GC components: function, plane-mask, line-width, line-style, cap-style,
join-style, fill-style, subwindow-mode, clip-x-origin, clip-y-origin, clip-mask

GC mode-dependent components: foreground, background, tile, stipple,
tile-stipple-x-origin, tile-stipple-y-origin, dash-offset, dashes
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['PolyLine', 'PolyLineChecked', ]


class PolyLineAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xII'
    code = 65

    def _getbinary(self, coordinate_mode, drawable, gc, points_len, points):
        buf = _StringIO()
        buf.write(_pack(self.fmt, coordinate_mode, drawable, gc,
                        points_len, points))
        return buf.getvalue()

    def __call__(self, coordinate_mode, drawable, gc, points_len, points):
        """Request PolyLine X protocol.

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


class PolyLine(PolyLineAbstract):
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


class PolyLineChecked(PolyLineAbstract):
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
# polyline.py ends here
