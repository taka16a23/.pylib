#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""keyboard_lock -- DESCRIPTION

"""
from xcb.xproto import Time, GrabMode, KeyPressEvent

from xahk.events.loop import EventLoop
from xahk.events.listener import EventListener
from xahk.x11.display import Display
from xahk.x11.modifier import Modifier
from xahk.bind.accelerator import Accelerator


class KeyboardLocker(EventListener):
    r"""KeyboardLocker

    KeyboardLocker is a EventListener.
    Responsibility:
    """
    def __init__(self, stopkeys):
        r"""
        """
        self.display = Display()
        self._stopkeys = set()
        for key in stopkeys:
            self.add_stop_key(key)

    def add_stop_key(self, accelerator):
        r"""SUMMARY

        add_stop_key(accelerator)

        @Arguments:
        - `accelerator`:

        @Return:

        @Error:
        """
        for mod in (0, Modifier.Mask.Lock, Modifier.Mask.Numlock):
            self._stopkeys.add(accelerator|mod)

    def can_dispatch_event(self, event):
        r"""SUMMARY

        can_dispatch_event(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        return isinstance(event, (KeyPressEvent, ))

    def handle_event(self, event):
        r"""SUMMARY

        handle_event(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        if Accelerator(event.detail, event.state) in self._stopkeys:
            self.stop_locking()

    def is_locking(self, ):
        r"""SUMMARY

        is_locking()

        @Return:

        @Error:
        """
        return EventLoop.get_instance(self.display).has_event_listener(self)

    def start_locking(self, ):
        r"""SUMMARY

        start_locking()

        @Return:

        @Error:
        """
        if self.is_locking():
            return True
        root = self.display.get_setup().roots[0].root
        self.display.core.GrabKeyboard(
            False, root, Time.CurrentTime, GrabMode.Async, GrabMode.Async)
        self.display.flush()
        EventLoop.get_instance(self.display).add_event_listener(self)

    def stop_locking(self, ):
        r"""SUMMARY

        stop_locking()

        @Return:

        @Error:
        """
        if not self.is_locking():
            return
        self.display.core.UngrabKeyboard(Time.CurrentTime)
        self.display.flush()
        EventLoop.get_instance(self.display).remove_event_listener(self)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# keyboard_lock.py ends here
