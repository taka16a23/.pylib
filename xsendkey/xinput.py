#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: xinput.py 277 2015-01-28 23:57:11Z t1 $
# $Revision: 277 $
# $Date: 2015-01-29 08:57:11 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 08:57:11 +0900 (Thu, 29 Jan 2015) $

r"""xinput -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod
from enum import IntEnum

from xsendkey.xsendevent import SendEventKey, SendEventButton


class Behave(IntEnum):
    r"""Behave

    Behave is a IntEnum.
    Responsibility:
    """
    up = 2
    down = 4
    both = up | down


class XInput(object):
    r"""XInput

    XInput is a object.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    def __init__(self, behave=Behave.both):
        r"""

        @Arguments:
        - `behave`:
        """
        self._behave = behave

    def get_behave(self):
        """function get_behave

        returns int
        """
        return self._behave

    def set_behave(self, behave):
        """function set_behave

        behave: int

        returns None
        """
        self._behave = Behave(behave)

    def reset_behave(self, ):
        r"""SUMMARY

        reset_behave()

        @Return:

        @Error:
        """
        self._behave = Behave.both

    behave = property(get_behave, set_behave, reset_behave)

    def add_behave(self, behave):
        r"""SUMMARY

        add_behave(behave)

        @Arguments:
        - `behave`:

        @Return:

        @Error:
        """
        self._behave |= behave

    def remove_behave(self, behave):
        r"""SUMMARY

        remove_behave(behave)

        @Arguments:
        - `behave`:

        @Return:

        @Error:
        """
        self._behave ^= behave

    def isdown(self, ):
        r"""SUMMARY

        isdown()

        @Return:

        @Error:
        """
        return (Behave.down & self._behave) != 0

    def isup(self, ):
        r"""SUMMARY

        isup()

        @Return:

        @Error:
        """
        return (Behave.up & self._behave) != 0

    @abstractmethod
    def input(self, ):
        pass


class XInputKey(XInput):
    r"""XInputKey

    XInputKey is a XInput.
    Responsibility:
    """
    def __init__(self, window, code, modifier=0, x=0, y=0,
                 behave=Behave.both, display=None):
        r"""

        @Arguments:
        - `window`:
        - `code`:
        - `modifier`:
        - `x`:
        - `y`:
        - `behave`:
        - `display`:
        """
        XInput.__init__(self, behave)
        self._sendevent = SendEventKey(window, code, modifier, x, y, display)

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self._sendevent.get_display()

    def set_display(self, display):
        r"""SUMMARY

        set_display(display)

        @Arguments:
        - `display`:

        @Return:

        @Error:
        """
        self._sendevent.set_display(display)

    display = property(get_display, set_display)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._sendevent.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        self._sendevent.set_window(window)

    window = property(get_window, set_window)

    def get_code(self, ):
        r"""SUMMARY

        get_code()

        @Return:

        @Error:
        """
        return self._sendevent.get_code()

    def set_code(self, code):
        r"""SUMMARY

        set_code(code)

        @Arguments:
        - `code`:

        @Return:

        @Error:
        """
        self._sendevent.set_code(code)

    code = property(get_code, set_code)

    def get_modifier(self, ):
        r"""SUMMARY

        get_modifier()

        @Return:

        @Error:
        """
        return self._sendevent.get_modifier()

    def set_modifier(self, modifier):
        r"""SUMMARY

        set_modifier(modifier)

        @Arguments:
        - `modifier`:

        @Return:

        @Error:
        """
        self._sendevent.set_modifier(modifier)

    def clear_modifier(self, ):
        r"""SUMMARY

        clear_modifier()

        @Return:

        @Error:
        """
        self._sendevent.clear_modifier()

    modifier = property(get_modifier, set_modifier, clear_modifier)

    def add_modifier(self, modifier):
        r"""SUMMARY

        add_modifier(modifier)

        @Arguments:
        - `modifier`:

        @Return:

        @Error:
        """
        self._sendevent.add_modifier(modifier)

    def remove_modifier(self, modifier):
        r"""SUMMARY

        remove_modifier(modifier)

        @Arguments:
        - `modifier`:

        @Return:

        @Error:
        """
        self._sendevent.remove_modifier(modifier)

    def ismodified(self, modifier):
        r"""SUMMARY

        ismodified(modifier)

        @Arguments:
        - `modifier`:

        @Return:

        @Error:
        """
        return self._sendevent.ismodified(modifier)

    def get_event_point(self, ):
        r"""SUMMARY

        get_event_point()

        @Return:

        @Error:
        """
        return self._sendevent.get_event_point()

    def set_event_point(self, point):
        r"""SUMMARY

        set_event_point(point)

        @Arguments:
        - `point`:

        @Return:

        @Error:
        """
        self._sendevent.set_event_point(point)

    def clear_event_point(self, ):
        r"""SUMMARY

        clear_event_point()

        @Return:

        @Error:
        """
        self._sendevent.clear_event_point()

    eventpoint = property(get_event_point, set_event_point, clear_event_point)

    def get_eventx(self, ):
        r"""SUMMARY

        get_eventx()

        @Return:

        @Error:
        """
        return self._sendevent.get_eventx()

    def set_eventx(self, eventx):
        r"""SUMMARY

        set_eventx(eventx)

        @Arguments:
        - `eventx`:

        @Return:

        @Error:
        """
        self._sendevent.set_eventx(eventx)

    def clear_eventx(self, ):
        r"""SUMMARY

        clear_eventx()

        @Return:

        @Error:
        """
        self.set_eventx(0)

    eventx = property(get_eventx, set_eventx, clear_eventx)

    def get_eventy(self, ):
        r"""SUMMARY

        get_eventy()

        @Return:

        @Error:
        """
        return self._sendevent.get_eventy()

    def set_eventy(self, eventy):
        r"""SUMMARY

        set_eventy(eventy)

        @Arguments:
        - `eventy`:

        @Return:

        @Error:
        """
        self._sendevent.set_eventy(eventy)

    def clear_eventy(self, ):
        r"""SUMMARY

        clear_eventy()

        @Return:

        @Error:
        """
        self.set_eventy(0)

    eventy = property(get_eventy, set_eventy, clear_eventy)

    def input(self, ):
        r"""SUMMARY

        input()

        @Return:

        @Error:
        """
        cookies = []
        if self.isdown():
            cookies.append(self._sendevent.press())
        if self.isup():
            cookies.append(self._sendevent.release())
        return cookies

    def flush(self, ):
        r"""SUMMARY

        flush()

        @Return:

        @Error:
        """
        self.window.flush()


