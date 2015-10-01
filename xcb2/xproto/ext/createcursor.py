#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: createcursor.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""createcursor -- a parts of xcb2

CreateCursor

cid: CURSOR
source: PIXMAP
mask: PIXMAP or None
fore-red, fore-green, fore-blue: CARD16
back-red, back-green, back-blue: CARD16
x, y: CARD16

Errors: Alloc, IDChoice, Match, Pixmap

This request creates a cursor and associates identifier cid with it. The
foreground and background RGB values must be specified, even if the server only
has a StaticGray or GrayScale screen. The foreground is used for the bits set to
1 in the source, and the background is used for the bits set to 0. Both source
and mask (if specified) must have depth one (or a Match error results), but they
can have any root. The mask pixmap defines the shape of the cursor. That is, the
bits set to 1 in the mask define which source pixels will be displayed, and
where the mask has bits set to 0, the corresponding bits of the source pixmap
are ignored. If no mask is given, all pixels of the source are displayed. The
mask, if present, must be the same size as the source (or a Match error
results). The x and y coordinates define the hotspot relative to the source's
origin and must be a point within the source (or a Match error results).

The components of the cursor may be transformed arbitrarily to meet display
limitations.

The pixmaps can be freed immediately if no further explicit references to them
are to be made.

Subsequent drawing in the source or mask pixmap has an undefined effect on the
cursor. The server might or might not make a copy of the pixmap.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['CreateCursor', 'CreateCursorChecked', ]


class CreateCursorAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xIIIHHHHHHHH'
    code = 93

    def _getbinary(self, cid, source, mask, fore_red, fore_green, fore_blue,
                    back_red, back_green, back_blue, x, y):
        buf = _StringIO()
        buf.write(_pack(self.fmt, cid, source, mask, fore_red, fore_green,
                        fore_blue, back_red, back_green, back_blue, x, y))
        return buf.getvalue()

    def __call__(self, cid, source, mask, fore_red, fore_green, fore_blue,
                 back_red, back_green, back_blue, x, y):
        """Request CreateCursor X protocol.

        @Arguments:
        - `cid`:
        - `source`:
        - `mask`:
        - `fore_red`:
        - `fore_green`:
        - `fore_blue`:
        - `back_red`:
        - `back_green`:
        - `back_blue`:
        - `x`:
        - `y`:

        @Return:
        VoidCookie

        @Error:
        BadAlloc, BadIDChoice, BadMatch, BadPixmap
        """
        return self.request(
            self._getbinary(cid, source, mask, fore_red, fore_green, fore_blue,
                            back_red, back_green, back_blue, x, y))


class CreateCursor(CreateCursorAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cid, source, mask, fore_red, fore_green, fore_blue, back_red,
        back_green, back_blue, x, y)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class CreateCursorChecked(CreateCursorAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cid, source, mask, fore_red, fore_green, fore_blue, back_red,
        back_green, back_blue, x, y)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# createcursor.py ends here
