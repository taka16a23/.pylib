#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _window_listener.py 348 2015-08-04 13:56:54Z t1 $
# $Revision: 348 $
# $Date: 2015-08-04 22:56:54 +0900 (Tue, 04 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-04 22:56:54 +0900 (Tue, 04 Aug 2015) $

r"""_window_listener -- DESCRIPTION

"""
from struct import unpack
from array import array
from observer import Observable

from xcb.xproto import (
    CW, EventMask,
    ConfigureNotifyEvent, DestroyNotifyEvent, PropertyNotifyEvent,
    KeyPressEvent, KeyReleaseEvent, )

from rectangle import Rectangle

from xahk.events.eventloop import EventLoop
from xahk.events.event_listener import EventListener
from xahk.events.event import KeyEvent
from xahk.events.event_target import EventTarget
from xahk.wm.atom_cache import AtomCache
from xahk.wm.window_client import WindowStateMode, WindowClient
from xahk.layout.layout_item import LayoutItem


KATOM_TO_CACHE_FOR_DESKTOP_WINDOW = ['ATOM',
                                     'WM_NAME',
                                     'WM_CLASS',
                                     '_NET_WM_NAME',
                                     '_NET_WM_STATE',
                                     '_NET_WM_PID',
                                     '_NET_WM_WINDOW_TYPE',
                                     '_NET_WM_STATE_FULLSCREEN',
                                     '_NET_WM_STATE_MAXIMIZED_VERT',
                                     '_NET_WM_STATE_MAXIMIZED_HORZ',
                                     '_NET_WM_STATE_HIDDEN',
                                     '_NET_WM_STATE_SHADED']


def find_window(event):
    r"""SUMMARY

    find_window(event)

    @Arguments:
    - `event`:

    @Return:

    @Error:
    """
    if isinstance(event, (KeyPressEvent, KeyReleaseEvent, )):
        return event.event
    return event.window


