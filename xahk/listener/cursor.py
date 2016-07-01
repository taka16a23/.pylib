#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""cursor -- DESCRIPTION

"""
from xcb.xproto import CW, EventMask
from xcb.xproto import EnterNotifyEvent, NotifyDetail, NotifyMode
from xcb.xproto import BadWindow, WindowError

from xahk.utils.observer import Observable
from xahk.utils.dotavoider import ListDotAvoider
from xahk.events import EventListenerSingleton, EventLoop
from xahk.input.cursor import Cursor
from xahk.log import logging

from .window_manager_observer import WindowManagerListenerObserver
from .window_manager import WindowManagerListener

from .client_observer import WindowClientListenerObserver


def add_attributes(window):
    r"""SUMMARY

    add_attributes(window)

    @Arguments:
    - `window`:

    @Return:

    @Error:
    """
    try:
        attrs = window.get_attributes().reply().your_event_mask
    except (BadWindow, WindowError) as err:
        logging.getLogger('xahk').error(
            '{0} {1}'.format(err.__class__.__name__, err))
        return None
    return window.change_attributes_checked(
        CW.EventMask, [EventMask.EnterWindow|attrs])


class CursorListener(EventListenerSingleton, Observable, Cursor,
                     WindowManagerListenerObserver, WindowClientListenerObserver):
    r"""CursorListener

    CursorListener is a EventListener, Observable.
    Responsibility:
    """
    def __init__(self, ):
        r"""

        @Arguments:
        - `display`:
        """
        Cursor.__init__(self, )
        Observable.__init__(self)
        self._under_window = None
        self._wm = WindowManagerListener()
        self._wm.add_observer(self)
        cookies, append = ListDotAvoider().append
        for window in self._wm.client_list():
            cookie = add_attributes(window.window)
            if cookie is None:
                continue
            append(cookie)
            window.add_observer(self)
        for cookie in cookies:
            try:
                cookie.check()
            except BadWindow as err:
                logging.getLogger('xahk').error(
                    '{0} {1}'.format(err.__class__.__name__, err))
        EventLoop.get_instance(self.display).add_event_listener(self)
        self._update_under_window()

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

    def get_under_window(self, ):
        r"""SUMMARY

        get_under_window()

        @Return:

        @Error:
        """
        return self._under_window

    def _update_under_window(self, ):
        r"""SUMMARY

        _update_under_window()

        @Return:

        @Error:
        """
        window = super(CursorListener, self).get_under_window()
        if window is None:
            return
        for win in self._wm.client_list():
            if window == win and self._under_window != win:
                self._under_window = win
                self._notify_changed_under_window()

    def _notify_changed_under_window(self, ):
        r"""SUMMARY

        _notify_changed_under_window()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_changed_under_window(self)

    def on_created_window_client(self, window):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        cookie = add_attributes(window.get_window())
        if cookie is not None:
            try:
                cookie.check()
            except BadWindow as err:
                logging.getLogger('xahk').error(
                    '{0} {1}'.format(err.__class__.__name__, err))
        window.add_observer(self)
        self._update_under_window()

    def on_destroyed_window_client(self, windowid):
        r"""SUMMARY

        name()

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



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# cursor.py ends here
