#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""event -- DESCRIPTION

"""
from struct import pack

from xcb.xproto import KeyPressEvent, EventMask

from xahk.x11.modifier import Modifier
from xahk.x11.eventcode import EventCode


class KeyEvent(object):
    r"""KeyEvent

    KeyEvent is a object.
    Responsibility:
    """
    __slots__ = ('_event', 'window')

    def __init__(self, event, window):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self._event = event
        self.window = window

    def get_code(self, ):
        r"""SUMMARY

        get_code()

        @Return:

        @Error:
        """
        return self._event.detail

    code = property(get_code)

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self.window.get_display()

    display = property(get_display)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self.window

    def get_modifiers(self, ):
        r"""SUMMARY

        get_modifiers()

        @Return:

        @Error:
        """
        modifiers = 0
        if self.is_shift_down():
            modifiers |= Modifier.Mask.Shift
        if self.is_control_down():
            modifiers |= Modifier.Mask.Control
        if self.is_alt_down():
            modifiers |= Modifier.Mask.Alt
        if self.is_hiper_down():
            modifiers |= Modifier.Mask.Hiper
        if self.is_super_down():
            modifiers |= Modifier.Mask.Super
        if self.is_button_left_down():
            modifiers |= Modifier.Mask.Left
        if self.is_button_middle_down():
            modifiers |= Modifier.Mask.Middle
        if self.is_button_right_down():
            modifiers |= Modifier.Mask.Right
        return modifiers

    modifiers = property(get_modifiers)

    def get_time(self, ):
        r"""SUMMARY

        get_time()

        @Return:

        @Error:
        """
        return self._event.time

    time = property(get_time)

    def is_pressed(self, ):
        r"""SUMMARY

        is_pressed()

        @Return:

        @Error:
        """
        return isinstance(self._event, (KeyPressEvent, ))

    def is_shift_down(self, ):
        r"""SUMMARY

        is_shifted()

        @Return:

        @Error:
        """
        return bool(self._event.state&Modifier.Mask.Shift)

    def is_control_down(self, ):
        r"""SUMMARY

        is_control_down()

        @Return:

        @Error:
        """
        return bool(self._event.state&Modifier.Mask.Control)

    def is_super_down(self, ):
        r"""SUMMARY

        is_super_down()

        @Return:

        @Error:
        """
        return bool(self._event.state&Modifier.Mask.Super)

    def is_alt_down(self, ):
        r"""SUMMARY

        is_alt_down()

        @Return:

        @Error:
        """
        return bool(self._event.state&Modifier.Mask.Alt)

    def is_hiper_down(self, ):
        r"""SUMMARY

        is_hiper_down()

        @Return:

        @Error:
        """
        return bool(self._event.state&Modifier.Mask.Hiper)

    def is_button_left_down(self, ):
        r"""SUMMARY

        is_button_left_down()

        @Return:

        @Error:
        """
        return bool(self._event.state&Modifier.Mask.Left)

    def is_button_middle_down(self, ):
        r"""SUMMARY

        is_button_middle_down()

        @Return:

        @Error:
        """
        return bool(self._event.state&Modifier.Mask.Middle)

    def is_button_right_down(self, ):
        r"""SUMMARY

        is_button_right_down()

        @Return:

        @Error:
        """
        return bool(self._event.state&Modifier.Mask.Right)

    def resend(self, ):
        r"""SUMMARY

        resend()

        @Return:

        @Error:
        """
        code, mask = EventCode.KeyPress, EventMask.KeyPress
        # print((self._event.root_x, self._event.root_y, self._event.event_x, self._event.event_y))
        if not self.is_pressed():
            code, mask = EventCode.KeyRelease, EventMask.KeyRelease
        ev = pack('BBH4I5HBx', code, self.code, 0,
                  self.time, self._event.root, self.window, self._event.child,
                  # self._event.root_x, self._event.root_y,
                  # self._event.event_x, self._event.event_y,
                  0, 0, 0, 0,
                  self._event.state, self._event.same_screen)
        return self.display.core.SendEventChecked(False, self.window, mask, ev)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# event.py ends here
