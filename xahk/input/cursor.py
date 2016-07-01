#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""cursor -- DESCRIPTION

"""
from xcb.xproto import BadWindow

from xahk.rectangle import Point
from xahk.wm.window_manager import WindowManager
from xahk.log import logging


class Cursor(object):
    """Cursor

    Cursor is a object.
    Responsibility:
    """
    def __init__(self, ):
        """

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self._wm = WindowManager()

    @property
    def root(self, ):
        r"""SUMMARY

        root()

        @Return:

        @Error:
        """
        return self._wm.root

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self._wm.display

    display = property(get_display)

    def get_under_window(self, ):
        r"""SUMMARY

        get_under_window()

        @Return:

        @Error:
        """
        child = self.root.query_pointer().reply().child
        try:
            children = self.display.core.QueryTree(child).reply().children
        except BadWindow as err:
            # TODO: (Atami) [2016/05/13]
            logging.getLogger('xahk').warning('get_under_window {}'.format(err))
            return None
        for window in self._wm.client_list():
            if window in children:
                return window

    def get_point(self, ):
        r"""SUMMARY

        get_point()

        @Return:

        @Error:
        """
        rep = self.root.query_pointer().reply()
        return Point(rep.win_x, rep.win_y)

    def move_cursor_to(self, point):
        r"""SUMMARY

        move_cursor_to(*args)

        @Arguments:
        - `newx`:
        - `newy`:

        @Return:

        @Error:
        """
        return self.root.warp_pointer_checked(
            0, 0, 0, 0, 0, int(point.x), int(point.y))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# cursor.py ends here
