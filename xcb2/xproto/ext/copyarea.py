#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""copyarea -- a parts of xcb2

CopyArea

src-drawable, dst-drawable: DRAWABLE
gc: GCONTEXT
src-x, src-y: INT16
width, height: CARD16
dst-x, dst-y: INT16

Errors: Drawable, GContext, Match

This request combines the specified rectangle of src-drawable with the specified
rectangle of dst-drawable. The src-x and src-y coordinates are relative to
src-drawable's origin. The dst-x and dst-y are relative to dst-drawable's
origin, each pair specifying the upper-left corner of the rectangle. The
src-drawable must have the same root and the same depth as dst-drawable (or a
Match error results).

If regions of the source rectangle are obscured and have not been retained in
backing store or if regions outside the boundaries of the source drawable are
specified, then those regions are not copied, but the following occurs on all
corresponding destination regions that are either visible or are retained in
backing-store. If the dst-drawable is a window with a background other than
None, these corresponding destination regions are tiled (with plane-mask of all
ones and function Copy) with that background. Regardless of tiling and whether
the destination is a window or a pixmap, if graphics-exposures in gc is True,
then GraphicsExposure events for all corresponding destination regions are
generated.

If graphics-exposures is True but no GraphicsExposure events are generated, then
a NoExposure event is generated.

GC components: function, plane-mask, subwindow-mode, graphics-exposures,
clip-x-origin, clip-y-origin, clip-mask
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['CopyArea', 'CopyAreaChecked', ]


class CopyAreaAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xIIIhhhhHH'
    code = 62

    def _getbinary(self, src_drawable, dst_drawable, gc,
                            src_x, src_y, dst_x, dst_y, width, height):
        buf = _StringIO()
        buf.write(_pack(self.fmt, src_drawable, dst_drawable, gc,
                        src_x, src_y, dst_x, dst_y, width, height))
        return buf.getvalue()

    def __call__(self, src_drawable, dst_drawable, gc,
                 src_x, src_y, dst_x, dst_y, width, height):
        """Request CopyArea X protocol.

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

        @Return:
        VoidCookie

        @Error:
        BadDrawable, BadGContext, BadMatch
        """
        return self.request(self._getbinary(src_drawable, dst_drawable, gc,
                            src_x, src_y, dst_x, dst_y, width, height))


class CopyArea(CopyAreaAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(src_drawable, dst_drawable, gc,
        src_x, src_y, dst_x, dst_y, width, height)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class CopyAreaChecked(CopyAreaAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(src_drawable, dst_drawable, gc,
        src_x, src_y, dst_x, dst_y, width, height)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# copyarea.py ends here
