#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: grabbutton.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""grabbutton -- a parts of xcb2

GrabButton

modifiers: SETofKEYMASK or AnyModifier
button: BUTTON or AnyButton
grab-window: WINDOW
owner-events: BOOL
event-mask: SETofPOINTEREVENT
pointer-mode, keyboard-mode: { Synchronous, Asynchronous}
confine-to: WINDOW or None
cursor: CURSOR or None

Errors: Access, Cursor, Value, Window

This request establishes a passive grab. In the future, the pointer is actively
grabbed as described in GrabPointer, the last-pointer-grab time is set to the
time at which the button was pressed (as transmitted in the ButtonPress event),
and the ButtonPress event is reported if all of the following conditions are
true: The pointer is not grabbed and the specified button is logically pressed
when the specified modifier keys are logically down, and no other buttons or
modifier keys are logically down. The grab-window contains the pointer. The
confine-to window (if any) is viewable. A passive grab on the same button/key
combination does not exist on any ancestor of grab-window.

The interpretation of the remaining arguments is the same as for
GrabPointer. The active grab is terminated automatically when the logical state
of the pointer has all buttons released, independent of the logical state of
modifier keys. Note that the logical state of a device (as seen by means of the
protocol) may lag the physical state if device event processing is frozen.

This request overrides all previous passive grabs by the same client on the same
button/key combinations on the same window. A modifier of AnyModifier is
equivalent to issuing the request for all possible modifier combinations
(including the combination of no modifiers). It is not required that all
specified modifiers have currently assigned keycodes. A button of AnyButton is
equivalent to issuing the request for all possible buttons. Otherwise, it is not
required that the button specified currently be assigned to a physical button.

An Access error is generated if some other client has already issued a
GrabButton request with the same button/key combination on the same window. When
using AnyModifier or AnyButton, the request fails completely (no grabs are
established), and an Access error is generated if there is a conflicting grab
for any combination. The request has no effect on an active grab.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import (
    CoreMethodAbstract, CoreSubMethodAbstract)
from xcb2.xproto import NamedButtonIndex, EventMask, GrabMode


__all__ = ['GrabButton', 'GrabButtonChecked', ]


