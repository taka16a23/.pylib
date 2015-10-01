#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: input_event_handler.py 339 2015-07-23 18:01:26Z t1 $
# $Revision: 339 $
# $Date: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $

r"""input_event_handler -- DESCRIPTION

"""
from xahk.events.event_handler import EventHandler


class InputEventHandler(EventHandler):
    def _dispatch_input(self, event):
        if event.is_down():
            self.on_down(event)
        elif event.is_up():
            self.on_up(event)

    def on_mouse_event(self, event):
        self._dispatch_input(event)

    def on_key_event(self, event):
        self._dispatch_input(event)

    def on_down(self, event):
        pass

    def on_up(self, event):
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# input_event_handler.py ends here
