#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: event_handler.py 339 2015-07-23 18:01:26Z t1 $
# $Revision: 339 $
# $Date: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $

r"""event_handler -- DESCRIPTION

"""


class EventHandler(object):
    """Class EventHandler
    """
    # Attributes:

    # Operations
    def on_event(self, event):
        """function on_event

        event:

        returns
        """
        if event.is_key_event():
            self.on_key_event(event)
        elif event.is_mouse_event():
            self.on_mouse_event(event)

    def on_key_event(self, event):
        """function on_key_event

        event:

        returns
        """

    def on_mouse_event(self, event):
        """function on_mouse_event

        event:

        returns
        """



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# event_handler.py ends here
