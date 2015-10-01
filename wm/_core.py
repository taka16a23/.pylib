#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id$
# $Revision$
# $Date$
# $Author$
# $LastChangedBy$
# $LastChangedDate$
r""" _core -- part of wm

$Revision$

"""

from collections import namedtuple
import sys as _sys
import curses as _curses
from datetime import datetime as _datetime
from time import sleep as _sleep

import psutil as _psutil
from Xlib.display import Display as Display
from Xlib import X as X
from Xlib.protocol.event import ClientMessage as _ClientMessage

from wm._display import _Display
from wm import error

from cache import Cache as _Cache


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision$'
__version__ = '0.1.0'


class Geometry(_Display, _Cache):
    r"""Window geometry Holder.


    `x`: x coordinate
    `y`: y coordinate
    `height`: window vertical size
    `width`: window horizontal size
    """

    def __init__(self, window, display=None, cachetime=0.5):
        r"""Initialize of Geometry.

        @Arguments:
        - `window`: parsable window object from python-xlib.
        - `display`: display object from python-xlib.
        - `cachetime`: interval cache time.
        """
        _Cache.__init__(self, duration=cachetime)
        _Display.__init__(self, display=display)
        self._window = window

    def get_geometry(self, key, force=False):
        r"""Return geometry or cached it of a Window.

        - `force`: skip cached value.

        @Return: dictionary
        """
        # cache return if not reached interval time
        if self._isneed_cache() or force is True:
            geo = self._window.get_geometry()
            translated = self._window.translate_coords(self._root, geo.x, geo.y)
            dic = {'x': -translated.x,
                   'y': -translated.y,
                   'height': geo.height,
                   'width': geo.width, }
            self._set_cache(dic)
            return self._get_cache().get(key, 0)
        return self._get_cache().get(key, 0)

    @property
    def x(self):
        r"""X-coordinate of a Window.

        @Return: integer value
        """
        return self.get_geometry('x')

    @property
    def y(self):
        r"""Y-coordinate of a Window.

        @Return: integer value
        """
        return self.get_geometry('y')

    @property
    def height(self):
        r"""Vertical size of a Window.

        @Return: interger value
        """
        return self.get_geometry('height')

    @property
    def width(self):
        r"""Horizontal size of a Window.

        @Return: integer value
        """
        return self.get_geometry('width')

    def __str__(self):
        r"""Represent geometry.

        @Return: string
        """
        fmt = '\n{0:<7}: {1}'.format
        str_ = ['Geometry', ]
        append = str_.append
        append(fmt('x', self.x))
        append(fmt('y', self.y))
        append(fmt('height', self.height))
        append(fmt('width', self.width))
        return ''.join(str_)

    def __eq__(self, other):
        r"""Compare each x, y, height, width.

        @Return: boolean
        """
        return (self.x == other.x and self.y == other.y and
                self.height == other.height and self.width == other.width)

    def __ne__(self, other):
        r"""Compare each x, y, height, width.

        @Return: boolean
        """
        return not (self.x == other.x and self.y == other.y and
                    self.height == other.height and self.width == other.width)


