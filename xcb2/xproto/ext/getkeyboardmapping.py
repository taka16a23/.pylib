#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""getkeyboardmapping -- a parts of xcb2

GetKeyboardMapping

first-keycode: KEYCODE
count: CARD8

keysyms-per-keycode: CARD8
keysyms: LISTofKEYSYM

Errors: Value

This request returns the symbols for the specified number of keycodes, starting
with the specified keycode. The first-keycode must be greater than or equal to
min-keycode as returned in the connection setup (or a Value error results), and:

	first-keycode + count - 1
must be less than or equal to max-keycode as returned in the connection setup
(or a Value error results). The number of elements in the keysyms list is:

	count * keysyms-per-keycode
and KEYSYM number N (counting from zero) for keycode K has an index (counting
from zero) of:

	(K - first-keycode) * keysyms-per-keycode + N
in keysyms. The keysyms-per-keycode value is chosen arbitrarily by the server to
be large enough to report all requested symbols. A special KEYSYM value of
NoSymbol is used to fill in unused elements for individual keycodes.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import GetKeyboardMappingCookie, GetKeyboardMappingReply
from xcb2.xproto.wcookie import WrapGetKeyboardMappingCookie


__all__ = ['GetKeyboardMapping', 'GetKeyboardMappingUnchecked', ]


class GetKeyboardMappingAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xBB'
    code = 101

    def _getbinary(self, first_keycode, count):
        buf = _StringIO()
        buf.write(_pack(self.fmt, first_keycode, count))
        return buf.getvalue()

    def __call__(self, first_keycode, count):
        """Request GetKeyboardMapping X protocol.

        @Arguments:
        - `first_keycode`:
        - `count`:

        @Return:
        GetKeyboardMappingCookie

        @Error:
        BadValue
        """
        return WrapGetKeyboardMappingCookie(
            self._connection,
            self.request(self._getbinary(first_keycode, count)))


class GetKeyboardMapping(GetKeyboardMappingAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(first_keycode, count)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            GetKeyboardMappingCookie(), GetKeyboardMappingReply)


class GetKeyboardMappingUnchecked(GetKeyboardMappingAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(first_keycode, count)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            GetKeyboardMappingCookie(), GetKeyboardMappingReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# getkeyboardmapping.py ends here
