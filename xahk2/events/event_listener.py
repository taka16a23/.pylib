#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""event_listener -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod


class EventListener(object):
    """Abstract class EventListener
    """
    # Attributes:
    __metaclass__ = ABCMeta

    # Operations
    @abstractmethod
    def can_accept_event(self, event):
        """function can_accept_event

        event:

        returns bool
        """
        raise NotImplementedError()

    @abstractmethod
    def handle_event(self, event):
        """function handle_event

        event:

        returns
        """
        raise NotImplementedError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# event_listener.py ends here