class ButtonAbstract(CoreSubMethodAbstract):
    r"""SUMMARY
    """

    _button = ''
    _press = _pack('H', EventMask.ButtonPress)
    _release = _pack('H', EventMask.ButtonRelease)
    _async = _pack('B', GrabMode.Async)
    _sync = _pack('B', GrabMode.Sync)

    def _getbinary(self, owner_events, grab_window, event_mask, confine_to,
                   cursor, modifiers, pointer_mode, keyboard_mode):
        r"""SUMMARY

        _getbinary()

        @Return:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xIH', owner_events, grab_window, event_mask))
        if pointer_mode:
            buf.write(_pack('B', pointer_mode))
        else:
            buf.write(self._async)
        if keyboard_mode:
            buf.write(_pack('B', keyboard_mode))
        else:
            buf.write(self._async)
        buf.write(_pack('II', confine_to, cursor))
        buf.write(self._button)
        buf.write(_pack('H', modifiers))
        return buf.getvalue()

    def _get_press_binary(self, owner_events, grab_window, confine_to, cursor,
                      modifiers, pointer_mode, keyboard_mode):
        r"""SUMMARY

        _get_pressbuf()

        @Return:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xI', owner_events, grab_window))
        buf.write(self._press)
        if pointer_mode:
            buf.write(_pack('B', pointer_mode))
        else:
            buf.write(self._async)
        if keyboard_mode:
            buf.write(_pack('B', keyboard_mode))
        else:
            buf.write(self._async)
        buf.write(_pack('II', confine_to, cursor))
        buf.write(self._button)
        buf.write(_pack('H', modifiers))
        return buf.getvalue()

    def _get_release_binary(self, owner_events, grab_window, confine_to, cursor,
                        modifiers, pointer_mode, keyboard_mode):
        r"""SUMMARY

        _get_releasebuf(owner_events, grab_window, confine_to, cursor,
                      modifiers, pointer_mode, keyboard_mode)

        @Arguments:
        - `owner_events`:
        - `grab_window`:
        - `confine_to`:
        - `cursor`:
        - `
modifiers`:
        - `pointer_mode`:
        - `keyboard_mode`:

        @Return:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xI', owner_events, grab_window))
        buf.write(self._release)
        if pointer_mode:
            buf.write(_pack('B', pointer_mode))
        else:
            buf.write(self._async)
        if keyboard_mode:
            buf.write(_pack('B', keyboard_mode))
        else:
            buf.write(self._async)
        buf.write(_pack('II', confine_to, cursor))
        buf.write(self._button)
        buf.write(_pack('H', modifiers))
        return buf.getvalue()

    def press(self, owner_events, grab_window, confine_to, cursor, modifiers,
              pointer_mode=None, keyboard_mode=None):
        r"""SUMMARY

        press(owner_events, grab_window, confine_to, cursor, modifier,
        pointer_mode=None, keyboard_mode)

        @Arguments:
        - `owner_events`:
        - `grab_window`:
        - `confine_to`:
        - `cursor`:
        - `modifier`:
        - `pointer_mode`:
        - `keyboard_mode`:

        @Return:
        """
        return self._parent.request(
            self._get_press_binary(owner_events, grab_window, confine_to, cursor,
                               modifiers, pointer_mode, keyboard_mode))

    def release(self, owner_events, grab_window, confine_to, cursor, modifiers,
                pointer_mode=None, keyboard_mode=None):
        r"""SUMMARY

        press(owner_events, grab_window, confine_to, cursor, modifier,
        pointer_mode=None, keyboard_mode)

        @Arguments:
        - `owner_events`:
        - `grab_window`:
        - `confine_to`:
        - `cursor`:
        - `modifier`:
        - `pointer_mode`:
        - `keyboard_mode`:

        @Return:
        """
        return self._parent.request(
            self._get_release_binary(
                owner_events, grab_window, confine_to, cursor, modifiers,
                pointer_mode, keyboard_mode))

    def __call__(self, owner_events, grab_window, event_mask, confine_to,
                 cursor, modifiers, pointer_mode=None, keyboard_mode=None):
        r"""SUMMARY

        press(owner_events, grab_window, confine_to, cursor, modifier,
        pointer_mode=None, keyboard_mode)

        @Arguments:
        - `owner_events`:
        - `grab_window`:
        - `confine_to`:
        - `cursor`:
        - `modifier`:
        - `pointer_mode`:
        - `keyboard_mode`:

        @Return:
        """
        return self._parent.request(
            self._getbinary(owner_events, grab_window, event_mask,
                            confine_to, cursor, modifiers, pointer_mode,
                            keyboard_mode))


class GrabButtonLeft(ButtonAbstract):
    r"""SUMMARY
    """
    _button = _pack('Bx', NamedButtonIndex.Left)


class GrabButtonRight(ButtonAbstract):
    r"""SUMMARY
    """

    _button = _pack('Bx', NamedButtonIndex.Right)


class GrabButtonMiddle(ButtonAbstract):
    r"""SUMMARY
    """

    _button = _pack('Bx', NamedButtonIndex.Middle)


class GrabButtonWheelUp(ButtonAbstract):
    r"""SUMMARY
    """

    _button = _pack('Bx', NamedButtonIndex.WheelUp)


class GrabButtonWheelDown(ButtonAbstract):
    r"""SUMMARY
    """

    _button = _pack('Bx', NamedButtonIndex.WheelDown)


class GrabButtonAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xIHBBIIBxH'
    code = 28

    def __init__(self, parent):
        r"""SUMMARY

        __init__(parent)

        @Arguments:
        - `parent`:

        @Return:
        """
        CoreMethodAbstract.__init__(self, parent)
        self.Left = GrabButtonLeft(self)
        self.Right = GrabButtonRight(self)
        self.Middle = GrabButtonMiddle(self)
        self.WheelUp = GrabButtonWheelUp(self)
        self.WheelDown = GrabButtonWheelDown(self)

    def _getbinary(self, owner_events, grab_window, event_mask, pointer_mode,
                keyboard_mode, confine_to, cursor, button, modifiers):
        buf = _StringIO()
        buf.write(
            _pack(self.fmt,
                  owner_events, grab_window, event_mask, pointer_mode,
                  keyboard_mode, confine_to, cursor, button, modifiers))
        return buf.getvalue()

    def __call__(self, owner_events, grab_window, event_mask, pointer_mode,
                keyboard_mode, confine_to, cursor, button, modifiers):
        """Request GrabButton X protocol.

        @Arguments:
        - `owner_events`:
        - `grab_window`:
        - `event_mask`:
        - `pointer_mode`:
        - `keyboard_mode`:
        - `confine_to`:
        - `cursor`:
        - `button`:
        - `modifiers`:

        @Return:
        VoidCookie

        @Error:
        BadAccess, BadCursor, BadValue, BadWindow
        """
        return self.request(
            self._getbinary(
                owner_events, grab_window, event_mask, pointer_mode,
                keyboard_mode, confine_to, cursor, button, modifiers))


class GrabButton(GrabButtonAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(owner_events, grab_window, event_mask, pointer_mode,
                keyboard_mode, confine_to, cursor, button, modifiers)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class GrabButtonChecked(GrabButtonAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(owner_events, grab_window, event_mask, pointer_mode,
                keyboard_mode, confine_to, cursor, button, modifiers)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# grabbutton.py ends here
