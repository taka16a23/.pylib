#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: mouse_listener_x11.py 348 2015-08-04 13:56:54Z t1 $
# $Revision: 348 $
# $Date: 2015-08-04 22:56:54 +0900 (Tue, 04 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-04 22:56:54 +0900 (Tue, 04 Aug 2015) $

r"""mouse_listener_x11 -- DESCRIPTION

"""
from dotavoider import dotavoid

from xcb.xproto import ButtonPressEvent, ButtonReleaseEvent

from xahk.wm.window_client import WindowClient
from xahk.events.eventloop import EventLoop
from xahk.events.event_listener import EventListener
from xahk.events.event import MouseEvent
from xahk.binder.input_listener import InputListener
from xahk.binder.define import ButtonIndex, ModifierMask
from xahk.binder.accelerator import Accelerator


class MouseListenerX11(InputListener, EventListener):
    """Class MouseListenerX11
    """
    # Attributes:
    _release_modifier = {ButtonIndex.Left: ModifierMask.Left,
                         ButtonIndex.Middle: ModifierMask.Middle,
                         ButtonIndex.Right: ModifierMask.Right,
                         ButtonIndex.WheelUp: ModifierMask.WheelUp,
                         ButtonIndex.WheelDown: ModifierMask.WheelDown,
                         }

    def __init__(self, display):
        r"""

        @Arguments:
        - `display`:
        """
        InputListener.__init__(self)
        self._root = WindowClient(display, display.get_setup().roots[0].root)
        self._is_listening = False

    # Operations
    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self._root.get_display()

    display = property(get_display)

    def can_dispatch_event(self, event):
        """function can_dispatch_event

        event:

        returns
        """
        return isinstance(event, (ButtonPressEvent, ButtonReleaseEvent, ))

    def handle_event(self, event):
        """function handle_event

        event:

        returns
        """
        mevent = MouseEvent(event)
        modifiers = 0
        if mevent.modifiers & ModifierMask.Shift:
            modifiers |= ModifierMask.Shift
        if mevent.modifiers & ModifierMask.Control:
            modifiers |= ModifierMask.Control
        if mevent.modifiers & ModifierMask.Alt:
            modifiers |= ModifierMask.Alt
        if mevent.modifiers & ModifierMask.Hiper:
            modifiers |= ModifierMask.Hiper
        if mevent.modifiers & ModifierMask.Super:
            modifiers |= ModifierMask.Super
        if mevent.modifiers & ModifierMask.Left:
            modifiers |= ModifierMask.Left
        if mevent.modifiers & ModifierMask.Middle:
            modifiers |= ModifierMask.Middle
        if mevent.modifiers & ModifierMask.Right:
            modifiers |= ModifierMask.Right
        # remove pressed button modifiers
        if modifiers & self._release_modifier.get(mevent.code, 0) != 0:
            modifiers = modifiers^self._release_modifier.get(mevent.code, 0)
        accelerator = Accelerator(mevent.code, modifiers)
        handler = self._binding.get(accelerator, None)
        if handler is None:
            print('handler not registered')
            # TODO: (Atami) [2015/07/07] missing call
            return
        handler.on_event(mevent)

    def start_listening(self):
        """function start_listening

        returns
        """
        if self.is_listening():
            return
        EventLoop(self.display).add_event_listener(self)
        self._is_listening = True

    def stop_listening(self):
        """function stop_listening

        returns
        """
        if not self.is_listening():
            return
        EventLoop(self.display).remove_event_listener(self)
        self._is_listening = False

    def is_listening(self):
        """function is_listening

        returns
        """
        return self._is_listening

    def _register_accelerator_impl(self, accelerators):
        """function register_accelerator_impl

        accelerator:

        returns
        """
        accs, append, extend = dotavoid([], 'append', 'extend')
        for acc in accelerators:
            if acc.get_modifiers()^ModifierMask.Left == 0:
                continue
            if acc.get_modifiers()^ModifierMask.Middle == 0:
                continue
            if acc.get_modifiers()^ModifierMask.Right == 0:
                continue
            if acc.get_modifiers()^ModifierMask.WheelUp == 0:
                continue
            if acc.get_modifiers()^ModifierMask.WheelDown == 0:
                continue
            append(acc)
        # extend firster than multi append
        for acc in accs[:]:
            extend((acc|ModifierMask.Numlock,
                    acc|ModifierMask.Lock,
                    acc|ModifierMask.Mod5,
                    acc|ModifierMask.Numlock|ModifierMask.Lock,
                    acc|ModifierMask.Numlock|ModifierMask.Mod5,
                    acc|ModifierMask.Lock|ModifierMask.Mod5,
                    acc|ModifierMask.Numlock|ModifierMask.Lock|ModifierMask.Mod5
                    ))
        cookies = self._root.grab_buttons(accs)
        for cookie in cookies:
            cookie.check()

    def _unregister_accelerator_impl(self, accelerators):
        """function unregister_accelerator_impl

        accelerator:

        returns
        """
        accs, append, extend = dotavoid([], 'append', 'extend')
        for acc in accelerators:
            if acc.get_modifiers()^ModifierMask.Left == 0:
                continue
            if acc.get_modifiers()^ModifierMask.Middle == 0:
                continue
            if acc.get_modifiers()^ModifierMask.Right == 0:
                continue
            if acc.get_modifiers()^ModifierMask.WheelUp == 0:
                continue
            if acc.get_modifiers()^ModifierMask.WheelDown == 0:
                continue
            append(acc)
        # extend firster than multi append
        for acc in accs[:]:
            extend((acc|ModifierMask.Numlock,
                    acc|ModifierMask.Lock,
                    acc|ModifierMask.Mod5,
                    acc|ModifierMask.Numlock|ModifierMask.Lock,
                    acc|ModifierMask.Numlock|ModifierMask.Mod5,
                    acc|ModifierMask.Lock|ModifierMask.Mod5,
                    acc|ModifierMask.Numlock|ModifierMask.Lock|ModifierMask.Mod5
                    ))
        cookies = self._root.ungrab_buttons(accs)
        for cookie in cookies:
            cookie.check()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# mouse_listener_x11.py ends here
