#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: setdashes.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""setdashes -- a parts of xcb2

SetDashes

gc: GCONTEXT
dash-offset: CARD16
dashes: LISTofCARD8

Errors: Alloc, GContext, Value

This request sets dash-offset and dashes in gc for dashed line styles. Dashes
cannot be empty (or a Value error results). Specifying an odd-length list is
equivalent to specifying the same list concatenated with itself to produce an
even-length list. The initial and alternating elements of dashes are the even
dashes; the others are the odd dashes. Each element specifies a dash length in
pixels. All of the elements must be nonzero (or a Value error results). The
dash-offset defines the phase of the pattern, specifying how many pixels into
dashes the pattern should actually begin in any single graphics request. Dashing
is continuous through path elements combined with a join-style but is reset to
the dash-offset between each sequence of joined lines.

The unit of measure for dashes is the same as in the ordinary coordinate
system. Ideally, a dash length is measured along the slope of the line, but
implementations are only required to match this ideal for horizontal and
vertical lines. Failing the ideal semantics, it is suggested that the length be
measured along the major axis of the line. The major axis is defined as the x
axis for lines drawn at an angle of between -45 and +45 degrees or between 135
and 225 degrees from the x axis. For all other lines, the major axis is the y
axis.

For any graphics primitive, the computation of the endpoint of an individual
dash only depends on the geometry of the primitive, the start position of the
dash, the direction of the dash, and the dash length.

For any graphics primitive, the total set of pixels used to render the primitive
(both even and odd numbered dash elements) with DoubleDash line-style is the
same as the set of pixels used to render the primitive with Solid line-style.

For any graphics primitive, if the primitive is drawn with OnOffDash or
DoubleDash line-style unclipped at position [x,y] and again at position
[x+dx,y+dy], then a point [x1,y1] is included in a dash in the first instance if
and only if the point [x1+dx,y1+dy] is included in the dash in the second
instance. In addition, the effective set of points comprising a dash cannot be
affected by clipping. A point is included in a clipped dash if and only if the
point lies inside the clipping region and the point would be included in the
dash when drawn unclipped.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['SetDashes', 'SetDashesChecked', ]


class SetDashesAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xIHH'
    code = 58

    def _getbinary(self, gc, dash_offset, dashes_len, dashes):
        buf = _StringIO()
        buf.write(_pack(self.fmt, gc, dash_offset, dashes_len))
        buf.write(str(buffer(_array('B', dashes))))
        return buf.getvalue()

    def __call__(self, gc, dash_offset, dashes_len, dashes):
        """Request SetDashes X protocol.

        @Arguments:
        - `gc`:
        - `dash_offset`:
        - `dashes_len`:
        - `dashes`:

        @Return:
        VoidCookie

        @Error:
        BadAlloc, BadGContext, BadValue
        """
        return self.request(self._getbinary(gc, dash_offset, dashes_len, dashes))


class SetDashes(SetDashesAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(gc, dash_offset, dashes_len, dashes)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class SetDashesChecked(SetDashesAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(gc, dash_offset, dashes_len, dashes)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# setdashes.py ends here
