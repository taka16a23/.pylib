#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: allocnamedcolor.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""allocnamedcolor -- a parts of xcb2

AllocNamedColor

cmap: COLORMAP
name: STRING8

pixel: CARD32
exact-red, exact-green, exact-blue: CARD16
visual-red, visual-green, visual-blue: CARD16

Errors: Alloc, Colormap, Name

This request looks up the named color with respect to the screen associated with
the colormap. Then, it does an AllocColor on cmap. The name should use the ISO
Latin-1 encoding, and uppercase and lowercase do not matter. The exact RGB
values specify the true values for the color, and the visual values specify the
values actually used in the colormap.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import AllocNamedColorCookie, AllocNamedColorReply


__all__ = ['AllocNamedColor', 'AllocNamedColorUnchecked', ]


class AllocNamedColorAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xIH2x'
    code = 85

    def _getbinary(self, cmap, name_len, name):
        r"""SUMMARY

        _getbinary(cmap, name_len)

        @Arguments:
        - `cmap`:
        - `name_len`:

        @Return:
        """
        buf = _StringIO()
        buf.write(_pack(self.fmt, cmap, name_len))
        buf.write(str(buffer(_array('b', name))))
        return buf.getvalue()

    def __call__(self, cmap, name_len, name):
        """Request AllocNamedColor X protocol.

        @Arguments:
        - `cmap`:
        - `name_len`:
        - `name`:

        @Return:
        AllocNamedColorCookie

        @Error:
        BadAlloc, BadColormap, BadName
        """
        return self.request(self._getbinary(cmap, name_len, name))


class AllocNamedColor(AllocNamedColorAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cmap, name_len)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            AllocNamedColorCookie(), AllocNamedColorReply)


class AllocNamedColorUnchecked(AllocNamedColorAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cmap, name_len)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            AllocNamedColorCookie(), AllocNamedColorReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# allocnamedcolor.py ends here
