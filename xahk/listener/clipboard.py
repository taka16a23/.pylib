#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""clipboard -- DESCRIPTION

"""
from xcb.xproto import PropertyNotifyEvent, SelectionNotifyEvent
from xcb.xproto import WindowClass, CW, EventMask, PropMode
from xcb import xfixes

from xahk.events import EventListener, EventLoop
from xahk.x11.display import Display
from xahk.x11.atom_cache import AtomCache
from xahk.x11.window import Window
from xahk.wm.window_manager import WindowManager


KATOM = [
    'UTF8_STRING',
    'PRIMARY',
    'CLIPBOARD',
]

def create_simple_window(display):
    r"""SUMMARY

    create_simple_window()

    @Return:

    @Error:
    """
    setup = display.get_setup()
    root = setup.roots[0].root
    depth = setup.roots[0].root_depth
    visual = setup.roots[0].root_visual
    white = setup.roots[0].white_pixel
    window = display.generate_id()

    display.core.CreateWindow(
        depth, window, root, 0, 0, 640, 480, 0,
        WindowClass.InputOutput, visual,
        CW.BackPixel | CW.EventMask,
        [ white, EventMask.ButtonPress|EventMask.EnterWindow
          |EventMask.LeaveWindow|EventMask.Exposure|EventMask.PropertyChange|
          EventMask.StructureNotify])
    display.flush()
    return window


class Clipboard(EventListener):
    r"""Clipboard

    Clipboard is a EventListener.
    Responsibility:
    """
    def __init__(self, ):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self.display = Display()
        self._atom = AtomCache(self.display, KATOM)
        win = create_simple_window(self.display)
        window = Window(self.display, win)
        fix = self.display(xfixes.key)
        fix.QueryVersion(xfixes.MAJOR_VERSION,xfixes.MINOR_VERSION).reply()
        fix.SelectSelectionInput(win, self._atom.get_atom('CLIPBOARD'), 1|2|4)
        self.display.flush()
        window.change_attributes_checked(
            CW.EventMask,
            [EventMask.StructureNotify|EventMask.PropertyChange|window.get_attributes().reply().your_event_mask]).check()
        # self.display.core.ChangeWindowAttributes(win, CW.EventMask, [EventMask.PropertyChange|EventMask.StructureNotify])
        self.display.core.ConvertSelection(
            win, self._atom.get_atom('CLIPBOARD'),
            self._atom.get_atom('UTF8_STRING'),
            self._atom.get_atom('CLIPBOARD'), 0)
        name = 'hello'
        self.display.core.ChangeProperty(
            PropMode.Replace, win, self._atom.get_atom('WM_NAME'),
            self._atom.get_atom('STRING'), 8, len(name), name)
        # self.display.core.ConvertSelection(
            # win, self._atom.get_atom('CLIPBOARD'), self._atom.get_atom('UTF8_STRING'), self._atom.get_atom('PRIMARY'), 0)
        self.display.flush()
        EventLoop.get_instance(Display()).add_event_listener(self)

    def can_dispatch_event(self, event):
        r"""SUMMARY

        can_dispatch_event(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        return isinstance(event, (PropertyNotifyEvent, SelectionNotifyEvent))

    def handle_event(self, event):
        r"""SUMMARY

        handle_event(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        if isinstance(event, (SelectionNotifyEvent, )):
            print('DEBUG-1-clipboard.py')
            print(event.selection)
            return
        if event.atom == self._atom.get_atom('PRIMARY'):
            print('PRIMARY')
            print(event.window)
        if event.atom == self._atom.get_atom('CLIPBOARD'):
            print('CLIPBOARD')
            print(event.window)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# clipboard.py ends here
