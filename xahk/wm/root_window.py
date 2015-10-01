#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""root_window -- DESCRIPTION

"""
from struct import unpack as _unpack
from array import array as _array

from rectangle import Dimension, Rectangle
from dotavoider import ListDotAvoider

from xahk.wm.window_client import WindowClient


class RootWindow(object):
    """Class RootWindow
    """
    # Attributes:
    def __init__(self, display):
        r"""

        @Arguments:
        - `display`:
        """
        self.window = WindowClient(display, display.get_setup().roots[0].root)

    # Operations
    def get_id(self):
        """function get_id

        returns
        """
        return int(self.window)

    id = property(get_id)

    def get_display(self):
        """function get_display

        returns
        """
        return self.window.get_display()

    display = property(get_display)

    def _get_property_windows(self, prop):
        r"""SUMMARY

        _get_property_window(prop)

        @Arguments:
        - `prop`:

        @Return:

        @Error:
        """
        rep = self.window.get_property(False, prop, 'WINDOW')
        if rep is None:
            return None
        return _unpack('I' * rep.value_len, _array('B', rep.value).tostring())

    def get_supporting_wm_id(self):
        """function get_supporting_wm_id

        returns int
        """
        wins = self._get_property_windows('_NET_SUPPORTING_WM_CHECK')
        if not wins:
            return None
        return wins[0]

    def get_active_window(self):
        """Return the window ID of the currently active window or None
        if no window has the focus.

        returns int
        """
        wins = self._get_property_windows('_NET_ACTIVE_WINDOW')
        if not wins:
            return None
        return wins[0]

    def client_list(self):
        """function client_list

        returns list
        """
        return self._get_property_windows('_NET_CLIENT_LIST')

    def client_list_stacking(self, ):
        r"""SUMMARY

        client_list_stacking()

        @Return:

        @Error:
        """
        return self._get_property_windows('_NET_CLIENT_LIST_STACKING')

    def get_current_desktop(self):
        """function get_current_desktop

        returns int
        """
        rep = self.window.get_property(False, '_NET_CURRENT_DESKTOP', 'CARDINAL')
        if rep is None:
            return None
        nums = _unpack('I' * rep.value_len, _array('B', rep.value).tostring())
        if not nums:
            return None
        return nums[0]

    def get_desktop_geometry(self):
        """function get_desktop_geometry

        returns
        """
        rep = self.window.get_property(False, '_NET_DESKTOP_GEOMETRY', 'CARDINAL')
        if rep is None:
            return Dimension()
        size = _unpack('I' * rep.value_len, _array('B', rep.value).tostring())
        if size < 2:
            return Dimension()
        return Dimension(size[0], size[1])

    def list_workarea(self):
        """function list_workarea

        returns Rectangle
        """
        rep = self.window.get_property(False, '_NET_WORKAREA', 'CARDINAL')
        if rep is None:
            return Rectangle(0, 0, 0, 0)
        rects = _unpack('I' * rep.value_len, _array('B', rep.value).tostring())
        if rects < 4:
            return Rectangle(0, 0, 0, 0)
        return [Rectangle(x, y, w, h) for x, y, w, h in zip(*[iter(rects)] * 4)]

    def get_viewport(self):
        """function get_viewport

        returns int
        """
        rep = self.window.get_property(False, '_NET_DESKTOP_VIEWPORT', 'CARDINAL')
        if rep is None:
            return None
        viewp = _unpack('I' * rep.value_len, _array('B', rep.value).tostring())
        if not viewp:
            return None
        return viewp[0]

    def list_desktop_names(self):
        """function list_desktop_names

        returns list
        """
        rep = self.window.get_property(False, '_NET_DESKTOP_NAMES', 'UTF8_STRING')
        names = str(rep.value.buf()).split('\x00')
        while '' in names:
            names.remove('')
        return names

    def get_number_of_desktop(self):
        """function get_number_of_desktop

        returns int
        """
        rep = self.window.get_property(
            False, '_NET_NUMBER_OF_DESKTOPS', 'CARDINAL')
        if rep is None:
            return None
        nums = _unpack('I' * rep.value_len, _array('B', rep.value).tostring())
        if not nums:
            return None
        return nums[0]

    def get_user_time(self, ):
        r"""SUMMARY

        get_user_time()

        @Return:

        @Error:
        """
        rep = self.window.get_property(
            False, '_NET_WM_USER_TIME', 'CARDINAL')
        if rep is None:
            return None
        nums = _unpack('I' * rep.value_len, _array('B', rep.value).tostring())
        if not nums:
            return None
        return nums[0]

    def move_cursor_to(self, newx, newy):
        r"""SUMMARY

        move_cursor_to(newx, newy)

        @Arguments:
        - `newx`:
        - `newy`:

        @Return:

        @Error:
        """
        return self.window.move_cursor_to(newx, newy)

    def get_attributes(self, ):
        r"""SUMMARY

        get_attributes()

        @Return:

        @Error:
        """
        return self.window.get_attributes()

    def add_attributes(self, value):
        r"""SUMMARY

        add_attributes(value)

        @Arguments:
        - `value`:

        @Return:

        @Error:
        """
        return self.window.add_attributes(value)

    def remove_attributes(self, value):
        r"""SUMMARY

        remove_attributes(value)

        @Arguments:
        - `value`:

        @Return:

        @Error:
        """
        return self.window.remove_attributes(value)

    def __int__(self):
        return self.id



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# root_window.py ends here
