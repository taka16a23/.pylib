#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""window_manager -- DESCRIPTION

"""
from array import array
from struct import unpack, pack

from rectangle import Dimension, Rectangle
from observer import Observable
from xcb.xproto import BadWindow, BadDrawable
from xcb.xproto import EventMask, CW, PropertyNotifyEvent

from .x11.display import Display
from .x11.window import Window
from .x11.atom_cache import AtomCache
from .events.loop import EventLoop
from .events.listener import EventListener

from .desktop_window_factory import WindowFacroty


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


class WindowManager(EventListener, Observable):
    r"""WindowManager

    WindowManager is a object.
    Responsibility:
    """
    _instance = None

    @classmethod
    def get_instance(cls, display):
        if cls._instance is None:
            cls._instance = cls(display)
        return cls._instance

    def __init__(self, display):
        r"""

        @Arguments:
        - `display`:
        """
        Observable.__init__(self)
        self.display = display
        self.root = Window(self.display, self.display.get_setup().roots[0].root)
        attrs = self.root.get_attributes().reply()
        reply = self.root.change_attributes_checked(
            CW.EventMask, [EventMask.PropertyChange|attrs.your_event_mask])
        if reply is None:
            raise StandardError()
        reply.check()

        self._factory = WindowFacroty(self.display)
        self._atom_cache = None
        self._update_factory()
        EventLoop.get_instance(
            self.display).get_event_dispatcher().add_event_listener(self)

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self.display

    def _update_factory(self, ):
        r"""SUMMARY

        _update_facroty()

        @Return:

        @Error:
        """
        self._factory.clear()
        for win in self._get_property_windows('_NET_CLIENT_LIST_STACKING'):
            self._factory.get_or_create(win)

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

    def _get_property(self, delete, prop, types, offset=0, length=20):
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
        try:
            reply = self.root.get_property(
                delete, self._get_atom(prop), self._get_atom(types),
                offset, length).reply()
        except BadWindow as err:
            # from xahk.logger import LOG
            # LOG.error('{}, {}'.format(err, prop))
            # TODO: (Atami) [2015/06/02]
            import os
            os.system('modprobe pcspkr')
            os.system('/usr/bin/beep -f250 -r2 -l50')
            os.system('rmmod pcspkr')
            return None
        if reply.bytes_after:
            after_reply = self._get_property(
                delete, prop, types, length, reply.bytes_after) # recursive call
            if after_reply is None:
                return None
            reply.value += after_reply.value
            reply.value_len += after_reply.value_len
            reply.bytes_after = after_reply.bytes_after
            return reply
        return reply

    def _get_property_windows(self, prop):
        r"""SUMMARY

        _get_property_window(prop)

        @Arguments:
        - `prop`:

        @Return:

        @Error:
        """
        rep = self._get_property(False, prop, 'WINDOW')
        if rep is None:
            return None
        return unpack('I' * rep.value_len, array('B', rep.value).tostring())

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
        return self._factory.get_or_create(wins[0])

    def get_window(self, window_id):
        r"""SUMMARY

        get_window(window_id)

        @Arguments:
        - `window_id`:

        @Return:

        @Error:
        """
        if not self._factory.exists(window_id):
            return None
        return self._factory.get_or_create(window_id)

    def client_list(self):
        """function client_list

        returns list
        """
        return self._factory.list_windows()

    def get_current_desktop(self):
        """function get_current_desktop

        returns int
        """
        rep = self._get_property(False, '_NET_CURRENT_DESKTOP', 'CARDINAL')
        if rep is None:
            return None
        nums = unpack('I' * rep.value_len, array('B', rep.value).tostring())
        if not nums:
            return None
        return nums[0]

    def get_desktop_geometry(self):
        """function get_desktop_geometry

        returns
        """
        rep = self._get_property(False, '_NET_DESKTOP_GEOMETRY', 'CARDINAL')
        if rep is None:
            return Dimension()
        size = unpack('I' * rep.value_len, array('B', rep.value).tostring())
        if size < 2:
            return Dimension()
        return Dimension(size[0], size[1])

    def list_workarea(self):
        """function list_workarea

        returns Rectangle
        """
        rep = self._get_property(False, '_NET_WORKAREA', 'CARDINAL')
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
        rep = self._get_property(False, '_NET_DESKTOP_VIEWPORT', 'CARDINAL')
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
        rep = self._get_property(False, '_NET_DESKTOP_NAMES', 'UTF8_STRING')
        names = str(rep.value.buf()).split('\x00')
        while '' in names:
            names.remove('')
        return names

    def get_number_of_desktop(self):
        """function get_number_of_desktop

        returns int
        """
        rep = self._get_property(
            False, '_NET_NUMBER_OF_DESKTOPS', 'CARDINAL')
        if rep is None:
            return None
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
        rep = self._get_property(
            False, '_NET_WM_USER_TIME', 'CARDINAL')
        if rep is None:
            return None
        nums = unpack('I' * rep.value_len, array('B', rep.value).tostring())
        if not nums:
            return None
        return nums[0]

    def can_dispatch_event(self, event):
        """abstract method can_dispatch_event

        determine dispatchable event.

        event: X event

        returns bool
        """
        return isinstance(event, PropertyNotifyEvent) and self.root == event.window

    def handle_event(self, event):
        """abstract method handle_event

        event: X event
        """
        if event.atom == self._get_atom('_NET_CLIENT_LIST_STACKING'):
            self._on_changed_client_list()
        elif event.atom == self._get_atom('_NET_ACTIVE_WINDOW'):
            self._notify_changed_active_window()
        elif event.atom == self._get_atom('_NET_CURRENT_DESKTOP'):
            self._notify_changed_current_desktop()
        elif event.atom == self._get_atom('_NET_DESKTOP_NAMES'):
            self._notify_changed_desktop_names()
        elif event.atom == self._get_atom('_NET_DESKTOP_VIEWPORT'):
            self._notify_changed_viewport()
        elif event.atom == self._get_atom('_NET_WM_USER_TIME'):
            pass
        elif event.atom == self._get_atom('_NET_NUMBER_OF_DESKTOPS'):
            self._notify_changed_number_of_desktops()
        elif event.atom == self._get_atom('_NET_WORKAREA'):
            self._notify_changed_workarea()

    def _on_changed_client_list(self, ):
        r"""SUMMARY

        _on_changed_client_list()

        @Return:

        @Error:
        """
        windows = set(self._factory.list_windows())
        window_ids = set(self._get_property_windows('_NET_CLIENT_LIST'))
        for wid in list(window_ids - windows):
            window = self._factory.get_or_create(wid)
            self._notify_created_window(window)
        for wid in list(windows - window_ids):
            self._factory.remove(wid)
            self._notify_destroyed_window(wid)

    def _notify_created_window(self, window):
        r"""SUMMARY

        _notify_created_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_created_window(window)

    def _notify_destroyed_window(self, window_id):
        r"""SUMMARY

        _notify_destroyed_window(window_id)

        @Arguments:
        - `window_id`:

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_destroyed_window(window_id)

    def _notify_changed_active_window(self, ):
        r"""SUMMARY

        _notify_changed_active_window()

        @Return:

        @Error:
        """
        window = self.get_active_window()
        for observer in self._observers:
            observer.on_changed_active_window(window)

    def _notify_changed_current_desktop(self, ):
        r"""SUMMARY

        _notify_changed_current_desktop()

        @Return:

        @Error:
        """
        desktop = self.get_current_desktop()
        for observer in self._observers:
            observer.on_changed_current_desktop(desktop)

    def _notify_changed_desktop_names(self, ):
        r"""SUMMARY

        _notify_changed_desktop_names()

        @Return:

        @Error:
        """
        names = self.list_desktop_names()
        for observer in self._observers:
            observer.on_changed_desktop_names(names)

    def _notify_changed_viewport(self, ):
        r"""SUMMARY

        _notify_changed_viewport()

        @Return:

        @Error:
        """
        viewport = self.get_viewport()
        for observer in self._observers:
            observer.on_changed_viewport(viewport)

    def _notify_changed_number_of_desktops(self, ):
        r"""SUMMARY

        _notify_changed_number_of_desktops()

        @Return:

        @Error:
        """
        desktop_num = self.get_number_of_desktop()
        for observer in self._observers:
            observer.on_changed_number_of_desktops(desktop_num)

    def _notify_changed_workarea(self, ):
        r"""SUMMARY

        _notify_changed_workarea()

        @Return:

        @Error:
        """
        workareas = self.list_workarea()
        for observer in self._observers:
            observer.on_changed_workarea(workareas)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# window_manager.py ends here
