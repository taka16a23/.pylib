#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""loop -- DESCRIPTION

"""
from time import sleep
from collections import deque

from .dispatcher import EventDispatcher


class EventLoop(object):
    r"""EventLoop

    EventLoop is a object.
    Responsibility: Catch X Event
    """
    _instance = None

    dispatcher = EventDispatcher()

    def __init__(self, display):
        r"""

        @Arguments:
        - `display`:
        - `dispatcher`:

        @Return:
        """
        self._display = display
        self._event_queue = deque()
        self._continue_stream = False

    @classmethod
    def get_instance(cls, display):
        if cls._instance is None:
            cls._instance = cls(display)
        return cls._instance

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self._display

    display = property(get_display)

    def get_event_dispatcher(self, ):
        r"""SUMMARY

        get_event_dispatcher()

        @Return:

        @Error:
        """
        return self.dispatcher

    def set_event_dispatcher(self, dispatcher):
        r"""SUMMARY

        set_event_dispatcher(dispatcher)

        @Arguments:
        - `dispatcher`:

        @Return:

        @Error:
        """
        self.dispatcher = dispatcher

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
        AttributeError
        """
        while self._event_queue:
            self.dispatcher.dispatch_event(self._event_queue.popleft())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# loop.py ends here
