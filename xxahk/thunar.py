#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""thunar -- DESCRIPTION

"""
from xahk.bind.mouse import MouseBinder, MIDDLE_ACCELERATOR
from xahk.bind.key import KeyBinder, KeyEventHandler
from xahk.bind.accelerator import Accelerator
from xahk.x11.modifier import Modifier
from xahk.listener.window_manager import WindowManagerListener
from lab.thunar.manager import ThunarManager
from lab.thunar.commons import THUNAR_WMSPEC
from xahk.rectangle import Rectangle
from .sendkey_handler import SendKeysHandler


class ThunarDefaltMapping(KeyEventHandler):
    r"""ThunarDefaltMapping

    ThunarDefaltMapping is a KeyEventHandler.
    Responsibility:
    """
    default = Rectangle.Builder(1640, 179, 877, 674).build()

    def __init__(self, ):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self._wm = WindowManagerListener()

    def on_key_release(self, event):
        """SUMMARY

        on_key_release(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        active = self._wm.get_active_window()
        active.set_bounds(self.default).check()


class ThunarHorizontalMapping(KeyEventHandler):
    r"""ThunarMapping

    ThunarMapping is a KeyEventHandler.
    Responsibility:
    """
    def __init__(self, ):
        r"""
        """
        self._wm = WindowManagerListener()
        self.thunar = ThunarManager()

    def on_key_release(self, event):
        """SUMMARY

        name()

        @Return:

        @Error:
        """
        for cookie in self.thunar.horizontal_layout(self._wm.list_screens()[0]):
            cookie.check()


class ThunarVerticalMapping(KeyEventHandler):
    r"""ThunarMapping

    ThunarMapping is a KeyEventHandler.
    Responsibility:
    """
    def __init__(self, ):
        r"""
        """
        self._wm = WindowManagerListener()
        self.thunar = ThunarManager()

    def on_key_release(self, event):
        """SUMMARY

        name()

        @Return:

        @Error:
        """
        for cookie in self.thunar.vertical_layout(self._wm.list_screens()[0]):
            cookie.check()


THUNAR_KEY_BINDER = KeyBinder(THUNAR_WMSPEC)
THUNAR_KEY_BINDER.bind(Accelerator.from_key_label('l', Modifier.Mask.Super), ThunarHorizontalMapping())
THUNAR_KEY_BINDER.bind(Accelerator.from_key_label('k', Modifier.Mask.Super), ThunarVerticalMapping())
THUNAR_KEY_BINDER.bind(Accelerator.from_key_label('d', Modifier.Mask.Super), ThunarDefaltMapping())
THUNAR_MOUSE_BINDER = MouseBinder(THUNAR_WMSPEC)
THUNAR_MOUSE_BINDER.bind(MIDDLE_ACCELERATOR, SendKeysHandler('^w'))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# thunar.py ends here
