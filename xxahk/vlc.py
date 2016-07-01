#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""vlc -- DESCRIPTION

"""
from psutil import Process

from xahk.wm.window_spec import WindowWMClassSpec
from xahk.bind.key import KeyBinder, KeyEventHandler
from xahk.bind.accelerator import Accelerator
from xahk.x11.modifier import Modifier
from .sendkey_handler import SendKeysHandler
from xahk.rectangle import Size
from xahk.bind.mouse import MouseBinder, MIDDLE_ACCELERATOR, MouseEventHandler
from xahk.listener.cursor import CursorListener
from xahk.listener.window_manager_observer import WindowManagerListenerObserver
from xahk.listener.window_manager import WindowManagerListener


VLC_SPEC = WindowWMClassSpec('vlc')


class VLCAutoResize(WindowManagerListenerObserver):
    """VLCAutoResize

    VLCAutoResize is a WindowManagerListenerObserver.
    Responsibility:
    """

    def __init__(self, ):
        wm = WindowManagerListener()
        wm.add_observer(self)

    def on_created_window_client(self, window):
        """SUMMARY

        on_created_window_client(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        if not VLC_SPEC.is_satisfied_window(window):
            return
        size = window.get_bounds().get_size()
        print(size)
        if (size.get_width(), size.get_height()) <= (1280, 1024):
            return
        window.set_size(Size(720, 480)).check()
        print('resized')


class VLCResize(KeyEventHandler):
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
        event.window.set_size(Size(720, 480)).check()


class VLCKill(MouseEventHandler):
    """VLCKill

    VLCKill is a MouseEventHandler.
    Responsibility:
    """
    def __init__(self, ):
        """
        """

        self._cursor = CursorListener()

    def on_button_release(self, event):
        """SUMMARY

        on_button_release(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        window = self._cursor.get_under_window()
        Process(window.pid).kill()


VLC_KEY_BINDER = KeyBinder(VLC_SPEC)
VLC_KEY_BINDER.bind(Accelerator.from_key_label('s', Modifier.Mask.Super),
                    VLCResize())
THUNAR_MOUSE_BINDER = MouseBinder(VLC_SPEC)
THUNAR_MOUSE_BINDER.bind(MIDDLE_ACCELERATOR, VLCKill())

VLCAutoResize()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# vlc.py ends here
