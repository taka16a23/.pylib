#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""window_client -- DESCRIPTION

"""
from enum import IntEnum
from peak.rules import dispatch
from cStringIO import StringIO
from array import array
from struct import pack, unpack

from rectangle import Rectangle, Point, Dimension
from xcb.xproto import ConfigWindow, EventMask
from xcb.xproto import BadWindow, BadDrawable, BadValue, BadMatch

from observer import Observable
from xahk2.events.event_listener import EventListener
from xahk2.atom_cache import AtomCache
from xahk2.eventcode import EventCode


WINDOW_ATOMS = [
    'ATOM',
    'CARDINAL',
    'STRING',
    'UTF8_STRING',
    'WINDOW',
    'WM_NAME',
    'WM_CLASS',
    'WM_CHANGE_STATE',
    'WM_DELETE_WINDOW',
    'WM_PROTOCOLS',
    '_NET_WM_NAME',
    '_NET_WM_PID',
    '_NET_WM_WINDOW_TYPE',
    '_NET_WM_STATE',
    '_NET_WM_STATE_HIDDEN',
    '_NET_WM_STATE_MAXIMIZED_VERT',
    '_NET_WM_STATE_MAXIMIZED_HORZ',
    '_NET_WM_STATE_ABOVE',
    '_NET_WM_STATE_BELOW',
    '_NET_WM_STATE_FULLSCREEN',
    '_NET_WM_STATE_SHADED',
    '_NET_WM_DESKTOP',
    '_NET_WM_USER_TIME',
    '_NET_ACTIVE_WINDOW',
    '_NET_CLOSE_WINDOW',
    '_NET_SUPPORTING_WM_CHECK',
    '_NET_CLIENT_LIST',
    '_NET_CLIENT_LIST_STACKING',
    '_NET_CURRENT_DESKTOP',
    '_NET_DESKTOP_GEOMETRY',
    '_NET_WORKAREA',
    '_NET_DESKTOP_NAMES',
    '_NET_DESKTOP_VIEWPORT',
    '_NET_NUMBER_OF_DESKTOPS',
    '_NET_WM_PING',
    ]


class WindowStateMode(IntEnum):
    r"""SUMMARY
    """
    Unset  = 0
    Set    = 1
    Toggle = 2


class ChangingWindowState(IntEnum):
    r"""ChangingWindowState

    ChangingWindowState is a _IntEnum.
    Responsibility:
    """
    WITHDRAWN_STATE = 0
    NORMAL_STATE = 1
    ZOOM_STATE = 2
    ICONIC_STATE = 3
    INACTIVE_STATE = 4


class WindowClient(EventListener, Observable):
    """Class WindowClient
    """
    # Attributes:
    def __init__(self, window):
        r"""

        @Arguments:
        - `window`:
        """
        Observable.__init__(self)
        self.window = window
        self._atom_cache = AtomCache(window.get_display(), WINDOW_ATOMS)
        self._root = None

    # Operations
    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self.window.get_display()

    display = property(get_display)

    @property
    def root(self, ):
        r"""SUMMARY

        root()

        @Return:

        @Error:
        """
        if self._root:
            return self._root
        self._root = self.display.get_setup().roots[0].root
        return self._root

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

    def get_id(self, ):
        r"""SUMMARY

        get_id()

        @Return:

        @Error:
        """
        return self.window.get_id()

    id = property(get_id)

    def get_pid(self, ):
        r"""SUMMARY

        get_pid()

        @Return:

        @Error:
        """
        return

    pid = property(get_pid)

    def get_type(self, ):
        r"""SUMMARY

        get_type()

        @Return:

        @Error:
        """
        return

    type = property(get_type)

    def get_title(self):
        """function get_title

        returns str
        """
        rep = self._get_property('_NET_WM_NAME', 'UTF8_STRING')
        if rep is None:
            return ''
        title = str(array('B', rep.value).tostring())
        if title != '':
            return title
        rep = self._get_property('WM_NAME', 'STRING')
        if rep is None:
            return ''
        return str(array('B', rep.value).tostring())

    def set_title(self, title):
        """function set_title

        title: str

        returns None
        """
        return self.window.change_property(title)

    title = property(get_title, set_title)

    def get_wmclass(self):
        """function get_wmclass

        returns WMClass
        """
        rep = self._get_property('WM_CLASS', 'STRING')
        if rep is None:
            return WMClass('', '')
        wmclasses = str(array('B', rep.value).tostring()).split('\x00')
        while '' in wmclasses:
            wmclasses.remove('')
        while len(wmclasses) < 2:
            wmclasses.append('')
        return WMClass(wmclasses[0], wmclasses[1])

    def get_bounds(self):
        """function get_bounds

        returns Rectangle
        """
        try:
            geo = self.window.get_geometry_unchecked().reply()
        except BadDrawable as err:
            # TODO: (Atami) [2016/01/04]
            print('DEBUG-1-window_client.py')
            return Rectangle(0, 0, 0, 0)
        root = self.display.get_setup().roots[0].root
        try:
            cood = self.window.translate_coordinates(
                root, geo.x, geo.y).reply()
        except BadWindow as err:
            # TODO: (Atami) [2016/01/04]
            print('DEBUG-2-window_client.py')
            return Rectangle(geo.x, geo.y, geo.width, geo.height)
        newx = cood.dst_x - (2 * geo.x)
        newy = cood.dst_y - (2 * geo.y)
        return Rectangle(newx, newy, geo.width, geo.height)

    @dispatch.generic()
    def set_bounds(self, newx, newy=0, width=0, height=0):
        r"""SUMMARY

        set_bounds(newx, newy=0, width=0, height=0)

        @Arguments:
        - `newx`:
        - `newy`:
        - `width`:
        - `height`:

        @Return:

        @Error:
        """

    @set_bounds.when('isinstance(newx, Rectangle)')
    def _set_bounds_rectangle(self, newx, newy=0, width=0, height=0):
        """function set_bounds

        rectangle: Rectangle

        returns None
        """
        cookie = self.window.configure_checked(
            ConfigWindow.X|ConfigWindow.Y|ConfigWindow.Width|ConfigWindow.Height,
            [newx.x, newx.y, newx.width, newx.height])
        try:
            cookie.check()
        except (BadWindow, BadMatch) as err:
            return False
        except BadValue as err:
            # TODO: (Atami) [2016/01/04]
            raise StandardError()

    @set_bounds.when('isinstance(newx, int)')
    def _set_bounds_int(self, newx, newy=0, width=0, height=0):
        """function set_bounds

        newx: int
        newy: int
        width: int
        height: int

        returns None
        """
        cookie = self.window.configure_checked(
            ConfigWindow.X|ConfigWindow.Y|ConfigWindow.Width|ConfigWindow.Height,
            [newx, newy, width, height])
        try:
            cookie.check()
        except (BadWindow, BadMatch) as err:
            return False
        except BadValue as err:
            # TODO: (Atami) [2016/01/04]
            raise StandardError()

    def get_point(self):
        """function get_point

        returns Point
        """
        return self.get_bounds().get_location()

    @dispatch.generic()
    def set_point(self, newx, newy=0):
        r"""SUMMARY

        set_point(newx, newy=0)

        @Arguments:
        - `newx`:
        - `newy`:

        @Return:

        @Error:
        """

    @set_point.when('isinstance(point, Point)')
    def _set_point_point(self, newx, newy=0):
        """function set_point

        point: Point

        returns None
        """
        point = newx
        cookie = self.window.configure_checked(
            ConfigWindow.X|ConfigWindow.Y, [point.x, point.y])
        try:
            cookie.check()
        except (BadWindow, BadMatch) as err:
            return False
        except BadValue as err:
            # TODO: (Atami) [2016/01/04]
            raise StandardError()

    @set_point.when('isinsstance(new, int)')
    def _set_point_int(self, newx, newy=0):
        """function set_point

        newx: int
        newy: int

        returns None
        """
        cookie = self.window.configure_checked(
            ConfigWindow.X|ConfigWindow.Y, [newx, newy])
        try:
            cookie.check()
        except (BadWindow, BadMatch) as err:
            return False
        except BadValue as err:
            # TODO: (Atami) [2016/01/04]
            raise StandardError()

    def get_size(self):
        """function get_size

        returns Dimension
        """
        return self.get_bounds().get_size()

    @dispatch.generic()
    def set_size(self, width, height=0):
        r"""SUMMARY

        set_size(width, height=0)

        @Arguments:
        - `width`:
        - `height`:

        @Return:

        @Error:
        """

    @set_size.when('isinstance(width, Dimension)')
    def set_size(self, width, height=0):
        """function set_size

        size: Dimension

        returns None
        """
        size = width
        cookie = self.window.configure_checked(
            ConfigWindow.Width|ConfigWindow.Height, [size.width, size.height])
        try:
            cookie.check()
        except (BadWindow, BadMatch) as err:
            return False
        except BadValue as err:
            # TODO: (Atami) [2016/01/04]
            raise StandardError()

    @set_size.when('isinstance(width, int)')
    def set_size(self, width, height=0):
        """function set_size

        width: int
        height: int

        returns None
        """
        cookie = self.window.configure_checked(
            ConfigWindow.Width|ConfigWindow.Height, [width, height])
        try:
            cookie.check()
        except (BadWindow, BadMatch) as err:
            return False
        except BadValue as err:
            # TODO: (Atami) [2016/01/04]
            raise StandardError()

    def _send_client_message(self, mask, types, data):
        r"""SUMMARY

        _send_client_message(mask, types, data)

        @Arguments:
        - `mask`:
        - `types`:
        - `data`:

        @Return: Cookie

        @Error:
        """
        event = StringIO()
        event.write(pack('BBHII', EventCode.ClientMessage, 32, 0, self.id, types))
        event.write(pack('I' * len(data), *data))
        return self.window.send_event_checked(True, mask, event.getvalue())

    def _list_wm_state(self, ):
        r"""SUMMARY

        _list_wm_state()

        @Return:

        @Error:
        """
        rep = self._get_property('_NET_WM_STATE', 'ATOM')
        if rep is None:
            return []
        return unpack('I' * rep.value_len, array('B', rep.value).tostring())

    def minimize(self):
        """function minimize

        returns None
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect|EventMask.SubstructureNotify,
            self._atom_cache.get_atom('WM_CHANGE_STATE'),
            [ChangingWindowState.ICONIC_STATE, 0, 0, 0, 0])

    def is_minimized(self):
        """function is_minimized

        returns bool
        """
        return (self._atom_cache.get_atom('_NET_WM_STATE_HIDDEN')
                in self._list_wm_state())

    def maximize(self):
        """function maximize

        returns None
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._atom_cache.get_atom('_NET_WM_STATE'),
            [WindowStateMode.Set,
             self._atom_cache.get_atom('_NET_WM_STATE_MAXIMIZED_VERT'),
             self._atom_cache.get_atom('_NET_WM_STATE_MAXIMIZED_HORZ'), 0, 0])

    def unset_maximize(self, ):
        r"""SUMMARY

        unset_maximize()

        @Return:

        @Error:
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._atom_cache.get_atom('_NET_WM_STATE'),
            [WindowStateMode.Unset,
             self._atom_cache.get_atom('_NET_WM_STATE_MAXIMIZED_VERT'),
             self._atom_cache.get_atom('_NET_WM_STATE_MAXIMIZED_HORZ'), 0, 0])

    def is_maximized(self):
        """function is_maximized

        returns bool
        """
        atoms = self._list_wm_state()
        if self._atom_cache.get_atom('_NET_WM_STATE_MAXIMIZED_VERT') not in atoms:
            return False
        if self._atom_cache.get_atom('_NET_WM_STATE_MAXIMIZED_HORZ') not in atoms:
            return False
        return True

    def activate(self):
        """function activate

        returns None
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect|EventMask.SubstructureNotify,
            self._atom_cache.get_atom('_NET_ACTIVE_WINDOW'), [0, 0, 0, 0, 0])

    def deactivate(self):
        """function deactivate

        returns None
        """
        return None # should raise NotImplementedError()

    def set_always_on_top(self):
        """function set_always_on_top

        returns None
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._atom_cache.get_atom('_NET_WM_STATE'),
            [WindowStateMode.Set,
             self._atom_cache.get_atom('_NET_WM_STATE_ABOVE'), 0, 0, 0])

    def unset_always_on_top(self):
        """function unset_always_on_top

        returns None
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._atom_cache.get_atom('_NET_WM_STATE'),
            [WindowStateMode.Unset,
             self._atom_cache.get_atom('_NET_WM_STATE_ABOVE'), 0, 0, 0])

    def is_always_on_top(self):
        """function is_always_on_top

        returns bool
        """
        return (self._atom_cache.get_atom('_NET_WM_STATE_ABOVE')
                in self._list_wm_state())

    def set_always_on_bottom(self):
        """function set_always_on_bottom

        returns None
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._atom_cache.get_atom('_NET_WM_STATE'),
            [WindowStateMode.Set,
             self._atom_cache.get_atom('_NET_WM_STATE_BELOW'), 0, 0, 0])

    def unset_always_on_bottom(self):
        """function unset_always_on_bottom

        returns None
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._atom_cache.get_atom('_NET_WM_STATE'),
            [WindowStateMode.Unset,
             self._atom_cache.get_atom('_NET_WM_STATE_BELOW'), 0, 0, 0])

    def is_always_on_bottom(self):
        """function is_always_on_bottom

        returns bool
        """
        return (self._atom_cache.get_atom('_NET_WM_STATE_BELOW')
                in self._list_wm_state())

    def set_fullscreen(self):
        """function set_fullscreen

        returns None
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._atom_cache.get_atom('_NET_WM_STATE'),
            [WindowStateMode.Set,
             self._atom_cache.get_atom('_NET_WM_STATE_FULLSCREEN'),
             0, 0, 0])

    def unset_fullscreen(self):
        """function unset_fullscreen

        returns None
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._atom_cache.get_atom('_NET_WM_STATE'),
            [WindowStateMode.Unset,
             self._atom_cache.get_atom('_NET_WM_STATE_FULLSCREEN'),
             0, 0, 0])

    def is_fullscreened(self):
        """function is_fullscreened

        returns bool
        """
        return (self._atom_cache.get_atom('_NET_WM_STATE_FULLSCREEN')
                in self._list_wm_state())

    def set_shade(self):
        """function set_shade

        returns None
        """
        return None # should raise NotImplementedError()

    def unset_shade(self):
        """function unset_shade

        returns None
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._atom_cache.get_atom('_NET_WM_STATE'),
            [WindowStateMode.Set,
             self._atom_cache.get_atom('_NET_WM_STATE_SHADED'), 0, 0, 0])

    def is_shaded(self):
        """function is_shaded

        returns bool
        """
        return (self._atom_cache.get_atom('_NET_WM_STATE_SHADED')
                in self._list_wm_state())

    def show(self):
        """function show

        returns None
        """
        return None # should raise NotImplementedError()

    def restore(self):
        """function restore

        returns None
        """
        return None # should raise NotImplementedError()

    def close(self):
        """function close

        returns None
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect|EventMask.SubstructureNotify,
            self._atom_cache.get_atom('_NET_CLOSE_WINDOW'),
            [0, 0, 0, 0, 0])

    def delete(self):
        """function delete

        returns None
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect|EventMask.SubstructureNotify,
            self._atom_cache.get_atom('WM_PROTOCOLS'),
            [self._atom_cache.get_atom('WM_DELETE_WINDOW'), 0, 0, 0, 0])

    def ping(self):
        """function ping

        returns bool
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect|EventMask.SubstructureNotify,
            self._atom_cache.get_atom('WM_PROTOCOLS'),
            [self._atom_cache.get_atom('_NET_WM_PING'), 0, 0, 0, 0])

    def destroy(self):
        """function destroy

        returns None
        """
        return self.window.destroy_checked()

    @dispatch.generic()
    def move_cursor_to(self, newx, newy=0):
        r"""SUMMARY

        move_cursor_to(newx, newy=0)

        @Arguments:
        - `newx`:
        - `newy`:

        @Return:

        @Error:
        """

    @move_cursor_to.when('isinstance(newx, Point)')
    def move_cursor_to_point(self, newx, newy=0):
        """function move_cursor_to

        point: Point

        returns None
        """
        return self.window.warp_pointer_checked(
            0, 0, 0, 0, 0, newx.x, newx.y)

    @move_cursor_to.when('isinstance(newx, int)')
    def move_cursor_to_int(self, newx, newy=0):
        """function move_cursor_to

        newx: int
        newy: int

        returns None
        """
        return self.window.warp_pointer_checked(
            0, 0, 0, 0, 0, newx, newx)

    def send_key(self, code, modifiers=0, pressed=True, x=0, y=0):
        """function send_key

        code: int
        modifiers: int
        pressed: bool
        x: int
        y: int

        returns Cookie
        """
        keystate = EventCode.KeyPress
        mask = EventMask.KeyPress
        if not pressed:
            keystate = EventCode.KeyRelease
            mask = EventMask.KeyRelease
        event = pack('BBH4I5HBx', keystate, code, 0,
                     0, self.root, self.id, 0, 0, 0, x, y, modifiers, 0)
        return self.window.send_event_checked(False, mask, event)

    def send_button(self, code, modifiers=0, pressed=True, x=0, y=0):
        """function send_button

        code: int
        modifiers: int
        pressed: bool
        x: int
        y: int

        returns Cookie
        """
        keystate = EventCode.ButtonPress
        mask = EventMask.ButtonPress
        if not pressed:
            keystate = EventCode.ButtonRelease
            mask = EventMask.ButtonRelease
        event = pack('BBH4I5HBx', keystate, code, 0,
                     0, self.root, self.id, 0, 0, 0, x, y, modifiers, 0)
        return self.window.send_event_checked(False, mask, event)

    def _notify_window_title_changed(self, window):
        r"""SUMMARY

        _notify_window_title_changed(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """

    def _notify_window_state_changed(self, window):
        r"""SUMMARY

        _notify_window_state_changed(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """

    def _notify_window_maximized(self, window):
        r"""SUMMARY

        _notify_window_maximized(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """

    def _notify_window_minimized(self, window):
        r"""SUMMARY

        _notify_window_minimized(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """

    def _notify_window_fullscreened(self, window):
        r"""SUMMARY

        _notify_window_fullscreened(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """

    def _notify_window_destroyed(self, window_id):
        r"""SUMMARY

        _notify_window_destroyed(window_id)

        @Arguments:
        - `window_id`:

        @Return:

        @Error:
        """

    def _notify_window_bounds_changed(self, window):
        r"""SUMMARY

        _notify_window_bounds_changed(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# window_client.py ends here
