#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""close -- DESCRIPTION

"""
from time import sleep
from xahk.listener.window_manager import WindowManagerListener
from xahk.bind.mouse import MouseEventHandler, GlobalMouseBinder, MIDDLE_ACCELERATOR


class CloseWindow(MouseEventHandler):
    r"""CloseWindow

    CloseWindow is a MouseEventHandler.
    Responsibility:
    """
    def __init__(self, ):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self._wm = WindowManagerListener()

    def on_button_release(self, event):
        r"""SUMMARY

        on_button_release(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        self._wm.get_active_window().close().check()
        sleep(0.1)


GLOBAL_BUTTON = GlobalMouseBinder()
GLOBAL_BUTTON.bind(MIDDLE_ACCELERATOR, CloseWindow())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# close.py ends here
