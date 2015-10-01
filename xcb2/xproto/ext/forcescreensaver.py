#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: forcescreensaver.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""forcescreensaver -- a parts of xcb2

ForceScreenSaver

mode: { Activate, Reset}

Errors: Value

If the mode is Activate and screen-saver is currently deactivated, then
screen-saver is activated (even if screen-saver has been disabled with a timeout
value of zero). If the mode is Reset and screen-saver is currently enabled, then
screen-saver is deactivated (if it was activated), and the activation timer is
reset to its initial state as if device input had just been received.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['ForceScreenSaver', 'ForceScreenSaverChecked', ]


class ForceScreenSaverAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2x'
    code = 115

    def _getbinary(self, mode):
        buf = _StringIO()
        buf.write(_pack(self.fmt, mode))
        return buf.getvalue()

    def __call__(self, mode):
        """Request ForceScreenSaver X protocol.

        @Arguments:
        - `mode`:

        @Return:
        VoidCookie

        @Error:
        BadValue
        """
        return self.request(self._getbinary(mode))


class ForceScreenSaver(ForceScreenSaverAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(mode)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class ForceScreenSaverChecked(ForceScreenSaverAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(mode)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# forcescreensaver.py ends here
