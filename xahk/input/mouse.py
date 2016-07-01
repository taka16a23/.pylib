#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""mouse -- DESCRIPTION

"""
from enum import IntEnum

from xcb import xtest
from xcb.xproto import ButtonIndex

from xahk.x11.display import Display
from xahk.x11.eventcode import EventCode
from .cursor import Cursor


class Mouse(object):
    r"""Mouse

    Mouse is a object.
    Responsibility:
    """
    class Button(object):
        """Button

        Button is a object.
        Responsibility:
        """
        class Index(IntEnum):
            r"""ButtonIndex

            ButtonIndex is a _IntEnum.
            Responsibility:
            """
            Left = ButtonIndex._1
            Middle = ButtonIndex._2
            Right = ButtonIndex._3
            WheelUp = ButtonIndex._4
            WheelDown = ButtonIndex._5

        def __init__(self, display, code):
            r"""

            @Arguments:
            - `display`:
            - `code`:
            - `label`:
            """
            self.display = display
            self.code = code
            self.root = self.display.get_setup().roots[0].root
            self._xtest = self.display(xtest.key)

        def get_display(self, ):
            r"""SUMMARY

            get_display()

            @Return:

            @Error:
            """
            return self.display

        def get_code(self, ):
            r"""SUMMARY

            get_code()

            @Return:

            @Error:
            """
            return self.code

        def _fake_input_checked(self, type, time, point):
            r"""SUMMARY

            _fake_input_checked(type, time, root_x, root_y)

            @Arguments:
            - `type`:
            - `time`:
            - `root_x`:
            - `root_y`:

            @Return:

            @Error:
            """
            return self._xtest.FakeInputChecked(
                type, self.code, time, self.root, point.x, point.y, 0)

        def press(self, point, time=0):
            r"""SUMMARY

            press(time=0, root_x=0, root_y=0)

            @Arguments:
            - `time`:
            - `root_x`:
            - `root_y`:

            @Return:

            @Error:
            """
            return self._fake_input_checked(
                EventCode.ButtonPress, time, point)

        def release(self, point, time=0):
            r"""SUMMARY

            release(time=0, root_x=0, root_y=0)

            @Arguments:
            - `time`:
            - `root_x`:
            - `root_y`:

            @Return:

            @Error:
            """
            return self._fake_input_checked(
                EventCode.ButtonRelease, time, point)

        # def press_event(self, window, time=0, x=0, y=0):
        #     """SUMMARY

        #     press_event(window, time=0, x=0, y=0)

        #     @Arguments:
        #     - `window`:
        #     - `time`:
        #     - `x`:
        #     - `y`:

        #     @Return:

        #     @Error:
        #     """
        #     event = pack('BBH4I5HBx', EventCode.ButtonPress, self.code, 0,
        #                  time, self.root, window, 0,
        #                  x, y, x, y, self.modifiers,
        #                  self.samescreen)
        #     print((self.x, self.y))
        #     return self.display.core.SendEventChecked(
        #         False, self.window, EventMask.ButtonPress, event)

        # def release_event(self, window, time=0, x=0, y=0):
        #     """SUMMARY

        #     release_event(window, time=0, x=0, y=0)

        #     @Arguments:
        #     - `window`:
        #     - `time`:
        #     - `x`:
        #     - `y`:

        #     @Return:

        #     @Error:
        #     """
        #     event = pack('BBH4I5HBx', EventCode.ButtonRelease, self.code, self.sequence,
        #                  self.time, self.root, self.window, self.child,
        #                  self.rootx, self.rooty, self.x, self.y,
        #                  self.modifiers|self._release_modifier.get(self.code, 0),
        #                  self.samescreen)
        #     return self.display.core.SendEventChecked(
        #         False, self.window, EventMask.ButtonRelease, event)

        def __repr__(self):
            return '{0.__class__.__name__}(code={0.code})'.format(self)

    def __init__(self, ):
        r"""

        @Arguments:
        - `display`:
        """
        self.display = Display()
        self.cursor = Cursor()
        self.left = self.Button(self.display, self.Button.Index.Left)
        self.middle = self.Button(self.display, self.Button.Index.Middle)
        self.right = self.Button(self.display, self.Button.Index.Right)
        self.wheelup = self.Button(self.display, self.Button.Index.WheelUp)
        self.wheeldown = self.Button(self.display, self.Button.Index.WheelDown)

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self.display

    def get_cursor(self, ):
        r"""SUMMARY

        get_cursor()

        @Return:

        @Error:
        """
        return self.cursor

    def get_left_button(self, ):
        r"""SUMMARY

        get_left_button()

        @Return:

        @Error:
        """
        return self.left

    def get_middle_button(self, ):
        r"""SUMMARY

        get_middle_button()

        @Return:

        @Error:
        """
        return self.middle

    def get_right_button(self, ):
        r"""SUMMARY

        get_right_button()

        @Return:

        @Error:
        """
        return self.right

    def get_wheelup_button(self, ):
        r"""SUMMARY

        get_wheelup_button()

        @Return:

        @Error:
        """
        return self.wheelup

    def get_wheeldown_button(self, ):
        r"""SUMMARY

        get_wheeldown_button()

        @Return:

        @Error:
        """
        return self.wheeldown

    def list_bottons(self, ):
        r"""SUMMARY

        list_bottons()

        @Return:

        @Error:
        """
        return [self.left, self.middle, self.right, self.wheelup, self.wheeldown]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# mouse.py ends here
