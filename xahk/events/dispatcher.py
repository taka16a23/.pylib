#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""event_dispatcher -- Dispatch event to listeners.

EventDispatcher hold EventListener or
object that has `can_dispatch_event(event)' and `handle_event(event)' methods.

イベント分配時の挙動を変更したい時は EventDispatcher を継承し
新たに作成すること。
"""
from xahk.utils.observer import Observable


class EventDispatcher(Observable):
    r"""EventDispatcher

    EventDispatcher is a object.
    Responsibility: Dispatch event to acceptable listeners.

    基本的にEventLoop で利用されるべき。
    受け取った Event を受け入れ可能な Listener に分配する。
    `can_dispatch_event(event)' and `handle_event(event)' methods
    """
    def __init__(self, listeners=None):
        r"""Initialize listeners list.
        """
        Observable.__init__(self)
        self._listeners = list(listeners or [])

    def dispatch_event(self, event):
        r"""Dispatch event to listeners.

        listener objects require
        `can_dispatch_event(event)' and `handle_event(event)' methods

        dispatch_event(event)

        @Arguments:
        - `event`: Event

        @Return: None

        @Error: AttributeError
        """
        for listener in self._listeners:
            if listener.can_dispatch_event(event):
                listener.handle_event(event)

    def add_event_listener(self, listener):
        r"""Add EventListener.

        add_event_listener(listener)

        @Arguments:
        - `listener`: EventListener

        @Return: None
        """
        self._listeners.append(listener)
        self._notify_changed_listeners()

    def remove_event_listener(self, listener):
        r"""Remove EventListener.

        remove_event_listener(listener)

        @Arguments:
        - `listener`: EventListener

        @Return: None
        """
        self._listeners.remove(listener)
        self._notify_changed_listeners()

    def has_event_listener(self, listener):
        r"""Check contain listener.

        has_event_listener(listener)

        @Arguments:
        - `listener`: EventListener

        @Return: bool
        """
        return listener in self._listeners

    def clear_event_listeners(self, ):
        r"""Clear holding listeners list.

        clear_event_listeners()

        @Return: None
        """
        self._listeners[:] = []

    def list_event_listeners(self, ):
        """SUMMARY

        list_event_listeners()

        @Return:

        @Error:
        """
        return self._listeners[:]

    def _notify_changed_listeners(self, ):
        """SUMMARY

        _notify_changed_listeners()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_changed_listeners(self)

    def __contains__(self, listener):
        return self.has_event_listener(listener)

    def __iter__(self):
        return iter(self._listeners)

    def __len__(self):
        return len(self._listeners)

    def __getslice__(self, i, j):
        return self._listeners[i:j]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# dispatcher.py ends here
