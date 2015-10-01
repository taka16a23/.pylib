#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: key_bind_service.py 339 2015-07-23 18:01:26Z t1 $
# $Revision: 339 $
# $Date: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $

r"""key_bind_service -- DESCRIPTION

"""
from observer import Observable
from xahk.binder.bind_service import BindService
from xahk.listener import WindowListenerFactory
from xahk.listener import WindowListenerFactoryObserver
from xahk.binder.key_listener_x11 import KeyListenerX11
from xahk.commons.display_multiton import multiton_display


@multiton_display()
class KeyBindService(Observable, BindService, WindowListenerFactoryObserver):
    """Class KeyBindService
    """
    # Attributes:
    def __init__(self, display):
        r"""
        """
        Observable.__init__(self)
        BindService.__init__(self)
        self._display = display
        self._listeners = []
        WindowListenerFactory(display).add_observer(self)
        for window in WindowListenerFactory(display).list_windows():
            self.on_created_window_listener(window)

    # Operations
    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self._display

    display = property(get_display)

    def update_listener(self):
        """function update_listener

        returns
        """
        self._clear_listeners_accelerators()
        for listener in self._listeners:
            self._candidate_proxy.build_listener(
                listener.get_window(), listener)

    def start_service(self):
        """function start_service

        returns
        """
        if self.is_serving():
            return
        for listener in self._listeners:
            listener.start_listening()
        self._is_serving = True
        self.update_listener()

    def stop_service(self):
        """function stop_service

        returns
        """
        if not self.is_serving():
            return
        self._clear_listeners_accelerators()
        for listener in self._listeners:
            listener.stop_listening()
        self._is_serving = False

    def _clear_listeners_accelerators(self, ):
        r"""SUMMARY

        _clear_listeners_accelerators()

        @Return:

        @Error:
        """
        for listener in self._listeners:
            listener.clear_accelerators()

    def on_created_window_listener(self, window):
        r"""SUMMARY

        on_created_window_listener(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        listener = KeyListenerX11(window)
        if self.is_serving():
            self._candidate_proxy.build_listener(window, listener)
            listener.start_listening()
        self._listeners.append(listener)
        self._notify_created_listener(listener)

    def _notify_created_listener(self, listener):
        r"""SUMMARY

        _notify_created_listener(listener)

        @Arguments:
        - `listener`:

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_created_listener(listener)

    def on_destroyed_window_listener(self, window_id):
        r"""SUMMARY

        on_destroyed_window_listener(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        for listener in self._listeners[:]:
            if listener.get_window() == window_id:
                self._listeners.remove(listener)
                self._notify_destroyed_listener(listener)

    def _notify_destroyed_listener(self, listener):
        r"""SUMMARY

        _notify_destroyed_listener(listener)

        @Arguments:
        - `listener`:

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_destroyed_listener(listener)

    def list_listeners(self, ):
        r"""SUMMARY

        list_listeners()

        @Return:

        @Error:
        """
        return self._listeners



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# key_bind_service.py ends here
