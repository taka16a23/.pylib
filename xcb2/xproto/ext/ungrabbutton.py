#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: ungrabbutton.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""ungrabbutton -- a parts of xcb2

UngrabButton

modifiers: SETofKEYMASK or AnyModifier
button: BUTTON or AnyButton
grab-window: WINDOW

Errors: Value, Window

This request releases the passive button/key combination on the specified window
if it was grabbed by this client. A modifiers argument of AnyModifier is
equivalent to issuing the request for all possible modifier combinations
(including the combination of no modifiers). A button of AnyButton is equivalent
to issuing the request for all possible buttons. The request has no effect on an
active grab.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['UngrabButton', 'UngrabButtonChecked', ]


class UngrabButtonAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xIH2x'
    code = 29

    def _getbinary(self, button, grab_window, modifiers):
        buf = _StringIO()
        buf.write(_pack(self.fmt, button, grab_window, modifiers))
        return buf.getvalue()

    def __call__(self, button, grab_window, modifiers):
        """Request UngrabButton X protocol.

        @Arguments:
        - `button`:
        - `grab_window`:
        - `modifiers`:

        @Return:
        VoidCookie

        @Error:
        BadValue, BadWindow
        """
        return self.request(self._getbinary(button, grab_window, modifiers))


class UngrabButton(UngrabButtonAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(button, grab_window, modifiers)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class UngrabButtonChecked(UngrabButtonAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(button, grab_window, modifiers)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# ungrabbutton.py ends here
