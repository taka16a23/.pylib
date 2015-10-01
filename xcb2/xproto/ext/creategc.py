#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: creategc.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""creategc -- a parts of xcb2

CreateGC

cid: GCONTEXT
drawable: DRAWABLE
value-mask: BITMASK
value-list: LISTofVALUE

Errors: Alloc, Drawable, Font, IDChoice, Match, Pixmap, Value

This request creates a graphics context and assigns the identifier cid to
it. The gcontext can be used with any destination drawable having the same root
and depth as the specified drawable; use with other drawables results in a Match
error.

The value-mask and value-list specify which components are to be explicitly
initialized. The context components are:

Component	Type
function	 { Clear, And, AndReverse, Copy, AndInverted, NoOp, Xor, Or, Nor, Equiv, Invert, OrReverse, CopyInverted, OrInverted, Nand, Set }
plane-mask	CARD32
foreground	CARD32
background	CARD32
line-width	CARD16
line-style	 { Solid, OnOffDash, DoubleDash }
cap-style	 { NotLast, Butt, Round, Projecting }
join-style	 { Miter, Round, Bevel }
fill-style	 { Solid, Tiled, OpaqueStippled, Stippled }
fill-rule	 { EvenOdd, Winding }
arc-mode	 { Chord, PieSlice }
tile	PIXMAP
stipple	PIXMAP
tile-stipple-x-origin	INT16
tile-stipple-y-origin	INT16
font	FONT
subwindow-mode	 { ClipByChildren, IncludeInferiors }
graphics-exposures	BOOL
clip-x-origin	INT16
clip-y-origin	INT16
clip-mask	 PIXMAP or None
dash-offset	CARD16
dashes	CARD8
In graphics operations, given a source and destination pixel, the result is
computed bitwise on corresponding bits of the pixels; that is, a Boolean
operation is performed in each bit plane. The plane-mask restricts the operation
to a subset of planes, so the result is:

	((src FUNC dst) AND plane-mask) OR (dst AND (NOT plane-mask))
Range checking is not performed on the values for foreground, background, or
plane-mask. They are simply truncated to the appropriate number of bits.

The meanings of the functions are:

Function	Operation
Clear	0
And	src AND dst
AndReverse	src AND (NOT dst)
Copy	src
AndInverted	(NOT src) AND dst
NoOp	dst
Xor	src XOR dst
Or	src OR dst
Nor	(NOT src) AND (NOT dst)
Equiv	(NOT src) XOR dst
Invert	NOT dst
OrReverse	src OR (NOT dst)
CopyInverted	NOT src
OrInverted	(NOT src) OR dst
Nand	(NOT src) OR (NOT dst)
Set	1
The line-width is measured in pixels and can be greater than or equal to one, a
wide line, or the special value zero, a thin line.

Wide lines are drawn centered on the path described by the graphics
request. Unless otherwise specified by the join or cap style, the bounding box
of a wide line with endpoints [x1, y1], [x2, y2] and width w is a rectangle with
vertices at the following real coordinates:

	[x1-(w*sn/2), y1+(w*cs/2)], [x1+(w*sn/2), y1-(w*cs/2)],
	[x2-(w*sn/2), y2+(w*cs/2)], [x2+(w*sn/2), y2-(w*cs/2)]
The sn is the sine of the angle of the line and cs is the cosine of the angle of
the line. A pixel is part of the line (and hence drawn) if the center of the
pixel is fully inside the bounding box, which is viewed as having infinitely
thin edges. If the center of the pixel is exactly on the bounding box, it is
part of the line if and only if the interior is immediately to its right (x
increasing direction). Pixels with centers on a horizontal edge are a special
case and are part of the line if and only if the interior or the boundary is
immediately below (y increasing direction) and if the interior or the boundary
is immediately to the right (x increasing direction). Note that this description
is a mathematical model describing the pixels that are drawn for a wide line and
does not imply that trigonometry is required to implement such a model. Real or
fixed point arithmetic is recommended for computing the corners of the line
endpoints for lines greater than one pixel in width.

Thin lines (zero line-width) are nominally one pixel wide lines drawn using an
unspecified, device-dependent algorithm. There are only two constraints on this
algorithm. First, if a line is drawn unclipped from [x1,y1] to [x2,y2] and
another line is drawn unclipped from [x1+dx,y1+dy] to [x2+dx,y2+dy], then a
point [x,y] is touched by drawing the first line if and only if the point
[x+dx,y+dy] is touched by drawing the second line. Second, the effective set of
points comprising a line cannot be affected by clipping. Thus, a point is
touched in a clipped line if and only if the point lies inside the clipping
region and the point would be touched by the line when drawn unclipped.

