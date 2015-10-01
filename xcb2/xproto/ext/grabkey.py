#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: grabkey.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""grabkey -- a parts of xcb2

GrabKey

key: KEYCODE or AnyKey
modifiers: SETofKEYMASK or AnyModifier
grab-window: WINDOW
owner-events: BOOL
pointer-mode, keyboard-mode: { Synchronous, Asynchronous}

Errors: Access, Value, Window

This request establishes a passive grab on the keyboard. In the future, the
keyboard is actively grabbed as described in GrabKeyboard, the
last-keyboard-grab time is set to the time at which the key was pressed (as
transmitted in the KeyPress event), and the KeyPress event is reported if all of
the following conditions are true: The keyboard is not grabbed and the specified
key (which can itself be a modifier key) is logically pressed when the specified
modifier keys are logically down, and no other modifier keys are logically
down. Either the grab-window is an ancestor of (or is) the focus window, or the
grab-window is a descendent of the focus window and contains the pointer. A
passive grab on the same key combination does not exist on any ancestor of
grab-window.

The interpretation of the remaining arguments is the same as for
GrabKeyboard. The active grab is terminated automatically when the logical state
of the keyboard has the specified key released, independent of the logical state
of modifier keys. Note that the logical state of a device (as seen by means of
the protocol) may lag the physical state if device event processing is frozen.

This request overrides all previous passive grabs by the same client on the same
key combinations on the same window. A modifier of AnyModifier is equivalent to
issuing the request for all possible modifier combinations (including the
combination of no modifiers). It is not required that all modifiers specified
have currently assigned keycodes. A key of AnyKey is equivalent to issuing the
request for all possible keycodes. Otherwise, the key must be in the range
specified by min-keycode and max-keycode in the connection setup (or a Value
error results).

An Access error is generated if some other client has issued a GrabKey with the
same key combination on the same window. When using AnyModifier or AnyKey, the
request fails completely (no grabs are established), and an Access error is
generated if there is a conflicting grab for any combination.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto import GrabMode
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['GrabKey', 'GrabKeyChecked', ]


class GrabKeyAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xIHBBB'
    _tail = _pack('3x')
    code = 33

    _async = _pack('B', GrabMode.Async)
    _sync = _pack('B', GrabMode.Sync)

    def _getbinary(self, owner_events, grab_window, modifiers, key,
                pointer_mode, keyboard_mode):
        buf = _StringIO()
        buf.write(_pack(self.fmt, owner_events, grab_window, modifiers, key,
                pointer_mode, keyboard_mode))
        buf.write(self._tail)
        return buf.getvalue()

    def __call__(self, owner_events, grab_window, modifiers, key,
                pointer_mode, keyboard_mode):
        """Request GrabKey X protocol.

        @Arguments:
        - `owner_events`:
        - `grab_window`:
        - `modifiers`:
        - `key`:
        - `pointer_mode`:
        - `keyboard_mode`:

        @Return:
        VoidCookie

        @Error:
        BadAccess, BadValue, BadWindow
        """
        return self.request(
            self._getbinary(
                owner_events, grab_window, modifiers, key, pointer_mode,
                keyboard_mode))

    def _get_async_binary(self, owner_events, grab_window, modifiers, key):
        r"""SUMMARY

        _get_async_binary(owner_events, grab_window, modifiers, key)

        @Arguments:
        - `owner_events`:
        - `grab_window`:
        - `modifiers`:
        - `key`:

        @Return:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xIHB', owner_events, grab_window, modifiers, key))
        buf.write(self._async) # pointer_mode
        buf.write(self._async) # keyboard_mode
        buf.write(self._tail)
        return buf.getvalue()

    def async(self, owner_events, grab_window, modifiers, key):
        r"""SUMMARY

        async(owner_events, grab_window, modifier, key)

        @Arguments:
        - `owner_events`:
        - `grab_window`:
        - `modifier`:
        - `key`:

        @Return:
        """
        return self.request(
            self._get_async_binary(owner_events, grab_window, modifiers, key))


class GrabKey(GrabKeyAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(owner_events, grab_window, modifiers, key,
                pointer_mode, keyboard_mode)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class GrabKeyChecked(GrabKeyAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(owner_events, grab_window, modifiers, key,
                pointer_mode, keyboard_mode)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# grabkey.py ends here
