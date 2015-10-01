#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: xsendevent.py 277 2015-01-28 23:57:11Z t1 $
# $Revision: 277 $
# $Date: 2015-01-29 08:57:11 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 08:57:11 +0900 (Thu, 29 Jan 2015) $

r"""xsendevent -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod
from sendevent import KeyPress, KeyRelease, ButtonPress, ButtonRelease

from xsendkey.obj.destination import Destination
from xsendkey.obj.pieces import XKey, XButton


class SendEventAbstract(object):
    r"""SendEventKey

    SendEventKey is a object.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    propagate = 0
    sequence_number = 0
    time = 0
    root = Destination(0, 0, 0)
    child = 0
    samescreen = 0

    def __init__(self, window, x=0, y=0, display=None):
        r"""

        @Arguments:
        - `window`:
        - `code`:
        - `x`:
        - `y`:
        - `modifier`:
        - `display`:
        """
        self._dest = Destination(window, x, y, display)

    @abstractmethod
    def press(self, ):
        pass

    @abstractmethod
    def release(self, ):
        pass

    @property
    def destination(self, ):
        r"""SUMMARY

        destination()

        @Return:

        @Error:
        """
        return self.window

    @property
    def rootx(self, ):
        r"""SUMMARY

        rootx()

        @Return:

        @Error:
        """
        return self.root.get_x()

    @property
    def rooty(self, ):
        r"""SUMMARY

        rooty()

        @Return:

        @Error:
        """
        return self.root.get_y()

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._dest.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        self._dest.set_window(window)

    window = property(get_window, set_window)

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self._dest.get_display()

    def set_display(self, display):
        r"""SUMMARY

        set_display(display)

        @Arguments:
        - `display`:

        @Return:

        @Error:
        """
        self._dest.set_display(display)

    display = property(get_display, set_display)

    def get_event_point(self, ):
        r"""SUMMARY

        get_event_point()

        @Return:

        @Error:
        """
        return self._dest.get_point()

    def set_event_point(self, point):
        r"""SUMMARY

        set_event_point(point)

        @Arguments:
        - `point`:

        @Return:

        @Error:
        """
        self._dest.set_point(point)

    def clear_event_point(self, ):
        r"""SUMMARY

        clear_event_point()

        @Return:

        @Error:
        """
        self.set_event_point((0, 0))

    eventpoint = property(get_event_point, set_event_point, clear_event_point)

    def get_eventx(self, ):
        r"""SUMMARY

        get_x()

        @Return:

        @Error:
        """
        return self._dest.get_x()

    def set_eventx(self, newx):
        r"""SUMMARY

        set_x(newx)

        @Arguments:
        - `newx`:

        @Return:

        @Error:
        """
        self._dest.set_x(newx)

    eventx = property(get_eventx, set_eventx)

    def get_eventy(self, ):
        r"""SUMMARY

        get_y()

        @Return:

        @Error:
        """
        return self._dest.get_y()

    def set_eventy(self, newy):
        r"""SUMMARY

        set_y(newy)

        @Arguments:
        - `newy`:

        @Return:

        @Error:
        """
        self._dest.set_y(newy)

    eventy = property(get_eventy, set_eventy)

    def flush(self, ):
        r"""SUMMARY

        flush()

        @Return:

        @Error:
        """
        self._dest.flush()


