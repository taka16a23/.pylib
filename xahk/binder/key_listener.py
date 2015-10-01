#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: key_listener.py 339 2015-07-23 18:01:26Z t1 $
# $Revision: 339 $
# $Date: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $

r"""key_listener -- DESCRIPTION

"""
from xahk.events.event_target import EventTarget
from xahk.binder.input_listener import InputListener
from xahk.binder.accelerator import Accelerator
from xahk.binder.define import ModifierMask


class KeyListener(EventTarget, InputListener):
    """Class KeyListener
    """
    # Attributes:
    def __init__(self, window):
        r"""

        @Arguments:
        - `window`:
        """
        EventTarget.__init__(self)
        InputListener.__init__(self)
        self._window = window
        self._is_listening = False

    # Operations
    def can_accept_event(self, event):
        """function can_accept_event

        event:

        returns
        """
        return event.is_key_event()

    def on_key_event(self, event):
        """function on_key_event

        event:

        returns
        """
        if not self.can_accept_event(event):
            return
        modifiers = 0
        if event.modifiers & ModifierMask.Shift:
            modifiers |= ModifierMask.Shift
        if event.modifiers & ModifierMask.Control:
            modifiers |= ModifierMask.Control
        if event.modifiers & ModifierMask.Alt:
            modifiers |= ModifierMask.Alt
        if event.modifiers & ModifierMask.Hiper:
            modifiers |= ModifierMask.Hiper
        if event.modifiers & ModifierMask.Super:
            modifiers |= ModifierMask.Super
        handler = self._binding.get(Accelerator(event.code, modifiers), None)
        if handler is None:
            print('missing key {} {}'.format(event.code, event.modifiers))
            # TODO: (Atami) [2015/07/05] missing call
            return
        handler.on_event(event)

    def get_window(self):
        """function get_window

        returns
        """
        return self._window

    def start_listening(self):
        """function start_listening

        returns
        """
        if self.is_listening():
            return
        self._window.add_posttarget_handler(self)
        self._is_listening = True

    def stop_listening(self):
        """function stop_listening

        returns
        """
        if not self.is_listening():
            return
        self._window.remove_posttarget_handler(self)
        self._is_listening = False

    def is_listening(self):
        """function is_listening

        returns
        """
        return self._is_listening



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# key_listener.py ends here
