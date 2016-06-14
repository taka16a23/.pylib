#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""root_window_listener -- DESCRIPTION

timeit wm.get_viewport()
10000 loops, best of 3: 116 µs per loop

get_atom=wm.root._atom_cache.get_atom
prop_cache={}
prop_cache[get_atom('_NET_DESKTOP_VIEWPORT')]=0
timeit prop_cache[get_atom('_NET_DESKTOP_VIEWPORT')]
1000000 loops, best of 3: 1.04 µs per loop



from xahk.eventloop import EventLoop
from xahk.desktop_root_window import DesktopRootWindow
from xahk.desktop_root_window_observer import DesktopRootWindowObserver
from xahk.wm.display import get_display


class DebugDesktopRootWindowObserver(DesktopRootWindowObserver):
    def on_changed_active_window(self, root_window):
        print('DEBUG-1-2015-07-14-173547.junk.py')
        print(root_window.get_active_window())

    def on_changed_client_list(self, root_window):
        print('DEBUG-2-2015-07-14-173547.junk.py')
        print(root_window.client_list())

    def on_changed_client_list_stacking(self, root_window):
        print('DEBUG-6-2015-07-14-173547.junk.py')
        print(root_window.client_list_stacking())

    def on_changed_current_desktop(self, root_window):
        print('DEBUG-3-2015-07-14-173547.junk.py')
        print(root_window.get_current_desktop())

    def on_changed_desktop_names(self, root_window):
        print('DEBUG-4-2015-07-14-173547.junk.py')
        print(root_window.list_desktop_names())

    def on_changed_viewport(self, root_window):
        print('DEBUG-5-2015-07-14-173547.junk.py')
        print(root_window.get_viewport())


d = DesktopRootWindow(get_display())
d.add_observer(DebugDesktopRootWindowObserver())

