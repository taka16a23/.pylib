#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""service -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod
from struct import pack

from xcb.xproto import GrabMode, ButtonPressEvent, ButtonReleaseEvent
from xcb.xproto import EventMask
from xcb import Exception as XCBException

# from xcb.xproto import AccessError
from xahk.x11.eventcode import EventCode
from xahk.x11.window import Window
from xahk.x11.modifier import Modifier
from xahk.x11.display import Display
from xahk.input.mouse import Mouse
from xahk.listener.cursor import CursorListener
from xahk.listener.cursor_observer import CursorListenerObserver
from xahk.events.listener import EventListenerSingleton
from xahk.events.loop import EventLoop
from xahk.bind.accelerator import Accelerator
from xahk.utils.observer import Observable
from xahk.log import logging
from .event import MouseEvent


class MissingMouseHandlerInterface(object):
    r"""MissingMouseHandlerInterface

    MissingMouseHandlerInterface is a object.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def on_missing_mouse_handler(self, event):
        """SUMMARY

        on_missing_mouse_handler(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """

class ResendMissingMouseHandler(MissingMouseHandlerInterface):
    r"""ResendMissingMouseHandler

    ResendMissingMouseHandler is a MissingMouseHandlerInterface.
    Responsibility:
    """
    def __init__(self, ):
        r"""
        """
        self._cursor = CursorListener()

    def on_missing_mouse_handler(self, event):
        """SUMMARY

        name()

        @Return:

        @Error:
        """
        evcode, mask = EventCode.ButtonPress, EventMask.ButtonPress
        if not event.is_pressed():
            evcode, mask = EventCode.ButtonRelease, EventMask.ButtonRelease
        win = self._cursor.get_under_window()
        rep = Display().core.TranslateCoordinates(
            win, int(event.window), event.x, event.y).reply()
        x = -(rep.dst_x - (2 * event.get_x()))
        y = -(rep.dst_y - (2 * event.get_y()))
        ev = pack('BBH4I5HBx', evcode, event.code,
                  0, event.time, event.root, win, event.child,
                  x, y, x, y, event.modifiers, event.same_screen)
        Display().core.SendEventChecked(False, win, mask, ev).check()


class MouseBindService(CursorListenerObserver, Observable, EventListenerSingleton):
    r"""MouseBindService

    MouseBindService is a object.
    Responsibility:
    """
    _release_modifier = {Mouse.Button.Index.Left: Modifier.Mask.Left,
                         Mouse.Button.Index.Middle: Modifier.Mask.Middle,
                         Mouse.Button.Index.Right: Modifier.Mask.Right,
                         Mouse.Button.Index.WheelUp: Modifier.Mask.WheelUp,
                         Mouse.Button.Index.WheelDown: Modifier.Mask.WheelDown,
                         }

    def __init__(self, ):
        r"""

        @Arguments:
        - `display`:
        """
        CursorListenerObserver.__init__(self)
        Observable.__init__(self)
        self._cursor = CursorListener()
        self.missing_handler = ResendMissingMouseHandler()
        self.root= Window(self.display, self.display.get_setup().roots[0].root)
        self._candidates = []
        self._binding = {}

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self._cursor.get_display()

    display = property(get_display)

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
        if self.is_starting():
            self.update_listener()

    def remove_candidate(self, candidate):
        r"""SUMMARY

        remove_candidate(candidate)

        @Arguments:
        - `candidate`:

        @Return:

        @Error:
        """
        self._candidates.remove(candidate)
        if self.is_starting():
            self.update_listener()

    def has_candidate(self, candidate):
        r"""SUMMARY

        has_candidate(candidate)

        @Arguments:
        - `candidate`:

        @Return:

        @Error:
        """
        return candidate in self._candidates

    def list_candidates(self, ):
        r"""SUMMARY

        list_candidates()

        @Return:

        @Error:
        """
        return self._candidates[:]

    def can_dispatch_event(self, event):
        r"""SUMMARY

        can_dispatch_event(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        return (isinstance(event, (ButtonPressEvent, ButtonReleaseEvent))
                and event.event == int(self.root))

    def handle_event(self, event):
        r"""SUMMARY

        handle_event(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        buttonevent = MouseEvent(event)
        accelerator = Accelerator(buttonevent.get_code(), buttonevent.get_modifiers())
        modifiers = accelerator.get_modifiers()
        releasemod = self._release_modifier.get(accelerator.get_code(), 0)
        if modifiers&releasemod != 0:
            accelerator.set_modifiers(modifiers^releasemod)
        handler = self._binding.get(accelerator, None)
        if handler is None:
            self.missing_handler.on_missing_mouse_handler(buttonevent)
            return
        try:
            handler.on_button_event(buttonevent)
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

        handler require method "on_button_event"
        """
        self._binding[accelerator] = handler
        if accelerator.get_modifiers()^Modifier.Mask.Left == 0:
            return []
        if accelerator.get_modifiers()^Modifier.Mask.Middle == 0:
            return []
        if accelerator.get_modifiers()^Modifier.Mask.Right == 0:
            return []
        if accelerator.get_modifiers()^Modifier.Mask.WheelUp == 0:
            return []
        if accelerator.get_modifiers()^Modifier.Mask.WheelDown == 0:
            return []
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
        mask = EventMask.ButtonPress|EventMask.ButtonRelease
        for acc in accelerators:
            self._binding[acc] = handler
            append(self.root.grab_button_checked(
                False, mask, GrabMode.Async, GrabMode.Async, 0, 0,
                acc.get_code(), acc.get_modifiers()))
        return cookies

    def unbind(self, accelerator):
        r"""SUMMARY

        unbind(accelerator)

        @Arguments:
        - `accelerator`:

        @Return:

        @Error:
        """
        if accelerator in self._binding:
            del self._binding[accelerator]
        cookies = []
        append = cookies.append
        if accelerator.get_modifiers()^Modifier.Mask.Left == 0:
            return cookies
        if accelerator.get_modifiers()^Modifier.Mask.Middle == 0:
            return cookies
        if accelerator.get_modifiers()^Modifier.Mask.Right == 0:
            return cookies
        if accelerator.get_modifiers()^Modifier.Mask.WheelUp == 0:
            return cookies
        if accelerator.get_modifiers()^Modifier.Mask.WheelDown == 0:
            return cookies
        accelerators = (accelerator,
                        accelerator|Modifier.Mask.Numlock,
                        accelerator|Modifier.Mask.Lock,
                        accelerator|Modifier.Mask.Mod5,
                        accelerator|Modifier.Mask.Numlock|Modifier.Mask.Lock,
                        accelerator|Modifier.Mask.Numlock|Modifier.Mask.Mod5,
                        accelerator|Modifier.Mask.Lock|Modifier.Mask.Mod5,
                        accelerator|Modifier.Mask.Numlock|Modifier.Mask.Lock|Modifier.Mask.Mod5
        )
        for acc in accelerators:
            if acc in self._binding:
                del self._binding[acc]
            append(self.root.ungrab_button_checked(
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

    def start_service(self, ):
        r"""SUMMARY

        start_service()

        @Return:

        @Error:
        """
        loop = EventLoop.get_instance(self.display)
        if not loop.has_event_listener(self):
            loop.add_event_listener(self)
        if not self._cursor.has_observer(self):
            self._cursor.add_observer(self)
        self.update_listener()

    def stop_service(self, ):
        r"""SUMMARY

        stop_service()

        @Return:

        @Error:
        """
        loop = EventLoop.get_instance(self.display)
        if loop.has_event_listener(self):
            loop.remove_event_listener(self)
        if self._cursor.has_observer(self):
            self._cursor.remove_observer(self)

    def is_starting(self, ):
        r"""SUMMARY

        is_starting()

        @Return:

        @Error:
        """
        loop = EventLoop.get_instance(self.display)
        return loop.has_event_listener(self)

    def __del__(self):
        # Do not imprement "raise"!!
        self.stop_service()

    def update_listener(self, ):
        r"""SUMMARY

        update_listener()

        @Return:

        @Error:
        """
        # TODO: (Atami) [2016/05/27]
        # before update notify
        cookies = []
        extend = cookies.extend
        extend(self.unbind_all())
        window = self._cursor.get_under_window()
        for candidate in self._candidates:
            if candidate.can_bind_window(window):
                extend(candidate.build_binder(self))
        for cookie in cookies:
            cookie.check()
        # TODO: (Atami) [2016/05/27]
        # after update notify
        self._notify_updated_binder(self, window)

    def _notify_updated_binder(self, bindservice, window):
        r"""SUMMARY

        _notify_updated_binder(bindservice)

        @Arguments:
        - `bindservice`:

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_updated_binder(self, window)

    def on_changed_under_window(self, cursor):
        r"""SUMMARY

        on_changed_under_window(cursor)

        called from CursorListener

        @Arguments:
        - `cursor`:

        @Return:

        @Error:
        """
        self.update_listener()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# service.py ends here
