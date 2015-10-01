#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: querykeymap.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""querykeymap -- a parts of xcb2

QueryKeymap

keys: LISTofCARD8

This request returns a bit vector for the logical state of the keyboard. Each
bit set to 1 indicates that the corresponding key is currently pressed. The
vector is represented as 32 bytes. Byte N (from 0) contains the bits for keys 8N
to 8N + 7 with the least significant bit in the byte representing key 8N. Note
that the logical state of a device (as seen by means of the protocol) may lag
the physical state if device event processing is frozen.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import QueryKeymapCookie, QueryKeymapReply


__all__ = ['QueryKeymap', 'QueryKeymapUnchecked', ]


class QueryKeymapAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2x'
    code = 44

    def _getbinary(self, ):
        buf = _StringIO()
        buf.write(_pack(self.fmt, ))
        return buf.getvalue()

    def __call__(self, ):
        """Request QueryKeymap X protocol.

        @Return:
        QueryKeymapCookie
        """
        return self.request(self._getbinary())


class QueryKeymap(QueryKeymapAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request()

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            QueryKeymapCookie(), QueryKeymapReply)


class QueryKeymapUnchecked(QueryKeymapAbstract):
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
            QueryKeymapCookie(), QueryKeymapReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# querykeymap.py ends here
