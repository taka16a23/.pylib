#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""event_listener -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod


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



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# event_listener.py ends here
