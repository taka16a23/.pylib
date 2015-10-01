#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""mouse_bind_service -- DESCRIPTION

"""
from xahk.listener import CursorListenerObserver
from xahk.listener import CursorListener
from xahk.binder.bind_service import BindService
from xahk.binder.mouse_listener_x11 import MouseListenerX11
from xahk.commons.display_multiton import multiton_display


@multiton_display()
class MouseBindService(CursorListenerObserver, BindService):
    """Class MouseBindService
    """
    # Attributes:
    def __init__(self, display):
        r"""
        """
        BindService.__init__(self)
        self._display = display
        self._listener = MouseListenerX11(display)

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
        self._listener.clear_accelerators()
        self._candidate_proxy.build_listener(
            CursorListener(self.display).get_under_window(), self._listener)

    def start_service(self):
        """function start_service

        returns
        """
        if self.is_serving():
            return
        self._listener.start_listening()
        d = CursorListener(self.display)
        d.add_observer(self)
        self._is_serving = True
        self.update_listener()

    def stop_service(self):
        """function stop_service

        returns
        """
        if not self.is_serving():
            return
        self._listener.clear_accelerators()
        CursorListener(self.display).remove_observer(self)
        self._is_serving = False

    def on_changed_under_window(self, cursor_listener):
        """function on_changed_under_window

        cursor_listener:

        returns
        """
        self.update_listener()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# mouse_bind_service.py ends here
