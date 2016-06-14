#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""cursor -- DESCRIPTION

"""
import xcb
from xcb.xproto import EnterNotifyEvent, NotifyDetail, NotifyMode, EventMask, CW
from xcb.xproto import BadWindow

from dotavoider import ListDotAvoider
from peak.rules import dispatch
from observer import Observable
from rectangle import Point

from xahk3.wm.window_manager import WindowManager
from xahk3.wm.window_manager_observer import WindowManagerObserver
from xahk3.wm.desktop_window_observer import DesktopWindowObserver
from xahk3.wm.events.listener import EventListener
from xahk3.wm.events.loop import EventLoop


class Cursor(WindowManagerObserver, DesktopWindowObserver, EventListener, Observable):
    r"""Cursor

    Cursor is a object.
    Responsibility:
    """
    def __init__(self, display):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        Observable.__init__(self)
        self._wm = WindowManager.get_instance(display)
        self._under_window = None
        cookies, append = ListDotAvoider().append
        for window in self._wm.client_list():
            append(self._add_attributes(window))
        for cookie in cookies:
            cookie.check()
        self._wm.add_observer(self)
        EventLoop.get_instance(display).dispatcher.add_event_listener(self)
        self._update_under_window()

    @property
    def root(self, ):
        r"""SUMMARY

        root()

        @Return:

        @Error:
        """
        return self._wm.root

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self.root.get_display()

    display = property(get_display)

    def _add_attributes(self, window):
        r"""SUMMARY

        _add_attributes(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        attrs = window.window.get_attributes().reply()
        return window.window.change_attributes_checked(
            CW.EventMask, [EventMask.EnterWindow|attrs.your_event_mask])

    def can_dispatch_event(self, event):
        r"""SUMMARY

        can_dispatch_event(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        if not isinstance(event, (EnterNotifyEvent, )):
            return False
        if event.detail == NotifyDetail.Inferior:
            return False
        if event.mode == NotifyMode.Grab:
            return False
        return True

    def handle_event(self, event):
        r"""SUMMARY

        handle_event(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        self._update_under_window()

    def _update_under_window(self, ):
        r"""SUMMARY

        _update_under_window()

        @Return:

        @Error:
        """
        child = self.root.query_pointer().reply().child
        try:
            children = self.display.core.QueryTree(child).reply().children
        except BadWindow as err:
            # TODO: (Atami) [2016/05/13]
            print('DEBUG-1-cursor.py')
            return None
        for window in self._wm.client_list():
            if window in children:
                if self._under_window != window:
                    self._under_window = window
                    self._notify_changed_under_window()

    def is_under_window(self, window):
        r"""SUMMARY

        is_under_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        return self._under_window == window

    def on_created_window(self, window):
        r"""SUMMARY

        on_created_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        try:
            self._add_attributes(window).reply()
        except xcb.Exception as err:
            print(err)
            print(type(err))
        self._update_under_window()

    def on_destroyed_window(self, window_id):
        r"""SUMMARY

        on_destroyed_window()

        @Return:

        @Error:
        """
        self._update_under_window()

    def on_window_minimized(self, window):
        r"""SUMMARY

        on_window_minimized(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        self._update_under_window()

    def get_under_window(self, ):
        r"""SUMMARY

        get_under_window()

        @Return:

        @Error:
        """
        return self._under_window

    def get_point(self, ):
        r"""SUMMARY

        get_point()

        @Return:

        @Error:
        """
        rep = self.root.query_pointer().reply()
        return Point(rep.win_x, rep.win_y)

    @dispatch.generic()
    def move_cursor_to(self, *args):
        r"""SUMMARY

        move_cursor_to(*args)

        @Arguments:
        - `newx`:
        - `newy`:

        @Return:

        @Error:
        """

    @move_cursor_to.when('2 == len(args) and isinstance(args[0], int)')
    def move_cursor_to_int(self, *args):
        r"""SUMMARY

        move_cursor_to()

        @Return:

        @Error:
        """
        return self.root.warp_pointer_checked(
            0, 0, 0, 0, 0, args[0], args[1])

    @move_cursor_to.when('1 == len(args) and isinstance(args[0], Point)')
    def move_cursor_to_point(self, *args):
        r"""SUMMARY

        move_cursor_to_point()

        @Return:

        @Error:
        """
        return self.root.warp_pointer_checked(
            0, 0, 0, 0, 0, args[0].x, args[0].y)

    def _notify_changed_under_window(self, ):
        r"""SUMMARY

        _notify_changed_under_window()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_changed_under_window(self)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# cursor.py ends here
