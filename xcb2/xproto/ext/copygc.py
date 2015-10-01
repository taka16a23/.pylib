#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: copygc.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""copygc -- a parts of xcb2

CopyGC

src-gc, dst-gc: GCONTEXT
value-mask: BITMASK

Errors: Alloc, GContext, Match, Value

This request copies components from src-gc to dst-gc. The value-mask specifies
which components to copy, as for CreateGC. The two gcontexts must have the same
root and the same depth (or a Match error results).
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['CopyGC', 'CopyGCChecked', ]


class CopyGCAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xIII'
    code = 57

    def _getbinary(self, src_gc, dst_gc, value_mask):
        buf = _StringIO()
        buf.write(_pack(self.fmt, src_gc, dst_gc, value_mask))
        return buf.getvalue()

    def __call__(self, src_gc, dst_gc, value_mask):
        """Request CopyGC X protocol.

        @Arguments:
        - `src_gc`:
        - `dst_gc`:
        - `value_mask`:

        @Return:
        VoidCookie

        @Error:
        BadAlloc, BadGContext, BadMatch, BadValue
        """
        return self.request(self._getbinary(src_gc, dst_gc, value_mask))


class CopyGC(CopyGCAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(src_gc, dst_gc, value_mask)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class CopyGCChecked(CopyGCAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(src_gc, dst_gc, value_mask)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# copygc.py ends here
