#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: event.py 339 2015-07-23 18:01:26Z t1 $
# $Revision: 339 $
# $Date: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $

r"""event -- DESCRIPTION

"""
from xcb.xproto import (ButtonPressEvent, ButtonReleaseEvent,
                        KeyPressEvent, KeyReleaseEvent)

from rectangle import Point


class Event(object):
    """Class Event
    """
    # Attributes:
    def __init__(self, event):
        r"""

        @Arguments:
        - `event`:
        """
        self._event = event
        self._handled = False

    # Operations
    def is_mouse_event(self):
        """function is_mouse_event

        returns
        """
        return isinstance(self._event, (ButtonPressEvent, ButtonReleaseEvent))

    def is_key_event(self):
        """function is_key_event

        returns
        """
        return isinstance(self._event, (KeyPressEvent, KeyReleaseEvent))

    def is_handled(self):
        """function is_handled

        returns
        """
        return self._handled

    def set_handled(self, handled=True):
        """function set_handled

        returns
        """
        self._handled = handled

    def get_code(self):
        """function get_code

        returns
        """
        return self._event.detail

    code = property(get_code)

    def get_modifiers(self):
        """function get_modifiers

        returns
        """
        return self._event.state

    modifiers = property(get_modifiers)

    def get_time(self):
        """function get_time

        returns
        """
        return self._event.time

    def is_down(self):
        """function is_down

        returns
        """
        return isinstance(self._event, (KeyPressEvent, ButtonPressEvent))

    def is_up(self):
        """function is_up

        returns
        """
        return isinstance(self._event, (KeyReleaseEvent, ButtonReleaseEvent))


class KeyEvent(Event):
    """Class KeyEvent
    """
    # Attributes:
    def __init__(self, event, window):
        r"""

        @Arguments:
        - `event`:
        - `window`:
        """
        Event.__init__(self, event)
        self._window = window

    # Operations
    def get_window(self):
        """function get_window

        returns
        """
        return self._window


class MouseEvent(Event):
    """Class MouseEvent
    """
    # Attributes:
    def __init__(self, event):
        r"""

        @Arguments:
        - `event`:
        """
        Event.__init__(self, event)
        self._point_cache = None

    # Operations
    def get_point(self):
        """function get_point

        returns
        """
        if self._point_cache is None:
            self._point_cache = Point(self._event.event_x, self._event.event_y)
        return self._point_cache

    def get_x(self):
        """function get_x

        returns
        """
        return self.get_point().get_x()

    def get_y(self):
        """function get_y

        returns
        """
        return self.get_point().get_y()

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._event.event



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# event.py ends here
