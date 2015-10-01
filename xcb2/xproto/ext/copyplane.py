#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: copyplane.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""copyplane -- a parts of xcb2

CopyPlane

src-drawable, dst-drawable: DRAWABLE
gc: GCONTEXT
src-x, src-y: INT16
width, height: CARD16
dst-x, dst-y: INT16
bit-plane: CARD32

Errors: Drawable, GContext, Match, Value

The src-drawable must have the same root as dst-drawable (or a Match error
results), but it need not have the same depth. The bit-plane must have exactly
one bit set to 1 and the value of bit-plane must be less than %2 sup n% where n
is the depth of src-drawable (or a Value error results). Effectively, a pixmap
of the same depth as dst-drawable and with size specified by the source region
is formed using the foreground/background pixels in gc (foreground everywhere
the bit-plane in src-drawable contains a bit set to 1, background everywhere the
bit-plane contains a bit set to 0), and the equivalent of a CopyArea is
performed, with all the same exposure semantics. This can also be thought of as
using the specified region of the source bit-plane as a stipple with a
fill-style of OpaqueStippled for filling a rectangular area of the destination.

GC components: function, plane-mask, foreground, background, subwindow-mode,
graphics-exposures, clip-x-origin, clip-y-origin, clip-mask
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['CopyPlane', 'CopyPlaneChecked', ]


class CopyPlaneAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xIIIhhhhHHI'
    code = 63

    def _getbinary(self, src_drawable, dst_drawable, gc,
                            src_x, src_y, dst_x, dst_y, width, height, bit_plane):
        buf = _StringIO()
        buf.write(_pack(self.fmt, src_drawable, dst_drawable, gc,
                        src_x, src_y, dst_x, dst_y, width, height, bit_plane))
        return buf.getvalue()

        raise NotImplementedError()

    def __call__(self, src_drawable, dst_drawable, gc,
                 src_x, src_y, dst_x, dst_y, width, height, bit_plane):
        """Request CopyPlane X protocol.

        @Arguments:
        - `src_drawable`:
        - `dst_drawable`:
        - `gc`:
        - `src_x`:
        - `src_y`:
        - `dst_x`:
        - `dst_y`:
        - `width`:
        - `height`:
        - `bit_plane`:

        @Return:
        VoidCookie

        @Error:
        BadDrawable, BadGContext, BadMatch, BadValue
        """
        return self.request(self._getbinary(src_drawable, dst_drawable, gc,
                            src_x, src_y, dst_x, dst_y, width, height, bit_plane))


class CopyPlane(CopyPlaneAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(src_drawable, dst_drawable, gc,
        src_x, src_y, dst_x, dst_y, width, height, bit_plane)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class CopyPlaneChecked(CopyPlaneAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(src_drawable, dst_drawable, gc,
        src_x, src_y, dst_x, dst_y, width, height, bit_plane)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# copyplane.py ends here
