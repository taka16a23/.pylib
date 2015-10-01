#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: destination.py 277 2015-01-28 23:57:11Z t1 $
# $Revision: 277 $
# $Date: 2015-01-29 08:57:11 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 08:57:11 +0900 (Thu, 29 Jan 2015) $

r"""destination -- DESCRIPTION

"""
from wxcb.xobj.window import Window
from wxcb.xobj.point import Point


class Destination(object):
    r"""Destination

    Destination is a object.
    Responsibility:
    """
    def __init__(self, window, x=0, y=0, display=None):
        r"""

        @Arguments:
        - `window`:
        - `x`:
        - `y`:
        - `display`:
        """
        self._window = Window(window, display)
        self._point = Point(x, y)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._window

    def set_window(self, window):
        r"""SUMMARY

        set_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        self._window.set_id(window)

    window = property(get_window, set_window)

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self.window.get_display()

    def set_display(self, display):
        r"""SUMMARY

        set_display(display)

        @Arguments:
        - `display`:

        @Return:

        @Error:
        """
        self.window.set_display(display)

    display = property(get_display, set_display)

    def get_point(self, ):
        r"""SUMMARY

        get_point()

        @Return:

        @Error:
        """
        return self._point

    def set_point(self, point):
        r"""SUMMARY

        set_point(point)

        @Arguments:
        - `point`:

        @Return:

        @Error:
        """
        self._point.set(point)

    point = property(get_point, set_point)

    def get_x(self, ):
        r"""SUMMARY

        get_x()

        @Return:

        @Error:
        """
        return self.point.get_x()

    def set_x(self, newx):
        r"""SUMMARY

        set_x(newx)

        @Arguments:
        - `newx`:

        @Return:

        @Error:
        """
        self.point.set_x(newx)

    x = property(get_x, set_x)

    def get_y(self, ):
        r"""SUMMARY

        get_y()

        @Return:

        @Error:
        """
        return self.point.get_y()

    def set_y(self, newy):
        r"""SUMMARY

        set_y(newy)

        @Arguments:
        - `newy`:

        @Return:

        @Error:
        """
        self.point.set_y(newy)
    y = property(get_y, set_y)

    def flush(self, ):
        r"""SUMMARY

        flush()

        @Return:

        @Error:
        """
        self.window.flush()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# destination.py ends here
