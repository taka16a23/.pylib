#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""desktop_window -- DESCRIPTION

"""
from array import array
from struct import unpack, pack
from cStringIO import StringIO
from enum import IntEnum

# TODO: (Atami) [2016/05/10] move to subdir
from rectangle import Rectangle, Point, Dimension
from observer import Observable
from peak.rules import dispatch
from xcb.xproto import PropMode, ConfigWindow, EventMask, StackMode, CW
from xcb.xproto import ConfigureNotifyEvent, PropertyNotifyEvent, DestroyNotifyEvent
from xcb.xproto import BadWindow, BadDrawable

from .x11.atom_cache import AtomCache
from .eventcode import EventCode
from .events.listener import EventListener
from .events.loop import EventLoop


KATOM_TO_CACHE_FOR_DESKTOP_WINDOW = [
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


class DesktopWindow(EventListener, Observable):
    r"""DesktopWindow

    DesktopWindow is a object.
    Responsibility:
    """

    def __init__(self, window):
        r"""

        @Arguments:
        - `window`:
        """
        Observable.__init__(self)
        self.window = window
        attrs = self.window.get_attributes().reply()
        reply = self.window.change_attributes_checked(
            CW.EventMask,
            [EventMask.StructureNotify|EventMask.PropertyChange|attrs.your_event_mask])
        reply.check()
        self._atom_cache = None
        self._current_state = self._list_current_state()
        EventLoop.get_instance(self.display).dispatcher.add_event_listener(self)

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self.window.get_display()

    display = property(get_display)

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
            self._atom_cache = AtomCache(
                self.display, KATOM_TO_CACHE_FOR_DESKTOP_WINDOW)
        return self._atom_cache.get_atom(name)

    def get_id(self, ):
        r"""SUMMARY

        get_id()

        @Return:

        @Error:
        """
        return self.window.get_id()

    id = property(get_id)

    def __int__(self):
        return self.id

    def __eq__(self, other):
        if isinstance(other, (DesktopWindow, )):
            return self.id == other.id
        return self.id == other

    def __ne__(self, other):
        return not self == other

    def __hash__(self, ):
        return hash(self.id)

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
            reply = self.window.get_property(
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

    def _change_property(self, mode, prop, types, format, datalen, data):
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
        return self.window.change_property_checked(
            mode, self._get_atom(prop), self._get_atom(types),
            format, datalen, data)

    def get_title(self):
        """function get_title

        returns
        """
        reply = self._get_property(False, '_NET_WM_NAME', 'UTF8_STRING')
        if reply is None:
            return ''
        if str(array('B', reply.value).tostring()) != '':
            return str(array('B', reply.value).tostring())
        reply2 = self._get_property(False, 'WM_NAME', 'STRING')
        if reply2 is None:
            return ''
        return str(array('B', reply2.value).tostring())

    def set_title(self, title):
        """function set_title

        title:

        returns
        """
        return self._change_property(
            PropMode.Replace, '_NET_WM_NAME', 'UTF8_STRING', 8,
            len(title), title)

    title = property(get_title, set_title)

    def get_wmclass(self):
        """function get_wmclass

        returns
        """
        reply = self._get_property(False, 'WM_CLASS', 'STRING')
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
        reply = self._get_property(
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
        reply = self._get_property(
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
        reply = self._get_property(False, '_NET_WM_DESKTOP', 'CARDINAL')
        if reply is None:
            return None
        num = unpack('I' * reply.value_len, array('B', reply.value).tostring())
        if not num:
            return None
        return num[0]

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
        return self.window.send_event_checked(True, mask, event.getvalue())

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
            self._get_atom('_NET_WM_DESKTOP'),
            [num, 0, 0, 0, 0])

    workspace = property(get_workspace, change_workspace)

    def get_bounds(self):
        """function get_bounds

        returns
        """
        # TODO: (Atami) [2016/05/11]
        # on_error handle object
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
        root = self.display.get_setup().roots[0].root
        try:
            cood = self.window.translate_coordinates(
                root, geo.x, geo.y).reply()
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
        return self.window.configure_checked(mask, value_list)

    @dispatch.generic()
    def set_bounds(self, *args):
        r"""SUMMARY

        set_bounds()

        @Return:

        @Error:
        """

    @set_bounds.when('1 <= len(args) and isinstance(args[0], int)')
    def set_bounds_int(self, *args):
        """function set_bounds

        rectangle:

        returns
        """
        return self._configure(
            ConfigWindow.X|ConfigWindow.Y|
            ConfigWindow.Width|ConfigWindow.Height,
            [args[0], args[1], args[2], args[3]])

    @set_bounds.when('1 <= len(args) and isinstance(args[0], Rectangle)')
    def set_bounds_rectangle(self, *args):
        r"""SUMMARY

        set_bounds_rectangle(rectangle)

        @Arguments:
        - `rectangle`:

        @Return:

        @Error:
        """
        rect = args[0]
        return self.set_bounds(rect.x, rect.y, rect.width, rect.height)

    @dispatch.generic()
    def set_size(self, *args):
        r"""SUMMARY

        set_size()

        @Return:

        @Error:
        """

    @set_size.when('1 <= len(args) and isinstance(args[0], int)')
    def set_size_int(self, *args):
        """function set_size

        size:

        returns
        """
        return self._configure(
            ConfigWindow.Width|ConfigWindow.Height, [args[0], args[1]])

    @set_size.when('1 <= len(args) and isinstance(args[0], Dimension)')
    def set_size_dimension(self, *args):
        r"""SUMMARY

        set_size()

        @Return:

        @Error:
        """
        size = args[0]
        return self.set_size(size.width, size.height)

    @dispatch.generic()
    def move(self, *args):
        r"""SUMMARY

        move()

        @Return:

        @Error:
        """

    @move.when('1 <= len(args) and isinstance(args[0], int)')
    def move_int(self, *args):
        """function move

        point:

        returns
        """
        return self._configure(
            ConfigWindow.X|ConfigWindow.Y, [args[0], args[1]])

    @move.when('1 <= len(args) and isinstance(args[0], Point)')
    def move_point(self, *args):
        """function move

        point:

        returns
        """
        return self.move(args[0].x, args[0].y)

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

    def minimize(self):
        """function minimize

        returns
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect|EventMask.SubstructureNotify,
            self._get_atom('WM_CHANGE_STATE'),
            [ChangingWindowState.ICONIC_STATE, 0, 0, 0, 0])

    def is_minimized(self):
        """function is_minimized

        returns bool
        """
        reply = self._get_property(False, '_NET_WM_STATE', 'ATOM')
        if reply is None:
            # TODO: (Atami) [2015/06/02]
            return False
        atoms = unpack('I' * reply.value_len,
                       array('B', reply.value).tostring())
        return self._get_atom('_NET_WM_STATE_HIDDEN') in atoms

    def show(self):
        """function show

        returns
        """
        # TODO: (Atami) [2015/05/29]
        # return self._send_client_message(
        #     EventMask.SubstructureRedirect|EventMask.SubstructureNotify,
        #     self._get_atom('WM_CHANGE_STATE'),
        #     [ChangingWindowState.NORMAL_STATE, 0, 0, 0, 0])
        self.window.map_checked()

    def unset_maximized(self, ):
        r"""SUMMARY

        unset_maximized()

        @Return:

        @Error:
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._get_atom('_NET_WM_STATE'),
            [WindowStateMode.Unset, self._get_atom('_NET_WM_STATE_MAXIMIZED_VERT'),
             self._get_atom('_NET_WM_STATE_MAXIMIZED_HORZ'), 0, 0])

    def maximize(self, ):
        """function maximize

        mode:

        returns
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._get_atom('_NET_WM_STATE'),
            [WindowStateMode.Set, self._get_atom('_NET_WM_STATE_MAXIMIZED_VERT'),
             self._get_atom('_NET_WM_STATE_MAXIMIZED_HORZ'), 0, 0])

    def toggle_maximize(self, ):
        r"""SUMMARY

        toggle_maximize()

        @Return:

        @Error:
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._get_atom('_NET_WM_STATE'),
            [WindowStateMode.Toggle, self._get_atom('_NET_WM_STATE_MAXIMIZED_VERT'),
             self._get_atom('_NET_WM_STATE_MAXIMIZED_HORZ'), 0, 0])

    def is_maximized(self):
        """function is_maximized

        returns
        """
        reply = self._get_property(False, '_NET_WM_STATE', 'ATOM')
        if reply is None:
            return False
        atoms = unpack('I' * reply.value_len,
                       array('B', reply.value).tostring())
        for atom in ('_NET_WM_STATE_MAXIMIZED_VERT', '_NET_WM_STATE_MAXIMIZED_HORZ'):
            if atom not in atoms:
                return False
        return True

    def activate(self):
        """function activate

        returns
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect|EventMask.SubstructureNotify,
            self._get_atom('_NET_ACTIVE_WINDOW'), [0, 0, 0, 0, 0])

    def deactivate(self):
        """function deactivate

        returns
        """
        return None # should raise NotImplementedError()

    def always_on_top(self, ):
        """function always_on_top

        mode:

        returns
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._get_atom('_NET_WM_STATE'),
            [WindowStateMode.Set, self._get_atom('_NET_WM_STATE_ABOVE'), 0, 0, 0])

    def unset_always_on_top(self, ):
        r"""SUMMARY

        unset_always_on_top()

        @Return:

        @Error:
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._get_atom('_NET_WM_STATE'),
            [WindowStateMode.Unset, self._get_atom('_NET_WM_STATE_ABOVE'), 0, 0, 0])

    def toggle_always_on_top(self, ):
        r"""SUMMARY

        toggle_always_on_top()

        @Return:

        @Error:
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._get_atom('_NET_WM_STATE'),
            [WindowStateMode.Toggle, self._get_atom('_NET_WM_STATE_ABOVE'), 0, 0, 0])

    def is_always_on_top(self):
        """function is_always_on_top

        returns bool
        """
        reply = self._get_property(False, '_NET_WM_STATE', 'ATOM')
        if reply is None:
            return False
        atoms = unpack('I' * reply.value_len,
                       array('B', reply.value).tostring())
        return self._get_atom('_NET_WM_STATE_ABOVE') in atoms

    def always_on_bottom(self, ):
        """function always_on_bottom

        mode:

        returns
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._get_atom('_NET_WM_STATE'),
            [WindowStateMode.Set, self._get_atom('_NET_WM_STATE_BELOW'), 0, 0, 0])

    def toggle_always_on_bottom(self, ):
        r"""SUMMARY

        toggle_always_on_top()

        @Return:

        @Error:
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._get_atom('_NET_WM_STATE'),
            [WindowStateMode.Toggle, self._get_atom('_NET_WM_STATE_BELOW'), 0, 0, 0])

    def unset_always_on_bottom(self, ):
        r"""SUMMARY

        unset_always_on_bottom()

        @Return:

        @Error:
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._get_atom('_NET_WM_STATE'),
            [WindowStateMode.Unset, self._get_atom('_NET_WM_STATE_BELOW'), 0, 0, 0])

    def is_always_on_bottom(self):
        """function is_always_on_bottom

        returns
        """
        reply = self._get_property(False, '_NET_WM_STATE', 'ATOM')
        if reply is None:
            return False
        atoms = unpack('I' * reply.value_len,
                       array('B', reply.value).tostring())
        return self._get_atom('_NET_WM_STATE_BELOW') in atoms

    def fullscreen(self, ):
        """function fullscreen

        mode:

        returns
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._get_atom('_NET_WM_STATE'),
            [WindowStateMode.Set, self._get_atom('_NET_WM_STATE_FULLSCREEN'),
             0, 0, 0])

    def unset_fullscreen(self, ):
        r"""SUMMARY

        unset_fullscreen()

        @Return:

        @Error:
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._get_atom('_NET_WM_STATE'),
            [WindowStateMode.Unset, self._get_atom('_NET_WM_STATE_FULLSCREEN'),
             0, 0, 0])

    def toggle_fullscreen(self, ):
        r"""SUMMARY

        toggle_fullscreen()

        @Return:

        @Error:
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._get_atom('_NET_WM_STATE'),
            [WindowStateMode.Toggle, self._get_atom('_NET_WM_STATE_FULLSCREEN'),
             0, 0, 0])

    def is_fullscreened(self):
        """function is_fullscreen

        returns
        """
        reply = self._get_property(False, '_NET_WM_STATE', 'ATOM')
        if reply is None:
            return None
        atoms = unpack('I' * reply.value_len,
                       array('B', reply.value).tostring())
        return self._get_atom('_NET_WM_STATE_FULLSCREEN') in atoms

    def shade(self, ):
        """function shade

        mode:

        returns
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._get_atom('_NET_WM_STATE'),
            [WindowStateMode.Set, self._get_atom('_NET_WM_STATE_SHADED'), 0, 0, 0])

    def unset_shade(self, ):
        r"""SUMMARY

        unset_shade()

        @Return:

        @Error:
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._get_atom('_NET_WM_STATE'),
            [WindowStateMode.Unset, self._get_atom('_NET_WM_STATE_SHADED'), 0, 0, 0])

    def toggle_shade(self, ):
        r"""SUMMARY

        toggle_shade()

        @Return:

        @Error:
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect,
            self._get_atom('_NET_WM_STATE'),
            [WindowStateMode.Toggle, self._get_atom('_NET_WM_STATE_SHADED'), 0, 0, 0])

    def is_shaded(self):
        """function is_shaded

        returns
        """
        reply = self._get_property(False, '_NET_WM_STATE', 'ATOM')
        if reply is None:
            return False
        atoms = unpack('I' * reply.value_len,
                       array('B', reply.value).tostring())
        return self._get_atom('_NET_WM_STATE_SHADED') in atoms

    # def hide(self):
    #     """function hide

    #     returns
    #     """
    #     # TODO: (Atami) [2015/05/29]
    #     return self._send_client_message(
    #         0xffffff, self._get_atom('WM_CHANGE_STATE'),
    #         [ChangingWindowState.WITHDRAWN_STATE, 0, 0, 0, 0])

    def close(self):
        """function close

        returns
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect|EventMask.SubstructureNotify,
            self._get_atom('_NET_CLOSE_WINDOW'),
            [0, 0, 0, 0, 0])

    def delete(self):
        """function delete

        returns
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect|EventMask.SubstructureNotify,
            self._get_atom('WM_PROTOCOLS'),
            [self._get_atom('WM_DELETE_WINDOW'), 0, 0, 0, 0])

    def ping(self, ):
        r"""SUMMARY

        ping()

        @Return:

        @Error:
        """
        return self._send_client_message(
            EventMask.SubstructureRedirect|EventMask.SubstructureNotify,
            self._get_atom('WM_PROTOCOLS'),
            [self._get_atom('_NET_WM_PING'), 0, 0, 0, 0])

    def destroy(self):
        """function destroy

        returns
        """
        return self.window.destroy_checked()

    def move_cursor_to(self, newx, newy):
        """function move_cursor_to

        point:

        returns
        """
        return self.window.warp_pointer_checked(
            0, 0, 0, 0, 0, newx, newy)

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

    def can_dispatch_event(self, event):
        r"""SUMMARY

        can_dispatch_event(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        return isinstance(
            event, (ConfigureNotifyEvent, PropertyNotifyEvent, DestroyNotifyEvent,
            )) and event.window == self.id

    def handle_event(self, event):
        r"""SUMMARY

        handle_event(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        if isinstance(event, (ConfigureNotifyEvent, )):
            self._notify_bounds_changed()
        elif isinstance(event, (PropertyNotifyEvent, )):
            self._notify_property_changed(event)
        elif isinstance(event, (DestroyNotifyEvent, )):
            EventLoop.get_instance(
                self.display).dispatcher.remove_event_listener(self)
            self._notify_destroyed()

    def _notify_bounds_changed(self, ):
        r"""SUMMARY

        _notify_bounds_changed()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_window_bounds_changed(self)

    def _notify_property_changed(self, event):
        r"""SUMMARY

        _dispatch_property_changed(event)

        @Return:

        @Error:
        """
        if event.atom == self._get_atom('WM_NAME'):
            self._notify_title_changed()
        elif event.atom == self._get_atom('WM_CLASS'):
            # TODO: (Atami) [2016/05/12]
            # debug
            print('window wmclass!!')
        elif event.atom == self._get_atom('_NET_WM_PID'):
            self._notify_pid_changed()
        elif event.atom == self._get_atom('_NET_WM_WINDOW_TYPE'):
            # TODO: (Atami) [2016/05/12]
            # debug
            print('window type!!')
        elif event.atom == self._get_atom('_NET_WM_STATE'):
            self._notify_state_changed()

    def _notify_title_changed(self, ):
        r"""SUMMARY

        _notify_title_changed()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_window_title_changed(self)

    def _notify_pid_changed(self, ):
        r"""SUMMARY

        _notify_pid_changed()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_window_pid_changed(self)

    def _list_current_state(self, ):
        r"""SUMMARY

        _list_current_state()

        @Return:

        @Error:
        """
        rep = self._get_property(False, '_NET_WM_STATE', 'ATOM')
        if rep is None:
            return set()
        return set(unpack('I' * rep.value_len, array('B', rep.value)))

    def _notify_state_changed(self, ):
        r"""SUMMARY

        _notify_state_changed()

        @Return:

        @Error:
        """
        state = self._list_current_state()
        added = state - self._current_state
        removed = self._current_state - state
        self._current_state = state
        if self._get_atom('_NET_WM_STATE_FULLSCREEN') in added:
            self._notify_fullscreened()
        elif (self._get_atom('_NET_WM_STATE_MAXIMIZED_VERT') in added
              and self._get_atom('_NET_WM_STATE_MAXIMIZED_HORZ') in added):
            self._notify_maximized()
        elif self._get_atom('_NET_WM_STATE_HIDDEN') in added:
            self._notify_minimized()
        elif self._get_atom('_NET_WM_STATE_SHADED') in added:
            self._notify_shaded()
        # unset
        if self._get_atom('_NET_WM_STATE_FULLSCREEN') in removed:
            self._notify_unset_fullscreened()
        elif (self._get_atom('_NET_WM_STATE_MAXIMIZED_VERT') in removed
              and self._get_atom('_NET_WM_STATE_MAXIMIZED_HORZ') in removed):
            self._notify_unset_maximized()
        elif self._get_atom('_NET_WM_STATE_HIDDEN') in removed:
            self._notify_unset_minimized()
        elif self._get_atom('_NET_WM_STATE_SHADED') in added:
            self._notify_unset_shaded()

    def _notify_fullscreened(self, ):
        r"""SUMMARY

        _notify_fullscreened()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_window_fullscreened(self)

    def _notify_unset_fullscreened(self, ):
        r"""SUMMARY

        _notify_unset_fullscreened()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_window_unset_fullscreened(self)

    def _notify_maximized(self, ):
        r"""SUMMARY

        _notify_maximized()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_window_maximized(self)

    def _notify_unset_maximized(self, ):
        r"""SUMMARY

        _notify_unset_maximized()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_window_unset_maximized(self)

    def _notify_minimized(self, ):
        r"""SUMMARY

        _notify_minimized()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_window_minimized(self)

    def _notify_unset_minimized(self, ):
        r"""SUMMARY

        _notify_unset_minimized()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_window_unset_minimized(self)

    def _notify_shaded(self, ):
        r"""SUMMARY

        _notify_shaded()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_window_shaded(self)

    def _notify_unset_shaded(self, ):
        r"""SUMMARY

        _notify_unset_shaded()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_window_unset_shaded(self)

    def _notify_destroyed(self, ):
        r"""SUMMARY

        _notify_destroyed()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_window_destroyed(self.id)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# desktop_window.py ends here
