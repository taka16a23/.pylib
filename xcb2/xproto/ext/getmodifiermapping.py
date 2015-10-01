#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""getmodifiermapping -- a parts of xcb2

GetModifierMapping

keycodes-per-modifier: CARD8
keycodes: LISTofKEYCODE
This request returns the keycodes of the keys being used as modifiers. The
number of keycodes in the list is 8*keycodes-per-modifier. The keycodes are
divided into eight sets, with each set containing keycodes-per-modifier
elements. The sets are assigned to the modifiers Shift, Lock, Control, Mod1,
Mod2, Mod3, Mod4, and Mod5, in order. The keycodes-per-modifier value is chosen
arbitrarily by the server; zeroes are used to fill in unused elements within
each set. If only zero values are given in a set, the use of the corresponding
modifier has been disabled. The order of keycodes within each set is chosen
arbitrarily by the server.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import GetModifierMappingCookie, GetModifierMappingReply


__all__ = ['GetModifierMapping', 'GetModifierMappingUnchecked', ]


class GetModifierMappingAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2x'
    code = 119

    def _getbinary(self, ):
        buf = _StringIO()
        buf.write(_pack(self.fmt, ))
        return buf.getvalue()

    def __call__(self, ):
        """Request GetModifierMapping X protocol.

        @Return:
        GetModifierMappingCookie
        """
        return self.request(self._getbinary())


class GetModifierMapping(GetModifierMappingAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request()

        @Arguments:

        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            GetModifierMappingCookie(), GetModifierMappingReply)


class GetModifierMappingUnchecked(GetModifierMappingAbstract):
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
            GetModifierMappingCookie(), GetModifierMappingReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# getmodifiermapping.py ends here
