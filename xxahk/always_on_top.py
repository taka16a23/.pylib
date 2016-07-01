#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""always_on_top -- DESCRIPTION

"""
from xahk.bind.mouse import GlobalMouseBinder, LEFT_ACCELERATOR, MouseEventHandler
from xahk.x11.modifier import Modifier
from xahk.listener.cursor import CursorListener


class ToggleAlwaysTop(MouseEventHandler):
    r"""ToggleAlwaysTop

    ToggleAlwaysTop is a KeyEventHandler.
    Responsibility:
    """
    def __init__(self, ):
        r"""
        """
        self._cursor = CursorListener()

    def on_button_press(self, event):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        window = self._cursor.get_under_window()
        window.toggle_always_on_top().check()



GLOBAL_BUTTON = GlobalMouseBinder()
GLOBAL_BUTTON.bind(LEFT_ACCELERATOR|Modifier.Mask.Shift, ToggleAlwaysTop())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# always_on_top.py ends here
