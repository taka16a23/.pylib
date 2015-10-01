#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: imagetext16.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""imagetext16 -- a parts of xcb2

ImageText16

drawable: DRAWABLE
gc: GCONTEXT
x, y: INT16
string: STRING16

Errors: Drawable, GContext, Match

This request is similar to ImageText8, except 2-byte (or 16-bit) characters are
used. For fonts defined with linear indexing rather than 2-byte matrix indexing,
the server will interpret each CHAR2B as a 16-bit number that has been
transmitted most significant byte first (that is, byte1 of the CHAR2B is taken
as the most significant byte).
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie, Iterator
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['ImageText16', 'ImageText16Checked', ]


class ImageText16Abstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xIIhh'
    code = 77

    def _getbinary(self, string_len, drawable, gc, x, y, string):
        buf = _StringIO()
        buf.write(_pack(self.fmt, string_len, drawable, gc, x, y, string))
        for elt in Iterator(string, 2, 'string', True):
            buf.write(_pack('=BB', *elt))
        return buf.getvalue()

    def __call__(self, string_len, drawable, gc, x, y, string):
        """Request ImageText16 X protocol.

        @Arguments:
        - `string_len`:
        - `drawable`:
        - `gc`:
        - `x`:
        - `y`:
        - `string`:

        @Return:
        VoidCookie

        @Error:
        BadDrawable, BadGContext, BadMatch
        """
        return self.request(
            self._getbinary(string_len, drawable, gc, x, y, string))


class ImageText16(ImageText16Abstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(string_len, drawable, gc, x, y, string)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class ImageText16Checked(ImageText16Abstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(string_len, drawable, gc, x, y, string)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# imagetext16.py ends here
