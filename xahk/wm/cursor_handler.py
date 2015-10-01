#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: cursor_handler.py 339 2015-07-23 18:01:26Z t1 $
# $Revision: 339 $
# $Date: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $

r"""cursor_handler -- DESCRIPTION

"""
from xcb.xproto import BadWindow

from xahk.logger import LOG
from xahk.wm.root_window import RootWindow


class CursorHandler(object):
    """Class CursorHandler
    """
    # Attributes:
    def __init__(self, display):
        r"""

        @Arguments:
        - `display`:
        """
        self._root = RootWindow(display)
        self._root_client = self._root.window

    # Operations
    def get_display(self):
        """function get_display

        returns
        """
        return self._root.get_display()

    display = property(get_display)

    def get_under_window(self):
        """function get_under_window

        returns
        """
        child = self._root_client.query_pointer().child
        try:
            children = self.display.core.QueryTree(child).reply().children
        except BadWindow as err:
            LOG.error('{}'.format(err))
            import os
            os.system('modprobe pcspkr')
            os.system('/usr/bin/beep -f250 -r2 -l50')
            os.system('rmmod pcspkr')
            return None
        for window in self._root.client_list():
            if window in children:
                return window

    def get_point(self):
        """function get_point

        returns Point
        """
        return self._root_client.get_cursor_point()

    def move_cursor_to(self, newx, newy):
        """function move

        point:

        returns
        """
        return self._root.move_cursor_to(newx, newy)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# cursor_handler.py ends here
