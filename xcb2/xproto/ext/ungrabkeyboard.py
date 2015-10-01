#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: ungrabkeyboard.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""ungrabkeyboard -- a parts of xcb2

UngrabKeyboard

time: TIMESTAMP or CurrentTime This request releases the keyboard if this client
has it actively grabbed (as a result of either GrabKeyboard or GrabKey) and
releases any queued events. The request has no effect if the specified time is
earlier than the last-keyboard-grab time or is later than the current server
time.

This request generates FocusIn and FocusOut events.

An UngrabKeyboard is performed automatically if the event window for an active
keyboard grab becomes not viewable.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['UngrabKeyboard', 'UngrabKeyboardChecked', ]


class UngrabKeyboardAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xI'
    code = 32

    def _getbinary(self, time):
        buf = _StringIO()
        buf.write(_pack(self.fmt, time))
        return buf.getvalue()

    def __call__(self, time):
        """Request UngrabKeyboard X protocol.

        @Arguments:
        - `time`:

        @Return:
        VoidCookie

        @Error:
        None
        """
        return self.request(self._getbinary(time))


class UngrabKeyboard(UngrabKeyboardAbstract):
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


class UngrabKeyboardChecked(UngrabKeyboardAbstract):
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
# ungrabkeyboard.py ends here