class SendEventKey(SendEventAbstract):
    r"""SendEventKey

    SendEventKey is a SendEventAbstract.
    Responsibility:
    """
    def __init__(self, window, code, modifier=0, x=0, y=0, display=None):
        r"""

        @Arguments:
        - `window`:
        - `code`:
        - `modifier`:
        - `x`:
        - `y`:
        - `display`:
        """
        SendEventAbstract.__init__(self, window, x, y, display)
        self._piece = XKey(code, modifier)

    def get_code(self, ):
        r"""SUMMARY

        get_code()

        @Return:

        @Error:
        """
        return self._piece.get_code()

    def set_code(self, code):
        r"""SUMMARY

        set_code(code)

        @Arguments:
        - `code`:

        @Return:

        @Error:
        """
        self._piece.set_code(code)

    code = property(get_code, set_code)

    def get_modifier(self, ):
        r"""SUMMARY

        get_modifier()

        @Return:

        @Error:
        """
        return self._piece.get_modifier()

    def set_modifier(self, modifier):
        r"""SUMMARY

        set_modifier(modifier)

        @Arguments:
        - `modifier`:

        @Return:

        @Error:
        """
        self._piece.set_modifier(modifier)

    modifier = property(get_modifier, set_modifier)

    def add_modifier(self, modifier):
        r"""SUMMARY

        add_modifier(modifier)

        @Arguments:
        - `modifier`:

        @Return:

        @Error:
        """
        self._piece.add_modifier(modifier)

    def remove_modifier(self, modifier):
        r"""SUMMARY

        remove_modifier(modifier)

        @Arguments:
        - `modifier`:

        @Return:

        @Error:
        """
        self._piece.remove_modifier(modifier)

    def clear_modifier(self, ):
        r"""SUMMARY

        clear_modifier()

        @Return:

        @Error:
        """
        self._piece.clear_modifier()

    def ismodified(self, modifier):
        r"""SUMMARY

        ismodified(modifier)

        @Arguments:
        - `modifier`:

        @Return:

        @Error:
        """
        return self._piece.ismodified(modifier)

    def press(self, ):
        r"""SUMMARY

        press()

        @Return:

        @Error:
        """
        return KeyPress(self.propagate, self.destination, self.code,
                        self.sequence_number, self.time, self.root.window,
                        self.window, self.child, self.rootx, self.rooty,
                        self.eventx, self.eventy, self.modifier,
                        self.samescreen, display=self.display).send()

    def release(self, ):
        r"""SUMMARY

        release()

        @Return:

        @Error:
        """
        return KeyRelease(self.propagate, self.destination, self.code,
                          self.sequence_number, self.time, self.root.window,
                          self.window, self.child, self.rootx, self.rooty,
                          self.eventx, self.eventy, self.modifier,
                          self.samescreen, display=self.display).send()


class SendEventButton(SendEventAbstract):
    r"""SendEventButton

    SendEventButton is a SendEventAbstract.
    Responsibility:
    """
    def __init__(self, window, code, modifier=0, x=0, y=0, display=None):
        r"""

        @Arguments:
        - `window`:
        - `code`:
        - `modifier`:
        - `x`:
        - `y`:
        - `display`:
        """
        SendEventAbstract.__init__(self, window, x, y, display)
        self._piece = XButton(code, modifier)

    def get_code(self, ):
        r"""SUMMARY

        get_code()

        @Return:

        @Error:
        """
        return self._piece.get_code()

    def set_code(self, code):
        r"""SUMMARY

        set_code(code)

        @Arguments:
        - `code`:

        @Return:

        @Error:
        """
        self._piece.set_code(code)

    code = property(get_code, set_code)

    def get_modifier(self, ):
        r"""SUMMARY

        get_modifier()

        @Return:

        @Error:
        """
        return self._piece.get_modifier()

    def set_modifier(self, modifier):
        r"""SUMMARY

        set_modifier(modifier)

        @Arguments:
        - `modifier`:

        @Return:

        @Error:
        """
        self._piece.set_modifier(modifier)

    modifier = property(get_modifier, set_modifier)

    def add_modifier(self, modifier):
        r"""SUMMARY

        add_modifier(modifier)

        @Arguments:
        - `modifier`:

        @Return:

        @Error:
        """
        self._piece.add_modifier(modifier)

    def remove_modifier(self, modifier):
        r"""SUMMARY

        remove_modifier(modifier)

        @Arguments:
        - `modifier`:

        @Return:

        @Error:
        """
        self._piece.remove_modifier(modifier)

    def clear_modifier(self, ):
        r"""SUMMARY

        clear_modifier()

        @Return:

        @Error:
        """
        self._piece.clear_modifier()

    def ismodified(self, modifier):
        r"""SUMMARY

        ismodified(modifier)

        @Arguments:
        - `modifier`:

        @Return:

        @Error:
        """
        return self._piece.ismodified(modifier)

    def press(self, ):
        r"""SUMMARY

        press()

        @Return:

        @Error:
        """
        return ButtonPress(self.propagate, self.destination, self.code,
                           self.sequence_number, self.time, self.root.window,
                           self.window, self.child, self.rootx, self.rooty,
                           self.eventx, self.eventy, self.modifier,
                           self.samescreen, display=self.display).send()

    def release(self, ):
        r"""SUMMARY

        release()

        @Return:

        @Error:
        """
        return ButtonRelease(self.propagate, self.destination, self.code,
                             self.sequence_number, self.time, self.root.window,
                             self.window, self.child, self.rootx, self.rooty,
                             self.eventx, self.eventy, self.modifier,
                             self.samescreen, display=self.display).send()






# For Emacs
# Local Variables:
# coding: utf-8
# End:
# xsendevent.py ends here
