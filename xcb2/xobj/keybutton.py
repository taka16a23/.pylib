#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""keybutton -- DESCRIPTION

"""
from struct import pack as _pack
from xcb2.abstract import ConnectionAbstract


class KeyButtonAbstract(ConnectionAbstract):
    r"""SUMMARY
    """
    format = 'B'

    def __init__(self, connection, value):
        r"""

        @Arguments:
        - `connection`:
        - `value`:
        """
        ConnectionAbstract.__init__(self, connection)
        self.value = value

    def pack(self, ):
        r"""SUMMARY

        pack()

        @Return:
        """
        return _pack(self.format, self.value)

    def flush(self, ):
        r"""SUMMARY

        flush()

        @Return:
        """
        self.connection.flush()


class Key(KeyButtonAbstract):
    r"""SUMMARY
    """

    def grab(self, owner_events, grab_window, modifiers, pointer_mode,
             keyboard_mode):
        r"""SUMMARY

        grab(owner_events,grab_window, modifiers, pointer_mode, keyboard_mode)

        @Arguments:
        - `owner_events`:
        - `grab_window`:
        - `modifiers`:
        - `pointer_mode`:
        - `keyboard_mode`:

        @Return:
        """
        return self.connection.core.GrabKeyChecked(
            owner_events, grab_window, modifiers, self.value, pointer_mode,
            keyboard_mode)

    def ungrab(self, grab_window, modifiers):
        r"""SUMMARY

        ungrab(grab_window, modifiers)

        @Arguments:
        - `grab_window`:
        - `modifiers`:

        @Return:
        """
        return self.connection.core.UngrabKeyChecked(
            self.value, grab_window, modifiers)

    def press(self, propagate, destination, sequence_number, time, root,
              window, child,  root_x, root_y, event_x, event_y, state,
              same_screen):
        r"""SUMMARY

        press(propagate, destination, sequence_number, time, root,
              window, child,  root_x, root_y, event_x, event_y, state,
              same_screen)

        @Arguments:
        - `propagate`:
        - `destination`:
        - `sequence_number`:
        - `time`:
        - `root`:
        - `window`:
        - `child`:
        - `root_x`:
        - `root_y`:
        - `event_x`:
        - `event_y`:
        - `state`:
        - `same_screen`:

        @Return:
        """
        return self.connection.core.SendEventChecked.KeyPress(
            propagate, destination, self.value, sequence_number, time, root,
            window, child, root_x, root_y, event_x, event_y, state, same_screen)

    def release(self, propagate, destination, sequence_number, time, root,
                window, child,  root_x, root_y, event_x, event_y, state,
                same_screen):
        r"""SUMMARY

        press(propagate, destination, sequence_number, time, root,
              window, child,  root_x, root_y, event_x, event_y, state,
              same_screen)

        @Arguments:
        - `propagate`:
        - `destination`:
        - `sequence_number`:
        - `time`:
        - `root`:
        - `window`:
        - `child`:
        - `root_x`:
        - `root_y`:
        - `event_x`:
        - `event_y`:
        - `state`:
        - `same_screen`:

        @Return:
        """
        return self.connection.core.SendEventChecked.KeyRelease(
            propagate, destination, self.value, sequence_number, time, root,
            window, child, root_x, root_y, event_x, event_y, state, same_screen)

    def to_keysym(self, modifiers):
        r"""SUMMARY

        to_keysym(modifiers)

        @Arguments:
        - `modifiers`:

        @Return:
        """

    def to_char(self, modifiers):
        r"""SUMMARY

        to_char(modifiers)

        @Arguments:
        - `modifiers`:

        @Return:
        """


class Button(KeyButtonAbstract):
    r"""SUMMARY
    """

    def grab(self, owner_events, grab_window, event_mask, pointer_mode,
             keyboard_mode, confine_to, cursor, modifiers):
        r"""SUMMARY

        grab(owner_events, grab_window, event_mask, pointer_mode,
             keyboard_mode, confine_to, cursor, modifiers)

        @Arguments:
        - `owner_events`:
        - `grab_window`:
        - `event_mask`:
        - `pointer_mode`:
        - `keyboard_mode`:
        - `confine_to`:
        - `cursor`:
        - `modifiers`:

        @Return:
        """
        return self.connection.core.GrabButtonChecked(
            owner_events, grab_window, event_mask, pointer_mode, keyboard_mode,
            confine_to, cursor, self.value, modifiers)

    def ungrab(self, grab_window, modifiers):
        r"""SUMMARY

        ungrab(grab_window, modifiers)

        @Arguments:
        - `grab_window`:
        - `modifiers`:

        @Return:
        """
        return self.connection.core.UngrabButtonChecked(
            self.value, grab_window, modifiers)

    def press(self, propagate, destination, sequence_number, time, root, window,
              child, root_x, root_y, event_x, event_y, state, samescreen):
        r"""SUMMARY

        press(propagate, destination, sequence_number, time, root, window,
              child, root_x, root_y, event_x, event_y, state, samescreen)

        @Arguments:
        - `propagate`:
        - `destination`:
        - `sequence_number`:
        - `time`:
        - `root`:
        - `window`:
        - `child`:
        - `root_x`:
        - `root_y`:
        - `event_x`:
        - `event_y`:
        - `state`:
        - `samescreen`:

        @Return:
        """
        return self.connection.core.SendEventChecked.ButtonPress(
            propagate, destination, self.value, sequence_number, time, root,
            window, child, root_x, root_y, event_x, event_y, state, samescreen)

    def release(self, propagate, destination, sequence_number, time, root,
                window, child, root_x, root_y, event_x, event_y, state,
                samescreen):
        r"""SUMMARY

        release(propagate, destination, sequence_number, time, root,
                window, child, root_x, root_y, event_x, event_y, state,
                samescreen)

        @Arguments:
        - `propagate`:
        - `destination`:
        - `sequence_number`:
        - `time`:
        - `root`:
        - `window`:
        - `child`:
        - `root_x`:
        - `root_y`:
        - `event_x`:
        - `event_y`:
        - `state`:
        - `samescreen`:

        @Return:
        """
        return self.connection.core.SendEventChecked.ButtonRelease(
            propagate, destination, self.value, sequence_number, time, root,
            window, child, root_x, root_y, event_x, event_y, state, samescreen)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# keybutton.py ends here
