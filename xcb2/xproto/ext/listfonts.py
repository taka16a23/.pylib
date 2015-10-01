#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""listfonts -- a parts of xcb2

"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import ListFontsCookie, ListFontsReply


__all__ = ['ListFonts', 'ListFontsUnchecked', ]


class ListFontsAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xHH'
    code = 49

    def _getbinary(self, max_names, pattern_len, pattern):
        buf = _StringIO()
        buf.write(_pack(self.fmt, max_names, pattern_len))
        buf.write(str(buffer(_array('b', pattern))))
        return buf.getvalue()

    def __call__(self, max_names, pattern_len, pattern):
        return self.request(self._getbinary(max_names, pattern_len, pattern))


class ListFonts(ListFontsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(max_names, pattern_len, pattern)

        @Arguments:
        - [yas] elisp error!:
        - [yas] elisp error!:
        - [yas] elisp error!:
        - [yas] elisp error!:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            ListFontsCookie(), ListFontsReply)


class ListFontsUnchecked(ListFontsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(max_names, pattern_len, pattern)

        @Arguments:
        - [yas] elisp error!:
        - [yas] elisp error!:
        - [yas] elisp error!:
        - [yas] elisp error!:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            ListFontsCookie(), ListFontsReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# listfonts.py ends here
