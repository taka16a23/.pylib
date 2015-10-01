#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: freepixmap.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""freepixmap -- a parts of xcb2

FreePixmap

pixmap: PIXMAP

Errors: Pixmap

This request deletes the association between the resource ID and the pixmap. The
pixmap storage will be freed when no other resource references it.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['FreePixmap', 'FreePixmapChecked', ]


class FreePixmapAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xI'
    code = 54

    def _getbinary(self, pixmap):
        buf = _StringIO()
        buf.write(_pack(self.fmt, pixmap))
        return buf.getvalue()

    def __call__(self, pixmap):
        """Request FreePixmap X protocol.

        @Arguments:
        - `pixmap`:

        @Return:
        VoidCookie

        @Error:
        BadPixmap
        """
        return self.request(self._getbinary(pixmap))


class FreePixmap(FreePixmapAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(pixmap)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class FreePixmapChecked(FreePixmapAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(pixmap)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# freepixmap.py ends here
