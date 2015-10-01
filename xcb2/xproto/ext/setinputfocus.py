#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: setinputfocus.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""setinputfocus -- a parts of xcb2

SetInputFocus

focus: WINDOW or PointerRoot or None
revert-to: { Parent, PointerRoot, None}
time: TIMESTAMP or CurrentTime

Errors: Match, Value, Window

This request changes the input focus and the last-focus-change time. The request
has no effect if the specified time is earlier than the current
last-focus-change time or is later than the current server time. Otherwise, the
last-focus-change time is set to the specified time with CurrentTime replaced by
the current server time.

If None is specified as the focus, all keyboard events are discarded until a new
focus window is set. In this case, the revert-to argument is ignored.

If a window is specified as the focus, it becomes the keyboard's focus
window. If a generated keyboard event would normally be reported to this window
or one of its inferiors, the event is reported normally. Otherwise, the event is
reported with respect to the focus window.

If PointerRoot is specified as the focus, the focus window is dynamically taken
to be the root window of whatever screen the pointer is on at each keyboard
event. In this case, the revert-to argument is ignored.

This request generates FocusIn and FocusOut events.

The specified focus window must be viewable at the time of the request (or a
Match error results). If the focus window later becomes not viewable, the new
focus window depends on the revert-to argument. If revert-to is Parent, the
focus reverts to the parent (or the closest viewable ancestor) and the new
revert-to value is taken to be None. If revert-to is PointerRoot or None, the
focus reverts to that value. When the focus reverts, FocusIn and FocusOut events
are generated, but the last-focus-change time is not affected.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['SetInputFocus', 'SetInputFocusChecked', ]


class SetInputFocusAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xII'
    code = 42

    def _getbinary(self, revert_to, focus, time):
        buf = _StringIO()
        buf.write(_pack(self.fmt, revert_to, focus, time))
        return buf.getvalue()

    def __call__(self, revert_to, focus, time):
        """Request SetInputFocus X protocol.

        @Arguments:
        - `revert_to`:
        - `focus`:
        - `time`:

        @Return:
        VoidCookie

        @Error:
        BadMatch, BadValue, BadWindow
        """
        return self.request(self._getbinary(revert_to, focus, time))


class SetInputFocus(SetInputFocusAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(revert_to, focus, time)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class SetInputFocusChecked(SetInputFocusAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(revert_to, focus, time)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# setinputfocus.py ends here
