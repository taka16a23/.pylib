#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""grabpointer -- a parts of xcb2

GrabPointer

grab-window: WINDOW
owner-events: BOOL
event-mask: SETofPOINTEREVENT
pointer-mode, keyboard-mode: { Synchronous, Asynchronous}
confine-to: WINDOW or None
cursor: CURSOR or None
time: TIMESTAMP or CurrentTime

status: { Success, AlreadyGrabbed, Frozen, InvalidTime, NotViewable}

Errors: Cursor, Value, Window

This request actively grabs control of the pointer. Further pointer events are
only reported to the grabbing client. The request overrides any active pointer
grab by this client.

If owner-events is False, all generated pointer events are reported with respect
to grab-window and are only reported if selected by event-mask. If owner-events
is True and a generated pointer event would normally be reported to this client,
it is reported normally. Otherwise, the event is reported with respect to the
grab-window and is only reported if selected by event-mask. For either value of
owner-events, unreported events are simply discarded.

If pointer-mode is Asynchronous, pointer event processing continues normally. If
the pointer is currently frozen by this client, then processing of pointer
events is resumed. If pointer-mode is Synchronous, the state of the pointer (as
seen by means of the protocol) appears to freeze, and no further pointer events
are generated by the server until the grabbing client issues a releasing
AllowEvents request or until the pointer grab is released. Actual pointer
changes are not lost while the pointer is frozen. They are simply queued for
later processing.

If keyboard-mode is Asynchronous, keyboard event processing is unaffected by
activation of the grab. If keyboard-mode is Synchronous, the state of the
keyboard (as seen by means of the protocol) appears to freeze, and no further
keyboard events are generated by the server until the grabbing client issues a
releasing AllowEvents request or until the pointer grab is released. Actual
keyboard changes are not lost while the keyboard is frozen. They are simply
queued for later processing.

If a cursor is specified, then it is displayed regardless of what window the
pointer is in. If no cursor is specified, then when the pointer is in
grab-window or one of its subwindows, the normal cursor for that window is
displayed. Otherwise, the cursor for grab-window is displayed.

If a confine-to window is specified, then the pointer will be restricted to stay
contained in that window. The confine-to window need have no relationship to the
grab-window. If the pointer is not initially in the confine-to window, then it
is warped automatically to the closest edge (and enter/leave events are
generated normally) just before the grab activates. If the confine-to window is
subsequently reconfigured, the pointer will be warped automatically as necessary
to keep it contained in the window.

This request generates EnterNotify and LeaveNotify events.

The request fails with status AlreadyGrabbed if the pointer is actively grabbed
by some other client. The request fails with status Frozen if the pointer is
frozen by an active grab of another client. The request fails with status
NotViewable if grab-window or confine-to window is not viewable or if the
confine-to window lies completely outside the boundaries of the root window. The
request fails with status InvalidTime if the specified time is earlier than the
last-pointer-grab time or later than the current server time. Otherwise, the
last-pointer-grab time is set to the specified time, with CurrentTime replaced
by the current server time.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import GrabPointerCookie, GrabPointerReply


__all__ = ['GrabPointer', 'GrabPointerUnchecked', ]


class GrabPointerAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xIHBBIII'
    code = 26

    def _getbinary(self, owner_events, grab_window, event_mask, pointer_mode,
                keyboard_mode, confine_to, cursor, time):
        buf = _StringIO()
        buf.write(_pack(self.fmt, owner_events, grab_window, event_mask,
                        pointer_mode, keyboard_mode, confine_to, cursor, time))
        return buf.getvalue()

    def __call__(self, owner_events, grab_window, event_mask, pointer_mode,
                keyboard_mode, confine_to, cursor, time):
        """Request GrabPointer X protocol.

        @Arguments:
        - `owner_events`:
        - `grab_window`:
        - `event_mask`:
        - `pointer_mode`:
        - `keyboard_mode`:
        - `confine_to`:
        - `cursor`:
        - `time`:

        @Return:
        GrabPointerCookie

        @Error:
        BadCursor, BadValue, BadWindow
        """
        return self.request(
            self._getbinary(owner_events, grab_window, event_mask, pointer_mode,
                            keyboard_mode, confine_to, cursor, time))


class GrabPointer(GrabPointerAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(owner_events, grab_window, event_mask, pointer_mode,
                keyboard_mode, confine_to, cursor, time)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            GrabPointerCookie(), GrabPointerReply)


class GrabPointerUnchecked(GrabPointerAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(owner_events, grab_window, event_mask, pointer_mode,
                keyboard_mode, confine_to, cursor, time)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            GrabPointerCookie(), GrabPointerReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# grabpointer.py ends here