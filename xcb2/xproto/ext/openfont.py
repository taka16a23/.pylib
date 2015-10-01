#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""openfont -- a parts of xcb2

OpenFont

fid: FONT
name: STRING8

Errors: Alloc, IDChoice, Name

This request loads the specified font, if necessary, and associates identifier
fid with it. The font name should use the ISO Latin-1 encoding, and uppercase
and lowercase do not matter. When the characters “?” and “*” are used in a
font name, a pattern match is performed and any matching font is used. In the
pattern, the “?” character (octal value 77) will match any single character,
and the “*” character (octal value 52) will match any number of characters. A
structured format for font names is specified in the X.Org standard X Logical
Font Description Conventions.

Fonts are not associated with a particular screen and can be stored as a
component of any graphics context.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['OpenFont', 'OpenFontChecked', ]


class OpenFontAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xIH2x'
    code = 45

    def _getbinary(self, fid, name_len, name):
        buf = _StringIO()
        buf.write(_pack(self.fmt, fid, name_len))
        buf.write(str(buffer(_array('b', name))))
        return buf.getvalue()

    def __call__(self, fid, name_len, name):
        """Request OpenFont X protocol.

        @Arguments:
        - `fid`:
        - `name_len`:
        - `name`:

        @Return:
        VoidCookie

        @Error:
        BadAlloc, BadIDChoice, BadName
        """
        return self.request(self._getbinary(fid, name_len, name))


class OpenFont(OpenFontAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(fid, name_len, name)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class OpenFontChecked(OpenFontAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(fid, name_len, name)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# openfont.py ends here
