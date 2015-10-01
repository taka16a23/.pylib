#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: window_manager.py 339 2015-07-23 18:01:26Z t1 $
# $Revision: 339 $
# $Date: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $

r"""window_manager -- DESCRIPTION

"""
from xahk.listener import RootWindowListener
from xahk.listener import WindowListenerFactory


class WindowManager(object):
    """Class WindowManager
    """
    # Attributes:
    def __init__(self, display):
        r"""

        @Arguments:
        - `display`:
        """
        self._root = RootWindowListener(display)
        self._window_factory = WindowListenerFactory(display)

    # Operations
    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self._root.get_display()

    display = property(get_display)

    def get_name(self):
        """function get_name

        returns
        """
        return self._root.get_name()

    def get_active_window(self):
        """function get_active_window

        returns
        """
        active_id = self._root.get_active_window()
        for window in self.list_windows():
            if active_id == window:
                return window
        return None

    def is_active_window(self, window):
        """function is_active_window

        window:

        returns
        """
        return window == self.get_active_window()

    def list_windows(self, filter=bool):
        """function list_windows

        filter:

        returns
        """
        return self._window_factory.list_windows(filter)

    def window_exists(self, window):
        """function window_exists

        window:

        returns
        """
        return window in self.list_windows()

    def list_desktop_names(self, ):
        r"""SUMMARY

        list_desktop_names()

        @Return:

        @Error:
        """
        return self._root.list_desktop_names()

    def get_current_desktop(self):
        """function get_current_desktop

        returns
        """
        return self._root.get_current_desktop()

    def get_desktop_geometry(self):
        """function get_desktop_geometry

        returns
        """
        return self._root.get_desktop_geometry()

    def get_workarea(self):
        """function get_workarea

        returns
        """
        return self._root.get_workarea()

    def get_viewport(self):
        """function get_viewport

        returns
        """
        return self._root.get_viewport()

    def get_number_of_desktop(self, ):
        r"""SUMMARY

        get_number_of_desktop()

        @Return:

        @Error:
        """
        return self._root.get_number_of_desktop()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# window_manager.py ends here
