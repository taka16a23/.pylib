#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""window_observer -- DESCRIPTION

"""


class WindowObserver(object):
    """Class WindowObserver
    """
    # Operations
    def on_window_title_changed(self, window):
        """function on_window_title_changed

        window: WindowClient

        returns None
        """
        return None # should raise NotImplementedError()

    def on_window_state_changed(self, window):
        r"""SUMMARY

        on_window_state_changed(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """

    def on_window_maximized(self, window):
        """function on_window_maximized

        window: WindowClient

        returns None
        """
        return None # should raise NotImplementedError()

    def on_window_minimized(self, window):
        """function on_window_minimized

        window: WindowClient

        returns None
        """
        return None # should raise NotImplementedError()

    def on_window_fullscreened(self, window):
        """function on_window_fullscreened

        window: WindowClient

        returns None
        """
        return None # should raise NotImplementedError()

    def on_window_shaded(self, window):
        """function on_window_shaded

        window: WindowClient

        returns None
        """
        return None # should raise NotImplementedError()

    def on_window_destroyed(self, window_id):
        """function on_window_destroyed

        window_id: int

        returns None
        """
        return None # should raise NotImplementedError()

    def on_window_bounds_changed(self, window):
        """function on_window_bounds_changed

        window: WindowClient

        returns None
        """
        return None # should raise NotImplementedError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# window_observer.py ends here
