#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""keyboard_lock -- DESCRIPTION

"""
from xcb.xproto import Time, GrabMode, ModMask, KeyPressEvent

from xahk.events.eventloop import EventLoop
from xahk.events.event_listener import EventListener
from xahk.binder.accelerator import Accelerator


class KeyboardLock(EventListener):
    r"""KeyboardLock

    KeyboardLock is a object.
    Responsibility:
    """
    default_keys = [Accelerator(9), ] # esc

    def __init__(self, display, accelerators=None):
        r"""

        @Arguments:
        - `display`:
        - `accelerators`:
        """
        self._display = display
        self._root = self._display.get_setup().roots[0].root
        self._is_locking = False
        self._stop_keys = set()
        for accelerator in accelerators or self.default_keys:
            self.add_stop_keys(accelerator)
        self.start_locking()

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self._display

    display = property(get_display)

    def add_stop_keys(self, accelerator):
        r"""SUMMARY

        add_stop_keys(accelerator)

        @Arguments:
        - `accelerator`:

        Lock, Mod2==Numlock

        @Return:

        @Error:
        """
        for mod in [0, ModMask.Lock, ModMask._2]:
            self._stop_keys.add(accelerator | mod)

    def can_dispatch_event(self, event):
        r"""SUMMARY

        can_dispatch_event(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        return isinstance(event, (KeyPressEvent))

    def handle_event(self, event):
        r"""SUMMARY

        dispatch_event(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        if Accelerator(event.detail, event.state) in self._stop_keys:
            self.stop_locking()

    def start_locking(self, ):
        r"""SUMMARY

        start_locking()

        @Return:

        @Error:
        """
        if self.is_locking():
            return
        self.display.core.GrabKeyboard(
            False, self._root, Time.CurrentTime, GrabMode.Async, GrabMode.Async)
        self.display.flush()
        EventLoop(self.display).add_event_listener(self)
        self._is_locking = True

    def stop_locking(self, ):
        r"""SUMMARY

        stop_locking()

        @Return:

        @Error:
        """
        if not self.is_locking():
            return
        print('stopping')
        self._display.core.UngrabKeyboard(Time.CurrentTime)
        self._display.flush()
        EventLoop(self.display).remove_event_listener(self)
        self._is_locking = False

    def is_locking(self, ):
        r"""SUMMARY

        is_locking()

        @Return:

        @Error:
        """
        return self._is_locking

    def __del__(self):
        """
        INTERNAL COMMENT
        Do not imprement `raise'!!
        """
        self.stop_locking()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# keyboard_lock.py ends here