class _AtomHolder(_Display):
    r"""Atom holder of Xlib."""

    # window type
    _WINDOW_TYPE = _Display._atom('_NET_WM_WINDOW_TYPE')
    _TYPE_DESKTOP = _Display._atom('_NET_WM_WINDOW_TYPE_DESKTOP')
    _TYPE_DOCK = _Display._atom('_NET_WM_WINDOW_TYPE_DOCK')
    _TYPE_TOOLBAR = _Display._atom('_NET_WM_WINDOW_TYPE_TOOLBAR')
    _TYPE_MENU = _Display._atom('_NET_WM_WINDOW_TYPE_MENU')
    _TYPE_UTILITY = _Display._atom('_NET_WM_WINDOW_TYPE_UTILITY')
    _TYPE_SPLASH = _Display._atom('_NET_WM_WINDOW_TYPE_SPLASH')
    _TYPE_DIALOG = _Display._atom('_NET_WM_WINDOW_TYPE_DIALOG')
    _TYPE_NORMAL = _Display._atom('_NET_WM_WINDOW_TYPE_NORMAL')

    # types dictionary
    _TYPES = {_TYPE_DESKTOP: 'Desktop',
              _TYPE_DOCK: 'Dock',
              _TYPE_TOOLBAR: 'Toolbar',
              _TYPE_MENU: 'Menu',
              _TYPE_UTILITY: 'Utility',
              _TYPE_SPLASH: 'Splash',
              _TYPE_DIALOG: 'Dialog',
              _TYPE_NORMAL: 'Normal',
              }

    # state
    _WM_STATE = _Display._atom('_NET_WM_STATE')
    _STATE_MODAL = _Display._atom('_NET_WM_STATE_MODAL')
    _STATE_STICKY = _Display._atom('_NET_WM_STATE_STICKY')
    _STATE_MAXIMIZED_VERT = _Display._atom('_NET_WM_STATE_MAXIMIZED_VERT')
    _STATE_MAXIMIZED_HORZ = _Display._atom('_NET_WM_STATE_MAXIMIZED_HORZ')
    _STATE_SHADED = _Display._atom('_NET_WM_STATE_SHADED')
    _STATE_SKIP_TASKBAR = _Display._atom('_NET_WM_STATE_SKIP_TASKBAR')
    _STATE_SKIP_PAGER = _Display._atom('_NET_WM_STATE_SKIP_PAGER')
    _STATE_HIDDEN = _Display._atom('_NET_WM_STATE_HIDDEN')
    _STATE_FULLSCREEN = _Display._atom('_NET_WM_STATE_FULLSCREEN')
    _STATE_ABOVE = _Display._atom('_NET_WM_STATE_ABOVE')
    _STATE_BELOW = _Display._atom('_NET_WM_STATE_BELOW')
    _STATE_DEMANDS_ATTENTION = _Display._atom('_NET_WM_STATE_DEMANDS_ATTENTION')

    # mode
    _MODE_UNSET = 0
    _MODE_SET = 1
    _MODE_TOGGLE = 2

    _PROTOCOLS = _Display._atom('WM_PROTOCOLS')
    _WM_PID = _Display._atom('_NET_WM_PID')
    _DELETE_WINDOW = _Display._atom('WM_DELETE_WINDOW')
    _CLOSE_WINDOW = _Display._atom('_NET_CLOSE_WINDOW')


class _WMInfo(_AtomHolder):
    r"""Window information.

    - `title`:
    - `klass`:
    - `type`:
    - `pid`:
    - `psname`:
    - `cmdline`:
    - `createtime`:
    - `io`:
    - `openfiles`:
    - `cwd`:
    - `monitor`:
    """

    def __init__(self, display=None):
        r"""Initialize.

        @Arguments:

        - `display`: display object from python-xlib.
        """
        _AtomHolder.__init__(self, display=display)
        try:
            self._ps = _psutil.Process(self.pid)
        except TypeError:
            self._ps = None

    @property
    def title(self):
        r"""Get window name.

        @Return: string
        """
        try:
            return self._window.get_wm_name()
        except:
            return ''

    @property
    def klass(self):
        r"""Get window class.

        @Return: string
        """
        try:
            return self._window.get_wm_class()
        except:
            return ''

    @property
    def type(self):
        r"""Get window types.

        @Return: string of
        Desktop, Dock, Toolbar, Menu, Utility, Splash, Dialog, Normal
        """
        try:
            prpty = (self
                     ._window
                     .get_full_property(self._WINDOW_TYPE, 0)
                     .value.tolist()[0])
            return self._TYPES.get(prpty, '')
        except:
            return ''

    @property
    def pid(self):
        r"""Get window process id.

        @Return: interger or None
        """
        try:
            pid_reply = self._window.get_full_property(self._WM_PID, 0)
            if pid_reply:
                return int(pid_reply.value.tolist()[0])
        except:
            return ''

    @property
    def psname(self):
        r"""Get process name.

        @Return: string
        """
        if self._ps:
            return self._ps.name()
        return ''

    @property
    def cmdline(self):
        r"""Get command line of window.

        @Return: list of string
        """
        if self._ps:
            return self._ps.cmdline
        return ''

    @property
    def createtime(self):
        r"""Get create time.

        @Return: float
        """
        if self._ps:
            return self._ps.create_time
        return ''

    @property
    def io(self):
        r"""Get window input and output.

        @Return: Struct of io
        """
        if self._ps:
            return self._ps.get_io_counters()
        return ''

    @property
    def openfiles(self):
        r"""Get opened files.

        @Return: list of string
        """
        if self._ps:
            return self._ps.get_open_files()
        return ''

    @property
    def cwd(self):
        r"""Get current directory.

        @Return: string
        """
        if self._ps:
            return self._ps.getcwd()
        return ''

    def monitor(self, idle=0.5):
        r"""Realtime monitoring window's informations.

        Press 'Control c' will exit.
        """
        onerror = ''
        stdscr = _curses.initscr()
        _curses.noecho()
        _curses.cbreak()

        maxlen = 20
        while 1:
            try:
                stdscr.addstr(0, 0, '* Press "Control c" will exit. *')
                for num, str_ in enumerate(str(self).split('\n'), start=1):
                    maxlen = max(len(str_), maxlen)
                    stdscr.addstr(num, 0, str_ + ' ' * maxlen)
                # for cursor point to beggining of line
                stdscr.addstr(num + 1, 0, '')
                stdscr.refresh()
                _sleep(idle)
            except error.BadWindow:
                onerror = 'Not exists or closed Window'
            except KeyboardInterrupt:
                onerror = 'Keyboard Interrupted'
                break
            finally:
                _curses.echo()
                _curses.nocbreak()
                _curses.endwin()
                print(onerror)


