#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""button -- DESCRIPTION

"""
from enum import IntEnum as _IntEnum
from xcb import xtest
from xcb import xproto

from xahk2.input.eventcode import EventCode


class ButtonIndex(_IntEnum):
    r"""ButtonIndex

    ButtonIndex is a _IntEnum.
    Responsibility:
    """
    Left = xproto.ButtonIndex._1
    Middle = xproto.ButtonIndex._2
    Right = xproto.ButtonIndex._3
    WheelUp = xproto.ButtonIndex._4
    WheelDown = xproto.ButtonIndex._5


class ModifierMask(_IntEnum):
    r"""SUMMARY
    """
    Null      = 0
    Shift     = xproto.KeyButMask.Shift
    Lock      = xproto.KeyButMask.Lock
    Control   = xproto.KeyButMask.Control
    Alt       = xproto.KeyButMask.Mod1
    Numlock   = xproto.KeyButMask.Mod2
    Hiper     = xproto.KeyButMask.Mod3
    Super     = xproto.KeyButMask.Mod4
    Mod5      = xproto.KeyButMask.Mod5
    Left      = xproto.KeyButMask.Button1
    Middle    = xproto.KeyButMask.Button2
    Right     = xproto.KeyButMask.Button3
    WheelUp   = xproto.KeyButMask.Button4
    WheelDown = xproto.KeyButMask.Button5
    Any       = 1 << 15 # 32768


class X11Button(object):
    """Class X11Button
    """
    # Attributes:
    def __init__(self, display, code):
        r"""

        @Arguments:
        - `display`:
        - `code`:
        """
        self.display = display
        self._code = code

    # Operations
    def get_display(self):
        """function get_display

        returns
        """
        return self.display

    def get_code(self):
        """function get_code

        returns
        """
        return self._code

    @property
    def root(self, ):
        r"""SUMMARY

        root()

        @Return:

        @Error:
        """
        return self.display.get_setup().roots[0].root

    def _fake_input(self, evcode):
        r"""SUMMARY

        _fake_input(evcode)

        @Arguments:
        - `evcode`:

        @Return:

        @Error:
        """
        return self.display(xtest.key).FakeInputChecked(
            # EventCode, code, time, window, x, y, deviceid
            evcode, self._code, 0, self.root, 0, 0, 0)

    def press(self, ):
        """function press

        returns
        """
        return self._fake_input(EventCode.ButtonPress)

    def release(self, ):
        """function release

        returns
        """
        return self._fake_input(EventCode.ButtonRelease)

    def tap(self, ):
        """function tap

        returns
        """
        return [self.press(), self.release()]

    def as_modifier(self):
        """function as_modifier

        returns
        """
        return {ButtonIndex.Left: ModifierMask.Left,
                ButtonIndex.Middle: ModifierMask.Middle,
                ButtonIndex.Right: ModifierMask.Right,
                ButtonIndex.WheelUp: ModifierMask.WheelUp,
                ButtonIndex.WheelDown: ModifierMask.WheelDown,}.get(self._code)

    def __repr__(self):
        return '{0.__class__.__name__}({0._code}, "{1}")'.format(
            self, ButtonIndex(self._code))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# button.py ends here
