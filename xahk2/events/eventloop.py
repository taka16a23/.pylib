#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""eventloop -- DESCRIPTION

"""
from time import sleep
from collections import deque

from xahk2.commons.display_multiton import multiton_display
from xahk2.events.event_dispatcher import EventDispatcher


@multiton_display()
class EventLoop(EventDispatcher):
    r"""EventLoop

    EventLoop is a EventDispatcher.
    Responsibility:
    """
    def __init__(self, display):
        r"""

        @Arguments:
        - `display`:
        """
        EventDispatcher.__init__(self)
        self._display = display
        self._event_queue = deque()
        self._continue_stream = False

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self._display

    display = property(get_display)

    def start_loop(self, ):
        r"""SUMMARY

        start_loop()

        @Return:

        @Error:
        """
        self._continue_stream = True
        while self._continue_stream:
            self._load_events()
            self.dispatch_events()

    def stop_loop(self, ):
        r"""SUMMARY

        stop_loop()

        @Return:

        @Error:
        """
        self._continue_stream = False

    def _load_events(self, ):
        r"""SUMMARY

        _load_events()

        @Return:

        @Error:
        """
        while 1:
            event = self._display.poll_for_event()
            if event is None:
                sleep(0.01)
                break
            self._event_queue.append(event)

    def dispatch_events(self, ):
        r"""SUMMARY

        process_event()

        @Return:

        @Error:
        """
        while self._event_queue:
            self.dispatch_event(self._event_queue.popleft())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# eventloop.py ends here