class WindowListener(EventTarget, EventListener, Observable, LayoutItem):
    """Class WindowListener
    """
    # Attributes:
    def __init__(self, display, window_id):
        r"""

        @Arguments:
        - `window`:
        """
        EventTarget.__init__(self)
        Observable.__init__(self)
        self.window = WindowClient(display, window_id)
        self._atom_cache = AtomCache(
            self.window.get_display(), KATOM_TO_CACHE_FOR_DESKTOP_WINDOW)
        self._prop_cache = {}
        # change attr
        reply = self.window.add_attributes(
            EventMask.StructureNotify|EventMask.PropertyChange)
        if not reply is None:
            reply.check()
        self._current_state = self._list_current_state()
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

    def can_dispatch_event(self, event):
        """function can_dispatch_event

        event:

        returns
        """
        return isinstance(event, (ConfigureNotifyEvent,
                                  PropertyNotifyEvent,
                                  DestroyNotifyEvent,
                                  KeyPressEvent, KeyReleaseEvent,
                                  )) and find_window(event) == self.id

    def handle_event(self, event):
        """function dispatch_event

        event:

        returns
        """
        if isinstance(event, (ConfigureNotifyEvent, )):
            # TODO: (Atami) [2015/07/21]
            # check other window manager
            # print([event.x - 4, event.y - 22, event.width, event.height])
            # print(self.window.get_bounds())
            # self._prop_cache['bounds'] = Rectangle(
                # event.x - 4, event.y - 22, event.width, event.height)
            # self._prop_cache['bounds'] = self.window.get_bounds()
            if 'bounds' in self._prop_cache:
                del self._prop_cache['bounds']
            self._notify_bounds_changed()
        elif isinstance(event, (DestroyNotifyEvent, )):
            EventLoop(self.display).remove_event_listener(self)
            self._notify_destroyed()
        elif isinstance(event, (PropertyNotifyEvent, )):
            self._dispatch_property_changed(event)
        elif isinstance(event, (KeyPressEvent, KeyReleaseEvent)):
            self._process_event(KeyEvent(event, self))

    def _process_event(self, event):
        r"""SUMMARY

        _process_event(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        for target in self.get_pretarget_handlers():
            target.on_event(event)
        if self._target_handlers is not None:
            self._target_handlers.on_event(event)
        for target in self.get_posttarget_handlers():
            target.on_event(event)

    def __int__(self):
        """function __int__

        returns
        """
        return self.id

    def __eq__(self, other):
        """function __eq__

        other:

        returns
        """
        if isinstance(other, (WindowListener, WindowClient)):
            return self.id == other.id
        return self.id == other

    def __ne__(self, other):
        """function __ne__

        other:

        returns
        """
        return not self == other

    def __repr__(self):
        return 'WindowListener(id={0.id}, wmclass={0.wmclass})'.format(self)

    def __hash__(self, ):
        return hash(self.id)

    def get_id(self, ):
        r"""SUMMARY

        get_id()

        @Return:

        @Error:
        """
        return int(self.window)

    id = property(get_id)

    def get_title(self):
        """function get_title

        returns
        """
        if 'title' not in self._prop_cache:
            self._prop_cache['title'] = self.window.get_title()
        return self._prop_cache['title']

    def set_title(self, title):
        """function set_title

        title:

        returns
        """
        self.window.set_title(title)

    title = property(get_title, set_title)

    def get_wmclass(self, ):
        r"""SUMMARY

        get_wmclass()

        @Return:

        @Error:
        """
        if 'wmclass' not in self._prop_cache:
            self._prop_cache['wmclass'] = self.window.get_wmclass()
        return self._prop_cache['wmclass']

    wmclass = property(get_wmclass)

    def get_pid(self):
        """function get_pid

        returns
        """
        if 'pid' not in self._prop_cache:
            self._prop_cache['pid'] = self.window.get_pid()
        return self._prop_cache['pid']

    pid = property(get_pid)

    def get_type(self):
        """function get_type

        returns
        """
        if 'type' not in self._prop_cache:
            self._prop_cache['type'] = self.window.get_type()
        return self._prop_cache['type']

    type = property(get_type)

    def get_bounds(self):
        """function get_bounds

        returns
        """
        # TODO: (Atami) [2015/07/21]
        # return self.window.get_bounds()
        if 'bounds' not in self._prop_cache:
            self._prop_cache['bounds'] = self.window.get_bounds()
        return self._prop_cache['bounds']

    def set_bounds(self, newx, newy, width, height):
        """function set_bounds

        returns
        """
        self.window.set_bounds(newx, newy, width, height)

    def layout(self, rect):
        r"""SUMMARY

        layout(rect)

        @Arguments:
        - `rect`:

        @Return:

        @Error:
        """
        self.set_bounds(rect.x, rect.y, rect.width, rect.height)

    def move(self, newx, newy):
        """function move

        point:

        returns
        """
        self.window.move(newx, newy)

    def set_size(self, width, height):
        """function set_size

        size:

        returns
        """
        self.window.set_size(width, height)

    def minimize(self):
        """function minimize

        returns
        """
        self.window.minimize()

    def is_minimized(self):
        """function is_minimized

        returns
        """
        return self.window.is_minimized()

    def show(self):
        """function show

        returns
        """
        self.window.show()

    def maximize(self, mode=WindowStateMode.Set):
        """function maximize

        returns
        """
        self.window.maximize(mode)

    def is_maximized(self):
        """function is_maximized

        returns
        """
        return self.window.is_maximized()

    def restore(self):
        """function restore

        returns
        """
        self.window.restore()

    def activate(self):
        """function activate

        returns
        """
        self.window.activate()

    def is_active(self):
        """function is_active

        returns
        """
        pass
        # return self.window.is_active()

    def deactivate(self):
        """function deactivate

        returns
        """
        self.window.deactivate()

    def set_always_on_top(self, mode=WindowStateMode.Set):
        """function set_always_on_top

        mode:

        returns
        """
        self.window.set_always_on_top(mode)

    def is_always_on_top(self):
        """function is_always_on_top

        returns
        """
        return self.window.is_always_on_top()

    def set_always_on_bottom(self, mode=WindowStateMode.Set):
        """function set_always_on_bottom

        mode:

        returns
        """
        self.window.set_always_on_bottom(mode)

    def is_always_on_bottom(self):
        """function is_always_on_bottom

        returns
        """
        return self.window.is_always_on_bottom()

    def set_fullscreen(self, mode=WindowStateMode.Set):
        """function set_fullscreen

        mode:

        returns
        """
        self.window.set_fullscreen(mode)

    def is_fullscreened(self):
        """function is_fullscreened

        returns
        """
        return self.window.is_fullscreened()

    def set_shade(self, mode=WindowStateMode.Set):
        """function set_shade

        mode:

        returns
        """
        self.window.set_shade(mode)

    def is_shaded(self):
        """function is_shaded

        returns
        """
        return self.window.is_shaded()

    def hide(self):
        """function hide

        returns
        """
        self.window.hide()

    def close(self):
        """function close

        returns
        """
        return self.window.close()

    def delete(self):
        """function delete

        returns
        """
        return self.window.delete()

    def destroy(self):
        """function destroy

        returns
        """
        return self.window.destroy()

    def move_cursor_to(self, newx, newy):
        """function move_cursor_to

        point:

        returns
        """
        return self.window.move_cursor_to(newx, newy)

    def get_cursor_point(self, ):
        r"""SUMMARY

        get_cursor_point()

        @Return:

        @Error:
        """
        return self.window.get_cursor_point()

    def raise_window(self):
        """function raise_window

        returns
        """
        return self.window.raise_window()

    def lower_window(self):
        """function lower_window

        returns
        """
        return self.window.lower_window()

    def get_workspace(self):
        """function get_desktop

        returns
        """
        return self.window.get_workspace()

    def change_workspace(self, num):
        """function change_desktop

        returns
        """
        return self.window.change_workspace(num)

    def grab_key(self, accelerator):
        r"""SUMMARY

        grab_key(owner_events, key, modifiers, pointer_mode, keyboard_mode)

        @Arguments:
        - `owner_events`:
        - `key`:
        - `modifiers`:
        - `pointer_mode`:
        - `keyboard_mode`:

        @Return:

        @Error:
        """
        return self.window.grab_key(accelerator)

    def grab_keys(self, accelerators):
        r"""SUMMARY

        grab_keys(targets)

        @Arguments:
        - `targets`:

        @Return:

        @Error:
        """
        return self.window.grab_keys(accelerators)

    def ungrab_key(self, accelerator):
        r"""SUMMARY

        ungrab_key(accelerator)

        @Arguments:
        - `accelerator`:

        @Return:

        @Error:
        """
        return self.window.ungrab_key(accelerator)

    def ungrab_keys(self, accelerators):
        r"""SUMMARY

        ungrab_keys(accelerators)

        @Arguments:
        - `accelerators`:

        @Return:

        @Error:
        """
        return self.window.ungrab_keys(accelerators)

    def grab_button(self, accelerator):
        r"""SUMMARY

        grab_button(accelerator)

        @Arguments:
        - `accelerator`:

        @Return:

        @Error:
        """
        return self.window.grab_button(accelerator)

    def grab_buttons(self, accelerators):
        r"""SUMMARY

        grab_buttons(accelerators)

        @Arguments:
        - `accelerators`:

        @Return:

        @Error:
        """
        return self.window.grab_buttons(accelerators)

    def ungrab_button(self, accelerator):
        r"""SUMMARY

        ungrab_button(accelerator)

        @Arguments:
        - `accelerator`:

        @Return:

        @Error:
        """
        return self.window.ungrab_button(accelerator)

    def ungrab_buttons(self, accelerators):
        r"""SUMMARY

        ungrab_butotns(accelerators)

        @Arguments:
        - `accelerators`:

        @Return:

        @Error:
        """
        return self.window.ungrab_buttons(accelerators)

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

    def _list_current_state(self):
        """function list_current_state

        returns
        """
        rep = self.window.get_property(False, '_NET_WM_STATE', 'ATOM')
        if rep is None:
            return set()
        return set(unpack('I' * rep.value_len, array('B', rep.value)))

    def _dispatch_property_changed(self, event):
        """function dispatch_property_changed

        event:

        returns
        """
        if event.atom == self._atom_cache.get_atom('_NET_WM_STATE'):
            self._notify_state_changed()
        elif event.atom == self._atom_cache.get_atom('WM_NAME'):
            self._prop_cache['title'] = self.window.get_title()
            self._notify_title_changed()
        elif event.atom == self._atom_cache.get_atom('WM_CLASS'):
            self._prop_cache['wmclass'] = self.window.get_wmclass()
        elif event.atom == self._atom_cache.get_atom('_NET_WM_PID'):
            self._prop_cache['pid'] = self.window.get_pid()
        elif event.atom == self._atom_cache.get_atom('_NET_WM_WINDOW_TYPE'):
            self._prop_cache['type'] = self.window.get_type()
        elif event.atom == self._atom_cache.get_atom('_NET_WM_NAME'):
            return

    def _notify_state_changed(self):
        """function notify_state_changed

        returns
        """
        states = self._list_current_state()
        added = states - self._current_state
        self._current_state = states
        if self._atom_cache.get_atom('_NET_WM_STATE_FULLSCREEN') in added:
            self._notify_fullscreened()
        elif (self._atom_cache.get_atom('_NET_WM_STATE_MAXIMIZED_VERT')
              in added
              and self._atom_cache.get_atom('_NET_WM_STATE_MAXIMIZED_HORZ')
              in added):
            self._notify_maximized()
        elif self._atom_cache.get_atom('_NET_WM_STATE_HIDDEN') in added:
            self._notify_minimized()
        elif self._atom_cache.get_atom('_NET_WM_STATE_SHADED') in added:
            self._notify_shaded()

    def _notify_title_changed(self, ):
        r"""SUMMARY

        _notify_title_changed()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_window_title_changed(self)

    def _notify_minimized(self):
        """function notify_minimized

        returns
        """
        for observer in self._observers:
            observer.on_window_minimized(self)

    def _notify_maximized(self):
        """function notify_maximized

        returns
        """
        for observer in self._observers:
            observer.on_window_maximized(self)

    def _notify_fullscreened(self):
        """function notify_fullscreened

        returns
        """
        for observer in self._observers:
            observer.on_window_fullscreened(self)

    def _notify_shaded(self):
        """function notify_shaded

        returns
        """
        for observer in self._observers:
            observer.on_window_shaded(self)

    def _notify_destroyed(self):
        """function notify_destroyed

        returns
        """
        for observer in self._observers:
            observer.on_window_destroyed(self.id)

    def _notify_bounds_changed(self):
        """function notify_bounds_changed

        returns
        """
        for observer in self._observers:
            observer.on_window_bounds_changed(self)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _window_listener.py ends here
