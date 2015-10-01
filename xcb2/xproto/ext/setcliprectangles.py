#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: setcliprectangles.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""setcliprectangles -- a parts of xcb2

SetClipRectangles

gc: GCONTEXT
clip-x-origin, clip-y-origin: INT16
rectangles: LISTofRECTANGLE
ordering: { UnSorted, YSorted, YXSorted, YXBanded}

Errors: Alloc, GContext, Match, Value

This request changes clip-mask in gc to the specified list of rectangles and
sets the clip origin. Output will be clipped to remain contained within the
rectangles. The clip origin is interpreted relative to the origin of whatever
destination drawable is specified in a graphics request. The rectangle
coordinates are interpreted relative to the clip origin. The rectangles should
be nonintersecting, or graphics results will be undefined. Note that the list of
rectangles can be empty, which effectively disables output. This is the opposite
of passing None as the clip-mask in CreateGC and ChangeGC.

If known by the client, ordering relations on the rectangles can be specified
with the ordering argument. This may provide faster operation by the server. If
an incorrect ordering is specified, the server may generate a Match error, but
it is not required to do so. If no error is generated, the graphics results are
undefined. UnSorted means that the rectangles are in arbitrary order. YSorted
means that the rectangles are nondecreasing in their Y origin. YXSorted
additionally constrains YSorted order in that all rectangles with an equal Y
origin are nondecreasing in their X origin. YXBanded additionally constrains
YXSorted by requiring that, for every possible Y scanline, all rectangles that
include that scanline have identical Y origins and Y extents.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['SetClipRectangles', 'SetClipRectanglesChecked', ]


class SetClipRectanglesAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xIhh'
    code = 59

    def _getbinary(self, ordering, gc, clip_x_origin, clip_y_origin,
                   rectangles_len, rectangles):
        buf = _StringIO()
        buf.write(_pack(self.fmt, ordering, gc, clip_x_origin, clip_y_origin,
                rectangles_len, rectangles))
        return buf.getvalue()

    def __call__(self, ordering, gc, clip_x_origin, clip_y_origin,
                 rectangles_len, rectangles):
        """Request SetClipRectangles X protocol.
        @Arguments:
        - `ordering`:
        - `gc`:
        - `clip_x_origin`:
        - `clip_y_origin`:
        - `rectangles`:

        @Return:
        VoidCookie

        @Error:
        BadAlloc, BadGContext, BadMatch, BadValue
        """
        return self.request(
            self._getbinary(ordering, gc, clip_x_origin, clip_y_origin,
                rectangles_len, rectangles))


class SetClipRectangles(SetClipRectanglesAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(ordering, gc, clip_x_origin, clip_y_origin,
                rectangles_len, rectangles)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class SetClipRectanglesChecked(SetClipRectanglesAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(ordering, gc, clip_x_origin, clip_y_origin,
                rectangles_len, rectangles)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# setcliprectangles.py ends here
