#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""cursor_listener -- DESCRIPTION

"""
from dotavoider import ListDotAvoider
from observer import Observable

from xcb.xproto import (EnterNotifyEvent, NotifyDetail, NotifyMode, EventMask,
                        BadWindow)

from xahk.commons.display_multiton import multiton_display
from xahk.windowspec import WindowIDSpec
from xahk.events.eventloop import EventLoop
from xahk.events.event_listener import EventListener
from xahk.wm.cursor_handler import CursorHandler
from xahk.listener.window_listener_observer import WindowListenerObserver
from xahk.listener.window_listener_factory import WindowListenerFactory
from xahk.listener.window_listener_factory_observer import WindowListenerFactoryObserver


@multiton_display()
class CursorListener(WindowListenerFactoryObserver, Observable, EventListener,
                     WindowListenerObserver):
    """Class CursorListener
    """
    # Attributes:
    def __init__(self, display):
        r"""

        @Arguments:
        - `display`:
        """
        Observable.__init__(self)
        self._cursor = CursorHandler(display)
        self._under_window = None
        self._window_factory = WindowListenerFactory(display)
        self._window_factory.add_observer(self)
        cookies, append = ListDotAvoider().append
        for window in self._window_factory.list_windows():
            reply = window.add_attributes(EventMask.EnterWindow)
            if not reply is None:
                append(reply)
            window.add_observer(self)
        for cookie in cookies:
            cookie.check()
        EventLoop(display).add_event_listener(self)
        self._update_under_window()

    # Operations
    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self._cursor.get_display()

    display = property(get_display)

    def can_dispatch_event(self, event):
        """function can_dispatch_event

        event:

        returns
        """
        if not isinstance(event, (EnterNotifyEvent, )):
            return False
        if event.detail == NotifyDetail.Inferior:
            return False
        if event.mode == NotifyMode.Grab:
            return False
        return True

    def handle_event(self, event):
        """function handle_event

        event:

        returns
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

    def get_under_window(self):
        """function get_under_window

        returns
        """
        return self._under_window

    def on_created_window_listener(self, window):
        """function on_created_window_listener

        window:

        returns
        """
        window.add_observer(self)
        reply = window.add_attributes(EventMask.EnterWindow)
        if not reply is None:
            try:
                reply.check()
            except BadWindow as err:
                from xahk.logger import LOG
                LOG.error('{}'.format(err))
                import os
                os.system('modprobe pcspkr')
                os.system('/usr/bin/beep -f250 -r2 -l50')
                os.system('rmmod pcspkr')
        self._update_under_window()

    def on_destroyed_window_listener(self, window_id):
        """function on_destroyed_window_listener

        window_id:

        returns
        """
        self._update_under_window()

    def move_cursor_to(self, newx, newy):
        """function move

        point:

        returns
        """
        try:
            self._cursor.move_cursor_to(newx, newy).check()
        except BadWindow as err:
            from xahk.logger import LOG
            import os
            LOG.error('{}'.format(err))
            os.system('modprobe pcspkr')
            os.system('/usr/bin/beep -f250 -r2 -l50')
            os.system('rmmod pcspkr')

    def is_under_window(self, window):
        """function is_under_window

        window:

        returns bool
        """
        return self._under_window == window

    def _update_under_window(self):
        """function update_under_window

        returns
        """
        under_window = self._cursor.get_under_window()
        if under_window is None:
            return
        windows = self._window_factory.list_windows(WindowIDSpec(under_window))
        if not windows or self._under_window == windows[0]:
            return
        self._under_window = windows[0]
        self._notify_changed_under_window()

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
# cursor_listener.py ends here
