#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""listfontswithinfo -- a parts of xcb2

ListFontsWithInfo

pattern: STRING8
max-names: CARD16

name: STRING8
info FONTINFO
replies-hint: CARD32
where:
FONTINFO: <same type definition as in QueryFont>
This request is similar to ListFonts, but it also returns information about each
font. The information returned for each font is identical to what QueryFont
would return except that the per-character metrics are not returned. Note that
this request can generate multiple replies. With each reply, replies-hint may
provide an indication of how many more fonts will be returned. This number is a
hint only and may be larger or smaller than the number of fonts actually
returned. A zero value does not guarantee that no more fonts will be
returned. After the font replies, a reply with a zero-length name is sent to
indicate the end of the reply sequence.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import ListFontsWithInfoCookie, ListFontsWithInfoReply


__all__ = ['ListFontsWithInfo', 'ListFontsWithInfoUnchecked', ]


class ListFontsWithInfoAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xHH'
    code = 50

    def _getbinary(self, max_names, pattern_len, pattern):
        buf = _StringIO()
        buf.write(_pack(self.fmt, max_names, pattern_len, pattern))
        buf.write(str(buffer(_array('b', pattern))))
        return buf.getvalue()

    def __call__(self, max_names, pattern_len, pattern):
        """Request ListFonts X protocol.

        @Arguments:
        - `max_names`:
        - `pattern_len`:
        - `pattern`:

        @Return:
        ListFontsWithInfoCookie
        """
        return self.request(self._getbinary(max_names, pattern_len, pattern))


class ListFontsWithInfo(ListFontsWithInfoAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(max_names, pattern_len, pattern)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            ListFontsWithInfoCookie(), ListFontsWithInfoReply)


class ListFontsWithInfoUnchecked(ListFontsWithInfoAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(max_names, pattern_len, pattern)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            ListFontsWithInfoCookie(), ListFontsWithInfoReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# listfontswithinfo.py ends here
