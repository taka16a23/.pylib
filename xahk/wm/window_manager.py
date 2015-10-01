#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: window_manager.py 344 2015-07-24 05:08:28Z t1 $
# $Revision: 344 $
# $Date: 2015-07-24 14:08:28 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:08:28 +0900 (Fri, 24 Jul 2015) $

r"""window_manager -- DESCRIPTION

"""
from xahk.wm.window_client import WindowClient
from xahk.wm.root_window import RootWindow


class WindowManager(object):
    """Class WindowManager
    """
    # Attributes:
    def __init__(self, display):
        r"""

        @Arguments:
        - `display`:
        """
        self.root = RootWindow(display)

    # Operations
    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self.root.get_display()

    display = property(get_display)

    def get_name(self):
        """function get_name

        returns
        """
        win = WindowClient(self.display, self.root.get_supporting_wm_id())
        return win.get_title()

    def get_active_window(self):
        """function get_active_window

        returns WindowClient
        """
        return WindowClient(self.display, self.root.get_active_window())

    def list_windows(self, filter=bool):
        """function list_windows

        filter: None

        returns list
        """
        windows = [WindowClient(self.display, wid)
                   for wid in self.root.client_list_stacking()]
        return [w for w in windows if filter(w)]

    def window_exists(self, window):
        """function window_exists

        window:

        returns
        """
        return window in self.root.client_list_stacking()

    def get_current_desktop(self):
        """function get_current_desktop

        returns
        """
        return self.root.get_current_desktop()

    def get_desktop_geometry(self):
        """function get_desktop_size

        returns
        """
        return self.root.get_desktop_geometry()

    def get_workarea(self):
        """function list_workarea

        returns
        """
        return self.root.get_workarea()

    def get_viewport(self):
        """function get_viewport

        returns
        """
        return self.get_viewport()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# window_manager.py ends here