class XInputButton(XInput):
    r"""XInputButton

    XInputButton is a XInput.
    Responsibility:
    """
    def __init__(self, window, code, modifier=0, x=0, y=0,
                 behave=Behave.both, display=None):
        r"""

        @Arguments:
        - `window`:
        - `code`:
        - `modifier`:
        - `x`:
        - `y`:
        - `behave`:
        - `display`:
        """
        XInput.__init__(self, behave)
        self._sendevent = SendEventButton(window, code, modifier, x, y, display)

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self._sendevent.get_display()

    def set_display(self, display):
        r"""SUMMARY

        set_display(display)

        @Arguments:
        - `display`:

        @Return:

        @Error:
        """
        self._sendevent.set_display(display)

    display = property(get_display, set_display)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._sendevent.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        self._sendevent.set_window(window)

    window = property(get_window, set_window)

    def get_code(self, ):
        r"""SUMMARY

        get_code()

        @Return:

        @Error:
        """
        return self._sendevent.get_code()

    def set_code(self, code):
        r"""SUMMARY

        set_code(code)

        @Arguments:
        - `code`:

        @Return:

        @Error:
        """
        self._sendevent.set_code(code)

    code = property(get_code, set_code)

    def get_modifier(self, ):
        r"""SUMMARY

        get_modifier()

        @Return:

        @Error:
        """
        return self._sendevent.get_modifier()

    def set_modifier(self, modifier):
        r"""SUMMARY

        set_modifier(modifier)

        @Arguments:
        - `modifier`:

        @Return:

        @Error:
        """
        self._sendevent.set_modifier(modifier)

    def clear_modifier(self, ):
        r"""SUMMARY

        clear_modifier()

        @Return:

        @Error:
        """
        self._sendevent.clear_modifier()

    modifier = property(get_modifier, set_modifier, clear_modifier)

    def add_modifier(self, modifier):
        r"""SUMMARY

        add_modifier(modifier)

        @Arguments:
        - `modifier`:

        @Return:

        @Error:
        """
        self._sendevent.add_modifier(modifier)

    def remove_modifier(self, modifier):
        r"""SUMMARY

        remove_modifier(modifier)

        @Arguments:
        - `modifier`:

        @Return:

        @Error:
        """
        self._sendevent.remove_modifier(modifier)

    def ismodified(self, modifier):
        r"""SUMMARY

        ismodified(modifier)

        @Arguments:
        - `modifier`:

        @Return:

        @Error:
        """
        return self._sendevent.ismodified(modifier)

    def get_event_point(self, ):
        r"""SUMMARY

        get_event_point()

        @Return:

        @Error:
        """
        return self._sendevent.get_event_point()

    def set_event_point(self, point):
        r"""SUMMARY

        set_event_point(point)

        @Arguments:
        - `point`:

        @Return:

        @Error:
        """
        self._sendevent.set_event_point(point)

    def clear_event_point(self, ):
        r"""SUMMARY

        clear_event_point()

        @Return:

        @Error:
        """
        self._sendevent.clear_event_point()

    eventpoint = property(get_event_point, set_event_point, clear_event_point)

    def get_eventx(self, ):
        r"""SUMMARY

        get_eventx()

        @Return:

        @Error:
        """
        return self._sendevent.get_eventx()

    def set_eventx(self, eventx):
        r"""SUMMARY

        set_eventx(eventx)

        @Arguments:
        - `eventx`:

        @Return:

        @Error:
        """
        self._sendevent.set_eventx(eventx)

    def clear_eventx(self, ):
        r"""SUMMARY

        clear_eventx()

        @Return:

        @Error:
        """
        self.set_eventx(0)

    eventx = property(get_eventx, set_eventx, clear_eventx)

    def get_eventy(self, ):
        r"""SUMMARY

        get_eventy()

        @Return:

        @Error:
        """
        return self._sendevent.get_eventy()

    def set_eventy(self, eventy):
        r"""SUMMARY

        set_eventy(eventy)

        @Arguments:
        - `eventy`:

        @Return:

        @Error:
        """
        self._sendevent.set_eventy(eventy)

    def clear_eventy(self, ):
        r"""SUMMARY

        clear_eventy()

        @Return:

        @Error:
        """
        self.set_eventy(0)

    eventy = property(get_eventy, set_eventy, clear_eventy)

    def input(self, ):
        r"""SUMMARY

        input()

        @Return:

        @Error:
        """
        cookies = []
        if self.isdown():
            cookies.append(self._sendevent.press())
        if self.isup():
            cookies.append(self._sendevent.release())
        return cookies

    def flush(self, ):
        r"""SUMMARY

        flush()

        @Return:

        @Error:
        """
        self.window.flush()


