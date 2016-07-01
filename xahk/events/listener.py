#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""event_listener -- DESCRIPTION

EventListener はイベントを受け取るか判断し、イベントを処理する。

"""
from abc import ABCMeta, abstractmethod


class SingletonABCMeta(ABCMeta):
    """Abstract class EventListener"""
    # Operations
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingletonABCMeta, cls).__call__(*args, **kwargs)
        return cls._instance


class EventListener(object):
    """Abstract class EventListener"""
    # Attributes:
    __metaclass__ = ABCMeta

    # Operations
    @abstractmethod
    def can_dispatch_event(self, event):
        """abstract method can_dispatch_event

        determine dispatchable event.

        event: X event

        returns bool
        """
        raise NotImplementedError()

    @abstractmethod
    def handle_event(self, event):
        """abstract method handle_event

        event: X event
        """
        raise NotImplementedError()


class EventListenerSingleton(object):
    r"""EventListenerSingleton

    EventListenerSingleton is a object.
    Responsibility:
    """
    __metaclass__ = SingletonABCMeta

    @abstractmethod
    def can_dispatch_event(self, event):
        """abstract method can_dispatch_event

        determine dispatchable event.

        event: X event

        returns bool
        """
        raise NotImplementedError()

    @abstractmethod
    def handle_event(self, event):
        """abstract method handle_event

        event: X event
        """
        raise NotImplementedError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# event_listener.py ends here
