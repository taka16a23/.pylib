#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""querybestsize -- a parts of xcb2

QueryBestSize

class: { Cursor, Tile, Stipple}
drawable: DRAWABLE
width, height: CARD16

width, height: CARD16

Errors: Drawable, Match, Value

This request returns the best size that is closest to the argument size. For
Cursor, this is the largest size that can be fully displayed. For Tile, this is
the size that can be tiled fastest. For Stipple, this is the size that can be
stippled fastest.

For Cursor, the drawable indicates the desired screen. For Tile and Stipple, the
drawable indicates the screen and also possibly the window class and depth. An
InputOnly window cannot be used as the drawable for Tile or Stipple (or a Match
error results).
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import QueryBestSizeCookie, QueryBestSizeReply


__all__ = ['QueryBestSize', 'QueryBestSizeUnchecked', ]


class QueryBestSizeAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xIHH'
    code = 97

    def _getbinary(self, _class, drawable, width, height):
        buf = _StringIO()
        buf.write(_pack(self.fmt, _class, drawable, width, height))
        return buf.getvalue()

    def __call__(self, _class, drawable, width, height):
        """Request QueryBestSize X protocol.

        @Arguments:
        - `_class`:
        - `drawable`:
        - `width`:
        - `height`:

        @Return:
        QueryBestSizeCookie

        @Error:
        BadDrawable, BadMatch, BadValue
        """
        return self.request(self._getbinary(_class, drawable, width, height))


class QueryBestSize(QueryBestSizeAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(_class, drawable, width, height)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            QueryBestSizeCookie(), QueryBestSizeReply)


class QueryBestSizeUnchecked(QueryBestSizeAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(_class, drawable, width, height)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            QueryBestSizeCookie(), QueryBestSizeReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# querybestsize.py ends here
