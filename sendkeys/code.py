#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""code -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod

from xcb2.xproto import Propagate, NamedButtonIndex, NamedButtonMask

from sendkeys.display import KeymapDisplay
from sendkeys.modifierstate import ModifierState



class KeyAbstract(KeymapDisplay):
    r"""SUMMARY
    """

    def __init__(self, data, display=None):
        r"""

        @Arguments:
        - `data`:
        - `display`:
        """
        KeymapDisplay.__init__(self, display)
        self._data = data

    def flush(self, ):
        r"""SUMMARY

        flush_()

        @Return:
        """
        self.connection.flush()

    def __cmp__(self, other):
        if isinstance(other, self.__class__):
            return cmp(self._data, other._data)
        return cmp(self._data, other)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._data == other._data
        return self._data == other

    def __ne__(self, other):
        return not (self == other)

    def __str__(self, ):
        return str(self._data)

    def __repr__(self, ):
        return '{0.__class__.__name__}({1})'.format(self, self._data)


class CodeAbstract(KeyAbstract):
    r"""SUMMARY
    """
    __metaclass__ = ABCMeta

    # for _sendkeys.py
    @abstractmethod
    def press(self, window, time=0):
        raise NotImplementedError()

    @abstractmethod
    def release(self, window, time=0):
        raise NotImplementedError()

    def __init__(self, data, state=0, display=None):
        r"""

        @Arguments:
        - `data`:
        - `state`:
        - `display`:
        """
        if isinstance(data, self.__class__):
            state = data.state | state
        KeyAbstract.__init__(self, int(data), display)
        self.state = ModifierState(state)

    @property
    def core(self, ):
        r"""SUMMARY

        code2()

        @Return:
        """
        return self.connection.core

    @property
    def sendevent(self, ):
        r"""SUMMARY

        sendevent()

        @Return:
        """
        return self.core.SendEvent

    @property
    def root(self, ):
        r"""SUMMARY

        root()

        @Return:
        """
        return self.connection.root

    def __ior__(self, other):
        self.state |= other
        return self

    def __cmp__(self, other):
        if isinstance(other, self.__class__):
            if (self._data == other._data and self.state == other.state):
                return 0
            return -1
        return cmp(self._data, other)

    def __hash__(self, ):
        return hash(self._data + int(self.state) * 1000)

    def __repr__(self, ):
        fmt = '{0.__class__.__name__}({1}, state={2})'.format
        return fmt(self, self._data, str(self.state))

    def __int__(self, ):
        return int(self._data)


class KeyCode(CodeAbstract):
    r"""SUMMARY
    """

    def to_keysym(self, ):
        r"""SUMMARY

        to_keysym()

        @Return:
        """
        index = 0
        if self.state.isshift():
            index += 1
        if self.state.isalt():
            index += 2
        sym = self.keymap.keycode_to_keysym(self._data, index)
        return KeySym(sym, display=self.display)

    def to_char(self, ):
        r"""SUMMARY

        to_char()

        @Return:
        """
        return self.to_keysym().to_char()

    def press(self, window, time=0):
        r"""SUMMARY

        press(time=0, window=None, state=0)

        @Arguments:
        - `time`:
        - `window`:
        - `state`:

        @Return:
        """
        # TODO: (Atami) [2014/03/29]
        return self.sendevent.KeyPress(
            Propagate.FALSE, window, self._data, 0, time, self.root, window,
            0, 0, 0, 0, 0, # child, root_x, root_y, event_x, event_y
            self.state, 1, # samescreen
            )

    def release(self, window, time=0):
        r"""SUMMARY

        release(time, window=None, state=0)

        @Arguments:
        - `time`:
        - `window`:
        - `state`:

        @Return:
        """
        # TODO: (Atami) [2014/03/29]
        return self.sendevent.KeyRelease(
            Propagate.FALSE, window, self._data, 0, time, self.root, window,
            0, 0, 0, 0, 0, # child, root_x, root_y, event_x, event_y
            self.state, 1, # samescreen
            )

    def grab(self, window):
        r"""SUMMARY

        grabkey(window)

        @Arguments:
        - `window`:

        @Return:
        """
        self.core.GrabKey.async(False, window, self.state, self._data)
        self.flush()

    def ungrab(self, window):
        r"""SUMMARY

        ungrabkey(window)

        @Arguments:
        - `window`:

        @Return:
        """
        self.core.UngrabKey(self._data, window, self.state)
        self.flush()