class _WMActive(_AtomHolder):
    r"""Handling activation of a window."""

    def isactive(self):
        r"""Check window is active.

        @Return:
        boolean
        """
        try:
            return self.id == ActiveWindow(display=self._display).id
        except AttributeError:
            return False

    def activate(self, mode=X.Above):
        r"""Set window to activate.

        @Arguments:
        - `mode`:

        @Return:
        boolean

        activate if mode is X.Above,
        deactivate if mode is X.Below
        """
        self._window.set_input_focus(X.RevertToNone, X.CurrentTime)
        self._window.configure(stack_mode=mode)
        self._sync()
        return self.isactive()

    def deactivate(self):
        r"""Set window to deactivate.

        @Return:
        boolean
        """
        return not self.activate(mode=X.Below)


class _WMMove(_AtomHolder):
    r"""Handling move or resize window."""

    def move(self, **args):
        r"""Move window geometry.

        @Arguments:

        - `x`: x coordinate
        - `y`: y coordinate
        - `height`: vertical size
        - `width`: horizontal size

        @Return: Geometry object
        """
        self._window.configure(**args)
        self._sync()
        return self.geo


class _WMState(_AtomHolder):
    r"""State command Abstract."""

    def _get_state(self):
        r"""Get '_NET_WM_STATE' property of window.

        @Return: list of long interger.
        """
        return self._window.get_full_property(self._WM_STATE, 0).value.tolist()

    def _isinstate(self, atom):
        r"""Check if in state property in window.

        @Arguments:

        - `atom`: display.intern_atom()

        @Return: boolean
        """
        try:
            if atom in self._get_state():
                return True
            return False
        except AttributeError:
            return False

    def _state_cmd(self, data):
        r"""Send state event.

        @Arguments:

        - `data`: state value
        """
        assert data[0] in (0, 1, 2)
        event = _ClientMessage(window=self._window, client_type=self._WM_STATE,
                               data=(32, (data)))
        self._send_event(event,
                         event_mask=X.SubstructureRedirectMask,
                         sender='root')

    def resetall(self):
        r"""SUMMARY

        @Return:
        """
        self.reset_maximize()
        self.reset_fullscreen()
        self.reset_shade()
        self.reset_above()
        self.reset_below()
        # TODO: (Atami) [2013/09/24]
        # self.reset_hide() # not implementated


