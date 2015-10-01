#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""changekeyboardcontrol -- a parts of xcb2

ChangeKeyboardControl

value-mask: BITMASK
value-list: LISTofVALUE

Errors: Match, Value

This request controls various aspects of the keyboard. The value-mask and
value-list specify which controls are to be changed. The possible values are:

Control	Type
key-click-percent	INT8
bell-percent	INT8
bell-pitch	INT16
bell-duration	INT16
led	CARD8
led-mode	 { On, Off }
key	KEYCODE
auto-repeat-mode	 { On, Off, Default }
The key-click-percent sets the volume for key clicks between 0 (off) and 100
(loud) inclusive, if possible. Setting to -1 restores the default. Other
negative values generate a Value error.

The bell-percent sets the base volume for the bell between 0 (off) and 100
(loud) inclusive, if possible. Setting to -1 restores the default. Other
negative values generate a Value error.

The bell-pitch sets the pitch (specified in Hz) of the bell, if
possible. Setting to -1 restores the default. Other negative values generate a
Value error.

The bell-duration sets the duration of the bell (specified in milliseconds), if
possible. Setting to -1 restores the default. Other negative values generate a
Value error.

If both led-mode and led are specified, then the state of that LED is changed,
if possible. If only led-mode is specified, then the state of all LEDs are
changed, if possible. At most 32 LEDs, numbered from one, are supported. No
standard interpretation of LEDs is defined. It is a Match error if an led is
specified without an led-mode.

If both auto-repeat-mode and key are specified, then the auto-repeat mode of
that key is changed, if possible. If only auto-repeat-mode is specified, then
the global auto-repeat mode for the entire keyboard is changed, if possible,
without affecting the per-key settings. It is a Match error if a key is
specified without an auto-repeat-mode. Each key has an individual mode of
whether or not it should auto-repeat and a default setting for that mode. In
addition, there is a global mode of whether auto-repeat should be enabled or not
and a default setting for that mode. When the global mode is On, keys should
obey their individual auto-repeat modes. When the global mode is Off, no keys
should auto-repeat. An auto-repeating key generates alternating KeyPress and
KeyRelease events. When a key is used as a modifier, it is desirable for the key
not to auto-repeat, regardless of the auto-repeat setting for that key.

A bell generator connected with the console but not directly on the keyboard is
treated as if it were part of the keyboard.

The order in which controls are verified and altered is server-dependent. If an
error is generated, a subset of the controls may have been altered.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['ChangeKeyboardControl', 'ChangeKeyboardControlChecked', ]


class ChangeKeyboardControlAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xI'
    code = 102

    def _getbinary(self, value_mask, value_list):
        buf = _StringIO()
        buf.write(_pack(self.fmt, value_mask))
        buf.write(str(buffer(_array('I', value_list))))
        return buf.getvalue()

    def __call__(self, value_mask, value_list):
        """Request ChangeKeyboardControl X protocol.

        @Arguments:
        - `value_mask`:
        - `value_list`:

        @Return:
        VoidCookie

        @Error:
        BadMatch, BadValue
        """
        return self.request(self._getbinary(value_mask, value_list))


class ChangeKeyboardControl(ChangeKeyboardControlAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(value_mask, value_list)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class ChangeKeyboardControlChecked(ChangeKeyboardControlAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(value_mask, value_list)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# changekeyboardcontrol.py ends here
