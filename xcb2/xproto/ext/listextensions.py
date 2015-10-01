#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""listext -- a parts of xcb2

ListExtensions


names: LISTofSTRING8
This request returns a list of all extensions supported by the server.

SetModifierMapping

keycodes-per-modifier: CARD8
keycodes: LISTofKEYCODE

status: { Success, Busy, Failed}

Errors: Alloc, Value

This request specifies the keycodes (if any) of the keys to be used as
modifiers. The number of keycodes in the list must be 8*keycodes-per-modifier
(or a Length error results). The keycodes are divided into eight sets, with each
set containing keycodes-per-modifier elements. The sets are assigned to the
modifiers Shift, Lock, Control, Mod1, Mod2, Mod3, Mod4, and Mod5, in order. Only
nonzero keycode values are used within each set; zero values are ignored. All of
the nonzero keycodes must be in the range specified by min-keycode and
max-keycode in the connection setup (or a Value error results). The order of
keycodes within a set does not matter. If no nonzero values are specified in a
set, the use of the corresponding modifier is disabled, and the modifier bit
will always be zero. Otherwise, the modifier bit will be one whenever at least
one of the keys in the corresponding set is in the down position.

A server can impose restrictions on how modifiers can be changed (for example,
if certain keys do not generate up transitions in hardware, if auto-repeat
cannot be disabled on certain keys, or if multiple keys per modifier are not
supported). The status reply is Failed if some such restriction is violated, and
none of the modifiers is changed.

If the new nonzero keycodes specified for a modifier differ from those currently
defined and any (current or new) keys for that modifier are logically in the
down state, then the status reply is Busy, and none of the modifiers is changed.

This request generates a MappingNotify event on a Success status.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import ListExtensionsCookie, ListExtensionsReply


__all__ = ['ListExtensions', 'ListExtensionsUnchecked', ]


class ListExtensionsAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2x'
    code = 99

    def _getbinary(self, ):
        buf = _StringIO()
        buf.write(_pack(self.fmt, ))
        return buf.getvalue()

    def __call__(self, ):
        """Request ListExtensions X protocol."""
        return self.request(self._getbinary())


class ListExtensions(ListExtensionsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request()

        @Arguments:

        @Return:
        ListExtensionsCookie

        @Error:
        BadAlloc, BadValue
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            ListExtensionsCookie(), ListExtensionsReply)


class ListExtensionsUnchecked(ListExtensionsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request()

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            ListExtensionsCookie(), ListExtensionsReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# listext.py ends here