class _WMMaximize(_WMState):
    r"""Handling Maximize Window."""

    def ismaximize(self):
        r"""Check window is maximizing.

        @Return: boolean
        """
        return (self._isinstate(self._STATE_MAXIMIZED_VERT) and
                self._isinstate(self._STATE_MAXIMIZED_HORZ))

    def _maximize(self, mode):
        r"""Handling maximize window.

        @Arguments:

        - `mode`:
        0 == remove
        1 == add
        2 == toggle
        """
        self._state_cmd(data=[mode, self._STATE_MAXIMIZED_VERT,
                              self._STATE_MAXIMIZED_HORZ, 0, 0])

    def reset_maximize(self):
        r"""Reset maximize window.

        @Return: boolean as True if success command.
        """
        self._maximize(mode=self._MODE_UNSET)
        return not self.ismaximize()

    def maximize(self):
        r"""Set maximize window.

        @Return: boolean as True if success command.
        """
        self._maximize(mode=self._MODE_SET)
        return self.ismaximize()

    def toggle_maximize(self):
        r"""Toggle maximize window."""
        self._maximize(mode=self._MODE_TOGGLE)


class _WMMinimize(_AtomHolder):
    r"""
    """

    def isminimize(self):
        r"""Check window is minimize.

        @Return: boolean
        """
        pass

    def minimize(self):
        r"""SUMMARY

        @Return:
        """
        # TODO: (Atami) [2013/09/24]
        # not implementated
        pass

    def minimizeall(self):
        r"""SUMMARY

        @Return:
        """
        # TODO: (Atami) [2013/09/24]
        # not implementated
        pass

    def reset_minimize_all(self):
        r"""SUMMARY

        @Return:
        """
        # TODO: (Atami) [2013/09/24]
        # not implementated
        pass


class _WMFullscreen(_WMState):
    r"""Handling fullscreen window."""

    def isfullscreen(self):
        r"""Check window is fullscreen.

        @Return: boolean
        """
        return self._isinstate(self._STATE_FULLSCREEN)

    def _fullscreen(self, mode):
        r"""Handling fullscreen window.

        @Arguments:

        - `mode`:
        0 == remove
        1 == add
        2 == toggle
        """
        self._state_cmd(data=[mode, self._STATE_FULLSCREEN, 0, 0, 0])

    def reset_fullscreen(self):
        r"""Reset fullscreen window.

        @Return: boolean as True if success command.
        """
        self._fullscreen(mode=self._MODE_UNSET)
        return not self.isfullscreen()

    def fullscreen(self):
        r"""Set fullscreen window.

        @Return: boolean as True if success command.
        """
        self._fullscreen(mode=self._MODE_SET)
        return self.isfullscreen()

    def toggle_fullscreen(self):
        r"""Toggle fullscreen window."""
        self._fullscreen(mode=self._MODE_TOGGLE)


class _WMShade(_WMState):
    r"""Handling shade window."""

    def isshade(self):
        r"""Check window is shade.

        @Return: boolean
        """
        return self._isinstate(self._STATE_SHADED)

    def _shade(self, mode):
        r"""Handling shade window.

        @Arguments:

        - `mode`:
        0 == remove
        1 == add
        2 == toggle
        """
        self._state_cmd(data=[mode, self._STATE_SHADED, 0, 0, 0])

    def reset_shade(self):
        r"""Reset shade window.

        @Return: boolean as True if success command.
        """
        self._shade(mode=self._MODE_UNSET)
        return not self.isshade()

    def shade(self):
        r"""Set shade window.

        @Return: boolean as True if success command.
        """
        self._shade(mode=self._MODE_UNSET)
        return self.shade()

    def toggle_shade(self):
        r"""Toggle shade window."""
        self._shade(mode=self._MODE_TOGGLE)


