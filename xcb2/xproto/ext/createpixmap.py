#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: createpixmap.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""createpixmap -- a parts of xcb2

CreatePixmap

pid: PIXMAP
drawable: DRAWABLE
depth: CARD8
width, height: CARD16

Errors: Alloc, Drawable, IDChoice, Value

This request creates a pixmap and assigns the identifier pid to it. The width
and height must be nonzero (or a Value error results). The depth must be one of
the depths supported by the root of the specified drawable (or a Value error
results). The initial contents of the pixmap are undefined.

It is legal to pass an InputOnly window as a drawable to this request.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['CreatePixmap', 'CreatePixmapChecked', ]


class CreatePixmapAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xIIHH'
    code = 53

    def _getbinary(self, depth, pid, drawable, width, height):
        buf = _StringIO()
        buf.write(_pack(self.fmt, depth, pid, drawable, width, height))
        return buf.getvalue()

    def __call__(self, depth, pid, drawable, width, height):
        """Request CreatePixmap X protocol.

        @Arguments:
        - `depth`:
        - `pid`:
        - `drawable`:
        - `width`:
        - `height`:

        @Return:
        VoidCookie

        @Error:
        BadAlloc, BadDrawable, BadIDChoice, BadValue
        """
        return self.request(self._getbinary(depth, pid, drawable, width, height))


class CreatePixmap(CreatePixmapAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(depth, pid, drawable, width, height)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class CreatePixmapChecked(CreatePixmapAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(depth, pid, drawable, width, height)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# createpixmap.py ends here
