#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: root_window_listener_observer.py 339 2015-07-23 18:01:26Z t1 $
# $Revision: 339 $
# $Date: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $

r"""root_window_listener_observer -- DESCRIPTION

"""


class RootWindowListenerObserver(object):
    """Class RootWindowListenerObserver
    """
    # Attributes:

    # Operations
    def on_changed_active_window(self, root_window):
        """function on_changed_active_window

        root_window:

        returns
        """
        return None # should raise NotImplementedError()

    def on_changed_client_list(self, root_window):
        """function on_changed_client_list

        root_window:

        returns
        """
        return None # should raise NotImplementedError()

    def on_changed_client_list_stacking(self, root_window):
        """function on_changed_client_list_stacking

        root_window:

        returns
        """
        return None # should raise NotImplementedError()

    def on_changed_current_desktop(self, root_window):
        """function on_changed_current_desktop

        root_window:

        returns
        """
        return None # should raise NotImplementedError()

    def on_changed_desktop_names(self, root_window):
        """function on_changed_desktop_names

        root_window:

        returns
        """
        return None # should raise NotImplementedError()

    def on_changed_viewport(self, root_window):
        """function on_changed_viewport

        root_window:

        returns
        """
        return None # should raise NotImplementedError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# root_window_listener_observer.py ends here
