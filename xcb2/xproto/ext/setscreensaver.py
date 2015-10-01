#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: setscreensaver.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""setscreensaver -- a parts of xcb2

SetScreenSaver

timeout, interval: INT16
prefer-blanking: { Yes, No, Default}
allow-exposures: { Yes, No, Default}

Errors: Value

The timeout and interval are specified in seconds; setting a value to -1
restores the default. Other negative values generate a Value error. If the
timeout value is zero, screen-saver is disabled (but an activated screen-saver
is not deactivated). If the timeout value is nonzero, screen-saver is
enabled. Once screen-saver is enabled, if no input from the keyboard or pointer
is generated for timeout seconds, screen-saver is activated. For each screen, if
blanking is preferred and the hardware supports video blanking, the screen will
simply go blank. Otherwise, if either exposures are allowed or the screen can be
regenerated without sending exposure events to clients, the screen is changed in
a server-dependent fashion to avoid phosphor burn. Otherwise, the state of the
screens does not change, and screen-saver is not activated. At the next keyboard
or pointer input or at the next ForceScreenSaver with mode Reset, screen-saver
is deactivated, and all screen states are restored.

If the server-dependent screen-saver method is amenable to periodic change,
interval serves as a hint about how long the change period should be, with zero
hinting that no periodic change should be made. Examples of ways to change the
screen include scrambling the color map periodically, moving an icon image about
the screen periodically, or tiling the screen with the root window background
tile, randomly reorigined periodically.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['SetScreenSaver', 'SetScreenSaverChecked', ]


class SetScreenSaverAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xhhBB'
    code = 107

    def _getbinary(self, timeout, interval, prefer_blanking, allow_exposures):
        buf = _StringIO()
        buf.write(_pack(self.fmt, timeout, interval, prefer_blanking,
                        allow_exposures))
        return buf.getvalue()

    def __call__(self, timeout, interval, prefer_blanking, allow_exposures):
        """Request SetScreenSaver X protocol.

        @Arguments:
        - `timeout`:
        - `interval`:
        - `prefer_blanking`:
        - `allow_exposures`:

        @Return:
        VoidCookie

        @Error:
        BadValue
        """
        return self.request(
            self._getbinary(timeout, interval, prefer_blanking, allow_exposures))


class SetScreenSaver(SetScreenSaverAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(timeout, interval, prefer_blanking, allow_exposures)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class SetScreenSaverChecked(SetScreenSaverAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(timeout, interval, prefer_blanking, allow_exposures)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# setscreensaver.py ends here
