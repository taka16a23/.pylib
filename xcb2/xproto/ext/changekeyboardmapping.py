#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""changekeyboardmapping -- a parts of xcb2

ChangeKeyboardMapping

first-keycode: KEYCODE
keysyms-per-keycode: CARD8
keysyms: LISTofKEYSYM

Errors: Alloc, Value

This request defines the symbols for the specified number of keycodes, starting
with the specified keycode. The symbols for keycodes outside this range remained
unchanged. The number of elements in the keysyms list must be a multiple of
keysyms-per-keycode (or a Length error results). The first-keycode must be
greater than or equal to min-keycode as returned in the connection setup (or a
Value error results) and:

        first-keycode + (keysyms-length / keysyms-per-keycode) - 1
must be less than or equal to max-keycode as returned in the connection setup
(or a Value error results). KEYSYM number N (counting from zero) for keycode K
has an index (counting from zero) of:

        (K - first-keycode) * keysyms-per-keycode + N
in keysyms. The keysyms-per-keycode can be chosen arbitrarily by the client to
be large enough to hold all desired symbols. A special KEYSYM value of NoSymbol
should be used to fill in unused elements for individual keycodes. It is legal
for NoSymbol to appear in nontrailing positions of the effective list for a
keycode.

This request generates a MappingNotify event.

There is no requirement that the server interpret this mapping; it is merely
stored for reading and writing by clients (see section 5).
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['ChangeKeyboardMapping', 'ChangeKeyboardMappingChecked', ]


class ChangeKeyboardMappingAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xBB2x'
    code = 100

    def _getbinary(self,
            keycode_count, first_keycode, keysyms_per_keycode, keysyms):
        buf = _StringIO()
        buf.write(_pack(self.fmt, keycode_count, first_keycode,
                        keysyms_per_keycode))
        buf.write(str(buffer(array('I', keysyms))))
        return buf.getvalue()


    def __call__(self, keycode_count, first_keycode, keysyms_per_keycode,
                 keysyms):
        """Request ChangeKeyboardMapping X protocol

        @Arguments:
        - `keycode_count`:
        - `first_keycode`:
        - `keysyms_per_keycode`:
        - `keysyms`:

        @Return:
        VoidCookie

        @Error:
        BadAlloc, BadValue
        """
        return self.request(self._getbinary(
            keycode_count, first_keycode, keysyms_per_keycode, keysyms))


class ChangeKeyboardMapping(ChangeKeyboardMappingAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(keycode_count, first_keycode, keysyms_per_keycode, keysyms)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class ChangeKeyboardMappingChecked(ChangeKeyboardMappingAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(keycode_count, first_keycode, keysyms_per_keycode, keysyms)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# changekeyboardmapping.py ends here
