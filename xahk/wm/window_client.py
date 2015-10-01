#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""window_client -- DESCRIPTION

# profile GrabKey
import xcb,xcb.xproto
c=xcb.connect()
# first try: 0.846740007401
# secound try: 0.747024059296
def grab1():
    start = time.time()
    for _ in xrange(0, 9999):
        c.core.GrabKey(True, 482, 0, 38, xcb.xproto.GrabMode.Async, xcb.xproto.GrabMode.Async)
    c.flush()
    return time.time() - start

# first try: 0.638881921768
# secound try: 0.63419508934
def grab2():
    cookies = []
    append = cookies.append
    start = time.time()
    for _ in xrange(0, 9999):
        append(c.core.GrabKeyChecked(True, 482, 0, 38, xcb.xproto.GrabMode.Async, xcb.xproto.GrabMode.Async))
    for cookie in cookies:
        cookie.check()
    return time.time() - start

"""
from enum import IntEnum
from array import array
from cStringIO import StringIO
from struct import unpack, pack
from dotavoider import ListDotAvoider
from rectangle import Rectangle, Point

from xcb.xproto import PropMode, ConfigWindow, EventMask, StackMode, GrabMode, CW
from xcb.xproto import BadMatch, BadWindow, BadValue, BadDrawable

from xahk.wm.atom_cache import AtomCache
from xahk.wm.eventcode import EventCode
from xahk.wm.window import Window
from xahk.layout.layout_item import LayoutItem



KATOM_TO_CACHE_FOR_WINDOW_CLIENT = [
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


class WindowClient(LayoutItem):
    """Class WindowClient
    """
    # Attributes:
    def __init__(self, display, window_id):
        r"""

        @Arguments:
        - `window`:
        """
        self.window = Window(display, window_id)
        self._root = None
        self._atom_cache = AtomCache(
            self.display, KATOM_TO_CACHE_FOR_WINDOW_CLIENT)

    # Operations
    def get_display(self):
        """function get_display

        returns
        """
        return self.window.get_display()

    display = property(get_display)

    def __int__(self):
        return self.id

    def __eq__(self, other):
        if isinstance(other, (WindowClient, )):
            return self.id == other.id
        return self.id == other

    def __ne__(self, other):
        return not self == other

    def __hash__(self, ):
        return hash(self.id)

    def __repr__(self):
        return ('{0.__class__.__name__}(id={0.id}, wmclass={0.wmclass})'
                .format(self))

    def get_root(self, ):
        r"""SUMMARY

        get_root()

        @Return:

        @Error:
        """
        if self._root is None:
            self._root = self.display.get_setup().roots[0].root
        return self._root

    root = property(get_root)

    def get_id(self):
        """function get_id

        returns
        """
        return self.window.get_id()

    id = property(get_id)

    def get_property(self, delete, prop, types, offset=0, length=20):
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
            reply = self.window.get_property(delete,
                                             self._atom_cache.get_atom(prop),
                                             self._atom_cache.get_atom(types),
                                             offset, length).reply()
        except BadWindow as err:
            from xahk.logger import LOG
            LOG.error('{}, {}'.format(err, prop))
            # TODO: (Atami) [2015/06/02]
            import os
            os.system('modprobe pcspkr')
            os.system('/usr/bin/beep -f250 -r2 -l50')
            os.system('rmmod pcspkr')
            return None
        if reply.bytes_after:
            after_reply = self.get_property(
                delete, prop, types, length, reply.bytes_after) # recursive call
            if after_reply is None:
                return None
            reply.value += after_reply.value
            reply.value_len += after_reply.value_len
            reply.bytes_after = after_reply.bytes_after
            return reply
        return reply

    def change_property(self, mode, prop, types, format, datalen, data):
        r"""SUMMARY

        change_property(mode, prop, types, format, data)

        @Arguments:
        - `mode`:
        - `prop`:
        - `types`:
        - `format`:
        - `data`:

        @Return:

        @Error:
        """
        cookie = self.window.change_property_checked(
            mode, self._atom_cache.get_atom(prop),
            self._atom_cache.get_atom(types), format, datalen, data)
        try:
            cookie.check()
            return True
        except (BadWindow, BadMatch) as err:
            from xahk.logger import LOG
            LOG.error('{}'.format(err))
            import os
            os.system('modprobe pcspkr')
            os.system('/usr/bin/beep -f250 -r2 -l50')
            os.system('rmmod pcspkr')
            return False
        except BadValue as err:
            from xahk.logger import LOG
            LOG.error('{}'.format(err))
            import os
            os.system('modprobe pcspkr')
            os.system('/usr/bin/beep -f250 -r2 -l50')
            os.system('rmmod pcspkr')
            # TODO: (Atami) [2015/06/02]
            raise StandardError(err)

    def get_title(self):
        """function get_title

        returns
        """
        reply = self.get_property(False, '_NET_WM_NAME', 'UTF8_STRING')
        if reply is None:
            return ''
        if str(array('B', reply.value).tostring()) != '':
            return str(array('B', reply.value).tostring())
        reply2 = self.get_property(False, 'WM_NAME', 'STRING')
        if reply2 is None:
            return ''
        return str(array('B', reply2.value).tostring())

    def set_title(self, title):
        """function set_title

        title:

        returns
        """
        return self.change_property(
            PropMode.Replace, '_NET_WM_NAME', 'UTF8_STRING', 8,
            len(title), title)

    title = property(get_title, set_title)

    def get_wmclass(self):
        """function get_wmclass

        returns
        """
        reply = self.get_property(False, 'WM_CLASS', 'STRING')
        if reply is None:
            return ['',  '']
        wmclasses = str(array('B', reply.value).tostring()).split('\x00')
        while '' in wmclasses:
            wmclasses.remove('')
        while len(wmclasses) < 2:
            wmclasses.append('')
        return wmclasses

    wmclass = property(get_wmclass)

    def get_pid(self):
        """function get_pid

        returns
        """
        reply = self.get_property(
            False, '_NET_WM_PID', 'CARDINAL', length=1)
        if reply is None:
            return None
        pids = unpack('I' * reply.value_len, array('B', reply.value).tostring())
        if not pids:
            return None
        return pids[0]

    pid = property(get_pid)

    def get_type(self):
        """function get_type

        returns
        """
        reply = self.get_property(
            False, '_NET_WM_WINDOW_TYPE', 'ATOM', length=1)
        if reply is None:
            return None
        types = unpack('I' * reply.value_len,
                       array('B', reply.value).tostring())
        if not types:
            return None
        return types[0]

    type = property(get_type)

    def get_workspace(self, ):
        r"""SUMMARY

        get_desktop()

        @Return:

        @Error:
        """
        reply = self.get_property(False, '_NET_WM_DESKTOP', 'CARDINAL')
        if reply is None:
            return None
        num = unpack('I' * reply.value_len, array('B', reply.value).tostring())
        if not num:
            return None
        return num[0]

    def change_workspace(self, num):
        r"""SUMMARY

        change_desktop(num)

        @Arguments:
        - `num`:

        @Return:

        @Error:
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect|EventMask.SubstructureNotify,
            self._atom_cache.get_atom('_NET_WM_DESKTOP'),
            [num, 0, 0, 0, 0])

    workspace = property(get_workspace, change_workspace)

    def get_bounds(self):
        """function get_bounds

        returns
        """
        try:
            geo = self.window.get_geometry_unchecked().reply()
        except BadDrawable as err:
            # TODO: (Atami) [2015/06/02]
            from xahk.logger import LOG
            LOG.error('{}'.format(err))
            import os
            os.system('modprobe pcspkr')
            os.system('/usr/bin/beep -f250 -r2 -l50')
            os.system('rmmod pcspkr')
            return None
        try:
            cood = self.window.translate_coordinates(
                self.root, geo.x, geo.y).reply()
        except BadWindow as err:
            # TODO: (Atami) [2015/06/02]
            from xahk.logger import LOG
            LOG.error('{}'.format(err))
            import os
            os.system('modprobe pcspkr')
            os.system('/usr/bin/beep -f250 -r2 -l50')
            os.system('rmmod pcspkr')
            return None
        newx = cood.dst_x - (2 * geo.x)
        newy = cood.dst_y - (2 * geo.y)
        return Rectangle(newx, newy, geo.width, geo.height)

    def _configure(self, mask, value_list):
        r"""SUMMARY

        _configure(mask, value_list)

        @Arguments:
        - `mask`:
        - `value_list`:

        @Return:

        @Error:
        """
        cookie = self.window.configure_checked(mask, value_list)
        try:
            cookie.check()
            return True
        except (BadWindow, BadMatch) as err:
            from xahk.logger import LOG
            LOG.error('{}'.format(err))
            import os
            os.system('modprobe pcspkr')
            os.system('/usr/bin/beep -f250 -r2 -l50')
            os.system('rmmod pcspkr')
            return False
        except BadValue as err:
            # TODO: (Atami) [2015/06/02]
            from xahk.logger import LOG
            LOG.error('{}'.format(err))
            import os
            os.system('modprobe pcspkr')
            os.system('/usr/bin/beep -f250 -r2 -l50')
            os.system('rmmod pcspkr')
            raise StandardError(err)

    def set_bounds(self, newx, newy, width, height):
        """function set_bounds

        rectangle:

        returns
        """
        return self._configure(
            ConfigWindow.X|ConfigWindow.Y|
            ConfigWindow.Width|ConfigWindow.Height,
            [newx, newy, width, height])

    def layout(self, rect):
        r"""SUMMARY

        layout(rect)

        @Arguments:
        - `rect`:

        @Return:

        @Error:
        """
        self.set_bounds(rect.x, rect.y, rect.width, rect.height)

    def set_size(self, width, height):
        """function set_size

        size:

        returns
        """
        return self._configure(
            ConfigWindow.Width|ConfigWindow.Height, [width, height])

    def move(self, newx, newy):
        """function move

        point:

        returns
        """
        return self._configure(
            ConfigWindow.X|ConfigWindow.Y, [newx, newy])

    def raise_window(self):
        """function raise

        returns
        """
        return self._configure(ConfigWindow.StackMode, [StackMode.Above])

    def lower_window(self):
        """function lower

        returns
        """
        return self._configure(ConfigWindow.StackMode, [StackMode.Below])

    def _send_client_message(self, mask, types, data):
        r"""SUMMARY

        _send_client_message(target, mask, types, data)

        @Arguments:
        - `target`:
        - `mask`:
        - `types`:
        - `data`:

        @Return:

        @Error:
        """
        event = StringIO()
        event.write(
            # code, format, sequence_number, window, messagetype
            pack('BBHII', EventCode.ClientMessage, 32, 0, self.id, types))
        event.write(pack('I' * len(data), *data))
        cookie = self.window.send_event_checked(True, mask, event.getvalue())
        try:
            cookie.check()
            return True
        except BadWindow as err:
            from xahk.logger import LOG
            LOG.error('{}'.format(err))
            import os
            os.system('modprobe pcspkr')
            os.system('/usr/bin/beep -f250 -r2 -l50')
            os.system('rmmod pcspkr')
            return False
        except BadValue as err:
            from xahk.logger import LOG
            LOG.error('{}'.format(err))
            import os
            os.system('modprobe pcspkr')
            os.system('/usr/bin/beep -f250 -r2 -l50')
            os.system('rmmod pcspkr')
            raise StandardError(err)

    def minimize(self):
        """function minimize

        returns
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect|EventMask.SubstructureNotify,
            self._atom_cache.get_atom('WM_CHANGE_STATE'),
            [ChangingWindowState.ICONIC_STATE, 0, 0, 0, 0])

    def is_minimized(self):
        """function is_minimized

        returns bool
        """
        reply = self.get_property(False, '_NET_WM_STATE', 'ATOM')
        if reply is None:
            # TODO: (Atami) [2015/06/02]
            return False
        atoms = unpack('I' * reply.value_len,
                       array('B', reply.value).tostring())
        return self._atom_cache.get_atom('_NET_WM_STATE_HIDDEN') in atoms

    def show(self):
        """function show

        returns
        """
        # TODO: (Atami) [2015/05/29]
        # return self._send_client_message(
        #     EventMask.SubstructureRedirect|EventMask.SubstructureNotify,
        #     self._atom_cache.get_atom('WM_CHANGE_STATE'),
        #     [ChangingWindowState.NORMAL_STATE, 0, 0, 0, 0])
        self.window.map_checked().check()

    def maximize(self, mode=WindowStateMode.Set):
        """function maximize

        mode:

        returns
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._atom_cache.get_atom('_NET_WM_STATE'),
            [mode, self._atom_cache.get_atom('_NET_WM_STATE_MAXIMIZED_VERT'),
             self._atom_cache.get_atom('_NET_WM_STATE_MAXIMIZED_HORZ'), 0, 0])

    def is_maximized(self):
        """function is_maximized

        returns
        """
        reply = self.get_property(False, '_NET_WM_STATE', 'ATOM')
        if reply is None:
            return False
        atoms = unpack('I' * reply.value_len,
                       array('B', reply.value).tostring())
        return (
            self._atom_cache.get_atom('_NET_WM_STATE_MAXIMIZED_VERT') in atoms
            and
            self._atom_cache.get_atom('_NET_WM_STATE_MAXIMIZED_HORZ') in atoms)

    def restore(self):
        """function restore

        returns
        """
        self.maximize(WindowStateMode.Unset)
        if self.is_minimized():
            # TODO: (Atami) [2015/05/23]
            self.show()

    def activate(self):
        """function activate

        returns
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect|EventMask.SubstructureNotify,
            self._atom_cache.get_atom('_NET_ACTIVE_WINDOW'), [0, 0, 0, 0, 0])

    def deactivate(self):
        """function deactivate

        returns
        """
        return None # should raise NotImplementedError()

    def set_always_on_top(self, mode=WindowStateMode.Set):
        """function set_always_on_top

        mode:

        returns
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._atom_cache.get_atom('_NET_WM_STATE'),
            [mode, self._atom_cache.get_atom('_NET_WM_STATE_ABOVE'), 0, 0, 0])

    def is_always_on_top(self):
        """function is_always_on_top

        returns bool
        """
        reply = self.get_property(False, '_NET_WM_STATE', 'ATOM')
        if reply is None:
            return False
        atoms = unpack('I' * reply.value_len,
                       array('B', reply.value).tostring())
        return self._atom_cache.get_atom('_NET_WM_STATE_ABOVE') in atoms

    def set_always_on_bottom(self, mode=WindowStateMode.Set):
        """function set_always_on_bottom

        mode:

        returns
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._atom_cache.get_atom('_NET_WM_STATE'),
            [mode, self._atom_cache.get_atom('_NET_WM_STATE_BELOW'), 0, 0, 0])

    def is_always_on_bottom(self):
        """function is_always_on_bottom

        returns
        """
        reply = self.get_property(False, '_NET_WM_STATE', 'ATOM')
        if reply is None:
            return False
        atoms = unpack('I' * reply.value_len,
                       array('B', reply.value).tostring())
        return self._atom_cache.get_atom('_NET_WM_STATE_BELOW') in atoms

    def set_fullscreen(self, mode=WindowStateMode.Set):
        """function set_fullscreen

        mode:

        returns
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._atom_cache.get_atom('_NET_WM_STATE'),
            [mode, self._atom_cache.get_atom('_NET_WM_STATE_FULLSCREEN'),
             0, 0, 0])

    def is_fullscreened(self):
        """function is_fullscreen

        returns
        """
        reply = self.get_property(False, '_NET_WM_STATE', 'ATOM')
        if reply is None:
            return None
        atoms = unpack('I' * reply.value_len,
                       array('B', reply.value).tostring())
        return self._atom_cache.get_atom('_NET_WM_STATE_FULLSCREEN') in atoms

    def set_shade(self, mode=WindowStateMode.Set):
        """function set_shade

        mode:

        returns
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._atom_cache.get_atom('_NET_WM_STATE'),
            [mode, self._atom_cache.get_atom('_NET_WM_STATE_SHADED'), 0, 0, 0])

    def is_shaded(self):
        """function is_shaded

        returns
        """
        reply = self.get_property(False, '_NET_WM_STATE', 'ATOM')
        if reply is None:
            return False
        atoms = unpack('I' * reply.value_len,
                       array('B', reply.value).tostring())
        return self._atom_cache.get_atom('_NET_WM_STATE_SHADED') in atoms

    # def hide(self):
    #     """function hide

    #     returns
    #     """
    #     # TODO: (Atami) [2015/05/29]
    #     return self._send_client_message(
    #         0xffffff, self._atom_cache.get_atom('WM_CHANGE_STATE'),
    #         [ChangingWindowState.WITHDRAWN_STATE, 0, 0, 0, 0])

    def close(self):
        """function close

        returns
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect|EventMask.SubstructureNotify,
            self._atom_cache.get_atom('_NET_CLOSE_WINDOW'),
            [0, 0, 0, 0, 0])

    def delete(self):
        """function delete

        returns
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect|EventMask.SubstructureNotify,
            self._atom_cache.get_atom('WM_PROTOCOLS'),
            [self._atom_cache.get_atom('WM_DELETE_WINDOW'), 0, 0, 0, 0])

    def ping(self, ):
        r"""SUMMARY

        ping()

        @Return:

        @Error:
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect|EventMask.SubstructureNotify,
            self._atom_cache.get_atom('WM_PROTOCOLS'),
            [self._atom_cache.get_atom('_NET_WM_PING'), 0, 0, 0, 0])

    def destroy(self):
        """function destroy

        returns
        """
        try:
            self.window.destroy_checked().check()
            return True
        except BadWindow as err:
            from xahk.logger import LOG
            LOG.error('{}'.format(err))
            import os
            os.system('modprobe pcspkr')
            os.system('/usr/bin/beep -f250 -r2 -l50')
            os.system('rmmod pcspkr')
            return False

    def move_cursor_to(self, newx, newy):
        """function move_cursor_to

        point:

        returns
        """
        return self.window.warp_pointer_checked(
            0, 0, 0, 0, 0, newx, newy)

    def grab_key(self, accelerator):
        r"""SUMMARY

        grab_key(key, modifiers)

        @Arguments:
        - `key`:
        - `modifiers`:

        @Return:

        @Error:
        """
        self.window.grab_key(
            False, accelerator.get_modifiers(), accelerator.get_code(),
            GrabMode.Async, GrabMode.Async)
        self.display.flush()

    def grab_keys(self, accelerators):
        r"""SUMMARY

        grab_keys(targets)

        @Arguments:
        - `targets`:

        @Return:

        @Error:
        """
        cookies, append = ListDotAvoider().append
        for accelerator in accelerators:
            append(self.window.grab_key_checked(
                False, accelerator.get_modifiers(),
                accelerator.get_code(), GrabMode.Async, GrabMode.Async))
        return cookies

    def ungrab_key(self, accelerator):
        r"""SUMMARY

        ungrab_key(accelerator)

        @Arguments:
        - `accelerator`:

        @Return:

        @Error:
        """
        self.window.ungrab_key(
            accelerator.get_code(), accelerator.get_modifiers())
        self.display.flush()

    def ungrab_keys(self, accelerators):
        r"""SUMMARY

        ungrab_keys(accelerators)

        @Arguments:
        - `accelerators`:

        @Return:

        @Error:
        """
        cookies, append = ListDotAvoider().append
        for accelerator in accelerators:
            append(self.window.ungrab_key_checked(
                accelerator.get_code(), accelerator.get_modifiers()))
        return cookies

    def grab_button(self, accelerator):
        r"""SUMMARY

        grab_button(accelerator)

        @Arguments:
        - `accelerator`:

        @Return:

        @Error:
        """
        self.window.grab_button(
            False, EventMask.ButtonPress|EventMask.ButtonRelease,
            GrabMode.Async, GrabMode.Async, 0, 0, accelerator.get_code(),
            accelerator.get_modifiers())
        self.display.flush()

    def grab_buttons(self, accelerators):
        r"""SUMMARY

        grab_button(accelerator)

        @Arguments:
        - `accelerator`:

        @Return:

        @Error:
        """
        cookies, append = ListDotAvoider().append
        for accelerator in accelerators:
            append(self.window.grab_button_checked(
                False, EventMask.ButtonPress|EventMask.ButtonRelease,
                GrabMode.Async, GrabMode.Async, 0, 0, accelerator.get_code(),
                accelerator.get_modifiers()))
        return cookies

    def ungrab_button(self, accelerator):
        r"""SUMMARY

        ungrab_button(accelerator)

        @Arguments:
        - `accelerator`:

        @Return:

        @Error:
        """
        self.window.ungrab_button(
            accelerator.get_code(), accelerator.get_modifiers())
        self.display.flush()

    def ungrab_buttons(self, accelerators):
        r"""SUMMARY

        ungrab_buttons(accelerators)

        @Arguments:
        - `accelerators`:

        @Return:

        @Error:
        """
        cookies, append = ListDotAvoider().append
        for accelerator in accelerators:
            append(self.window.ungrab_button_checked(
                accelerator.get_code(), accelerator.get_modifiers()))
        return cookies

    def query_pointer(self, ):
        r"""SUMMARY

        get_query_pointer()

        @Return:

        @Error:
        """
        return self.window.query_pointer().reply()

    def get_cursor_point(self, ):
        r"""SUMMARY

        get_cursor_point()

        @Return:

        @Error:
        """
        rep = self.query_pointer()
        return Point(rep.win_x, rep.win_y)

    def get_attributes(self, ):
        r"""SUMMARY

        get_attributes()

        @Return:

        @Error:
        """
        try:
            return self.window.get_attributes().reply()
        except BadWindow as err:
            from xahk.logger import LOG
            LOG.error('{} {}'.format(err, self.id))
            import os
            os.system('modprobe pcspkr')
            os.system('/usr/bin/beep -f250 -r2 -l50')
            os.system('rmmod pcspkr')

    def add_attributes(self, value):
        r"""SUMMARY

        add_attributes(value)

        @Arguments:
        - `value`:

        @Return:

        @Error:
        """
        reply = self.get_attributes()
        if reply is None:
            return None
        return self.window.change_attributes_checked(
            CW.EventMask, [value|reply.your_event_mask])

    def remove_attributes(self, value):
        r"""SUMMARY

        remove_attributes(value)

        @Arguments:
        - `value`:

        @Return: cookie

        @Error:
        """
        current_attr = self.get_attributes().your_event_mask
        if current_attr is None or current_attr^value == 0: # has not attr
            return None
        return self.window.change_attributes_checked(
            CW.EventMask, [current_attr^value])



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# window_client.py ends here