Note that a wide line drawn from [x1,y1] to [x2,y2] always draws the same pixels
as a wide line drawn from [x2,y2] to [x1,y1], not counting cap-style and
join-style. Implementors are encouraged to make this property true for thin
lines, but it is not required. A line-width of zero may differ from a line-width
of one in which pixels are drawn. In general, drawing a thin line will be faster
than drawing a wide line of width one, but thin lines may not mix well
aesthetically with wide lines because of the different drawing algorithms. If it
is desirable to obtain precise and uniform results across all displays, a client
should always use a line-width of one, rather than a line-width of zero.

The line-style defines which sections of a line are drawn:

Solid	 The full path of the line is drawn.
DoubleDash The full path of the line is drawn, but the even dashes are filled
differently than the odd dashes (see fill-style), with Butt cap-style used where
even and odd dashes meet.  OnOffDash Only the even dashes are drawn, and
cap-style applies to all internal ends of the individual dashes (except NotLast
is treated as Butt).
The cap-style defines how the endpoints of a path are drawn:

NotLast The result is equivalent to Butt, except that for a line-width of zero
the final endpoint is not drawn.  Butt The result is square at the endpoint
(perpendicular to the slope of the line) with no projection beyond.  Round The
result is a circular arc with its diameter equal to the line-width, centered on
the endpoint; it is equivalent to Butt for line-width zero.  Projecting The
result is square at the end, but the path continues beyond the endpoint for a
distance equal to half the line-width; it is equivalent to Butt for line-width
zero.  The join-style defines how corners are drawn for wide lines:

Miter The outer edges of the two lines extend to meet at an angle. However, if
the angle is less than 11 degrees, a Bevel join-style is used instead.  Round
The result is a circular arc with a diameter equal to the line-width, centered
on the joinpoint.  Bevel The result is Butt endpoint styles, and then the
triangular notch is filled.  For a line with coincident endpoints (x1=x2,
y1=y2), when the cap-style is applied to both endpoints, the semantics depends
on the line-width and the cap-style:

NotLast thin This is device-dependent, but the desired effect is that nothing is
drawn.  Butt thin This is device-dependent, but the desired effect is that a
single pixel is drawn.  Round thin This is the same as Butt/thin.  Projecting
thin This is the same as Butt/thin.  Butt wide Nothing is drawn.  Round wide The
closed path is a circle, centered at the endpoint and with a diameter equal to
the line-width.  Projecting wide The closed path is a square, aligned with the
coordinate axes, centered at the endpoint and with sides equal to the
line-width.  For a line with coincident endpoints (x1=x2, y1=y2), when the
join-style is applied at one or both endpoints, the effect is as if the line was
removed from the overall path. However, if the total path consists of (or is
reduced to) a single point joined with itself, the effect is the same as when
the cap-style is applied at both endpoints.

The tile/stipple represents an infinite two-dimensional plane with the
tile/stipple replicated in all dimensions. When that plane is superimposed on
the drawable for use in a graphics operation, the upper-left corner of some
instance of the tile/stipple is at the coordinates within the drawable specified
by the tile/stipple origin. The tile/stipple and clip origins are interpreted
relative to the origin of whatever destination drawable is specified in a
graphics request.

The tile pixmap must have the same root and depth as the gcontext (or a Match
error results). The stipple pixmap must have depth one and must have the same
root as the gcontext (or a Match error results). For fill-style Stippled (but
not fill-style OpaqueStippled), the stipple pattern is tiled in a single plane
and acts as an additional clip mask to be ANDed with the clip-mask. Any size
pixmap can be used for tiling or stippling, although some sizes may be faster to
use than others.

The fill-style defines the contents of the source for line, text, and fill
requests. For all text and fill requests (for example, PolyText8, PolyText16,
PolyFillRectangle, FillPoly, and PolyFillArc) as well as for line requests with
line-style Solid, (for example, PolyLine, PolySegment, PolyRectangle, PolyArc )
and for the even dashes for line requests with line-style OnOffDash or
DoubleDash:

Solid	Foreground
Tiled	Tile
OpaqueStippled A tile with the same width and height as stipple but with
background everywhere stipple has a zero and with foreground everywhere stipple
has a one
Stippled	 Foreground masked by stipple
For the odd dashes for line requests with line-style DoubleDash:

Solid	Background
Tiled	Same as for even dashes
OpaqueStippled	Same as for even dashes
Stippled	Background masked by stipple
The dashes value allowed here is actually a simplified form of the more general
patterns that can be set with SetDashes. Specifying a value of N here is
equivalent to specifying the two element list [N, N] in SetDashes. The value
must be nonzero (or a Value error results). The meaning of dash-offset and
dashes are explained in the SetDashes request.

