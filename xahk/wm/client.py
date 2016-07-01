#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""window_client -- DESCRIPTION

"""
from array import array
from struct import unpack, pack
from cStringIO import StringIO
from enum import IntEnum

from xcb.xproto import PropMode, ConfigWindow, EventMask, StackMode
from xcb.xproto import BadWindow, BadDrawable

from xahk.rectangle import Rectangle, Point
from xahk.x11.atom_cache import AtomCache
from xahk.x11.eventcode import EventCode
from xahk.x11.request.get_full_property import GetFullProperty
from xahk.log import logging

from xahk.layout.layout_item import LayoutItem


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


class WindowClient(LayoutItem):
    r"""WindowClient

    WindowClient is a object.
    Responsibility:
    """

    def __init__(self, window):
        r"""

        @Arguments:
        - `window`:
        """
        self.window = window
        self._atom_cache = None # lazy load

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self.window.get_display()

    display = property(get_display)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self.window

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
        if isinstance(other, (WindowClient, )):
            return self.id == other.id
        return self.id == other

    def __ne__(self, other):
        return not self == other

    def __hash__(self, ):
        return hash(self.id)

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
            self.display, self.window.id, self._get_atom(prop),
            self._get_atom(types)).set_length(length).build()
        return requestor.request().reply()

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
        try:
            reply = self._get_property('_NET_WM_NAME', 'UTF8_STRING', 100)
        except BadWindow as err:
            logging.getLogger('xahk').warning(
                '{} {}'.format(err.__class__.__name__, err))
            return ''
        string = str(array('B', reply.value).tostring())
        if string != '':
            return string
        # alternate request if _NET_WM_NAME is null
        try:
            reply = self._get_property('WM_NAME', 'STRING', 100)
        except BadWindow as err:
            logging.getLogger('xahk').warning(
                '{} {}'.format(err.__class__.__name__, err))
            return ''
        return str(array('B', reply.value).tostring())

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
        try:
            reply = self._get_property('WM_CLASS', 'STRING', 10)
        except BadWindow as err:
            logging.getLogger('xahk').warning(
                '{} {}'.format(err.__class__.__name__, err))
            return ['', '']
        wmclasses = str(array('B', reply.value).tostring()).split('\x00')
        # make to ['', ''] if wmclass is null
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
        try:
            reply = self._get_property('_NET_WM_PID', 'CARDINAL', 1)
        except BadWindow as err:
            logging.getLogger('xahk').warning(
                '{} {}'.format(err.__class__.__name__, err))
        pids = unpack('I' * reply.value_len, array('B', reply.value).tostring())
        if not pids:
            return None
        return pids[0]

    pid = property(get_pid)

    def get_type(self):
        """function get_type

        returns
        """
        try:
            reply = self._get_property('_NET_WM_WINDOW_TYPE', 'ATOM', 1)
        except BadWindow as err:
            logging.getLogger('xahk').warning(
                '{} {}'.format(err.__class__.__name__, err))
            return ''
        types = unpack('I' * reply.value_len,
                       array('B', reply.value).tostring())
        if not types:
            return ''
        buf = self.display.core.GetAtomName(types[0]).reply().name.buf()
        return str(buf)

    type = property(get_type)

    def get_workspace(self, ):
        r"""SUMMARY

        get_desktop()

        @Return:

        @Error:
        """
        try:
            reply = self._get_property('_NET_WM_DESKTOP', 'CARDINAL', 1)
        except BadWindow as err:
            logging.getLogger('xahk').warning(
                '{} {}'.format(err.__class__.__name__, err))
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
            from xahk.log import logging
            logging.getLogger('xahk').warning(
                '{} {}'.format(err.__class__.__name__, err))
            return None
        except BadWindow as err:
            from xahk.log import logging
            logging.getLogger('xahk').warning(
                '{} {}'.format(err.__class__.__name__, err))
            return None
        root = self.display.get_setup().roots[0].root
        try:
            cood = self.window.translate_coordinates(
                root, geo.x, geo.y).reply()
        except BadWindow as err:
            # TODO: (Atami) [2015/06/02]
            from xahk.log import logging
            logging.getLogger('xahk').warning(
                '{} {}'.format(err.__class__.__name__, err))
            return None
        newx = cood.dst_x - (2 * geo.x)
        newy = cood.dst_y - (2 * geo.y)
        return Rectangle.Builder(newx, newy, geo.width, geo.height).build()

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

    def set_bounds(self, rect):
        r"""SUMMARY

        set_bounds(rect)

        @Return:

        @Error:
        """
        return self._configure(
            ConfigWindow.X|ConfigWindow.Y|
            ConfigWindow.Width|ConfigWindow.Height,
            [int(rect.x), int(rect.y), int(rect.width), int(rect.height)])

    def layout(self, rect):
        r"""SUMMARY

        layout(rect)

        @Arguments:
        - `rect`:

        @Return:

        @Error:
        """
        return (self.set_bounds(rect), )

    def set_size(self, size):
        r"""SUMMARY

        set_size(size)

        @Return:

        @Error:
        """
        return self._configure(
            ConfigWindow.Width|ConfigWindow.Height,
            [int(size.width), int(size.height)])

    def move(self, point):
        r"""SUMMARY

        move()

        @Return:

        @Error:
        """
        return self._configure(
            ConfigWindow.X|ConfigWindow.Y, [int(point.x), int(point.y)])

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
        try:
            reply = self._get_property('_NET_WM_STATE', 'ATOM', 5)
        except BadWindow as err:
            logging.getLogger('xahk').warning(
                '{} {}'.format(err.__class__.__name__, err))
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
        try:
            reply = self._get_property('_NET_WM_STATE', 'ATOM', 5)
        except BadWindow as err:
            logging.getLogger('xahk').warning(
                '{} {}'.format(err.__class__.__name__, err))
            return False
        atoms = unpack('I' * reply.value_len,
                       array('B', reply.value).tostring())
        for atom in ('_NET_WM_STATE_MAXIMIZED_VERT', '_NET_WM_STATE_MAXIMIZED_HORZ'):
            if self._get_atom(atom) not in atoms:
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
        try:
            reply = self._get_property('_NET_WM_STATE', 'ATOM', 5)
        except BadWindow as err:
            logging.getLogger('xahk').warning(
                '{} {}'.format(err.__class__.__name__, err))
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

    def unset_always_on_top(self, ):
        r"""SUMMARY

        unset_always_on_top()

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
        try:
            reply = self._get_property('_NET_WM_STATE', 'ATOM', 5)
        except BadWindow as err:
            logging.getLogger('xahk').warning(
                '{} {}'.format(err.__class__.__name__, err))
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
        try:
            reply = self._get_property('_NET_WM_STATE', 'ATOM', 5)
        except BadWindow as err:
            logging.getLogger('xahk').warning(
                '{} {}'.format(err.__class__.__name__, err))
            return False
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
        try:
            reply = self._get_property('_NET_WM_STATE', 'ATOM', 5)
        except BadWindow as err:
            logging.getLogger('xahk').warning(
                '{} {}'.format(err.__class__.__name__, err))
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

    def move_cursor_to(self, point):
        """function move_cursor_to

        point:

        returns
        """
        return self.window.warp_pointer_checked(
            0, 0, 0, 0, 0, int(point.x), int(point.y))

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



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# window_client.py ends here
