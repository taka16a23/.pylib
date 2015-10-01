#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: ungrabpointer.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""ungrabpointer -- a parts of xcb2

UngrabPointer

time: TIMESTAMP or CurrentTime
This request releases the pointer if this client has it actively grabbed (from
either GrabPointer or GrabButton or from a normal button press) and releases any
queued events. The request has no effect if the specified time is earlier than
the last-pointer-grab time or is later than the current server time.

This request generates EnterNotify and LeaveNotify events.

An UngrabPointer request is performed automatically if the event window or
confine-to window for an active pointer grab becomes not viewable or if window
reconfiguration causes the confine-to window to lie completely outside the
boundaries of the root window.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['UngrabPointer', 'UngrabPointerChecked', ]


class UngrabPointerAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xI'
    code = 27

    def _getbinary(self, time):
        buf = _StringIO()
        buf.write(_pack(self.fmt, time))
        return buf.getvalue()

    def __call__(self, time):
        """Request UngrabPointer X protocol.

        @Arguments:
        - `time`:

        @Return:
        VoidCookie

        @Error:
        None
        """
        return self.request(self._getbinary(time))


class UngrabPointer(UngrabPointerAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(time)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class UngrabPointerChecked(UngrabPointerAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(time)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# ungrabpointer.py ends here
