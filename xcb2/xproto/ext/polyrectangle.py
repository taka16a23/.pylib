#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: polyrectangle.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""polyrectangle -- a parts of xcb2

PolyRectangle

drawable: DRAWABLE
gc: GCONTEXT
rectangles: LISTofRECTANGLE

Errors: Drawable, GContext, Match

This request draws the outlines of the specified rectangles, as if a five-point
PolyLine were specified for each rectangle:

	[x,y] [x+width,y] [x+width,y+height] [x,y+height] [x,y]
The x and y coordinates of each rectangle are relative to the drawable's origin
and define the upper-left corner of the rectangle.

The rectangles are drawn in the order listed. For any given rectangle, no pixel
is drawn more than once. If rectangles intersect, the intersecting pixels are
drawn multiple times.

GC components: function, plane-mask, line-width, line-style, cap-style,
join-style, fill-style, subwindow-mode, clip-x-origin, clip-y-origin, clip-mask

GC mode-dependent components: foreground, background, tile, stipple,
tile-stipple-x-origin, tile-stipple-y-origin, dash-offset, dashes
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie, Iterator
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['PolyRectangle', 'PolyRectangleChecked', ]


class PolyRectangleAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xII'
    code = 67

    def _getbinary(self, drawable, gc, rectangles_len, rectangles):
        buf = _StringIO()
        buf.write(_pack(self.fmt, drawable, gc))
        for elt in Iterator(rectangles, 4, 'rectangles', True):
            buf.write(_pack('=hhHH', *elt))
        return buf.getvalue()

    def __call__(self, drawable, gc, rectangles_len, rectangles):
        """Request PolyRectangle X protocol.

        @Arguments:
        - `drawable`:
        - `gc`:
        - `rectangles_len`:
        - `rectangles`:

        @Return:
        VoidCookie

        @Error:
        BadDrawable, BadGContext, BadMatch
        """
        return self.request(
            self._getbinary(drawable, gc, rectangles_len, rectangles))


class PolyRectangle(PolyRectangleAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(drawable, gc, rectangles_len, rectangles)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class PolyRectangleChecked(PolyRectangleAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(drawable, gc, rectangles_len, rectangles)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# polyrectangle.py ends here
