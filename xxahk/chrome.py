#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""chrome -- DESCRIPTION

"""
from time import sleep


from xahk.bind.mouse import (MouseEventHandler, MouseBinder,
                              MIDDLE_ACCELERATOR, LEFT_ACCELERATOR, RIGHT_ACCELERATOR,
                              WHEELUP_ACCELERATOR, WHEELDOWN_ACCELERATOR)
from xahk.bind.key import KeyEventHandler, KeyBinder
from xahk.wm.window_spec import WindowWMClassSpec
from xahk.bind.accelerator import Accelerator
from xahk.sendkeys.sendkeys import SendKeys
from xahk.listener.window_manager import WindowManagerListener
from .sendkey_handler import SendKeysHandler
from xahk.x11.modifier import Modifier
from xahk.listener.cursor import CursorListener
from xahk.input.mouse import Mouse
from xahk.rectangle import Size, Point


GOOGLE_CHROME_SPEC = WindowWMClassSpec('google-chrome')


class ChromeCloseTab(MouseEventHandler):
    r"""ChromeCloseTab

    ChromeCloseTab is a MouseEventHandler.
    Responsibility:
    """
    def __init__(self, ):
        r"""
        """
        self._closetab = SendKeys('^w')
        self._feedly_read = SendKeys('+a')
        self._middle = SendKeys('{mbutton}')
        self._wm = WindowManagerListener()
        self._cursor = CursorListener()
        self._pressed_time = 0
        self._mbutton = Mouse().get_middle_button()
        self._pressed = False

    @property
    def display(self, ):
        r"""SUMMARY

        display()

        @Return:

        @Error:
        """
        return self._wm.get_display()

    def on_button_press(self, event):
        r"""SUMMARY

        on_button_press(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        self._pressed_time = event.time
        self._pressed = True

    # def _normal(self, event):
    #     r"""SUMMARY

    #     _normal(event)

    #     @Arguments:
    #     - `event`:

    #     @Return:

    #     @Error:
    #     """
        # lastwin = self._cursor.get_under_window()
        # rep = self.display.core.TranslateCoordinates(
            # lastwin, event.window, event.x, event.y).reply()
        # lastx = -(rep.dst_x - (2 * event.get_x()))
        # lasty = -(rep.dst_y - (2 * event.get_y()))
        # lastx, lasty = event.x, event.y
        # print((lastx, lasty))
        # ev = pack('BBH4I5HBx', EventCode.ButtonPress, event.code,
                  # 0, event.time, event.root, event.root, event.child,
                  # lastx, lasty, lastx, lasty,
                  # event.modifiers, 1)
        # self.display.core.SendEventChecked(
            # False, event.root, EventMask.ButtonPress, ev).check()
        # ev = pack('BBH4I5HBx', EventCode.ButtonRelease, event.code,
                  # 0, event.time, event.root, event.root, event.child,
                  # lastx, lasty, lastx, lasty,
                  # event.modifiers, 1)
        # self.display.core.SendEventChecked(
            # False, event.root, EventMask.ButtonRelease, ev).check()
        # self._middle.send(event.root)
        # self._mbutton.press(root_x=event.x, root_y=event.y).check()
        # self._mbutton.release(root_x=event.x, root_y=event.y).check()

    def on_button_release(self, event):
        r"""SUMMARY

        on_button_release(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        # print(event.time - self._pressed_time)
        # if 200 <= event.time - self._pressed_time:
            # self._normal(event)
            # return
        if not self._pressed:
            return
        if 'all - Google Chrome' == self._wm.get_active_window().title:
            self._feedly_read.send()
            sleep(1)
        self._closetab.send()
        self._pressed = False


class ChromeResize(KeyEventHandler):
    r"""ChromeResize

    ChromeResize is a KeyEventHandler.
    Responsibility:
    """
    def on_key_press(self, event):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        event.window.set_size(Size(1130, 940)).check()


# class ResendButtonEvent(MouseEventHandler):
#     r"""ReSendButtonEvent

#     ReSendButtonEvent is a MouseEventHandler.
#     Responsibility:
#     """
#     def __init__(self, ):
#         r"""
#         """
#         self.display = Display()
#         self._cursor = CursorListener.get_instance()
#         self._lastwin = 0
#         self._lastx = 0
#         self._lasty = 0

#     def on_button_press(self, event):
#         r"""SUMMARY

#         on_mouse_press(event)

#         @Arguments:
#         - `event`:

#         @Return:

#         @Error:
#         """
#         self._lastwin = self._cursor.get_under_window()
#         rep = self.display.core.TranslateCoordinates(
#             self._lastwin, event.window, event.x, event.y).reply()
#         self._lastx = -(rep.dst_x - (2 * event.get_x()))
#         self._lasty = -(rep.dst_y - (2 * event.get_y()))
#         ev = pack('BBH4I5HBx', EventCode.ButtonPress, event.code,
#                   0, event.time, event.root, self._lastwin, event.child,
#                   self._lastx, self._lasty, self._lastx, self._lasty,
#                   event.modifiers, 1)
#         self.display.core.SendEventChecked(
#             False, self._lastwin, EventMask.ButtonPress, ev).check()

#     def on_button_release(self, event):
#         r"""SUMMARY

#         on_button_release(event)

#         @Arguments:
#         - `event`:

#         @Return:

#         @Error:
#         """
#         ev = pack('BBH4I5HBx', EventCode.ButtonRelease, event.code,
#                   0, event.time, event.root, self._lastwin, event.child,
#                   self._lastx, self._lasty, self._lastx, self._lasty,
#                   event.modifiers, 1)
#         self.display.core.SendEventChecked(
#             False, self._lastwin, EventMask.ButtonRelease, ev).check()

class ChromeMoveLeftDisplay(KeyEventHandler):
    r"""ChromeMoveLeftDisplay

    ChromeMoveLeftDisplay is a KeyEventHandler.
    Responsibility:
    """
    left_point = Point(97, 49)

    def on_key_release(self, event):
        """SUMMARY

        name()

        @Return:

        @Error:
        """
        event.window.move(self.left_point).check()


class ChromeMoveRightDisplay(KeyEventHandler):
    r"""ChromeMoveRightDisplay

    ChromeMoveRightDisplay is a KeyEventHandler.
    Responsibility:
    """
    right_point = Point(1477, 70)

    def on_key_release(self, event):
        """SUMMARY

        name()

        @Return:

        @Error:
        """
        event.window.move(self.right_point).check()


CHROME_KEY_BINDER = KeyBinder(GOOGLE_CHROME_SPEC)
CHROME_KEY_BINDER.bind(Accelerator.from_key_label('e', Modifier.Mask.Control),
                       SendKeysHandler('^l'))
CHROME_KEY_BINDER.bind(Accelerator.from_key_label('q', Modifier.Mask.Control),
                       SendKeysHandler('^+t'))
CHROME_KEY_BINDER.bind(Accelerator.from_key_label('s', Modifier.Mask.Super),
                       ChromeResize())
CHROME_KEY_BINDER.bind(Accelerator.from_key_label('a', Modifier.Mask.Super),
                       SendKeysHandler('!{Home}'))
CHROME_KEY_BINDER.bind(Accelerator.from_key_label('j', Modifier.Mask.Super),
                       ChromeMoveLeftDisplay())
CHROME_KEY_BINDER.bind(Accelerator.from_key_label('l', Modifier.Mask.Super),
                       ChromeMoveRightDisplay())

CHROME_MOUSE_BINDER = MouseBinder(GOOGLE_CHROME_SPEC)
CHROME_MOUSE_BINDER.bind(MIDDLE_ACCELERATOR, ChromeCloseTab())
CHROME_MOUSE_BINDER.bind(
    WHEELUP_ACCELERATOR|Modifier.Mask.Right, SendKeysHandler('{Escape}^+{Tab}'))
CHROME_MOUSE_BINDER.bind(
    WHEELDOWN_ACCELERATOR|Modifier.Mask.Right, SendKeysHandler('{Escape}^{Tab}'))
# CHROME_MOUSE_BINDER.bind(RIGHT_ACCELERATOR, ResendButtonEvent())
CHROME_MOUSE_BINDER.bind(RIGHT_ACCELERATOR, None)
CHROME_MOUSE_BINDER.bind(
    LEFT_ACCELERATOR|Modifier.Mask.Right, SendKeysHandler('{Escape}!{Home}'))
CHROME_MOUSE_BINDER.bind(
    MIDDLE_ACCELERATOR|Modifier.Mask.Right, SendKeysHandler('{Escape}^+{Tab}^w'))
# CHROME_MOUSE_BINDER.bind(
    # LEFT_ACCELERATOR, ResendButtonEvent())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# chrome.py ends here
