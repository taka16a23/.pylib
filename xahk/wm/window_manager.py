#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""window_manager -- DESCRIPTION

"""
from array import array
from struct import unpack

from xcb.xproto import BadWindow
from xcb import xinerama

from xahk.rectangle import Size, Rectangle
from xahk.x11.window import Window
from xahk.x11.atom_cache import AtomCache
from xahk.x11.display import Display
from .client import WindowClient
from xahk.x11.request.get_full_property import GetFullProperty


KATOM_TO_CACHE_FOR_ROOT = [
    'ATOM',
    'CARDINAL',
    'STRING',
    'UTF8_STRING',
    'WINDOW',
    '_NET_SUPPORTING_WM_CHECK',
    '_NET_ACTIVE_WINDOW',
    '_NET_CLIENT_LIST',
    '_NET_CLIENT_LIST_STACKING',
    '_NET_CURRENT_DESKTOP',
    '_NET_DESKTOP_GEOMETRY',
    '_NET_WORKAREA',
    '_NET_DESKTOP_VIEWPORT',
    '_NET_DESKTOP_NAMES',
    '_NET_NUMBER_OF_DESKTOPS',
    '_NET_WM_USER_TIME',
    ]


class WindowManager(object):
    r"""WindowManager

    WindowManager is a object.
    Responsibility:
    """
    def __init__(self, ):
        r"""

        @Arguments:
        - `display`:
        """
        self.display = Display()
        self.root = Window(self.display, self.display.get_setup().roots[0].root)
        self._atom_cache = None # lazy load

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self.display

    def _get_atom(self, name):
        r"""SUMMARY

        _get_atom(name)

        @Arguments:
        - `name`:

        razy load

        @Return:

        @Error:
        """
        if self._atom_cache is None:
            self._atom_cache = AtomCache(self.display, KATOM_TO_CACHE_FOR_ROOT)
        return self._atom_cache.get_atom(name)

    def _get_property(self, prop, types, length):
        r"""SUMMARY

        get_property(delete, prop, types, offset=0, length=20)

        @Arguments:
        - `delete`:
        - `prop`:
        - `types`:
        - `offset`:
        - `length`:

        @Return:

        @Error:
        """
        requestor = GetFullProperty.Builder(
            self.display, self.root.id, self._get_atom(prop),
            self._get_atom(types)).set_length(length).build()
        return requestor.request().reply()

    def _get_property_windows(self, prop, length):
        r"""SUMMARY

        _get_property_window(prop)

        @Arguments:
        - `prop`:

        @Return:

        @Error:
        """
        rep = self._get_property(prop, 'WINDOW', length)
        return unpack('I' * rep.value_len, array('B', rep.value).tostring())

    def get_supporting_wm_id(self):
        """function get_supporting_wm_id

        returns int
        """
        wins = self._get_property_windows('_NET_SUPPORTING_WM_CHECK', 1)
        if not wins:
            return None
        return wins[0]

    def _create_client(self, wid):
        """SUMMARY

        _create_client(wid)

        @Arguments:
        - `wid`:

        @Return:

        @Error:
        """
        return WindowClient(Window(self.display, wid))

    def get_active_window(self):
        """Return the window ID of the currently active window or None
        if no window has the focus.

        returns int
        """
        wins = self._get_property_windows('_NET_ACTIVE_WINDOW', 1)
        if not wins:
            return None
        return self._create_client(wins[0])

    def client_list(self):
        """function client_list

        returns list
        """
        return [self._create_client(i)
                for i in self._get_property_windows('_NET_CLIENT_LIST', 20)]

    def client_list_stacking(self, ):
        r"""SUMMARY

        client_list_stacking()

        @Return:

        @Error:
        """
        return [self._create_client(i)
                for i in self._get_property_windows('_NET_CLIENT_LIST_STACKING', 20)]

    def get_current_desktop(self):
        """function get_current_desktop

        returns int
        """
        rep = self._get_property('_NET_CURRENT_DESKTOP', 'CARDINAL', 1)
        nums = unpack('I' * rep.value_len, array('B', rep.value).tostring())
        if not nums:
            return None
        return nums[0]

    def get_desktop_geometry(self):
        """function get_desktop_geometry

        returns
        """
        rep = self._get_property('_NET_DESKTOP_GEOMETRY', 'CARDINAL', 2)
        size = unpack('I' * rep.value_len, array('B', rep.value).tostring())
        if size < 2:
            return Size()
        return Size(size[0], size[1])

    def list_workarea(self):
        """function list_workarea

        returns Rectangle
        """
        rep = self._get_property('_NET_WORKAREA', 'CARDINAL', 1)
        rects = unpack('I' * rep.value_len, array('B', rep.value).tostring())
        if rects < 4:
            return Rectangle.Builder(0, 0, 0, 0).build()
        return [Rectangle.Builder(x, y, w, h).build()
                for x, y, w, h in zip(*[iter(rects)] * 4)]

    def get_viewport(self):
        """function get_viewport

        returns int
        """
        rep = self._get_property('_NET_DESKTOP_VIEWPORT', 'CARDINAL', 1)
        viewp = unpack('I' * rep.value_len, array('B', rep.value).tostring())
        if not viewp:
            return None
        return viewp[0]

    def list_desktop_names(self):
        """function list_desktop_names

        returns list
        """
        rep = self._get_property('_NET_DESKTOP_NAMES', 'UTF8_STRING', 30)
        names = str(rep.value.buf()).split('\x00')
        while '' in names:
            names.remove('')
        return names

    def get_number_of_desktop(self):
        """function get_number_of_desktop

        returns int
        """
        rep = self._get_property('_NET_NUMBER_OF_DESKTOPS', 'CARDINAL', 1)
        nums = unpack('I' * rep.value_len, array('B', rep.value).tostring())
        if not nums:
            return None
        return nums[0]

    def get_user_time(self, ):
        r"""SUMMARY

        get_user_time()

        @Return:

        @Error:
        """
        rep = self._get_property('_NET_WM_USER_TIME', 'CARDINAL', 1)
        nums = unpack('I' * rep.value_len, array('B', rep.value).tostring())
        if not nums:
            return None
        return nums[0]

    def list_screens(self, ):
        r"""SUMMARY

        list_screens()

        @Return:

        @Error:
        """
        xnrm = self.display(xinerama.key)
        screens = xnrm.QueryScreens().reply().screen_info
        return [Rectangle.Builder(x.x_org, x.y_org, x.width, x.height).build()
                for x in screens]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# window_manager.py ends here
