#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""window_manager_observer -- DESCRIPTION

"""


class WindowManagerObserver(object):
    r"""WindowManagerObserver

    WindowManagerObserver is a object.
    Responsibility:
    """
    def on_created_window(self, window):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """

    def on_destroyed_window(self, window_id):
        r"""SUMMARY

        on_destroyed_window(window_id)

        @Arguments:
        - `window_id`:

        @Return:

        @Error:
        """

    def on_changed_active_window(self, window):
        r"""SUMMARY

        on_changed_active_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """

    def on_changed_current_desktop(self, desktop):
        r"""SUMMARY

        on_changed_current_desktop(desktop)

        @Arguments:
        - `desktop`:

        @Return:

        @Error:
        """

    def on_changed_desktop_names(self, names):
        r"""SUMMARY

        on_changed_desktop_names(names)

        @Arguments:
        - `names`:

        @Return:

        @Error:
        """

    def on_changed_viewport(self, viewport):
        r"""SUMMARY

        on_changed_viewport(viewport)

        @Arguments:
        - `viewport`:

        @Return:

        @Error:
        """

    def on_changed_number_of_desktops(self, desktop_num):
        r"""SUMMARY

        on_changed_number_of_desktops(desktop_num)

        @Arguments:
        - `desktop_num`:

        @Return:

        @Error:
        """

    def on_changed_workarea(self, workareas):
        r"""SUMMARY

        on_changed_workarea(workareas)

        @Arguments:
        - `workareas`:

        @Return:

        @Error:
        """



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# window_manager_observer.py ends here