class ButtonCode(CodeAbstract):
    r"""SUMMARY
    """
    _release_mod = {NamedButtonIndex.Left: NamedButtonMask.Left,
                    NamedButtonIndex.Middle: NamedButtonMask.Middle,
                    NamedButtonIndex.Right: NamedButtonMask.Right,
                    NamedButtonIndex.WheelUp: NamedButtonMask.WheelUp,
                    NamedButtonIndex.WheelDown: NamedButtonMask.WheelDown,
                    }

    def press(self, window, time=0, event_x=0, event_y=0):
        r"""SUMMARY

        press(time=0, window=None, state=0)

        @Arguments:
        - `time`:
        - `window`:
        - `state`:

        @Return:
        """
        # TODO: (Atami) [2014/03/29]
        return self.core.SendEvent.ButtonPress(
            Propagate.FALSE, window, self._data, 0, time, self.root, window,
            0, 0, 0, # child, root_x, root_y
            event_x, event_y, self.state, 1, #same_screen
            )

    def release(self, window, time=0, event_x=0, event_y=0):
        r"""SUMMARY

        release(time=0, window=None, state=0)

        @Arguments:
        - `time`:
        - `window`:
        - `state`:

        @Return:
        """
        # TODO: (Atami) [2014/03/24]
        self.core.SendEvent.ButtonRelease(
            Propagate.FALSE, window, self._data, 0, time, self.root, window,
            0, 0, 0, # child, root_x, root_y
            event_x, event_y,
            self.state | self._release_mod.get(self._data, 0), 1, #same_screen
            )

    def _getgrabber(self, ):
        r"""SUMMARY

        _getgrabber()

        @Return:
        """
        buttonname = '{0.name}'.format(NamedButtonIndex(self._data))
        return getattr(self.core.GrabButton, buttonname)

    def grabpress(self, window):
        r"""SUMMARY

        GrabPressButton()

        @Return:
        """
        self._getgrabber().press(False, window, 0, 0, self.state)
        self.flush()

    def grabrelease(self, window):
        r"""SUMMARY

        grabreleasebutton(window)

        @Arguments:
        - `window`:

        @Return:
        """
        self._getgrabber().release(False, window, 0, 0, self.state)
        self.flush()

    def grab(self, window):
        r"""SUMMARY

        grabbuttons(window)

        @Arguments:
        - `window`:

        @Return:
        """
        self.grabpress(window)
        self.grabrelease(window)

    def ungrab(self, window):
        r"""SUMMARY

        ungrabbutton(window)

        @Arguments:
        - `window`:

        @Return:
        """
        self.core.UngrabButton(self._data, window, self.state)
        self.flush()

    def __repr__(self, ):
        fmt = '{0.__class__.__name__}(<{1.name}: {1}>, state={2})'.format
        return fmt(self, NamedButtonIndex(self._data), str(self.state))


class KeySym(KeyAbstract):
    r"""SUMMARY
    """

    def to_keycode(self, ):
        r"""SUMMARY

        to_keycode()

        @Return:
        """
        code, state = self.keymap.keysym_to_keycodes(self._data)[0]
        return KeyCode(code, state, display=self.display)

    def to_char(self, ):
        r"""SUMMARY

        to_char()

        @Return:
        """
        char_ = self.keymap.keysym_to_str(self._data)
        return KeyChar(char_, display=self.display)

    def press(self, window, time=0):
        r"""SUMMARY

        press(time=0, window=None)

        @Arguments:
        - `time`:
        - `window`:
        - `state`:

        @Return:
        """
        self.to_keycode().press(window, time)

    def release(self, window, time=0):
        r"""SUMMARY

        release()

        @Return:
        """
        self.to_keycode().release(window, time)


class KeyChar(KeyAbstract):
    r"""SUMMARY
    """

    def to_keysym(self, ):
        r"""SUMMARY

        to_keysym()

        @Return:
        """
        sym = self.keymap.str_to_keysym(self._data)
        return KeySym(sym, display=self.display)

    def to_keycode(self, ):
        r"""SUMMARY

        to_keycode()

        @Return:
        """
        return self.to_keysym().to_keycode()

    def press(self, window, time=0):
        r"""SUMMARY

        press_key()

        @Return:
        """
        self.to_keycode().press(window, time)

    def release(self, window, time=0):
        r"""SUMMARY

        press_key()

        @Return:
        """
        self.to_keycode().release(window, time)

    def __repr__(self, ):
        return '{0.__class__.__name__}("{1}")'.format(self, self._data)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# code.py ends here
