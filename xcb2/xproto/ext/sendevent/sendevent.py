#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: sendevent.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""sendevent -- a parts of xcb2

SendEvent

destination: WINDOW or PointerWindow or InputFocus
propagate: BOOL
event-mask: SETofEVENT
event: <normal-event-format>

Errors: Value, Window

If PointerWindow is specified, destination is replaced with the window that the
pointer is in. If InputFocus is specified and the focus window contains the
pointer, destination is replaced with the window that the pointer is
in. Otherwise, destination is replaced with the focus window.

If the event-mask is the empty set, then the event is sent to the client that
created the destination window. If that client no longer exists, no event is
sent.

If propagate is False, then the event is sent to every client selecting on
destination any of the event types in event-mask.

If propagate is True and no clients have selected on destination any of the
event types in event-mask, then destination is replaced with the closest
ancestor of destination for which some client has selected a type in event-mask
and no intervening window has that type in its do-not-propagate-mask. If no such
window exists or if the window is an ancestor of the focus window and InputFocus
was originally specified as the destination, then the event is not sent to any
clients. Otherwise, the event is reported to every client selecting on the final
destination any of the types specified in event-mask.

The event code must be one of the core events or one of the events defined by an
extension (or a Value error results) so that the server can correctly byte-swap
the contents as necessary. The contents of the event are otherwise unaltered and
unchecked by the server except to force on the most significant bit of the event
code and to set the sequence number in the event correctly.

Active grabs are ignored for this request.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto.ext.sendevent.keypress import KeyPress
from xcb2.xproto.ext.sendevent.keyrelease import KeyRelease
from xcb2.xproto.ext.sendevent.buttonpress import ButtonPress
from xcb2.xproto.ext.sendevent.buttonrelease import ButtonRelease
from xcb2.xproto.ext.sendevent.clientmessage import ClientMessage
from xcb2.xproto.ext.sendevent.motionnotify import MotionNotify


__all__ = ['SendEvent', 'SendEventChecked', ]


class SendEventAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xII'
    code = 25

    def __init__(self, connection):
        r"""SUMMARY

        __init__(connection)

        @Arguments:
        - `connection`:

        @Return:
        """
        CoreMethodAbstract.__init__(self, connection)
        self.KeyPress = KeyPress(self)
        self.KeyRelease = KeyRelease(self)
        self.ButtonPress = ButtonPress(self)
        self.ButtonRelease = ButtonRelease(self)
        self.ClientMessage = ClientMessage(self)
        self.MotionNotify = MotionNotify(self)

    def _getbinary(self, propagate, destination, event_mask, event):
        buf = _StringIO()
        buf.write(_pack(self.fmt, propagate, destination, event_mask))
        buf.write(str(buffer(_array('b', event))))
        return buf.getvalue()

    def __call__(self, propagate, destination, event_mask, event):
        """Request SendEvent X protocol.

        @Arguments:
        - `propagate`:
        - `destination`:
        - `event_mask`:
        - `event`:

        @Return:
        VoidCookie

        @Error:
        BadValue, BadWindow
        """
        return self.request(
            self._getbinary(propagate, destination, event_mask, event))


class SendEvent(SendEventAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(propagate, destination, event_mask, event)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class SendEventChecked(SendEventAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(propagate, destination, event_mask, event)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sendevent.py ends here
