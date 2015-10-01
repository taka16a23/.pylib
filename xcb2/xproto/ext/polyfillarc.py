#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""polyfillarc -- a parts of xcb2

PolyFillArc

drawable: DRAWABLE
gc: GCONTEXT
arcs: LISTofARC

Errors: Drawable, GContext, Match

For each arc, this request fills the region closed by the infinitely thin path
described by the specified arc and one or two line segments, depending on the
arc-mode. For Chord, the single line segment joining the endpoints of the arc is
used. For PieSlice, the two line segments joining the endpoints of the arc with
the center point are used.

For an arc specified as [x,y,w,h,a1,a2], the origin of the major and minor axes
is at [x+(w/2),y+(h/2)], and the infinitely thin path describing the entire
circle/ellipse intersects the horizontal axis at [x,y+(h/2)] and [x+w,y+(h/2)]
and intersects the vertical axis at [x+(w/2),y] and [x+(w/2),y+h]. These
coordinates are not necessarily integral; that is, they are not truncated to
discrete coordinates.

The arc angles are interpreted as specified in the PolyArc request. When the
angle of an arc face is not an integral multiple of 90 degrees, then the precise
endpoint on the arc is implementation dependent. However, for Chord arc-mode,
the computation of the pair of endpoints (relative to the center of the arc)
only depends on the width and height of the arc and the angles of the two arc
faces. For PieSlice arc-mode, the computation of an endpoint only depends on the
angle of the arc face for that endpoint and the ratio of the arc width to arc
height.

The arcs are filled in the order listed. For any given arc, no pixel is drawn
more than once. If regions intersect, the intersecting pixels are drawn multiple
times.

GC components: function, plane-mask, fill-style, arc-mode, subwindow-mode,
clip-x-origin, clip-y-origin, clip-mask

GC mode-dependent components: foreground, background, tile, stipple,
tile-stipple-x-origin, tile-stipple-y-origin
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie, Iterator
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['PolyFillArc', 'PolyFillArcChecked', ]


class PolyFillArcAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xII'
    code = 71

    def _getbinary(self, drawable, gc, arcs_len, arcs):
        buf = _StringIO()
        buf.write(_pack(self.fmt, drawable, gc))
        for elt in Iterator(arcs, 6, 'arcs', True):
            buf.write(_pack('=hhHHhh', *elt))
        return buf.getvalue()

    def __call__(self, drawable, gc, arcs_len, arcs):
        """Request PolyFillArc X protocol.

        @Arguments:
        - `drawable`:
        - `gc`:
        - `arcs_len`:
        - `arcs`:

        @Return:
        VoidCookie

        @Error:
        BadDrawable, BadGContext, BadMatch
        """
        return self.request(self._getbinary(drawable, gc, arcs_len, arcs))


class PolyFillArc(PolyFillArcAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(drawable, gc, arcs_len, arcs)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False),
            VoidCookie())


class PolyFillArcChecked(PolyFillArcAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(drawable, gc, arcs_len, arcs)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# polyfillarc.py ends here
