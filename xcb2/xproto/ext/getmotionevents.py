#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""getmotionevents -- a parts of xcb2

GetMotionEvents

start, stop: TIMESTAMP or CurrentTime
window: WINDOW

events: LISTofTIMECOORD
where:
TIMECOORD:	[x, y: INT16
time: TIMESTAMP]

Errors: Window

This request returns all events in the motion history buffer that fall between
the specified start and stop times (inclusive) and that have coordinates that
lie within (including borders) the specified window at its present
placement. The x and y coordinates are reported relative to the origin of the
window.

If the start time is later than the stop time or if the start time is in the
future, no events are returned. If the stop time is in the future, it is
equivalent to specifying CurrentTime.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import GetMotionEventsCookie, GetMotionEventsReply


__all__ = ['GetMotionEvents', 'GetMotionEventsUnchecked', ]


class GetMotionEventsAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xIII'
    code = 39

    def _getbinary(self, window, start, stop):
        buf = _StringIO()
        buf.write(_pack(self.fmt, window, start, stop))
        return buf.getvalue()

    def __call__(self, window, start, stop):
        """GetMotionEvents

        @Arguments:
        - `window`:
        - `start`:
        - `stop`:

        @Return:
        GetMotionEventsCookie

        @Error:
        BadWindow
        """
        return self.request(self._getbinary(window, start, stop))


class GetMotionEvents(GetMotionEventsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(window, start, stop)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            GetMotionEventsCookie(), GetMotionEventsReply)


class GetMotionEventsUnchecked(GetMotionEventsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(window, start, stop)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            GetMotionEventsCookie(), GetMotionEventsReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# getmotionevents.py ends here