EventLoop(get_display()).start_loop()
"""
from xcb.xproto import EventMask, PropertyNotifyEvent

from observer import Observable

from xahk.commons.display_multiton import multiton_display
from xahk.events.eventloop import EventLoop
from xahk.events.event_listener import EventListener
from xahk.wm.root_window import RootWindow
from xahk.wm.atom_cache import AtomCache
from xahk.wm.window_client import WindowClient


KATOM_TO_CACHE_FOR_DESKTOP_ROOT_WINDOW = [
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
    ]


@multiton_display()
class RootWindowListener(Observable, EventListener):
    """Class RootWindowListener
    """
    # Attributes:
    def __init__(self, display):
        r"""

        @Arguments:
        - `display`:
        """
        Observable.__init__(self)
        self._root = RootWindow(display)
        self._atom_cache = AtomCache(
            display, KATOM_TO_CACHE_FOR_DESKTOP_ROOT_WINDOW)
        self._atom_cache.disallow_uncached_atoms()
        self._prop_cache = {}
        self._set_cache('_NET_ACTIVE_WINDOW', self._root.get_active_window())
        self._set_cache('_NET_CLIENT_LIST', self._root.client_list())
        self._set_cache('_NET_CLIENT_LIST_STACKING',
                        self._root.client_list_stacking())
        self._set_cache('_NET_CURRENT_DESKTOP',
                        self._root.get_current_desktop())
        self._set_cache('_NET_DESKTOP_NAMES', self._root.list_desktop_names())
        self._set_cache('_NET_DESKTOP_VIEWPORT', self._root.get_viewport())
        self._set_cache('_NET_WM_USER_TIME', self._root.get_user_time())
        self._set_cache('_NET_SUPPORTING_WM_CHECK',
                        self._root.get_supporting_wm_id())
        self._set_cache('_NET_WORKAREA', self._root.list_workarea())
        self._set_cache('_NET_DESKTOP_GEOMETRY',
                        self._root.get_desktop_geometry())
        self._set_cache('_NET_NUMBER_OF_DESKTOPS',
                        self._root.get_number_of_desktop())
        reply = self._root.add_attributes(EventMask.PropertyChange)
        if reply is None:
            raise StandardError()
        reply.check()
        EventLoop(self.display).add_event_listener(self)

    # Operations
    def _get_atom(self, prop):
        r"""SUMMARY

        _get_atom(prop)

        @Arguments:
        - `prop`:

        @Return:

        @Error:
        """
        return self._atom_cache.get_atom(prop)

    def _get_cache(self, prop, default=None):
        r"""SUMMARY

        _get_cache(prop)

        @Arguments:
        - `prop`:

        @Return:

        @Error:
        """
        return self._prop_cache.get(self._get_atom(prop), default)

    def _set_cache(self, prop, value):
        r"""SUMMARY

        _set_cache(prop, value)

        @Arguments:
        - `prop`:
        - `value`:

        @Return:

        @Error:
        """
        self._prop_cache[self._get_atom(prop)] = value

    def get_display(self):
        """function get_display

        returns
        """
        return self._root.get_display()

    display = property(get_display)

    def get_id(self):
        """function get_id

        returns
        """
        return self._root.get_id()

    id = property(get_id)

    def get_supporting_wm_id(self):
        """function get_supporting_wm_id

        returns
        """
        return self._get_cache('_NET_SUPPORTING_WM_CHECK')

    def get_name(self, ):
        r"""SUMMARY

        get_name()

        @Return:

        @Error:
        """
        window = WindowClient(self.display, self.get_supporting_wm_id())
        return window.get_title()

    def get_active_window(self):
        """function get_active_window

        returns
        """
        return self._get_cache('_NET_ACTIVE_WINDOW')

    def get_current_desktop(self):
        """function get_current_desktop

        returns
        """
        return self._get_cache('_NET_CURRENT_DESKTOP')

    def client_list(self):
        """function client_list

        returns
        """
        return self._get_cache('_NET_CLIENT_LIST')

    def client_list_stacking(self):
        """function client_list_stacking

        returns
        """
        return self._get_cache('_NET_CLIENT_LIST_STACKING')

    def list_workarea(self):
        """function get_workarea

        returns Rectangle
        """
        return self._get_cache('_NET_WORKAREA')

    def get_viewport(self):
        """function get_viewport

        returns int
        """
        return self._get_cache('_NET_DESKTOP_VIEWPORT')

    def list_desktop_names(self):
        """function list_desktop_names

        returns list
        """
        return self._get_cache('_NET_DESKTOP_NAMES')

    def get_desktop_geometry(self):
        """function get_desktop_geometry

        returns Dimension
        """
        return self._get_cache('_NET_DESKTOP_GEOMETRY')

    def get_number_of_desktop(self):
        """function get_number_of_desktop

        returns int
        """
        return self._get_cache('_NET_NUMBER_OF_DESKTOPS')

    def get_user_time(self, ):
        r"""SUMMARY

        get_user_time()

        @Return:

        @Error:
        """
        return self._get_cache('_NET_WM_USER_TIME')

    def can_dispatch_event(self, event):
        """function can_dispatch_evnet

        event:

        returns
        """
        return (isinstance(event, (PropertyNotifyEvent, ))
                and event.window == self.id)

    def handle_event(self, event):
        """function dispatch_event

        event:

        returns
        """
        if event.atom == self._get_atom('_NET_CLIENT_LIST'):
            self._set_cache('_NET_CLIENT_LIST', self._root.client_list())
            self._notify_changed_client_list()
        elif event.atom == self._get_atom('_NET_CLIENT_LIST_STACKING'):
            self._set_cache(
                '_NET_CLIENT_LIST_STACKING', self._root.client_list_stacking())
            self._notify_changed_client_list_stacking()
        elif event.atom == self._get_atom('_NET_ACTIVE_WINDOW'):
            window = self._root.get_active_window()
            if window in (0, None, self._get_cache('_NET_ACTIVE_WINDOW')):
                return
            self._set_cache('_NET_ACTIVE_WINDOW', window)
            self._notify_changed_active_window()
        elif event.atom == self._get_atom('_NET_CURRENT_DESKTOP'):
            self._set_cache(
                '_NET_CURRENT_DESKTOP', self._root.get_current_desktop())
            self._notify_changed_current_desktop()
        elif event.atom == self._get_atom('_NET_DESKTOP_NAMES'):
            self._set_cache('_NET_DESKTOP_NAMES', self._root.list_desktop_names())
            self._notify_changed_desktop_names()
        elif event.atom == self._get_atom('_NET_DESKTOP_VIEWPORT'):
            self._set_cache('_NET_DESKTOP_VIEWPORT', self._root.get_viewport())
            self._notify_changed_viewport()
        elif event.atom == self._get_atom('_NET_WM_USER_TIME'):
            self._set_cache('_NET_WM_USER_TIME', self._root.get_user_time())
            print('DEBUG-8-root_window_listener.py')
            print(self._get_cache('_NET_WM_USER_TIME'))
        elif event.atom == self._get_atom('_NET_NUMBER_OF_DESKTOPS'):
            self._set_cache('_NET_NUMBER_OF_DESKTOPS',
                            self._root.get_number_of_desktop())
        elif event.atom == self._get_atom('_NET_WORKAREA'):
            self._set_cache('_NET_WORKAREA', self._root.list_workarea())
        elif event.atom in (self._get_atom('_WIN_CLIENT_LIST'),
                            self._get_atom('_WIN_WORKSPACE_COUNT'),
                            self._get_atom('_WIN_WORKSPACE'),
                            self._get_atom('_NET_WM_ICON'),
                            self._get_atom('WM_HINTS')):
            return
        else:
            # debug
            print('DEBUG-9-root_window_listener.py')
            import os
            print(event.atom)
            os.system('modprobe pcspkr')
            os.system('/usr/bin/beep -f 100 -l 350')
            os.system('rmmod pcspkr')

    def _notify_changed_active_window(self):
        """function notify_changed_active_window

        returns
        """
        for observer in self._observers:
            observer.on_changed_active_window(self)

    def _notify_changed_client_list(self):
        """function notify_changed_client_list

        returns
        """
        for observer in self._observers:
            observer.on_changed_client_list(self)

    def _notify_changed_client_list_stacking(self):
        """function notify_changed_client_list_stacking

        returns
        """
        for observer in self._observers:
            observer.on_changed_client_list_stacking(self)

    def _notify_changed_current_desktop(self):
        """function notify_changed_current_desktop

        returns
        """
        for observer in self._observers:
            observer.on_changed_current_desktop(self)

    def _notify_changed_desktop_names(self):
        """function notify_changed_desktop_names

        returns
        """
        for observer in self._observers:
            observer.on_changed_desktop_names(self)

    def _notify_changed_viewport(self, ):
        r"""SUMMARY

        _notify_changed_viewport()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_changed_viewport(self)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# root_window_listener.py ends here
