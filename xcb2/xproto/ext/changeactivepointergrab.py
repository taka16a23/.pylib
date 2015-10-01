#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: changeactivepointergrab.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""changeactivepointergrab -- a parts of xcb2

ChangeActivePointerGrab

event-mask: SETofPOINTEREVENT
cursor: CURSOR or None
time: TIMESTAMP or CurrentTime

Errors: Cursor, Value

This request changes the specified dynamic parameters if the pointer is actively
grabbed by the client and the specified time is no earlier than the
last-pointer-grab time and no later than the current server time. The
interpretation of event-mask and cursor are the same as in GrabPointer. This
request has no effect on the parameters of any passive grabs established with
GrabButton.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['ChangeActivePointerGrab', 'ChangeActivePointerGrabChecked', ]


class ChangeActivePointerGrabAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xIIH2x'
    code = 30

    def _getbinary(self, cursor, time, event_mask):
        buf = _StringIO()
        buf.write(_pack(self.fmt, cursor, time, event_mask))
        return buf.getvalue()

    def __call__(self, cursor, time, event_mask):
        """Request ChangeActivePointerGrab X protocol.

        @Arguments:
        - `cursor`:
        - `time`:
        - `event_mask`:

        @Return:
        VoidCookie

        @Error:
        BadCursor, BadValue
        """
        return self.request(self._getbinary(cursor, time, event_mask))


class ChangeActivePointerGrab(ChangeActivePointerGrabAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cursor, time, event_mask)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class ChangeActivePointerGrabChecked(ChangeActivePointerGrabAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cursor, time, event_mask)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# changeactivepointergrab.py ends here
