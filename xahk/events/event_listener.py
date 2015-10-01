#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: event_listener.py 339 2015-07-23 18:01:26Z t1 $
# $Revision: 339 $
# $Date: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $

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
    def can_dispatch_event(self, event):
        """function can_dispatch_event

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
