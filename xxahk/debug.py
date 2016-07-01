#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""debug -- DESCRIPTION

"""
from xahk.bind.key import (KeyBindServiceObserver, KeyBindService,
                            GlobalKeyBinder, KeyEventHandler)
from xahk.bind.mouse import MouseBindServiceObserver, MouseBindService
from xahk.input.keyboard import Keyboard
from xahk.input.mouse import Mouse
from xahk.x11.modifier import Modifier
from xahk.bind.accelerator import Accelerator
from xahk.listener.client_observer import WindowClientListenerObserver
from xahk.log import logging
from xahk.listener.window_manager_observer import WindowManagerListenerObserver
from xahk.listener.window_manager import WindowManagerListener
from xahk.events.listener import EventListener
from xahk.events.loop import EventLoop
from xahk.x11.display import Display
from xahk.events.loop_observer import EventLoopObserver

from xcb.xproto import ButtonPressEvent


class DebugKeyBindServiceObserver(KeyBindServiceObserver, MouseBindServiceObserver):
    r"""DebugKeyBindServiceObserver

    DebugKeyBindServiceObserver is a KeyBindServiceObserver.
    Responsibility:
    """
    def __init__(self, start=True):
        r"""
        """
        self.keyboard = Keyboard()
        if start:
            self.start()

    def on_builded_binder(self, binder):
        r"""SUMMARY

        on_builded_binder(binder)

        @Arguments:
        - `binder`:

        @Return:

        @Error:
        """
        print('')
        print('*** KeyBinding  {0.id} {0.wmclass}'.format(binder.client))
        print('  "{0.title}"'.format(binder.client))
        for acc, handler in binder.iter_binding():
            key = self.keyboard.get_key(acc.get_code())
            keyname = key.get_label()
            if acc.get_modifiers().isflaged(Modifier.Mask.Shift):
                keyname = key.get_shift_label() or keyname
            mods = [str(Modifier.Mask(mod)).split('.')[1] for mod in acc.modifiers if mod]
            print('    ("{}", {}) = {}'.format(
                keyname, str(mods).replace("'", ''), str(handler)))

    def on_updated_binder(self, bindservice, window):
        r"""SUMMARY

        on_updated_binder(bindservice)

        @Arguments:
        - `bindservice`:

        @Return:

        @Error:



        """
        print('')
        print('*** MouseBinding  {0.id} {0.wmclass}'.format(window))
        print('  "{0.title}"'.format(window))
        for acc, handler in bindservice.iter_binding():
            mod = acc.get_modifiers()
            mods = [str(mod.Mask(x)).split('.')[1] for x in mod.list() if x]
            print('    ({}, {}) = {}'.format(
                str(Mouse.Button.Index(acc.get_code())).split('.')[1],
                str(mods).replace("'", ''), handler))

    def start(self, ):
        r"""SUMMARY

        start()

        @Return:

        @Error:
        """
        keybindservice = KeyBindService()
        if not keybindservice.has_observer(self):
            keybindservice.add_observer(self)
        mousebindservice = MouseBindService()
        if not mousebindservice.has_observer(self):
            mousebindservice.add_observer(self)

    def stop(self, ):
        r"""SUMMARY

        stop()

        @Return:

        @Error:
        """
        keybindservice = KeyBindService()
        if keybindservice.has_observer(self):
            keybindservice.remove_observer(self)
        mousebindservice = MouseBindService()
        if mousebindservice.has_observer(self):
            mousebindservice.remove_observer(self)


class Debug(KeyEventHandler):
    r"""Debug

    Debug is a KeyEventHandler.
    Responsibility:
    """
    def __init__(self, start=True):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self.starting = start
        self.debug = DebugKeyBindServiceObserver()

    def on_key_press(self, event):
        r"""SUMMARY

        on_key_press(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        print('DEBUG-1-debug.py')
        if self.starting:
            self.debug.stop()
            self.starting = False
        else:
            self.debug.start()
            self.starting = True


class DebugClientObserver(WindowClientListenerObserver):
    r"""DebugClientObserver

    DebugClientObserver is a ClientListenerObserver.
    Responsibility:
    """
    def __init__(self, client):
        r"""

        @Arguments:
        - `client`:
        """
        self._client = client
        self._cache = {'bounds': self._client.get_bounds(),
                       'title': self._client.get_title(),
                       'pid': self._client.get_pid(),
        }
        self._logger = logging.getLogger('xahk')
        self.start()

    def start(self, ):
        r"""SUMMARY

        start()

        @Return:

        @Error:
        """
        if not self._client.has_observer(self):
            self._client.add_observer(self)

    def stop(self, ):
        r"""SUMMARY

        stop()

        @Return:

        @Error:
        """
        if self._client.has_observer(self):
            self._client.remove_observer(self)

    def on_window_bounds_changed(self, window):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        print('* Window Bounds Changed')
        old = self._cache.get('bounds')
        new = window.get_bounds()
        self._cache['bounds'] = new
        self._logger.debug('  Id:{} Bounds {} => {}'.format(window.id, old, new))
        self._logger.debug('  {}'.format(window.title))

    def on_window_title_changed(self, window):
        r"""SUMMARY

        on_window_title_changed(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        print('* Window Title Changed')
        old = self._cache.get('title')
        new = window.get_title()
        self._cache['title'] = new
        self._logger.debug('  Id:{} title "{}" => "{}"'.format(window.id, old, new))

    def on_window_pid_changed(self, window):
        r"""SUMMARY

        on_window_pid_changed(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        print('* Window Pid Changed')
        old = self._cache.get('pid')
        new = window.get_pid()
        self._cache['pid'] = new
        self._logger.debug('  Id:{} pid {} => {}'.format(window.id, old, new))

    def on_window_fullscreened(self, window):
        r"""SUMMARY

        on_window_fullscreened(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        print('* Window Fullscreened')

    def on_window_unset_fullscreened(self, window):
        r"""SUMMARY

        on_window_unset_fullscreened(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        print('* Window Reset Fullscreened')

    def on_window_maximized(self, window):
        r"""SUMMARY

        on_window_maximized(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        print('* Window Maximized')

    def on_window_unset_maximized(self, window):
        r"""SUMMARY

        on_window_unset_maximized(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        print('* Window Reset Maximized')

    def on_window_minimized(self, window):
        r"""SUMMARY

        on_window_minimized(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        print('* Window Minimized')

    def on_window_unset_minimized(self, window):
        r"""SUMMARY

        on_window_unset_minimized(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        print('* Window Reset Minimized')

    def on_window_shaded(self, window):
        r"""SUMMARY

        on_window_shaded(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        print('* Window Shaded')

    def on_window_unset_shaded(self, window):
        r"""SUMMARY

        on_window_unset_shaded(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        print('* Window Reset Shaded')

    def on_window_destroyed(self, windowid):
        r"""SUMMARY

        on_window_destroyed(windowid)

        @Arguments:
        - `windowid`:

        @Return:

        @Error:
        """
        self.stop()


class DebugClientService(WindowManagerListenerObserver):
    r"""DebugClientService

    DebugClientService is a WindowManagerListenerObserver.
    Responsibility:
    """
    def __init__(self, ):
        r"""
        """
        self._debugging = {}
        self.start()

    def on_created_window_client(self, window):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        self._debugging[window.id] = DebugClientObserver(window)

    def on_destroyed_window_client(self, windowid):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        self._debugging[windowid].stop()
        del self._debugging[windowid]

    def start(self, ):
        r"""SUMMARY

        start()

        @Return:

        @Error:
        """
        wm = WindowManagerListener()
        if wm.has_observer(self):
            return True
        for client in wm.client_list():
            self._debugging[client.id] = DebugClientObserver(client)
        wm.add_observer(self)

    def stop(self, ):
        r"""SUMMARY

        stop()

        @Return:

        @Error:
        """
        wm = WindowManagerListener()
        if not wm.has_observer(self):
            return
        for observer in self._debugging.values():
            observer.stop()
        wm.remove_observer(self)


from xcb.xproto import PropertyNotifyEvent

class DebugListener(EventListener):
    r"""DebugListener

    DebugListener is a EventListener.
    Responsibility:
    """
    def __init__(self, ):
        r"""

        @Arguments:
        - `log`:
        """
        self._log = logging.getLogger('xahk')

    def can_dispatch_event(self, event):
        """SUMMARY

        can_dispatch_event(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        return True

    def handle_event(self, event):
        """SUMMARY

        handle_event(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        self._log.debug('{}'.format(event))
        # if isinstance(event, (PropertyNotifyEvent, )):
            # self._log.debug('{}'.format(Display().core.GetAtomName(event.atom).reply().name.buf()))
        if isinstance(event, (ButtonPressEvent, )):
            self._log.debug('{}'.format(event.event))

class DebugEventLoop(EventLoopObserver):
    r"""DebugEventLoop

    DebugEventLoop is a EventLoopObserver.
    Responsibility:
    """
    def __init__(self, ):
        r"""
        """
        self._log = logging.getLogger('xahk')

    def on_changed_listeners(self, loop):
        """SUMMARY

        name()

        @Return:

        @Error:
        """
        self._log.debug('* EventLoop changed event listeners')
        for listener in loop.list_event_listeners():
            self._log.debug('  {}'.format(listener))

    def on_changed_dispatcher(self, loop):
        """SUMMARY

        on_changed_dispatcher(loop)

        @Arguments:
        - `loop`:

        @Return:

        @Error:
        """
        self._log.debug('* EventLoop changed dispatcher')
        self._log.debug('  changed dispatcher to {}'.format(
            loop.get_event_dispatcher()))

    def on_before_start_loop(self, loop):
        """SUMMARY

        on_before_start_loop(loop)

        @Arguments:
        - `loop`:

        @Return:

        @Error:
        """
        self._log.debug('* EventLoop starting loop')

    def on_after_stopped_loop(self, loop):
        """SUMMARY

        on_after_stopped_loop(loop)

        @Arguments:
        - `loop`:

        @Return:

        @Error:
        """
        self._log.debug('* EventLoop stopping loop')


EventLoop.get_instance(Display()).add_observer(DebugEventLoop())

# DebugClientService()
# EventLoop.get_instance(Display()).add_event_listener(DebugListener())

GLOBALKEY = GlobalKeyBinder()
GLOBALKEY.bind(Accelerator.from_key_label('q', Modifier.Mask.Super), Debug())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# debug.py ends here
