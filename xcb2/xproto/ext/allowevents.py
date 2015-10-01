#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: allowevents.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""allowevents -- a parts of xcb2

AllowEvents

mode: { AsyncPointer, SyncPointer, ReplayPointer, AsyncKeyboard,
SyncKeyboard, ReplayKeyboard, AsyncBoth, SyncBoth}
time: TIMESTAMP or CurrentTime

Errors: Value

This request releases some queued events if the client has caused a device to
freeze. The request has no effect if the specified time is earlier than the
last-grab time of the most recent active grab for the client or if the specified
time is later than the current server time.

For AsyncPointer, if the pointer is frozen by the client, pointer event
processing continues normally. If the pointer is frozen twice by the client on
behalf of two separate grabs, AsyncPointer thaws for both. AsyncPointer has no
effect if the pointer is not frozen by the client, but the pointer need not be
grabbed by the client.

For SyncPointer, if the pointer is frozen and actively grabbed by the client,
pointer event processing continues normally until the next ButtonPress or
ButtonRelease event is reported to the client, at which time the pointer again
appears to freeze. However, if the reported event causes the pointer grab to be
released, then the pointer does not freeze. SyncPointer has no effect if the
pointer is not frozen by the client or if the pointer is not grabbed by the
client.

For ReplayPointer, if the pointer is actively grabbed by the client and is
frozen as the result of an event having been sent to the client (either from the
activation of a GrabButton or from a previous AllowEvents with mode SyncPointer
but not from a GrabPointer), then the pointer grab is released and that event is
completely reprocessed, this time ignoring any passive grabs at or above
(towards the root) the grab-window of the grab just released. The request has no
effect if the pointer is not grabbed by the client or if the pointer is not
frozen as the result of an event.

For AsyncKeyboard, if the keyboard is frozen by the client, keyboard event
processing continues normally. If the keyboard is frozen twice by the client on
behalf of two separate grabs, AsyncKeyboard thaws for both. AsyncKeyboard has no
effect if the keyboard is not frozen by the client, but the keyboard need not be
grabbed by the client.

For SyncKeyboard, if the keyboard is frozen and actively grabbed by the client,
keyboard event processing continues normally until the next KeyPress or
KeyRelease event is reported to the client, at which time the keyboard again
appears to freeze. However, if the reported event causes the keyboard grab to be
released, then the keyboard does not freeze. SyncKeyboard has no effect if the
keyboard is not frozen by the client or if the keyboard is not grabbed by the
client.

For ReplayKeyboard, if the keyboard is actively grabbed by the client and is
frozen as the result of an event having been sent to the client (either from the
activation of a GrabKey or from a previous AllowEvents with mode SyncKeyboard
but not from a GrabKeyboard), then the keyboard grab is released and that event
is completely reprocessed, this time ignoring any passive grabs at or above
(towards the root) the grab-window of the grab just released. The request has no
effect if the keyboard is not grabbed by the client or if the keyboard is not
frozen as the result of an event.

For SyncBoth, if both pointer and keyboard are frozen by the client, event
processing (for both devices) continues normally until the next ButtonPress,
ButtonRelease, KeyPress, or KeyRelease event is reported to the client for a
grabbed device (button event for the pointer, key event for the keyboard), at
which time the devices again appear to freeze. However, if the reported event
causes the grab to be released, then the devices do not freeze (but if the other
device is still grabbed, then a subsequent event for it will still cause both
devices to freeze). SyncBoth has no effect unless both pointer and keyboard are
frozen by the client. If the pointer or keyboard is frozen twice by the client
on behalf of two separate grabs, SyncBoth thaws for both (but a subsequent
freeze for SyncBoth will only freeze each device once).

For AsyncBoth, if the pointer and the keyboard are frozen by the client, event
processing for both devices continues normally. If a device is frozen twice by
the client on behalf of two separate grabs, AsyncBoth thaws for both. AsyncBoth
has no effect unless both pointer and keyboard are frozen by the client.

AsyncPointer, SyncPointer, and ReplayPointer have no effect on processing of
keyboard events. AsyncKeyboard, SyncKeyboard, and ReplayKeyboard have no effect
on processing of pointer events.

It is possible for both a pointer grab and a keyboard grab to be active
simultaneously (by the same or different clients). When a device is frozen on
behalf of either grab, no event processing is performed for the device. It is
possible for a single device to be frozen because of both grabs. In this case,
the freeze must be released on behalf of both grabs before events can again be
processed. If a device is frozen twice by a single client, then a single
AllowEvents releases both.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['AllowEvents', 'AllowEventsChecked', ]


class AllowEventsAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xI'
    code = 35

    def _getbinary(self, mode, time):
        buf = _StringIO()
        buf.write(_pack(self.fmt, mode, time))
        return buf.getvalue()

    def __call__(self, mode, time):
        """Request AllowEvents X protocol.

        @Arguments:
        - `mode`:
        - `time`:

        @Return:
        VoidCookie

        @Error:
        BadValue
        """
        return self.request(self._getbinary(mode, time))


class AllowEvents(AllowEventsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(mode, time)

        @Arguments:

        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class AllowEventsChecked(AllowEventsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(mode, time)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# allowevents.py ends here
