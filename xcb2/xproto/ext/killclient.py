#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""killclient -- a parts of xcb2

KillClient

resource: CARD32 or AllTemporary

Errors: Value

If a valid resource is specified, KillClient forces a close-down of the client
that created the resource. If the client has already terminated in either
RetainPermanent or RetainTemporary mode, all of the client's resources are
destroyed (see section 10). If AllTemporary is specified, then the resources of
all clients that have terminated in RetainTemporary are destroyed.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['KillClient', 'KillClientChecked', ]


class KillClientAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xI'
    code = 113

    def _getbinary(self, resource):
        buf = _StringIO()
        buf.write(_pack(self.fmt, resource))
        return buf.getvalue()

    def __call__(self, resource):
        """Request KillClient X protocol.

        @Arguments:
        - `resource`:

        @Return:
        VoidCookie

        @Error:
        BadValue
        """
        return self.request(self._getbinary(resource))


class KillClient(KillClientAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(resource)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class KillClientChecked(KillClientAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(resource)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# killclient.py ends here
