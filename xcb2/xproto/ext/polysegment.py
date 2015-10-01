#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: polysegment.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""polysegment -- a parts of xcb2

PolySegment

drawable: DRAWABLE
gc: GCONTEXT
segments: LISTofSEGMENT
where:
SEGMENT: [x1, y1, x2, y2: INT16]

Errors: Drawable, GContext, Match

For each segment, this request draws a line between [x1, y1] and [x2, y2]. The
lines are drawn in the order listed. No joining is performed at coincident
endpoints. For any given line, no pixel is drawn more than once. If lines
intersect, the intersecting pixels are drawn multiple times.

GC components: function, plane-mask, line-width, line-style, cap-style,
fill-style, subwindow-mode, clip-x-origin, clip-y-origin, clip-mask

GC mode-dependent components: foreground, background, tile, stipple,
tile-stipple-x-origin, tile-stipple-y-origin, dash-offset, dashes
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie, Iterator
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['PolySegment', 'PolySegmentChecked', ]


class PolySegmentAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xII'
    code = 66

    def _getbinary(self, drawable, gc, segments_len, segments):
        buf = _StringIO()
        buf.write(_pack(self.fmt, drawable, gc))
        for elt in Iterator(segments, 4, 'segments', True):
            buf.write(_pack('=hhhh', *elt))
        return buf.getvalue()

    def __call__(self, drawable, gc, segments_len, segments):
        """Request PolySegment X protocol.

        @Arguments:
        - `drawable`:
        - `gc`:
        - `segments_len`:
        - `segments`:

        @Return:
        VoidCookie

        @Error:
        BadDrawable, BadGContext, BadMatch
        """
        return self.request(self._getbinary(drawable, gc, segments_len, segments))


class PolySegment(PolySegmentAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(drawable, gc, segments_len, segments)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class PolySegmentChecked(PolySegmentAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(drawable, gc, segments_len, segments)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# polysegment.py ends here
