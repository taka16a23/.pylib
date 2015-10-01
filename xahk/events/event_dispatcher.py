#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: event_dispatcher.py 348 2015-08-04 13:56:54Z t1 $
# $Revision: 348 $
# $Date: 2015-08-04 22:56:54 +0900 (Tue, 04 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-04 22:56:54 +0900 (Tue, 04 Aug 2015) $

r"""event_dispatcher -- DESCRIPTION

"""


class EventDispatcher(object):
    r"""EventDispatcher

    EventDispatcher is a object.
    Responsibility:
    """
    def __init__(self, ):
        r"""
        """
        self._listeners = []

    def dispatch_event(self, event):
        r"""SUMMARY

        dispatch_event(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        listeners = [x for x in self._listeners if x.can_dispatch_event(event)]
        for listener in listeners:
            listener.handle_event(event)

    def add_event_listener(self, listener):
        r"""SUMMARY

        add_event_listener(listener)

        @Arguments:
        - `listener`:

        @Return:

        @Error:
        """
        self._listeners.append(listener)

    def remove_event_listener(self, listener):
        r"""SUMMARY

        remove_event_listener(listener)

        @Arguments:
        - `listener`:

        @Return:

        @Error:
        """
        self._listeners.remove(listener)

    def has_event_listener(self, listener):
        r"""SUMMARY

        has_event_listener(listener)

        @Arguments:
        - `listener`:

        @Return:

        @Error:
        """
        self._listeners.remove(listener)

    def clear_event_listeners(self, ):
        r"""SUMMARY

        clear_event_listeners()

        @Return:

        @Error:
        """
        self._listeners[:] = []



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# event_dispatcher.py ends here
