#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""cursor -- DESCRIPTION

"""
from rectangle import Point


class X11Cursor(object):
    """Class X11Cursor
    """
    # Attributes:
    def __init__(self, display):
        r"""

        @Arguments:
        - `display`:
        """
        self.display = display

    # Operations
    def get_display(self):
        """function get_display

        returns
        """
        return self.display

    @property
    def root(self, ):
        r"""SUMMARY

        root()

        @Return:

        @Error:
        """
        return self.display.get_setup().roots[0].root

    def _query_pointer(self, ):
        r"""SUMMARY

        _query_pointer()

        @Return:

        @Error:
        """
        return self.display.core.QueryPointer(self.root).reply()

    def get_point(self):
        """function get_point

        returns Point
        """
        rep = self._query_pointer()
        return Point(rep.win_x, rep.win_y)

    def set_point(self, newx, newy):
        """function set_point

        newx:
        newy:

        returns
        """
        return self.display.core.WarpPointerChecked(
            0, self.root, 0, 0, 0, 0, newx, newy)

    # def set_point(self, point):
    #     """function set_point

    #     point: Point

    #     returns
    #     """
    #     return None # should raise NotImplementedError()

    def get_under_window(self):
        """function get_under_window

        returns
        """
        # TODO: (Atami) [2015/12/09]
        child = self._query_pointer().child
        children = self.display.core.QueryTree(child).reply().children




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# cursor.py ends here
