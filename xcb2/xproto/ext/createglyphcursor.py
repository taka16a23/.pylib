#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: createglyphcursor.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""createglyphcursor -- a parts of xcb2

CreateGlyphCursor

cid: CURSOR
source-font: FONT
mask-font: FONT or None
source-char, mask-char: CARD16
fore-red, fore-green, fore-blue: CARD16
back-red, back-green, back-blue: CARD16

Errors: Alloc, Font, IDChoice, Value

This request is similar to CreateCursor, except the source and mask bitmaps are
obtained from the specified font glyphs. The source-char must be a defined glyph
in source-font, and if mask-font is given, mask-char must be a defined glyph in
mask-font (or a Value error results). The mask font and character are
optional. The origins of the source and mask (if it is defined) glyphs are
positioned coincidently and define the hotspot. The source and mask need not
have the same bounding box metrics, and there is no restriction on the placement
of the hotspot relative to the bounding boxes. If no mask is given, all pixels
of the source are displayed. Note that source-char and mask-char are CARD16, not
CHAR2B. For 2-byte matrix fonts, the 16-bit value should be formed with byte1 in
the most significant byte and byte2 in the least significant byte.

The components of the cursor may be transformed arbitrarily to meet display
limitations.

The fonts can be freed immediately if no further explicit references to them are
to be made.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['CreateGlyphCursor', 'CreateGlyphCursorChecked', ]


class CreateGlyphCursorAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xIIIHHHHHHHH'
    code = 94

    def _getbinary(self, cid, source_font, mask_font, source_char, mask_char,
                            fore_red, fore_green, fore_blue, back_red,
                            back_green, back_blue):
        buf = _StringIO()
        buf.write(_pack(self.fmt, cid, source_font, mask_font, source_char,
                        mask_char, fore_red, fore_green, fore_blue, back_red,
                        back_green, back_blue))
        return buf.getvalue()

    def __call__(self, cid, source_font, mask_font, source_char, mask_char,
                 fore_red, fore_green, fore_blue, back_red,
                 back_green, back_blue):
        """Request CreateGlyphCursor X protocol.

        @Arguments:
        - `cid`:
        - `source_font`:
        - `mask_font`:
        - `source_char`:
        - `mask_char`:
        - `fore_red`:
        - `fore_green`:
        - `fore_blue`:
        - `back_red`:
        - `back_green`:
        - `back_blue`:

        @Return:
        VoidCookie

        @Error:
        BadAlloc, BadFont, BadIDChoice, BadValue
        """
        return self.request(
            self._getbinary(cid, source_font, mask_font, source_char, mask_char,
                            fore_red, fore_green, fore_blue, back_red,
                            back_green, back_blue))


class CreateGlyphCursor(CreateGlyphCursorAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cid, source_font, mask_font, source_char, mask_char, fore_red,
        fore_green, fore_blue, back_red, back_green, back_blue)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class CreateGlyphCursorChecked(CreateGlyphCursorAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cid, source_font, mask_font, source_char, mask_char, fore_red,
        fore_green, fore_blue, back_red, back_green, back_blue)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# createglyphcursor.py ends here
