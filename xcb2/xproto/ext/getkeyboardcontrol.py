#!/usr/bin/env python
# -*- coding: utf-8 -*-

r"""getkeyboardcontrol -- a parts of xcb2

GetKeyboardControl

key-click-percent: CARD8
bell-percent: CARD8
bell-pitch: CARD16
bell-duration: CARD16
led-mask: CARD32
global-auto-repeat: { On, Off}
auto-repeats: LISTofCARD8
This request returns the current control values for the keyboard. For the LEDs,
the least significant bit of led-mask corresponds to LED one, and each one bit
in led-mask indicates an LED that is lit. The auto-repeats is a bit vector; each
one bit indicates that auto-repeat is enabled for the corresponding key. The
vector is represented as 32 bytes. Byte N (from 0) contains the bits for keys 8N
to 8N + 7, with the least significant bit in the byte representing key 8N.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import GetKeyboardControlCookie, GetKeyboardControlReply


__all__ = ['GetKeyboardControl', 'GetKeyboardControlUnchecked', ]


class GetKeyboardControlAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2x'
    code = 103

    def _getbinary(self, ):
        buf = _StringIO()
        buf.write(_pack(self.fmt, ))
        return buf.getvalue()

    def __call__(self, ):
        """Request GetKeyboardControl X protocol.

        @Return:
        GetKeyboardControlCookie
        """
        return self.request(self._getbinary())


class GetKeyboardControl(GetKeyboardControlAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request()

        @Arguments:

        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            GetKeyboardControlCookie(), GetKeyboardControlReply)


class GetKeyboardControlUnchecked(GetKeyboardControlAbstract):
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
            GetKeyboardControlCookie(), GetKeyboardControlReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# getkeyboardcontrol.py ends here