class _WMAbove(_WMState):
    r"""Handling above window."""

    def isabove(self):
        r"""Check window is above.

        @Return: boolean
        """
        self._isinstate(self._STATE_ABOVE)

    def _above(self, mode):
        r"""Handling above window.

        @Arguments:

        - `mode`:
        0 == remove
        1 == add
        2 == toggle
        """
        self._state_cmd(data=[mode, self._STATE_ABOVE, 0, 0, 0])

    def reset_above(self):
        r"""Reset above window.

        @Return: boolean as True if success command.
        """
        self._above(mode=self._MODE_UNSET)
        return not self.isabove()

    def above(self):
        r"""Set above window.

        @Return: boolean as True if success command.
        """
        self._above(mode=self._MODE_SET)
        return self.isabove()

    def toggle_above(self):
        r"""Toggle above window."""
        self._above(mode=self._MODE_TOGGLE)


class _WMBelow(_WMState):
    r"""Handling Below window."""

    def isbelow(self):
        r"""Check window is below.

        @Return: boolean
        """
        return self._isinstate(self._STATE_BELOW)

    def _below(self, mode):
        r"""Handling below window.

        @Arguments:

        - `mode`:
        0 == remove
        1 == add
        2 == toggle
        """
        self._state_cmd(data=[mode, self._STATE_BELOW, 0, 0, 0])

    def reset_below(self):
        r"""Reset below window.

        @Return: boolean as True if success command.
        """
        self._below(mode=self._MODE_UNSET)
        return not self.isbelow()

    def below(self):
        r"""Set below window.

        @Return: boolean as True if success command.
        """
        self._below(mode=self._MODE_SET)
        return self.isbelow()

    def toggle_below(self):
        r"""Toggle below window."""
        self._below(mode=self._MODE_TOGGLE)


class _WMHide(_WMState):
    r"""
    """

    def ishide(self):
        r"""SUMMARY

        @Return:
        """
        pass

    def _hide(self):
        r"""SUMMARY

        @Return:
        """
        # TODO: (Atami) [2013/09/23]
        # not implemented
        pass

    def hide(self):
        r"""SUMMARY

        @Return:
        """
        pass

    def toggle_hide(self):
        r"""SUMMARY

        @Return:
        """
        pass


class _WMDestroy(_AtomHolder):
    r"""Handling kill or close window."""

    def kill(self):
        r"""Force close window."""
        event = _ClientMessage(window=self._window, client_type=self._PROTOCOLS,
                    data=(32, [self._DELETE_WINDOW, X.CurrentTime, 0, 0, 0]))
        self._send_event(event=event, event_mask=0, sender='window')

    def close(self):
        r"""Close window."""
        event = _ClientMessage(window=self._window,
                               client_type=self._CLOSE_WINDOW,
                               data=(32, [X.CurrentTime, 0, 0, 0, 0]))
        self._send_event(event=event, event_mask=X.SubstructureRedirectMask,
                         sender='root')


