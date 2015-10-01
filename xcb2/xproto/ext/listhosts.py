#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""listhosts -- a parts of xcb2

ListHosts

mode: { Enabled, Disabled}
hosts: LISTofHOST
This request returns the hosts on the access control list and whether use of the
list at connection setup is currently enabled or disabled.

Each HOST is padded to a multiple of four bytes.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import ListHostsCookie, ListHostsReply


__all__ = ['ListHosts', 'ListHostsUnchecked', ]


class ListHostsAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2x'
    code = 110

    def _getbinary(self, ):
        buf = _StringIO()
        buf.write(_pack(self.fmt, ))
        return buf.getvalue()

    def __call__(self, ):
        """Request ListHosts X protocol.

        @Return:
        ListHostsCookie
        """
        return self.request(self._getbinary())


class ListHosts(ListHostsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request()

        @Arguments:

        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            ListHostsCookie(), ListHostsReply)


class ListHostsUnchecked(ListHostsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request()

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            ListHostsCookie(), ListHostsReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# listhosts.py ends here
