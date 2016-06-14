#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""root_widow -- DESCRIPTION

"""
from struct import unpack
from array import array

from observer import Observable
from rectangle import Dimension, Rectangle

from xcb.xproto import CW, EventMask, PropertyNotifyEvent

from xahk2.events.event_listener import EventListener
from xahk2.atom_cache import AtomCache
from xahk2.commons.display_multiton import multiton_display
from xahk2.window import Window
from xahk2.events.eventloop import EventLoop


ROOT_WINDOW_ATOMS = [
    '_NET_ACTIVE_WINDOW',
    '_NET_CLIENT_LIST',
    '_WIN_CLIENT_LIST',
    '_NET_CLIENT_LIST_STACKING',
    '_NET_CURRENT_DESKTOP',
    '_NET_DESKTOP_NAMES',
    '_NET_DESKTOP_VIEWPORT',
    '_NET_SUPPORTING_WM_CHECK',
    '_NET_WORKAREA',
    '_NET_DESKTOP_GEOMETRY',
    '_NET_NUMBER_OF_DESKTOPS',
    '_NET_WM_USER_TIME',
    '_WIN_WORKSPACE_COUNT',
    '_WIN_WORKSPACE',
    '_NET_WM_ICON',
    'WM_HINTS',
    'UTF8_STRING',
    # '_NET_WM_NAME',
    # 'WM_NAME',
    # 'STRING',
]


@multiton_display()
class RootWindow(EventListener, Observable):
    """Class RootWindow
    """
    # Attributes:
    def __init__(self, display):
        r"""

        @Arguments:
        - `display`:
        """
        Observable.__init__(self)
        self._atom_cache = AtomCache(display, ROOT_WINDOW_ATOMS)
        self._atom_cache.disallow_uncached_atoms() # for safety
        self.window = Window(display, display.get_setup().roots[0])
        attrs = self.window.get_attributes()
        if attrs is None:
            # TODO: (Atami) [2016/01/01]
            raise StandardError()
        self.window.change_attributes_checked(
            CW.EventMask,
            [attrs.your_event_mask|EventMask.PropertyChange]).check()
        # use in handle_event
        atom = self._atom_cache.get_atom
        self.__notifiers = {
            atom('_NET_CLIENT_LIST'): self._notify_clientlist_changed,
            atom('_NET_CLIENT_LIST_STACKING'): self._notify_clientlist_stacking_changed,
            atom('_NET_ACTIVE_WINDOW'): self._notify_active_window_changed,
            atom('_NET_CURRENT_DESKTOP'): self._notify_current_desktop_changed,
            atom('_NET_DESKTOP_NAMES'): self._notify_desktop_names_changed,
            atom('_NET_DESKTOP_VIEWPORT'): self._notify_viewport_changed,
            atom('_NET_WM_USER_TIME'): self._notify_wm_user_time_changed,
            atom('_NET_NUMBER_OF_DESKTOPS'): self._notify_number_of_desktops_changed,
            atom('_NET_WORKAREA'): self._notify_workarea_changed,
        }
        EventLoop(display).add_event_listener(self)

    # Operations
    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self.window.get_display()

    display = property(get_display)

    def get_id(self):
        """function get_id

        returns int
        """
        return self.window.get_id()

    id = property(get_id)

    def _get_property(self, prop, types, offset=0, length=20):
        r"""SUMMARY

        _get_property(prop, types, length)

        @Arguments:
        - `prop`:
        - `types`:
        - `length`:

        @Return:

        @Error:
        """
        rep = self.window.get_property(
            delete=False,
            property=self._atom_cache.get_atom(prop),
            type=self._atom_cache.get_atom(types),
            long_offset=offset,
            long_length=length)
        if rep.bytes_after:
            # recursive call
            after_rep = self._get_property(prop, types, length, rep.bytes_after)
            if after_rep is None:
                return None
            rep.value += after_rep.value
            rep.value_len += after_rep.value_len
            rep.bytes_after = after_rep.bytes_after
            return rep
        return rep

    def get_supporting_wm_id(self):
        """function get_supporting_wm_id

        returns int
        """
        rep = self._get_property(
            prop='_NET_SUPPORTING_WM_CHECK', types='WINDOW', offset=0, length=5)
        if rep is None:
            return None
        return unpack('I' * rep.value_len, array('B', rep.value).tostring())

    # def get_name(self):
    #     """function get_name

    #     returns str
    #     """
    #     window = Window(self.display, self.get_supporting_wm_id())
    #     return None # should raise NotImplementedError()

    def get_active_window(self):
        """function get_active_window

        returns int
        """
        rep = self._get_property(
            prop='_NET_ACTIVE_WINDOW', types='WINDOW', offset=0, length=1)
        if rep is None:
            return None
        wins = unpack('I' * rep.value_len, array('B', rep.value).tostring())
        if not wins:
            return None
        return int(wins[0])

    def get_current_desktop(self):
        """function get_current_desktop

        returns str
        """
        rep = self._get_property(
            prop='_NET_CURRENT_DESKTOP', types='CARDINAL', offset=0, length=10)
        if rep is None:
            return None
        nums = unpack('I' * rep.value_len, array('B', rep.value).tostring())
        if not nums:
            return None
        return nums[0]

    def client_list(self):
        """function client_list

        returns int
        """
        rep = self._get_property(
            prop='_NET_CLIENT_LIST', types='WINDOW', offset=0, length=20)
        if rep is None:
            return None
        return unpack('I' * rep.value_len, array('B', rep.value).tostring())

    def client_list_stacking(self):
        """function client_list_stacking

        returns list
        """
        rep = self._get_property(
            prop='_NET_CLIENT_LIST_STACKING', types='WINDOW', offset=0, length=20)
        if rep is None:
            return None
        return unpack('I' * rep.value_len, array('B', rep.value).tostring())

    def list_workarea(self):
        """function list_workarea

        returns list
        """
        rep = self._get_property(
            prop='_NET_WORKAREA', types='CARDINAL', offset=0, length=20)
        if rep is None:
            return Rectangle(0, 0, 0, 0)
        rects = unpack('I' * rep.value_len, array('B', rep.value).tostring())
        if rects < 4:
            return Rectangle(0, 0, 0, 0)
        return [Rectangle(x, y, w, h) for x, y, w, h in zip(*[iter(rects)] * 4)]

    def get_viewport(self):
        """function get_viewport

        returns int
        """
        rep = self._get_property(
            prop='_NET_DESKTOP_VIEWPORT', types='CARDINAL', offset=0, length=5)
        if rep is None:
            return None
        viewp = unpack('I' * rep.value_len, array('B', rep.value).tostring())
        if not viewp:
            return None
        return viewp[0]

    def list_desktop_names(self):
        """function list_desktop_names

        returns list
        """
        rep = self._get_property(
            prop='_NET_DESKTOP_NAMES', types='UTF8_STRING', offset=0, length=30)
        names = str(rep.value.buf()).split('\x00')
        while '' in names:
            names.remove('')
        return names

    def get_desktop_geometry(self):
        """function get_desktop_geometry

        returns Rectangle
        """
        rep = self._get_property(
            prop='_NET_DESKTOP_GEOMETRY', types='CARDINAL', offset=0, length=20)
        if rep is None:
            return Dimension()
        size = unpack('I' * rep.value_len, array('B', rep.value).tostring())
        if size < 2:
            return Dimension()
        return Dimension(size[0], size[1])

    def get_number_of_desktop(self):
        """function get_number_of_desktop

        returns int
        """
        rep = self._get_property(
            prop='_NET_NUMBER_OF_DESKTOPS', types='CARDINAL', offset=0, length=20)
        if rep is None:
            return None
        nums = unpack('I' * rep.value_len, array('B', rep.value).tostring())
        if not nums:
            return None
        return nums[0]

    def get_user_time(self):
        """function get_user_time

        returns int
        """
        rep = self._get_property(
            prop='_NET_WM_USER_TIME', types='CARDINAL', offset=0, length=20)
        if rep is None:
            return None
        nums = unpack('I' * rep.value_len, array('B', rep.value).tostring())
        if not nums:
            return None
        return nums[0]

    def can_accept_event(self, event):
        r"""SUMMARY

        can_accept_event(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        return isinstance(event, PropertyNotifyEvent) and event.window == self.id

    def handle_event(self, event):
        r"""SUMMARY

        handle_event(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        if event.atom in self.__notifiers:
            self.__notifiers[event.atom]()

    def _notify_active_window_changed(self, ):
        r"""SUMMARY

        _notify_active_window_changed()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_active_window_changed(self)

    def _notify_clientlist_changed(self, ):
        r"""SUMMARY

        _notify_clientlist_changed()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_clientlist_changed(self)

    def _notify_clientlist_stacking_changed(self, ):
        r"""SUMMARY

        _notify_clientlist_stacking_changed()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_clientlist_stacking_changed(self)

    def _notify_current_desktop_changed(self, ):
        r"""SUMMARY

        _notify_current_desktop_changed()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_current_desktop_changed(self)

    def _notify_desktop_names_changed(self, ):
        r"""SUMMARY

        _notify_desktop_names_changed()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_desktop_names_changed(self)

    def _notify_viewport_changed(self, ):
        r"""SUMMARY

        _notify_viewport_changed()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_viewport_changed(self)

    def _notify_wm_user_time_changed(self, ):
        r"""SUMMARY

        _notify_wm_user_time_changed()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_wm_user_time_changed(self)

    def _notify_number_of_desktops_changed(self, ):
        r"""SUMMARY

        _notify_number_of_desktops_changed()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_number_of_desktops_changed(self)

    def _notify_workarea_changed(self, ):
        r"""SUMMARY

        _notify_workarea_changed()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_workarea_changed(self)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# root_widow.py ends here
