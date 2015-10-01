#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""queryextension -- a parts of xcb2

QueryExtension

name: STRING8

present: BOOL
major-opcode: CARD8
first-event: CARD8
first-error: CARD8
This request determines if the named extension is present. If so, the major
opcode for the extension is returned, if it has one. Otherwise, zero is
returned. Any minor opcode and the request formats are specific to the
extension. If the extension involves additional event types, the base event type
code is returned. Otherwise, zero is returned. The format of the events is
specific to the extension. If the extension involves additional error codes, the
base error code is returned. Otherwise, zero is returned. The format of
additional data in the errors is specific to the extension.

The extension name should use the ISO Latin-1 encoding, and uppercase and
lowercase matter.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import QueryExtensionCookie, QueryExtensionReply


__all__ = ['QueryExtension', 'QueryExtensionUnchecked', ]


class QueryExtensionAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xH2x'
    code = 98

    def _getbinary(self, name_len, name):
        buf = _StringIO()
        buf.write(_pack(self.fmt, name_len))
        buf.write(str(buffer(_array('b', name))))
        return buf.getvalue()

    def __call__(self, name_len, name):
        """Request QueryExtension X protocol.

        @Arguments:
        - `name_len`:
        - `name`:

        @Return:
        QueryExtensionCookie
        """
        return self.request(self._getbinary(name_len, name))


class QueryExtension(QueryExtensionAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(name_len, name)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            QueryExtensionCookie(), QueryExtensionReply)


class QueryExtensionUnchecked(QueryExtensionAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(name_len, name)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            QueryExtensionCookie(), QueryExtensionReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# queryextension.py ends here
