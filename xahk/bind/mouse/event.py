#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""event -- DESCRIPTION

"""
from xcb.xproto import ButtonPressEvent

from xahk.x11.modifier import Modifier


class MouseEvent(object):
    """MouseEvent

    MouseEvent is a object.
    Responsibility:
    """
    __slots__ = ('_event', 'window')

    def __init__(self, event):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self._event = event

    def get_code(self, ):
        r"""SUMMARY

        get_code()

        @Return:

        @Error:
        """
        return self._event.detail

    code = property(get_code)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._event.event

    window = property(get_window)

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

    def get_root(self, ):
        r"""SUMMARY

        get_root()

        @Return:

        @Error:
        """
        return self._event.root

    root = property(get_root)

    def get_child(self, ):
        r"""SUMMARY

        get_child()

        @Return:

        @Error:
        """
        return self._event.child

    child = property(get_child)

    def get_rootx(self, ):
        r"""SUMMARY

        get_rootx()

        @Return:

        @Error:
        """
        return self._event.root_x

    rootx = property(get_rootx)

    def get_rooty(self, ):
        r"""SUMMARY

        get_rooty()

        @Return:

        @Error:
        """
        return self._event.root_y

    rooty = property(get_rooty)

    def get_x(self, ):
        r"""SUMMARY

        get_x()

        @Return:

        @Error:
        """
        return self._event.event_x

    x = property(get_x)

    def get_y(self, ):
        r"""SUMMARY

        get_y()

        @Return:

        @Error:
        """
        return self._event.event_y

    y = property(get_y)

    def get_same_screen(self, ):
        """SUMMARY

        get_same_screen()

        @Return:

        @Error:
        """
        return self._event.same_screen

    same_screen = property(get_same_screen)

    def is_pressed(self, ):
        r"""SUMMARY

        is_pressed()

        @Return:

        @Error:
        """
        return isinstance(self._event, (ButtonPressEvent, ))

    def is_shift_down(self, ):
        r"""SUMMARY

        is_shifted()

        @Return:

        @Error:
        """
        return bool(self._event.state & Modifier.Mask.Shift)

    def is_control_down(self, ):
        r"""SUMMARY

        is_control_down()

        @Return:

        @Error:
        """
        return bool(self._event.state & Modifier.Mask.Control)

    def is_super_down(self, ):
        r"""SUMMARY

        is_super_down()

        @Return:

        @Error:
        """
        return bool(self._event.state & Modifier.Mask.Super)

    def is_alt_down(self, ):
        r"""SUMMARY

        is_alt_down()

        @Return:

        @Error:
        """
        return bool(self._event.state & Modifier.Mask.Alt)

    def is_hiper_down(self, ):
        r"""SUMMARY

        is_hiper_down()

        @Return:

        @Error:
        """
        return bool(self._event.state & Modifier.Mask.Hiper)

    def is_button_left_down(self, ):
        r"""SUMMARY

        is_button_left_down()

        @Return:

        @Error:
        """
        return bool(self._event.state & Modifier.Mask.Left)

    def is_button_middle_down(self, ):
        r"""SUMMARY

        is_button_middle_down()

        @Return:

        @Error:
        """
        return bool(self._event.state & Modifier.Mask.Middle)

    def is_button_right_down(self, ):
        r"""SUMMARY

        is_button_right_down()

        @Return:

        @Error:
        """
        return bool(self._event.state & Modifier.Mask.Right)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# event.py ends here
