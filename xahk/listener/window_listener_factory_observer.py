#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: window_listener_factory_observer.py 339 2015-07-23 18:01:26Z t1 $
# $Revision: 339 $
# $Date: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $

r"""window_listener_factory_observer -- DESCRIPTION

"""


class WindowListenerFactoryObserver(object):
    """Class WindowListenerFactoryObserver
    """
    # Attributes:

    # Operations
    def on_created_window_listener(self, window):
        """function on_created_window_listener

        window:

        returns
        """
        return None # should raise NotImplementedError()

    def on_destroyed_window_listener(self, window_id):
        """function on_destroyed_window_listener

        window_id:

        returns
        """
        return None # should raise NotImplementedError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# window_listener_factory_observer.py ends here
