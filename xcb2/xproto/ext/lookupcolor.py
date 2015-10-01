#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: lookupcolor.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""lookupcolor -- a parts of xcb2

LookupColor

cmap: COLORMAP
name: STRING8

exact-red, exact-green, exact-blue: CARD16
visual-red, visual-green, visual-blue: CARD16

Errors: Colormap, Name

This request looks up the string name of a color with respect to the screen
associated with cmap and returns both the exact color values and the closest
values provided by the hardware with respect to the visual type of cmap. The
name should use the ISO Latin-1 encoding, and uppercase and lowercase do not
matter.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import LookupColorCookie, LookupColorReply


__all__ = ['LookupColor', 'LookupColorUnchecked', ]


class LookupColorAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xIH2x'
    code = 92

    def _getbinary(self, cmap, name_len, name):
        buf = _StringIO()
        buf.write(_pack(self.fmt, cmap, name_len, name))
        return buf.getvalue()

    def __call__(self, cmap, name_len, name):
        """Request LookupColor X protocol.

        @Arguments:
        - `cmap`:
        - `name_len`:
        - `name`:

        @Return:
        LookupColorCookie

        @Error:
        BadColormap, BadName
        """
        return self.request(self._getbinary(cmap, name_len, name))


class LookupColor(LookupColorAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cmap, name_len, name)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            LookupColorCookie(), LookupColorReply)


class LookupColorUnchecked(LookupColorAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cmap, name_len, name)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            LookupColorCookie(), LookupColorReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# lookupcolor.py ends here
