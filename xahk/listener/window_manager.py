#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""window_manager -- DESCRIPTION

"""
from xcb.xproto import CW, EventMask, PropertyNotifyEvent

from xahk.events import EventListenerSingleton, EventLoop
from xahk.wm.window_manager import WindowManager
from xahk.x11.window import Window
from xahk.utils.observer import Observable
from .client import WindowClientListener


class WindowManagerListener(EventListenerSingleton, Observable, WindowManager):
    """WindowManagerListener

    WindowManagerListener is a EventListener, Observable.
    Responsibility:
    """

    def __init__(self, ):
        """

        @Arguments:
        - `display`:
        """
        Observable.__init__(self)
        WindowManager.__init__(self)
        attrs = self.root.get_attributes().reply().your_event_mask
        reply = self.root.change_attributes_checked(
            CW.EventMask, [EventMask.PropertyChange|attrs])
        reply.check()
        self._windows = []
        self.client_list_stacking() # create
        EventLoop.get_instance(self.display).add_event_listener(self)

    def _create_client(self, wid):
        """SUMMARY

        _create_client(wid)

        @Arguments:
        - `wid`:

        @Return:

        @Error:
        """
        if wid not in self._windows:
            client = WindowClientListener(Window(self.display, wid))
            self._windows.append(client)
            self._notify_created_window_client(client)
        return self._windows[self._windows.index(wid)]

    def client_list(self, ):
        """SUMMARY

        client_list()

        @Return:

        @Error:
        """
        return self._windows[:]

    def client_list_stacking(self, ):
        """SUMMARY

        client_list_stacking()

        @Return:

        @Error:
        """
        return super(WindowManagerListener, self).client_list_stacking()

    def get_active_window(self, ):
        """SUMMARY

        get_active_window()

        @Return:

        @Error:
        """
        win = super(WindowManagerListener, self).get_active_window()
        if win is None:
            return None
        if win not in self._windows:
            return None
        return self._windows[self._windows.index(win)]

    def can_dispatch_event(self, event):
        """SUMMARY

        can_dispatch_event(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        return isinstance(event, PropertyNotifyEvent) and self.root == event.window

    def handle_event(self, event):
        """SUMMARY

        handle_event(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        if event.atom == self._get_atom('_NET_CLIENT_LIST_STACKING'):
            self._notify_changed_client_list_stacking()
        elif event.atom == self._get_atom('_NET_ACTIVE_WINDOW'):
            self._notify_changed_active_window()
        elif event.atom == self._get_atom('_NET_CURRENT_DESKTOP'):
            self._notify_changed_current_desktop()
        elif event.atom == self._get_atom('_NET_DESKTOP_NAMES'):
            self._notify_changed_desktop_names()
        elif event.atom == self._get_atom('_NET_DESKTOP_VIEWPORT'):
            self._notify_changed_viewport()
        elif event.atom == self._get_atom('_NET_WM_USER_TIME'):
            pass
        elif event.atom == self._get_atom('_NET_NUMBER_OF_DESKTOPS'):
            self._notify_changed_number_of_desktops()
        elif event.atom == self._get_atom('_NET_WORKAREA'):
            self._notify_changed_workarea()

    def _notify_created_window_client(self, window):
        """SUMMARY

        _notify_created_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_created_window_client(window)

    def _notify_destroyed_window_client(self, windowid):
        """SUMMARY

        _notify_destroyed_window(windowid)

        @Arguments:
        - `windowid`:

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_destroyed_window_client(windowid)

    def _notify_changed_client_list(self, ):
        """SUMMARY

        _notify_changed_client_list()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_changed_client_list(self)

    def _notify_changed_client_list_stacking(self, ):
        """SUMMARY

        _notify_changed_client_list_stacking()

        @Return:

        @Error:
        """
        current = set(self._windows)
        news = set(self.client_list_stacking())
        # destroyed
        for listener in list(current - news):
            if listener in self._windows:
                self._windows.remove(listener)
                self._notify_destroyed_window_client(int(listener))
        # observer
        for observer in self._observers:
            observer.on_changed_client_list_stacking(self)

    def _notify_changed_active_window(self, ):
        """SUMMARY

        _notify_changed_active_window()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_changed_active_window(self)

    def _notify_changed_current_desktop(self, ):
        """SUMMARY

        _notify_changed_current_desktop()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_changed_current_desktop(self)

    def _notify_changed_desktop_names(self, ):
        """SUMMARY

        _notify_changed_desktop_names()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_changed_desktop_names(self)

    def _notify_changed_viewport(self, ):
        """SUMMARY

        _notify_changed_viewport()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_changed_viewport(self)

    def _notify_changed_number_of_desktops(self, ):
        """SUMMARY

        _notify_changed_number_of_desktops()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_changed_number_of_desktops(self)

    def _notify_changed_workarea(self, ):
        """SUMMARY

        _notify_changed_workarea()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_changed_workarea(self)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# window_manager.py ends here
