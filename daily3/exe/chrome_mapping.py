#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""chrome_mapping -- DESCRIPTION

"""
import sys
from xcb.xproto import BadWindow

from xahk.listener.window_manager_observer import WindowManagerListenerObserver
from xahk.listener.window_manager import WindowManagerListener
from xahk.listener.client_observer import WindowClientListenerObserver
from xahk.wm.window_manager import WindowManager
from xahk.x11.display import Display
from xahk.events import EventLoop
from daily3.exe.specs import GOOGLE_CHROME_SPEC


class WindowInfo(object):
    r"""WindowInfo

    WindowInfo is a object.
    Responsibility:
    """
    def __init__(self, spec, param):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self.spec = spec
        self.param = param


class ChromeMapping(WindowManagerListenerObserver, WindowClientListenerObserver):
    r"""ChromeMapping

    ChromeMapping is a WindowManagerListenerObserver, WindowClientListenerObserver.
    Responsibility:
    """
    def __init__(self, info_list, layout, screen):
        r"""

        @Arguments:
        - `info_list`:
        - `layout`:
        """
        self.display = Display()
        self._layout = layout
        self._screen = screen
        self._infos = {}
        for info in info_list:
            self._infos[info] = None # bool for window mapped
        self.loop = EventLoop.get_instance(self.display)

    def start_mapping(self, ):
        """SUMMARY

        start_mapping()

        @Return:

        @Error:
        """
        wm = WindowManagerListener()
        wm.add_observer(self)
        for win in wm.client_list():
            self.on_created_window_client(win)
            self.on_window_title_changed(win)

        if self.is_all_mapped():
            self.layout()
            return
        self.loop.start_loop()

    def stop_mapping(self, ):
        """SUMMARY

        _notify_mapped()

        @Return:

        @Error:
        """
        wm = WindowManagerListener()
        for win in wm.client_list():
            if win.has_observer(self):
                win.remove_observer(self)

        if wm.has_observer(self):
            wm.remove_observer(self)
        self.loop.stop_loop()

    def layout(self, ):
        """SUMMARY

        _layout()

        @Return:

        @Error:
        """
        for info, win in self._infos.items():
            self._layout.set_layout_item(win, info.param)
        for cookie in self._layout.layout(self._screen):
            cookie.check()

    def is_all_mapped(self, ):
        """SUMMARY

        is_all_mapped()

        @Return:

        @Error:
        """
        for mapped in self._infos.values():
            if mapped is None:
                return False # not all mapped
        return True

    def on_window_title_changed(self, window):
        r"""SUMMARY

        on_window_title_changed(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        for info in self._infos.keys():
            if info.spec.is_satisfied_window(window):
                self._infos[info] = window
                break
        if not self.is_all_mapped():
            return
        self.layout()
        self.stop_mapping()

    def on_created_window_client(self, window):
        """SUMMARY

        on_created_window_client()

        @Return:

        @Error:
        """
        if GOOGLE_CHROME_SPEC.is_satisfied_window(window):
            window.add_observer(self)

    def list_windows(self, ):
        """SUMMARY

        list_windows()

        @Return:

        @Error:
        """
        return self._infos.values()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# chrome_mapping.py ends here