#### Repeat XInput # must be sync to XInputKey, XInputButton
##
class RepeatXInput(object):
    r"""RepeatXInput

    RepeatXInput is a object.
    Responsibility:
    """
    def __init__(self, xinput, times):
        r"""

        @Arguments:
        - `xinput`:
        - `times`:
        """
        self._xinput = None
        self._times = times
        self.set_xinput(xinput)

    def get_xinput(self, ):
        r"""SUMMARY

        get_xinput()

        @Return:

        @Error:
        """
        return self._xinput

    def set_xinput(self, xinput):
        r"""SUMMARY

        set_xinput(xinput)

        @Arguments:
        - `xinput`:

        @Return:

        @Error:
        """
        if not isinstance(xinput, (XInput, )):
            # TODO: (Atami) [2015/01/29]
            raise TypeError()
        self._xinput = xinput

    xinput = property(get_xinput, set_xinput)

    def get_times(self, ):
        r"""SUMMARY

        get_times()

        @Return:

        @Error:
        """
        return self._times

    def set_times(self, times):
        r"""SUMMARY

        set_times(times)

        @Arguments:
        - `times`:

        @Return:

        @Error:
        """
        self._times = int(times)

    def clear_times(self, ):
        r"""SUMMARY

        clear_times()

        @Return:

        @Error:
        """
        self._times = 0

    times = property(get_times, set_times, clear_times)

    def get_behave(self, ):
        r"""SUMMARY

        get_behave()

        @Return:

        @Error:
        """
        return self._xinput.get_behave()

    def set_behave(self, behave):
        r"""SUMMARY

        set_behave(behave)

        @Arguments:
        - `behave`:

        @Return:

        @Error:
        """
        self._xinput.set_behave(behave)

    def reset_behave(self, ):
        r"""SUMMARY

        reset_behave()

        @Return:

        @Error:
        """
        self._xinput.reset_behave()

    behave = property(get_behave, set_behave, reset_behave)

    def remove_behave(self, behave):
        r"""SUMMARY

        remove_behave(behave)

        @Arguments:
        - `behave`:

        @Return:

        @Error:
        """
        self._xinput.remove_behave(behave)

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self._xinput.get_display()

    def set_display(self, display):
        r"""SUMMARY

        set_display(display)

        @Arguments:
        - `display`:

        @Return:

        @Error:
        """
        self._xinput.set_display(display)

    display = property(get_display, set_display)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._xinput.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        self._xinput.set_window(window)

    window = property(get_window, set_window)

    def get_code(self, ):
        r"""SUMMARY

        get_code()

        @Return:

        @Error:
        """
        return self._xinput.get_code()

    def set_code(self, code):
        r"""SUMMARY

        set_code(code)

        @Arguments:
        - `code`:

        @Return:

        @Error:
        """
        self._xinput.set_code(code)

    code = property(get_code, set_code)

    def get_modifier(self, ):
        r"""SUMMARY

        get_modifier()

        @Return:

        @Error:
        """
        return self._xinput.get_modifier()

    def set_modifier(self, modifier):
        r"""SUMMARY

        set_modifier(modifier)

        @Arguments:
        - `modifier`:

        @Return:

        @Error:
        """
        self._xinput.set_modifier(modifier)

    def clear_modifier(self, ):
        r"""SUMMARY

        clear_modifier()

        @Return:

        @Error:
        """
        self._xinput.clear_modifier()

    modifier = property(get_modifier, set_modifier, clear_modifier)

    def add_modifier(self, modifier):
        r"""SUMMARY

        add_modifier(modifier)

        @Arguments:
        - `modifier`:

        @Return:

        @Error:
        """
        self._xinput.add_modifier(modifier)

    def remove_modifier(self, modifier):
        r"""SUMMARY

        remove_modifier(modifier)

        @Arguments:
        - `modifier`:

        @Return:

        @Error:
        """
        self._xinput.remove_modifier(modifier)

    def ismodified(self, modifier):
        r"""SUMMARY

        ismodified(modifier)

        @Arguments:
        - `modifier`:

        @Return:

        @Error:
        """
        return self._xinput.ismodified(modifier)

    def get_event_point(self, ):
        r"""SUMMARY

        get_event_point()

        @Return:

        @Error:
        """
        return self._xinput.get_event_point()

    def set_event_point(self, point):
        r"""SUMMARY

        set_event_point(point)

        @Arguments:
        - `point`:

        @Return:

        @Error:
        """
        self._xinput.set_event_point(point)

    def clear_event_point(self, ):
        r"""SUMMARY

        clear_event_point()

        @Return:

        @Error:
        """
        self._xinput.clear_event_point()

    eventpoint = property(get_event_point, set_event_point, clear_event_point)

    def get_eventx(self, ):
        r"""SUMMARY

        get_eventx()

        @Return:

        @Error:
        """
        return self._xinput.get_eventx()

    def set_eventx(self, eventx):
        r"""SUMMARY

        set_eventx(eventx)

        @Arguments:
        - `eventx`:

        @Return:

        @Error:
        """
        self._xinput.set_eventx(eventx)

    def clear_eventx(self, ):
        r"""SUMMARY

        clear_eventx()

        @Return:

        @Error:
        """
        self._xinput.clear_eventx()

    eventx = property(get_eventx, set_eventx, clear_eventx)

    def get_eventy(self, ):
        r"""SUMMARY

        get_eventy()

        @Return:

        @Error:
        """
        return self._xinput.get_eventy()

    def set_eventy(self, eventy):
        r"""SUMMARY

        set_eventy(eventy)

        @Arguments:
        - `eventy`:

        @Return:

        @Error:
        """
        self._xinput.set_eventy(eventy)

    def clear_eventy(self, ):
        r"""SUMMARY

        clear_eventy()

        @Return:

        @Error:
        """
        self._xinput.clear_eventy()

    eventy = property(get_eventy, set_eventy, clear_eventy)

    def input(self, ):
        r"""SUMMARY

        input()

        @Return:

        @Error:
        """
        cookies = []
        for _ in range(self.times):
            cookies.extend(self._xinput.input())
        return cookies

    def flush(self, ):
        r"""SUMMARY

        flush()

        @Return:

        @Error:
        """
        self._xinput.flush()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# xinput.py ends here
