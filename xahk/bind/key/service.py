#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""service -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod

from xcb.xproto import GrabMode, KeyPressEvent, KeyReleaseEvent
from xcb.xproto import BadWindow
from xcb import Exception as XCBException

from xahk.x11.display import Display
from xahk.x11.modifier import Modifier
from xahk.events.listener import EventListener
from xahk.events.loop import EventLoop
from xahk.listener.window_manager_observer import WindowManagerListenerObserver
from xahk.listener.window_manager import WindowManagerListener
from xahk.bind.accelerator import Accelerator
from xahk.bind.key.event import KeyEvent
from xahk.utils.observer import Observable
from xahk.utils.singleton import SingletonMeta

from xahk.log import logging


class MissingHandlerInterface(object):
    r"""MissingHandlerInterface

    MissingHandlerInterface is a object.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def on_missing_handler(self, event):
        r"""SUMMARY

        on_missing_handler(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """


class ResendMissingHandler(MissingHandlerInterface):
    r"""ResendMissingHandler

    ResendMissingHandler is a MissingHandlerInterface.
    Responsibility:
    """
    def on_missing_handler(self, event):
        r"""SUMMARY

        on_missing(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        try:
            event.resend().check()
        except BadWindow as err:
            logging.getLogger('xahk').warning(
                '{0} {1}'.format(err.__class__.__name__, err))


class WindowKeyBinder(EventListener):
    r"""WindowKeyBinder

    WindowKeyBinder is a EventListener.
    Responsibility:

    window ごとに作成される。
    window の keybind を保持し　keyevent
    """
    missing_handler = ResendMissingHandler()

    def __init__(self, client):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self.client = client
        self._binding = {}
        self.start_binder()

    @property
    def window(self, ):
        r"""SUMMARY

        window()

        @Return:

        @Error:
        """
        return self.client.get_window()

    def can_dispatch_event(self, event):
        r"""SUMMARY

        can_dispatch_event(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        return (isinstance(event, (KeyPressEvent, KeyReleaseEvent))
                and event.event == int(self.client))

    def handle_event(self, event):
        r"""SUMMARY

        handle_event(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        keyevent = KeyEvent(event, self.client)
        accelerator = Accelerator(keyevent.get_code(), keyevent.get_modifiers())
        handler = self._binding.get(accelerator, None)
        if handler is None:
            self.missing_handler.on_missing_handler(keyevent)
            return
        try:
            handler.on_key_event(keyevent)
        except StandardError as err:
            logging.getLogger('xahk').warning(
                '{0} {1}'.format(err.__class__.__name__, err))
        except XCBException as err:
            logging.getLogger('xahk').warning(
                '{0} {1}'.format(err.__class__.__name__, err))

    def bind(self, accelerator, handler):
        r"""SUMMARY

        bind(accelerator, handler)

        @Arguments:
        - `accelerator`:
        - `handler`:

        @Return:

        @Error:

        handler require method "on_key_event"
        """
        accelerators = (accelerator,
                        accelerator|Modifier.Mask.Numlock,
                        accelerator|Modifier.Mask.Lock,
                        accelerator|Modifier.Mask.Mod5,
                        accelerator|Modifier.Mask.Numlock|Modifier.Mask.Lock,
                        accelerator|Modifier.Mask.Numlock|Modifier.Mask.Mod5,
                        accelerator|Modifier.Mask.Lock|Modifier.Mask.Mod5,
                        accelerator|Modifier.Mask.Numlock|Modifier.Mask.Lock|Modifier.Mask.Mod5
        )
        cookies = []
        append = cookies.append
        for acc in accelerators:
            self._binding[acc] = handler
            append(self.window.grab_key_checked(
                False, acc.get_modifiers(), acc.get_code(),
                GrabMode.Async, GrabMode.Async))
        return cookies

    def unbind(self, accelerator):
        r"""SUMMARY

        unbind(accelerator)

        @Arguments:
        - `accelerator`:

        @Return:

        @Error:
        """
        accelerators = (accelerator,
                        accelerator|Modifier.Mask.Numlock,
                        accelerator|Modifier.Mask.Lock,
                        accelerator|Modifier.Mask.Mod5,
                        accelerator|Modifier.Mask.Numlock|Modifier.Mask.Lock,
                        accelerator|Modifier.Mask.Numlock|Modifier.Mask.Mod5,
                        accelerator|Modifier.Mask.Lock|Modifier.Mask.Mod5,
                        accelerator|Modifier.Mask.Numlock|Modifier.Mask.Lock|Modifier.Mask.Mod5
        )
        cookies = []
        append = cookies.append
        for acc in accelerators:
            if acc in self._binding:
                del self._binding[acc]
                append(self.window.ungrab_key_checked(
                    acc.get_code(), acc.get_modifiers()))
        return cookies

    def unbind_all(self, ):
        r"""SUMMARY

        unbind_all()

        @Return:

        @Error:
        """
        cookies = []
        extend = cookies.extend
        for accelerator in self._binding.keys():
            extend(self.unbind(accelerator))
        return cookies

    def list_accelerators(self, ):
        r"""SUMMARY

        list_accelerators()

        @Return:

        @Error:
        """
        return self._binding.keys()

    def list_handlers(self, ):
        r"""SUMMARY

        list_handlers()

        @Return:

        @Error:
        """
        return self._binding.values()

    def iter_binding(self, ):
        r"""SUMMARY

        iter_binding()

        @Return:

        @Error:
        """
        return self._binding.iteritems()

    def start_binder(self, ):
        """SUMMARY

        start_binder()

        @Return:

        @Error:
        """
        loop = EventLoop.get_instance(self.client.get_display())
        if not loop.has_event_listener(self):
            loop.add_event_listener(self)

    def stop_binder(self, ):
        """SUMMARY

        stop_binder()

        @Return:

        @Error:
        """
        for cookie in self.unbind_all():
            try:
                cookie.check()
            except BadWindow as err:
                break
        loop = EventLoop.get_instance(self.client.get_display())
        if loop.has_event_listener(self):
            loop.remove_event_listener(self)

    def __repr__(self):
        return '{0.__class__.__name__}(id={1})'.format(self, self.client.id)



class KeyBindService(Observable, WindowManagerListenerObserver):
    r"""KeyBindService

    KeyBindService is a object.
    Responsibility:
    """
    __metaclass__ = SingletonMeta

    def __init__(self, ):
        r"""

        @Arguments:
        - `display`:
        """
        Observable.__init__(self)
        self.display = Display()
        self._binders = {}
        self._candidates = []

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self.display

    def add_candidate(self, candidate):
        r"""SUMMARY

        add_candidate(candidate)

        @Arguments:
        - `candidate`:

        @Return:

        @Error:
        """
        self._candidates.append(candidate)
        self._candidates.sort(key=lambda x: x.priority)
        self.reload()

    def remove_candidate(self, candidate):
        r"""SUMMARY

        remove_candidate(candidate)

        @Arguments:
        - `candidate`:

        @Return:

        @Error:
        """
        self._candidates.remove(candidate)
        self.reload()

    def has_candidate(self, candidate):
        r"""SUMMARY

        has_candidate(candidate)

        @Arguments:
        - `candidate`:

        @Return:

        @Error:
        """
        return candidate in self._candidates

    def _build_binder(self, binder):
        r"""SUMMARY

        _build_binder(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        cookies = []
        extend = cookies.extend
        for candidate in self._candidates:
            if candidate.can_bind_window(binder.client):
                extend(candidate.build_binder(binder))
        self._notify_builded_binder(binder)
        return cookies

    def _notify_builded_binder(self, binder):
        r"""SUMMARY

        _notify_builded_binder(binder)

        @Arguments:
        - `binder`:

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_builded_binder(binder)

    def start_service(self, ):
        r"""SUMMARY

        start_service()

        @Return:

        @Error:
        """
        wm = WindowManagerListener()
        if wm.has_observer(self):
            return True
        wm.add_observer(self)
        for client in wm.client_list():
            self.on_created_window_client(client)
        return True

    def stop_service(self, ):
        r"""SUMMARY

        stop_service()

        @Return:

        @Error:
        """
        wm = WindowManagerListener()
        if not wm.has_observer(self):
            return
        wm.remove_observer(self)
        cookies = []
        extend = cookies.extend
        for win in self._binders.keys():
            extend(self._binders[win].unbind_all())
        for cookie in cookies:
            cookie.check()
        self._binders.clear()

    def is_starting_service(self, ):
        r"""SUMMARY

        is_starting_service()

        @Return:

        @Error:
        """
        wm = WindowManagerListener()
        return wm.has_observer(self)

    def reload(self, ):
        r"""SUMMARY

        reload()

        @Return:

        @Error:
        """
        if not self.is_starting_service():
            return False
        cookies = []
        extend = cookies.extend
        for win in self._binders.keys():
            extend(self._binders[win].unbind_all())
        for win in self._binders.keys():
            extend(self._build_binder(self._binders[win]))
        for cookie in cookies:
            try:
                cookie.check()
            except BadWindow as err:
                logging.getLogger('xahk').warning(
                    '{} {}'.format(err.__class__.__name__, err))
        return True

    def on_created_window_client(self, window):
        r"""SUMMARY

        on_created_window_client(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        binder = WindowKeyBinder(window)
        self._binders[window] = binder
        for cookie in self._build_binder(binder):
            try:
                cookie.check()
            except BadWindow as err:
                logging.getLogger('xahk').warning(
                    '{} {}'.format(err.__class__.__name__, err))

    def on_destroyed_window_client(self, window_id):
        r"""SUMMARY

        on_destroyed_window_client(window_id)

        @Arguments:
        - `window_id`:

        @Return:

        @Error:
        """
        if window_id in self._binders:
            self._binders[window_id].stop_binder()
            del self._binders[window_id]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# service.py ends here
