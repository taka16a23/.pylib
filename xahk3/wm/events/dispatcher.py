#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""event_dispatcher -- Dispatch event to listeners.

EventDispatcher hold EventListener or
object that has `can_dispatch_event(event)' and `handle_event(event)' methods.

イベント分配時の挙動を変更したい時は EventDispatcher を継承し
新たに作成すること。
"""


class EventDispatcher(object):
    r"""EventDispatcher

    EventDispatcher is a object.
    Responsibility: Dispatch event to acceptable listeners.

    基本的にEventLoop で利用されるべき。
    受け取った Event を受け入れ可能な Listener に分配する。
    """
    def __init__(self, ):
        r"""Initialize listeners list.
        """
        self._listeners = []

    def _list_dispatchable_listeners(self, event):
        r"""return list of dispatchable listeners.

        _list_dispatchable_listeners(event)

        @Arguments:
        - `event`: Event

        @Return: list of listeners

        @Error:
        """
        return [x for x in self._listeners if x.can_dispatch_event(event)]

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
        for listener in self._list_dispatchable_listeners(event):
            listener.handle_event(event)

    def add_event_listener(self, listener):
        r"""Add EventListener.

        add_event_listener(listener)

        @Arguments:
        - `listener`: EventListener

        @Return: None
        """
        self._listeners.append(listener)

    def remove_event_listener(self, listener):
        r"""Remove EventListener.

        remove_event_listener(listener)

        @Arguments:
        - `listener`: EventListener

        @Return: None
        """
        self._listeners.remove(listener)

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

    def __contains__(self, listener):
        return self.has_event_listener(listener)

    def __iter__(self):
        return iter(self._listeners)

    def __len__(self):
        return len(self._listeners)

    def __getslice__(self, i, j):
        return self._listeners[i:j]


class SafeEventDispatcher(EventDispatcher):
    r"""SafeEventDispatcher

    SafeEventDispatcher is a EventDispatcher.
    Responsibility:
    """
    def __init__(self, safemode=True):
        r"""Initialize listeners list.
        """
        EventDispatcher.__init__(self, )
        self._safemode = safemode

    def enable_safemode(self, ):
        r"""SUMMARY

        enable_safemode()

        @Return:

        @Error:
        """
        self._safemode = True

    def disable_safemode(self, ):
        r"""SUMMARY

        disable_safemode()

        @Return:

        @Error:
        """
        self._safemode = False

    def is_safemode(self, ):
        r"""SUMMARY

        is_safemode()

        @Return:

        @Error:
        """
        return self._safemode

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
        for listener in self._list_dispatchable_listeners(event):
            try:
                listener.handle_event(event)
            except AttributeError as err:
                if not self._safemode:
                    raise err
                # TODO: (Atami) [2016/05/08]
                # debug print
                print(err)
                self.remove_event_listener(listener)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# dispatcher.py ends here
