#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""sleipnir_launcher -- DESCRIPTION

"""
import sys
import os
from time import sleep
import subprocess as sbp
from xcb.xproto import BadWindow

from xahk.wm.window_spec import WindowSpec, WindowWMClassSpec
from xahk.x11.display import Display
from xahk.rectangle import Point
from xahk.listener.window_manager_observer import WindowManagerListenerObserver
from xahk.listener.window_manager import WindowManagerListener
from xahk.events.loop import EventLoop
from xahk.sendkeys.input_event import ButtonEvent, Mouse


BINARY_PATH = '/opt/portable-sleipnir-299/PortableSleipnir/PortableSleipnir.exe'

A = 'wine start /unix /opt/portable-sleipnir-299/PortableSleipnir/PortableSleipnir.exe > /dev/null 2>&1 &'

BIN = 'Sleipnir.exe'

FEEDBACK_SPEC = WindowWMClassSpec('FeedbackAgent.exe')
SLEIPNIR_WMCLASS_SPEC = WindowWMClassSpec('Sleipnir.exe')


class SleipnirDialogSpec(WindowSpec):
    r"""SleipnirDialogSpec

    SleipnirDialogSpec is a WindowSpec.
    Responsibility:
    """
    _wmclass_spec = SLEIPNIR_WMCLASS_SPEC

    def is_satisfied_window(self, window):
        """SUMMARY

        name()

        @Return:

        @Error:
        """
        # check sleipnir window
        if not self._wmclass_spec.is_satisfied_window(window):
            return False
        if '_NET_WM_WINDOW_TYPE_DIALOG' == window.type:
            return True
        return False


class SleipnirMainSpec(WindowSpec):
    r"""SleipnirMainSpec

    SleipnirMainSpec is a WindowSpec.
    Responsibility:
    """
    _spec = SLEIPNIR_WMCLASS_SPEC

    def is_satisfied_window(self, window):
        """SUMMARY

        is_satisfied_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        if not self._spec.is_satisfied_window(window):
            return False
        if '_NET_WM_WINDOW_TYPE_NORMAL' == window.type:
            return True
        return False


class SleipnirWindowCloser(WindowManagerListenerObserver):
    r"""SleipnirDialogHandler

    SleipnirDialogHandler is a WindowManagerListenerObserver.
    Responsibility:
    """
    def __init__(self, spec):
        r"""
        """
        self._spec = spec
        self._wm = WindowManagerListener()
        self._wm.add_observer(self)
        self._window = None

    def on_created_window_client(self, window):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        if not self._spec.is_satisfied_window(window):
            return
        self._window = window
        try:
            self._window.close().check()
        except BadWindow as err:
            print(err)

    def on_destroyed_window_client(self, windowid):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        if self._window != windowid:
            return
        if self._wm.has_observer(self):
            self._wm.remove_observer(self)


class SleipnirManager(WindowManagerListenerObserver):
    r"""SleipnirManager

    SleipnirManager is a object.
    Responsibility:
    """
    point = Point(1380, 0)

    def __init__(self, ):
        r"""

        @Arguments:
        - `managers`:
        """
        self.display = Display()
        self._window = None
        self._spec = SleipnirMainSpec()
        self._wm = WindowManagerListener()
        self.screens = self._wm.list_screens()
        self._context = {'child': 0,
                         'display': self.display,
                         'root': self.display.get_setup().roots[0].root,
                         'rootx': 75,
                         'rooty': 130,
                         'samescreen': 1,
                         'sequence': 0,
                         'time': 0,}
        self._left_button = ButtonEvent(
            self._context, Mouse.Button.Index.Left, 0, Point(75, 130))
        self._pressed = False

    def _get_window(self, ):
        """SUMMARY

        _get_window()

        @Return:

        @Error:
        """
        for window in self._wm.client_list():
            if self._spec.is_satisfied_window(window):
                return window
        return None

    def start(self, ):
        """SUMMARY

        start()

        @Return:

        @Error:
        """
        display = Display()
        SleipnirWindowCloser(SleipnirDialogSpec())
        SleipnirWindowCloser(FEEDBACK_SPEC)
        window = self._get_window()
        if window: # already exists
            self.on_created_window_client(window) # initialize
        if window is None:
            devnull = open(os.devnull, 'wb')
            sbp.Popen(('wine', 'start', '/unix', BINARY_PATH), stdout=devnull)
        self._wm.add_observer(self)
        EventLoop.get_instance(display).start_loop()

    def _move_window(self, ):
        """SUMMARY

        _move_window()

        @Return:

        @Error:
        """
        if self._window.is_maximized():
            self._window.unset_maximized()
            self.display.flush()
        self._window.move(self.point)
        self.display.flush()
        sleep(1)
        self._window.set_bounds(self.screens[0])
        # window.maximize()
        self.display.flush()

    def on_changed_active_window(self, wm):
        """SUMMARY

        on_changed_active_window(wm)

        @Arguments:
        - `wm`:

        @Return:

        @Error:
        """
        if self._pressed:
            return
        if wm.get_active_window() == self._window:
            self._pressed = True
            sleep(3)
            self._context['window'] = self._window
            self._left_button.press()
            self._left_button.release()
            self.display.flush()

    def on_created_window_client(self, window):
        """SUMMARY

        on_created_window_client(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        if not self._spec.is_satisfied_window(window):
            return
        if self._window is None:
            self._window = window
            self._move_window()

    def on_destroyed_window_client(self, windowid):
        """SUMMARY

        on_destroyed_window_client(windowid)

        @Arguments:
        - `windowid`:

        @Return:

        @Error:
        """
        if self._window != windowid:
            return
        self._wm.remove_observer(self)
        display = Display()
        EventLoop.get_instance(display).stop_loop()
        display.flush()


def _main():
    SleipnirManager().start()
    return 0

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sleipnir_launcher.py ends here
