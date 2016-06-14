#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