The clip-mask restricts writes to the destination drawable. Only pixels where
the clip-mask has bits set to 1 are drawn. Pixels are not drawn outside the area
covered by the clip-mask or where the clip-mask has bits set to 0. The clip-mask
affects all graphics requests, but it does not clip sources. The clip-mask
origin is interpreted relative to the origin of whatever destination drawable is
specified in a graphics request. If a pixmap is specified as the clip-mask, it
must have depth 1 and have the same root as the gcontext (or a Match error
results). If clip-mask is None, then pixels are always drawn, regardless of the
clip origin. The clip-mask can also be set with the SetClipRectangles request.

For ClipByChildren, both source and destination windows are additionally clipped
by all viewable InputOutput children. For IncludeInferiors, neither source nor
destination window is clipped by inferiors. This will result in including
subwindow contents in the source and drawing through subwindow boundaries of the
destination. The use of IncludeInferiors with a source or destination window of
one depth with mapped inferiors of differing depth is not illegal, but the
semantics is undefined by the core protocol.

The fill-rule defines what pixels are inside (that is, are drawn) for paths
given in FillPoly requests. EvenOdd means a point is inside if an infinite ray
with the point as origin crosses the path an odd number of times. For Winding, a
point is inside if an infinite ray with the point as origin crosses an unequal
number of clockwise and counterclockwise directed path segments. A clockwise
directed path segment is one that crosses the ray from left to right as observed
from the point. A counter-clockwise segment is one that crosses the ray from
right to left as observed from the point. The case where a directed line segment
is coincident with the ray is uninteresting because one can simply choose a
different ray that is not coincident with a segment.

For both fill rules, a point is infinitely small and the path is an infinitely
thin line. A pixel is inside if the center point of the pixel is inside and the
center point is not on the boundary. If the center point is on the boundary, the
pixel is inside if and only if the polygon interior is immediately to its right
(x increasing direction). Pixels with centers along a horizontal edge are a
special case and are inside if and only if the polygon interior is immediately
below (y increasing direction).

The arc-mode controls filling in the PolyFillArc request.

The graphics-exposures flag controls GraphicsExposure event generation for
CopyArea and CopyPlane requests (and any similar requests defined by
extensions).

The default component values are:

Component	Default
function	Copy
plane-mask	all ones
foreground	0
background	1
line-width	0
line-style	Solid
cap-style	Butt
join-style	Miter
fill-style	Solid
fill-rule	EvenOdd
arc-mode	PieSlice
tile
Pixmap of unspecified size filled with foreground pixel
(that is, client specified pixel if any, else 0)
(subsequent changes to foreground do not affect this pixmap)
stipple	 Pixmap of unspecified size filled with ones
tile-stipple-x-origin	0
tile-stipple-y-origin	0
font	<server-dependent-font>
subwindow-mode	ClipByChildren
graphics-exposures	True
clip-x-origin	0
clip-y-origin	0
clip-mask	None
dash-offset	0
dashes	4 (that is, the list [4, 4])
Storing a pixmap in a gcontext might or might not result in a copy being
made. If the pixmap is later used as the destination for a graphics request, the
change might or might not be reflected in the gcontext. If the pixmap is used
simultaneously in a graphics request as both a destination and as a tile or
stipple, the results are not defined.

It is quite likely that some amount of gcontext information will be cached in
display hardware and that such hardware can only cache a small number of
gcontexts. Given the number and complexity of components, clients should view
switching between gcontexts with nearly identical state as significantly more
expensive than making minor changes to a single gcontext.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['CreateGC', 'CreateGCChecked', ]


class CreateGCAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xIII'
    code = 55

    def _getbinary(self, cid, drawable, value_mask, value_list):
        buf = _StringIO()
        buf.write(_pack(self.fmt, cid, drawable, value_mask))
        buf.write(str(buffer(_array('I', value_list))))
        return buf.getvalue()

    def __call__(self, cid, drawable, value_mask, value_list):
        """Request CreateGC X protocol.

        @Arguments:
        - `cid`:
        - `drawable`:
        - `value_mask`:
        - `value_list`:

        @Return:
        VoidCookie

        @Error:
        BadAlloc, BadDrawable, BadFont, BadIDChoice, BadMatch,
        BadPixmap, BadValue
        """
        return self.request(
            self._getbinary(cid, drawable, value_mask, value_list))


class CreateGC(CreateGCAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cid, drawable, value_mask, value_list)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class CreateGCChecked(CreateGCAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cid, drawable, value_mask, value_list)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# creategc.py ends here
