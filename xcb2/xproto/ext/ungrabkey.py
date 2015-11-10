#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""ungrabkey -- a parts of xcb2

UngrabKey

key: KEYCODE or AnyKey
modifiers: SETofKEYMASK or AnyModifier
grab-window: WINDOW

Errors: Value, Window

This request releases the key combination on the specified window if it was
grabbed by this client. A modifiers argument of AnyModifier is equivalent to
issuing the request for all possible modifier combinations (including the
combination of no modifiers). A key of AnyKey is equivalent to issuing the
request for all possible keycodes. This request has no effect on an active grab.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['UngrabKey', 'UngrabKeyChecked', ]


class UngrabKeyAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xIH2x'
    code = 34

    def _getbinary(self, key, grab_window, modifiers):
        buf = _StringIO()
        buf.write(_pack(self.fmt, key, grab_window, modifiers))
        return buf.getvalue()

    def __call__(self, key, grab_window, modifiers):
        """Request UngrabKey X protocol.

        @Arguments:
        - `key`:
        - `grab_window`:
        - `modifiers`:

        @Return:
        VoidCookie

        @Error:
        BadValue, BadWindow
        """
        return self.request(self._getbinary(key, grab_window, modifiers))


class UngrabKey(UngrabKeyAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(key, grab_window, modifiers)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class UngrabKeyChecked(UngrabKeyAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(key, grab_window, modifiers)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# ungrabkey.py ends here