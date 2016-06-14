#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""desktop_window_factory -- DESCRIPTION

"""
from .x11.window import Window
from .desktop_window import DesktopWindow


class WindowFacroty(object):
    r"""WindowFacroty

    WindowFacroty is a object.
    Responsibility:
    """
    def __init__(self, display):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self.display = display
        self._windows = []

    def get_or_create(self, window):
        r"""SUMMARY

        get_or_create(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        if window not in self:
            self._windows.append(DesktopWindow(Window(self.display, int(window))))
        return self._windows[self._windows.index(window)]

    def remove(self, window):
        r"""SUMMARY

        remove(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        if window in self:
            self._windows.remove(window)

    def list_windows(self, ):
        r"""SUMMARY

        list_windows()

        @Return:

        @Error:
        """
        return self._windows[:]

    def exists(self, window):
        r"""SUMMARY

        exists(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        return window in self._windows

    def clear(self, ):
        r"""SUMMARY

        clear()

        @Return:

        @Error:
        """
        self._windows = []

    def __contains__(self, window):
        return self.exists(window)

    def __iter__(self):
        return iter(self._windows[:])



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# desktop_window_factory.py ends here
