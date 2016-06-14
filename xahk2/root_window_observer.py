#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""root_window_observer -- DESCRIPTION

"""


class RootWindowObserver(object):
    """Class RootWindowObserver
    """
    # Operations
    def on_active_window_changed(self, root):
        """function on_active_window_changed

        root: RootWindow

        returns None
        """
        return None # should raise NotImplementedError()

    def on_clientlist_changed(self, root):
        """function on_clientlist_changed

        root: RootWindow

        returns None
        """
        return None # should raise NotImplementedError()

    def on_clientlist_stacking_changed(self, root):
        """function on_clientlist_stacking_changed

        root: RootWindow

        returns None
        """
        return None # should raise NotImplementedError()

    def on_current_desktop_changed(self, root):
        """function on_current_desktop_changed

        root: RootWindow

        returns None
        """
        return None # should raise NotImplementedError()

    def on_desktop_names_changed(self, root):
        """function on_desktop_names_changed

        root: RootWindow

        returns None
        """
        return None # should raise NotImplementedError()

    def on_viewport_changed(self, root):
        """function on_viewport_changed

        root: RootWindow

        returns None
        """
        return None # should raise NotImplementedError()

    def on_wm_user_time_changed(self, root):
        r"""SUMMARY

        on_wm_user_time_changed(root)

        @Arguments:
        - `root`:

        @Return:

        @Error:
        """

    def on_number_of_desktops_changed(self, root):
        r"""SUMMARY

        on_number_of_desktops_changed(root)

        @Arguments:
        - `root`:

        @Return:

        @Error:
        """

    def on_workarea_changed(self, root):
        r"""SUMMARY

        on_workarea_changed(root)

        @Arguments:
        - `root`:

        @Return:

        @Error:
        """



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# root_window_observer.py ends here
