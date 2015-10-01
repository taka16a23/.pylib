#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: getimage.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""getimage -- a parts of xcb2

GetImage

drawable: DRAWABLE
x, y: INT16
width, height: CARD16
plane-mask: CARD32
format: { XYPixmap, ZPixmap}

depth: CARD8
visual: VISUALID or None
data: LISTofBYTE

Errors: Drawable, Match, Value

This request returns the contents of the given rectangle of the drawable in the
given format. The x and y coordinates are relative to the drawable's origin and
define the upper-left corner of the rectangle. If XYPixmap is specified, only
the bit planes specified in plane-mask are transmitted, with the planes
appearing from most significant to least significant in bit order. If ZPixmap is
specified, then bits in all planes not specified in plane-mask are transmitted
as zero. Range checking is not performed on plane-mask; extraneous bits are
simply ignored. The returned depth is as specified when the drawable was created
and is the same as a depth component in a FORMAT structure (in the connection
setup), not a bits-per-pixel component. If the drawable is a window, its visual
type is returned. If the drawable is a pixmap, the visual is None.

If the drawable is a pixmap, then the given rectangle must be wholly contained
within the pixmap (or a Match error results). If the drawable is a window, the
window must be viewable, and it must be the case that, if there were no
inferiors or overlapping windows, the specified rectangle of the window would be
fully visible on the screen and wholly contained within the outside edges of the
window (or a Match error results). Note that the borders of the window can be
included and read with this request. If the window has a backing store, then the
backing-store contents are returned for regions of the window that are obscured
by noninferior windows; otherwise, the returned contents of such obscured
regions are undefined. Also undefined are the returned contents of visible
regions of inferiors of different depth than the specified window. The pointer
cursor image is not included in the contents returned.

This request is not general-purpose in the same sense as other graphics-related
requests. It is intended specifically for rudimentary hardcopy support.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import GetImageCookie, GetImageReply


__all__ = ['GetImage', 'GetImageUnchecked', ]


class GetImageAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xIhhHHI'
    code = 73

    def _getbinary(self, format, drawable, x, y, width, height, plane_mask):
        buf = _StringIO()
        buf.write(_pack(self.fmt, format, drawable, x, y, width, height,
                        plane_mask))
        return buf.getvalue()

    def __call__(self, format, drawable, x, y, width, height, plane_mask):
        """Request GetImage X protocol.

        @Arguments:
        - `format`:
        - `drawable`:
        - `x`:
        - `y`:
        - `width`:
        - `height`:
        - `plane_mask`:

        @Return:
        GetImageCookie

        @Error:
        BadDrawable, BadMatch, BadValue
        """
        return self.request(
            self._getbinary(format, drawable, x, y, width, height, plane_mask))


class GetImage(GetImageAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(format, drawable, x, y, width, height, plane_mask)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            GetImageCookie(), GetImageReply)


class GetImageUnchecked(GetImageAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(format, drawable, x, y, width, height, plane_mask)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            GetImageCookie(), GetImageReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# getimage.py ends here
