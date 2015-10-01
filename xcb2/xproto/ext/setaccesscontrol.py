#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: setaccesscontrol.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""setaccesscontrol -- a parts of xcb2

SetAccessControl

mode: { Enable, Disable}

Errors: Access, Value

This request enables or disables the use of the access control list at
connection setups.

The client must reside on the same host as the server and/or have been granted
permission by a server-dependent method to execute this request (or an Access
error results).
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['SetAccessControl', 'SetAccessControlChecked', ]


class SetAccessControlAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2x'
    code = 111

    def _getbinary(self, mode):
        buf = _StringIO()
        buf.write(_pack(self.fmt, mode))
        return buf.getvalue()

    def __call__(self, mode):
        """Request SetAccessControl X protocol.

        @Arguments:
        - `mode`:

        @Return:
        VoidCookie

        @Error:
        BadAccess, BadValue
        """
        return self.request(self._getbinary(mode))


class SetAccessControl(SetAccessControlAbstract):
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


class SetAccessControlChecked(SetAccessControlAbstract):
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
# setaccesscontrol.py ends here
