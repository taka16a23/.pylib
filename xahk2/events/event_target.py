#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""event_target -- DESCRIPTION

"""
from xahk2.events.event_handler import EventHandler


class EventTarget(EventHandler):
    """Class EventTarget
    """
    # Attributes:
    def __init__(self, ):
        r"""
        """
        self._target_handlers = None
        self._pretarget_handlers = []
        self._posttarget_handlers = []

    # Operations
    def can_accept_event(self, event):
        """function can_accept_event

        event:

        returns bool
        """

    def set_target_handler(self, handler):
        """function set_target_handler

        handler:

        returns
        """
        self._target_handlers = handler

    def add_pretarget_handler(self, handler):
        """function add_pretarget_handler

        handler:

        returns
        """
        self._pretarget_handlers.append(handler)

    def prepend_pretarget_handler(self, handler):
        """function prepend_pretarget_handler

        handler:

        returns
        """
        self._pretarget_handlers.insert(0, handler)

    def remove_pretarget_handler(self, handler):
        """function remove_pretarget_handler

        handler:

        returns
        """
        self._pretarget_handlers.remove(handler)

    def add_posttarget_handler(self, handler):
        """function add_posttarget_handler

        handler:

        returns
        """
        self._posttarget_handlers.append(handler)

    def prepend_posttarget_handler(self, handler):
        """function prepend_posttarget_handler

        handler:

        returns
        """
        self._posttarget_handlers.insert(0, handler)

    def remove_posttarget_handler(self, handler):
        """function remove_posttarget_handler

        handler:

        returns
        """
        self._posttarget_handlers.remove(handler)

    def on_event(self, event):
        r"""SUMMARY

        on_event(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        if self._target_handlers is not None:
            self._target_handlers.on_event(event)
        else:
            super(EventTarget, self).on_event(event)

    def on_key_event(self, event):
        """function on_key_event

        event:

        returns
        """
        if self._target_handlers is None:
            return
        self._target_handlers.on_key_event(event)

    def on_mouse_event(self, event):
        """function on_mouse_event

        event:

        returns
        """
        if self._target_handlers is None:
            return
        self._target_handlers.on_mouse_event(event)

    def get_pretarget_handlers(self, ):
        r"""SUMMARY

        get_pretarget_handlers()

        @Return:

        @Error:
        """
        return self._pretarget_handlers

    def get_posttarget_handlers(self, ):
        r"""SUMMARY

        get_posttarget_handlers()

        @Return:

        @Error:
        """
        return self._posttarget_handlers



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# event_target.py ends here
