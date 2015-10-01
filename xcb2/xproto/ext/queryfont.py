#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""queryfont -- a parts of xcb2

QueryFont

font: FONTABLE

font-info: FONTINFO
char-infos: LISTofCHARINFO
where:
FONTINFO:	 [draw-direction: { LeftToRight, RightToLeft }
min-char-or-byte2, max-char-or-byte2: CARD16
min-byte1, max-byte1: CARD8
all-chars-exist: BOOL
default-char: CARD16
min-bounds: CHARINFO
max-bounds: CHARINFO
font-ascent: INT16
font-descent: INT16
properties: LISTofFONTPROP]
FONTPROP:	 [name: ATOM
value: <32-bit-value>]
CHARINFO:	 [left-side-bearing: INT16
right-side-bearing: INT16
character-width: INT16
ascent: INT16
descent: INT16
attributes: CARD16]

Errors: Font

This request returns logical information about a font. If a gcontext is given
for font, the currently contained font is used.

The draw-direction is just a hint and indicates whether most char-infos have a
positive, LeftToRight, or a negative, RightToLeft, character-width metric. The
core protocol defines no support for vertical text.

If min-byte1 and max-byte1 are both zero, then min-char-or-byte2 specifies the
linear character index corresponding to the first element of char-infos, and
max-char-or-byte2 specifies the linear character index of the last element. If
either min-byte1 or max-byte1 are nonzero, then both min-char-or-byte2 and
max-char-or-byte2 will be less than 256, and the 2-byte character index values
corresponding to char-infos element N (counting from 0) are:

	byte1 = N/D + min-byte1
	byte2 = N\\D + min-char-or-byte2
where:

	D = max-char-or-byte2 - min-char-or-byte2 + 1
	/ = integer division
	\\ = integer modulus
If char-infos has length zero, then min-bounds and max-bounds will be identical,
and the effective char-infos is one filled with this char-info, of length:

	L = D * (max-byte1 - min-byte1 + 1)
That is, all glyphs in the specified linear or matrix range have the same
information, as given by min-bounds (and max-bounds). If all-chars-exist is
True, then all characters in char-infos have nonzero bounding boxes.

The default-char specifies the character that will be used when an undefined or
nonexistent character is used. Note that default-char is a CARD16, not
CHAR2B. For a font using 2-byte matrix format, the default-char has byte1 in the
most significant byte and byte2 in the least significant byte. If the
default-char itself specifies an undefined or nonexistent character, then no
printing is performed for an undefined or nonexistent character.

The min-bounds and max-bounds contain the minimum and maximum values of each
individual CHARINFO component over all char-infos (ignoring nonexistent
characters). The bounding box of the font (that is, the smallest rectangle
enclosing the shape obtained by superimposing all characters at the same origin
[x,y]) has its upper-left coordinate at:

	[x + min-bounds.left-side-bearing, y - max-bounds.ascent]
with a width of:

	max-bounds.right-side-bearing - min-bounds.left-side-bearing
and a height of:

	max-bounds.ascent + max-bounds.descent
The font-ascent is the logical extent of the font above the baseline and is used
for determining line spacing. Specific characters may extend beyond this. The
font-descent is the logical extent of the font at or below the baseline and is
used for determining line spacing. Specific characters may extend beyond
this. If the baseline is at Y-coordinate y, then the logical extent of the font
is inclusive between the Y-coordinate values (y - font-ascent) and (y +
font-descent - 1).

A font is not guaranteed to have any properties. The interpretation of the
property value (for example, INT32, CARD32) must be derived from a priori
knowledge of the property. A basic set of font properties is specified in the
X.Org standard X Logical Font Description Conventions.

For a character origin at [x,y], the bounding box of a character (that is, the
smallest rectangle enclosing the character's shape), described in terms of
CHARINFO components, is a rectangle with its upper-left corner at:

	[x + left-side-bearing, y - ascent]
with a width of:

	right-side-bearing - left-side-bearing
and a height of:

	ascent + descent
and the origin for the next character is defined to be:

	[x + character-width, y]
Note that the baseline is logically viewed as being just below nondescending
characters (when descent is zero, only pixels with Y-coordinates less than y are
drawn) and that the origin is logically viewed as being coincident with the left
edge of a nonkerned character (when left-side-bearing is zero, no pixels with
X-coordinate less than x are drawn).

Note that CHARINFO metric values can be negative.

A nonexistent character is represented with all CHARINFO components zero.

The interpretation of the per-character attributes field is server-dependent.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import QueryFontCookie, QueryFontReply


__all__ = ['QueryFont', 'QueryFontUnchecked', ]


class QueryFontAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xI'
    code = 47

    def _getbinary(self, font):
        buf = _StringIO()
        buf.write(_pack(self.fmt, font))
        return buf.getvalue()

    def __call__(self, font):
        """Request QueryFont X protocol.

        @Arguments:
        - `font`:

        @Return:
        QueryFontCookie

        @Error:
        BadFont
        """
        return self.request(self._getbinary(font))


class QueryFont(QueryFontAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(font)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            QueryFontCookie(), QueryFontReply)


class QueryFontUnchecked(QueryFontAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(font)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            QueryFontCookie(), QueryFontReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# queryfont.py ends here
