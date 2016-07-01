#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""taskmanager -- DESCRIPTION

"""
from psutil import Process
from xahk.wm.window_spec import WindowTitleSpec
from xahk.bind.mouse import MouseEventHandler, MouseBinder, MIDDLE_ACCELERATOR
from xahk.listener.cursor import CursorListener


TASKMANAGER_SPEC = WindowTitleSpec('Task Manager')



class KillTaskManager(MouseEventHandler):
    r"""KillTaskManager

    KillTaskManager is a MouseEventHandler.
    Responsibility:
    """
    def __init__(self, ):
        r"""
        """
        self._cursor = CursorListener()

    def on_button_release(self, event):
        """SUMMARY

        name()

        @Return:

        @Error:
        """
        window = self._cursor.get_under_window()
        Process(window.pid).kill()


TASKMANAGER_MOUSE_BINDER = MouseBinder(TASKMANAGER_SPEC)
TASKMANAGER_MOUSE_BINDER.bind(MIDDLE_ACCELERATOR, KillTaskManager())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# taskmanager.py ends here
