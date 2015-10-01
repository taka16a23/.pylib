#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""polyarc -- a parts of xcb2

PolyArc

drawable: DRAWABLE
gc: GCONTEXT
arcs: LISTofARC

Errors: Drawable, GContext, Match

This request draws circular or elliptical arcs. Each arc is specified by a
rectangle and two angles. The angles are signed integers in degrees scaled by
64, with positive indicating counterclockwise motion and negative indicating
clockwise motion. The start of the arc is specified by angle1 relative to the
three-o'clock position from the center of the rectangle, and the path and extent
of the arc is specified by angle2 relative to the start of the arc. If the
magnitude of angle2 is greater than 360 degrees, it is truncated to 360
degrees. The x and y coordinates of the rectangle are relative to the origin of
the drawable. For an arc specified as [x,y,w,h,a1,a2], the origin of the major
and minor axes is at [x+(w/2),y+(h/2)], and the infinitely thin path describing
the entire circle/ellipse intersects the horizontal axis at [x,y+(h/2)] and
[x+w,y+(h/2)] and intersects the vertical axis at [x+(w/2),y] and
[x+(w/2),y+h]. These coordinates are not necessarily integral; that is, they are
not truncated to discrete coordinates.

For a wide line with line-width lw, the ideal bounding outlines for filling are
given by the two infinitely thin paths consisting of all points whose
perpendicular distance from a tangent to the path of the circle/ellipse is equal
to lw/2 (which may be a fractional value). When the width and height of the arc
are not equal and both are nonzero, then the actual bounding outlines are
implementation dependent. However, the computation of the shape and position of
the bounding outlines (relative to the center of the arc) only depends on the
width and height of the arc and the line-width.

The cap-style is applied the same as for a line corresponding to the tangent of
the circle/ellipse at the endpoint. When the angle of an arc face is not an
integral multiple of 90 degrees, and the width and height of the arc are both
are nonzero, then the shape and position of the cap at that face is
implementation dependent. However, for a Butt cap, the face is defined by a
straight line, and the computation of the position (relative to the center of
the arc) and the slope of the line only depends on the width and height of the
arc and the angle of the arc face. For other cap styles, the computation of the
position (relative to the center of the arc) and the shape of the cap only
depends on the width and height of the arc, the line-width, the angle of the arc
face, and the direction (clockwise or counter clockwise) of the arc from the
endpoint.

The join-style is applied the same as for two lines corresponding to the
tangents of the circles/ellipses at the join point. When the width and height of
both arcs are nonzero, and the angle of either arc face is not an integral
multiple of 90 degrees, then the shape of the join is implementation
dependent. However, the computation of the shape only depends on the width and
height of each arc, the line-width, the angles of the two arc faces, the
direction (clockwise or counter clockwise) of the arcs from the join point, and
the relative orientation of the two arc center points.

For an arc specified as [x,y,w,h,a1,a2], the angles must be specified in the
effectively skewed coordinate system of the ellipse (for a circle, the angles
and coordinate systems are identical). The relationship between these angles and
angles expressed in the normal coordinate system of the screen (as measured with
a protractor) is as follows:

	skewed-angle = atan(tan(normal-angle) * w/h) + adjust
The skewed-angle and normal-angle are expressed in radians (rather than in
degrees scaled by 64) in the range [0,2*PI). The atan returns a value in the
range [-PI/2,PI/2]. The adjust is:

0	for normal-angle in the range [0,PI/2)
PI	for normal-angle in the range [PI/2,(3*PI)/2)
2*PI	for normal-angle in the range [(3*PI)/2,2*PI)
The arcs are drawn in the order listed. If the last point in one arc coincides
with the first point in the following arc, the two arcs will join correctly. If
the first point in the first arc coincides with the last point in the last arc,
the two arcs will join correctly. For any given arc, no pixel is drawn more than
once. If two arcs join correctly and the line-width is greater than zero and the
arcs intersect, no pixel is drawn more than once. Otherwise, the intersecting
pixels of intersecting arcs are drawn multiple times. Specifying an arc with one
endpoint and a clockwise extent draws the same pixels as specifying the other
endpoint and an equivalent counterclockwise extent, except as it affects joins.

By specifying one axis to be zero, a horizontal or vertical line can be drawn.

Angles are computed based solely on the coordinate system, ignoring the aspect
ratio.

GC components: function, plane-mask, line-width, line-style, cap-style,
join-style, fill-style, subwindow-mode, clip-x-origin, clip-y-origin, clip-mask

GC mode-dependent components: foreground, background, tile, stipple,
tile-stipple-x-origin, tile-stipple-y-origin, dash-offset, dashes
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie, Iterator
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['PolyArc', 'PolyArcChecked', ]


class PolyArcAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xII'
    code = 68

    def _getbinary(self, drawable, gc, arcs_len, arcs):
        buf = _StringIO()
        buf.write(_pack(self.fmt, drawable, gc))
        for elt in Iterator(arcs, 6, 'arcs', True):
            buf.write(_pack('=hhHHhh', *elt))
        return buf.getvalue()

    def __call__(self, drawable, gc, arcs_len, arcs):
        """Request PolyArc X protocol.

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


class PolyArc(PolyArcAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(drawable, gc, arcs_len, arcs)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class PolyArcChecked(PolyArcAbstract):
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
# polyarc.py ends here
