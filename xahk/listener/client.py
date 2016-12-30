#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""client -- DESCRIPTION

"""
from array import array
from struct import unpack

from xcb.xproto import ConfigureNotifyEvent, PropertyNotifyEvent, DestroyNotifyEvent
from xcb.xproto import CW, EventMask
from xcb.xproto import BadWindow

from xahk.events import EventListener, EventLoop
from xahk.log import logging
from xahk.utils.observer import Observable
from xahk.x11.request.get_full_property import GetFullProperty
from xahk.wm.client import WindowClient


class WindowClientListener(EventListener, Observable, WindowClient):
    r"""WindowClientListener

    WindowClientListener is a object.
    Responsibility:
    """
    def __init__(self, window):
        r"""

        @Arguments:
        - `client`:
        """
        Observable.__init__(self)
        WindowClient.__init__(self, window)
        try:
            your_event_mask = self.window.get_attributes().reply().your_event_mask
        except BadWindow as err:
            logging.getLogger('xahk').warning(
                '{} {}'.format(err.__class__.__name__, err))
            your_event_mask = 0
        reply = self.window.change_attributes(
            CW.EventMask, [EventMask.StructureNotify| # ConfigureNotify
                           EventMask.PropertyChange| # PropertyNotify
                           your_event_mask, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        #try:
        #    reply.check()
        #except BadWindow as err:
        #    logging.getLogger('xahk').warning(
        #        '{} {}'.format(err.__class__.__name__, err))
        self._current_state = self._list_current_state()
        EventLoop.get_instance(self.display).add_event_listener(self)

    def can_dispatch_event(self, event):
        """method can_dispatch_event

        determine dispatchable event.

        event: X event

        returns bool
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
        if event.atom == self._get_atom('_NET_WM_NAME'):
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
        try:
            rep = GetFullProperty.Builder(
                self.display, self.id, self._get_atom('_NET_WM_STATE'),
                self._get_atom('ATOM')).set_length(10).build().request().reply()
        except BadWindow as err:
            logging.getLogger('xahk').warning(
                '{} {}'.format(err.__class__.__name__, err))
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
# client.py ends here
