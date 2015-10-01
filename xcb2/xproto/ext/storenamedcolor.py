#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: storenamedcolor.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""storenamedcolor -- a parts of xcb2

StoreNamedColor

cmap: COLORMAP
pixel: CARD32
name: STRING8
do-red, do-green, do-blue: BOOL

Errors: Access, Colormap, Name, Value

This request looks up the named color with respect to the screen associated with
cmap and then does a StoreColors in cmap. The name should use the ISO Latin-1
encoding, and uppercase and lowercase do not matter. The Access and Value errors
are the same as in StoreColors.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['StoreNamedColor', 'StoreNamedColorChecked', ]


class StoreNamedColorAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xIIH2x'
    code = 90

    def _getbinary(self, flags, cmap, pixel, name_len, name):
        buf = _StringIO()
        buf.write(_pack(self.fmt, flags, cmap, pixel, name_len))
        buf.write(str(buffer(_array('b', name))))
        return buf.getvalue()

    def __call__(self, flags, cmap, pixel, name_len, name):
        """Request StoreNamedColor X protocol.

        @Arguments:
        - `flags`:
        - `cmap`:
        - `pixel`:
        - `name_len`:
        - `name`:

        @Return:
        VoidCookie

        @Error:
        BadAccess, BadColormap, BadName, BadValue
        """
        return self.request(self._getbinary(flags, cmap, pixel, name_len, name))


class StoreNamedColor(StoreNamedColorAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(flags, cmap, pixel, name_len, name)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class StoreNamedColorChecked(StoreNamedColorAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(flags, cmap, pixel, name_len, name)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# storenamedcolor.py ends here