class WindowManager(_WMInfo, _WMActive, _WMMove, _WMAbove, _WMBelow, _WMShade,
                    _WMFullscreen, _WMMaximize, _WMDestroy):
    r"""Handling window.

    Window Information:
    - `id`: integer of this window id.
    - `title`: string of this window name.
    - `klass`: tuple string of this window class.
    - `type`: string of this window type.
    - `pid`: integer of this window pid.
    - `psname`: string of this window's process name.
    - `cmdline`: tuple of string that command line.
    - `createtime`: interger of epoc time that created whis window.
    - `io`: struct of this window's input and output.
    - `openfiles`: tuple of string as opened file path by this window process.
    - `cwd`: string of this window's directory.

    Geometry:
    - `geo.x`: integer of x coordinate.
    - `geo.y`: integer of y coordinate.
    - `geo.height`: interger of vertical this window size.
    - `geo.width`: interger of horizontal this window size.

    Monitoring:
    - `monitor`: function as monitoring above informations.

    Active Window:
    - `isactive`: boolean what is activing this window now.
    - `activate`: boolean what is success command that set activate this window.
    - `deactivate`: boolean what is success command that reset activate this window.

    Maximize Window:
    - `ismaximize`: boolean what is maximizing this window now.
    - `reset_maximize`: boolean what is success command that reset maximize this window.
    - `maximize`: boolean what is success command that set maximize this window.
    - `toggle_maximize` unbound, toggle maximize or reset maximize.

    Fullscreen Window:
    - `isfullscreen`: boolean what is fullscreening this window now.
    - `reset_fullscreen`: boolean what is success command that reset fullscreen this window.
    - `fullscreen`: boolean what is success command that set fullscreen this window.
    - `toggle_fullscreen` unbound, toggle fullscreen or reset fullscreen.

    Shade Window:
    - `isshade`: boolean what is shading this window now.
    - `reset_shade`: boolean what is success command that reset shade this window.
    - `shade`: boolean what is success command that set shade this window.
    - `toggle_shade` unbound, toggle shade or reset shade.

    Above Window:
    - `isabove`: boolean what is aboving this window now.
    - `reset_above`: boolean what is success command that reset above this window.
    - `above`: boolean what is success command that set above this window.
    - `toggle_above` unbound, toggle above or reset above.

    Below Window:
    - `isbelow`: boolean what is belowing this window now.
    - `reset_below`: boolean what is success command that reset below this window.
    - `below`: boolean what is success command that set below this window.
    - `toggle_below` unbound, toggle below or reset below.

    Destroy Window:
    - `kill`: unbound, force delete this window.
    - `close` unbound, close this window.
    """

    def __init__(self, id_, display=None):
        r"""Initialize object.

        Arguments:
        - `id_`: window id
        """
        _WMActive.__init__(self, display=display) # make self._display
        self._window = self._display.create_resource_object('window', id_)
        _WMInfo.__init__(self, display=self._display)
        self.id = self._window.id
        self.geo = Geometry(window=self._window, display=self._display)

    def _send_event(self, event, event_mask=0, propagate=0,
                    onerror=None, sender='root'):
        r"""Sending event.

        @Arguments:

        - `event`: event object
        - `event_mask`:
        - `propagate`:
        """
        if 'root' == sender:
            self._root.send_event(
                event, event_mask=event_mask, propagate=propagate)
        elif 'window' == sender:
            self._window.send_event(
                event, event_mask=event_mask, propagate=propagate)
        self._sync()

    def __str__(self):
        str_ = [str(self.__class__)]
        io = self.io

        keys = (
            'isactive',
            'id',
            'title',
            'klass',
            'type',
            'x',
            'y',
            'height',
            'width',
            'pid',
            'psname',
            'cmdline',
            'ctime',
            'cwd',
            'read count',
            'write count',
            'read bytes',
            'write bytes',
            )

        if not self.createtime:
            timestamp = ''
        else:
            timestamp = _datetime.fromtimestamp(
                int(self.createtime)).strftime('%Y-%m-%d %H:%M:%S')

        if not io:
            from collections import namedtuple
            inout = namedtuple('io', ('read_count write_count'
                                      ' read_bytes write_bytes'))
            io = inout(read_count='', write_count='',
                       read_bytes='', write_bytes='')

        values = (
            self.isactive(),
            self.id,
            self.title,
            self.klass,
            self.type,
            self.geo.x,
            self.geo.y,
            self.geo.height,
            self.geo.width,
            self.pid,
            self.psname,
            ' '.join(self.cmdline),
            timestamp,
            self.cwd,
            io.read_count,
            io.write_count,
            io.read_bytes,
            io.write_bytes,
            )

        leftlen = len(max(keys, key=len)) + 1
        fmt = '\n{0:<' + str(leftlen) + '}: {1}'
        for k, v in zip(keys, values):
            str_.append(fmt.format(k, v))
        # POSTPHONE: (Atami) [2013/09/26]
        # self.openfiles
        return ''.join(str_)

    def __eq__(self, other):
        r"""Compare id.

        @Return: boolean
        """
        return self.id == other.id

    def __ne__(self, other):
        r"""Compare id.

        @Return: not equal boolean
        """
        return not self.id == other.id


class ActiveWindow(WindowManager):
    r"""Handling active window."""

    def __init__(self, display=None):
        r"""Initialize active window.

        @Arguments:

        - `display`: xlib display object
        """
        display = (display or Display())
        win = display.get_input_focus().focus
        if not (win.get_wm_name() or win.get_wm_class()):
            win = win.query_tree().parent
        super(ActiveWindow, self).__init__(id_=win.id, display=display)


def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _core.py ends here
