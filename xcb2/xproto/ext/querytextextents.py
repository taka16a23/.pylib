#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: querytextextents.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""querytextextents -- a parts of xcb2

QueryTextExtents

font: FONTABLE
string: STRING16

draw-direction: { LeftToRight, RightToLeft}
font-ascent: INT16
font-descent: INT16
overall-ascent: INT16
overall-descent: INT16
overall-width: INT32
overall-left: INT32
overall-right: INT32

Errors: Font

This request returns the logical extents of the specified string of characters
in the specified font. If a gcontext is given for font, the currently contained
font is used. The draw-direction, font-ascent, and font-descent are the same as
described in QueryFont. The overall-ascent is the maximum of the ascent metrics
of all characters in the string, and the overall-descent is the maximum of the
descent metrics. The overall-width is the sum of the character-width metrics of
all characters in the string. For each character in the string, let W be the sum
of the character-width metrics of all characters preceding it in the string, let
L be the left-side-bearing metric of the character plus W, and let R be the
right-side-bearing metric of the character plus W. The overall-left is the
minimum L of all characters in the string, and the overall-right is the maximum
R.

For fonts defined with linear indexing rather than 2-byte matrix indexing, the
server will interpret each CHAR2B as a 16-bit number that has been transmitted
most significant byte first (that is, byte1 of the CHAR2B is taken as the most
significant byte).

Characters with all zero metrics are ignored. If the font has no defined
default-char, then undefined characters in the string are also ignored.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, Iterator
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import QueryTextExtentsCookie, QueryTextExtentsReply


__all__ = ['QueryTextExtents', 'QueryTextExtentsUnchecked', ]


class QueryTextExtentsAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=x'
    code = 48

    def _getbinary(self, font, string_len, string):
        buf = _StringIO()
        buf.write(_pack(self.fmt, ))
        buf.write(_pack('=B', (string_len & 1)))
        buf.write(_pack('=2xI', font))
        for elt in Iterator(string, 2, 'string', True):
            buf.write(_pack('=BB', *elt))
        return buf.getvalue()

    def __call__(self, font, string_len, string):
        """Request QueryTextExtents X protocol.

        @Arguments:
        - `font`:
        - `string_len`:
        - `string`:

        @Return:
        QueryTextExtentsCookie

        @Error:
        BadFont
        """
        return self.request(self._getbinary(font, string_len, string))


class QueryTextExtents(QueryTextExtentsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(font, string_len, string)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            QueryTextExtentsCookie(), QueryTextExtentsReply)


class QueryTextExtentsUnchecked(QueryTextExtentsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(font, string_len, string)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            QueryTextExtentsCookie(), QueryTextExtentsReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# querytextextents.py ends here
