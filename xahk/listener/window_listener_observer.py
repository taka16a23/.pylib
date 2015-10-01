#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: window_listener_observer.py 348 2015-08-04 13:56:54Z t1 $
# $Revision: 348 $
# $Date: 2015-08-04 22:56:54 +0900 (Tue, 04 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-04 22:56:54 +0900 (Tue, 04 Aug 2015) $

r"""window_listener_observer -- DESCRIPTION

"""


class WindowListenerObserver(object):
    """Class WindowListenerObserver
    """
    # Operations
    def on_window_title_changed(self, window):
        """function on_window_title_changed

        window:

        returns
        """
        return None # should raise NotImplementedError()

    def on_window_maximized(self, window):
        """function on_window_maximized

        window:

        returns
        """
        return None # should raise NotImplementedError()

    def on_window_minimized(self, window):
        """function on_window_minimized

        window:

        returns
        """
        return None # should raise NotImplementedError()

    def on_window_fullscreened(self, window):
        """function on_window_fullscreened

        window:

        returns
        """
        return None # should raise NotImplementedError()

    def on_window_shaded(self, window):
        """function on_window_shaded

        window:

        returns
        """
        return None # should raise NotImplementedError()

    def on_window_destroyed(self, window_id):
        """function on_window_destroyed

        window_id:

        returns
        """
        return None # should raise NotImplementedError()

    def on_window_bounds_changed(self, window):
        """function on_window_bounds_changed

        window:

        returns
        """
        return None # should raise NotImplementedError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# window_listener_observer.py ends here
