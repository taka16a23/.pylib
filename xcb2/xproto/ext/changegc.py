#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""changegc -- a parts of xcb2

ChangeGC

gc: GCONTEXT
value-mask: BITMASK
value-list: LISTofVALUE

Errors: Alloc, Font, GContext, Match, Pixmap, Value

This request changes components in gc. The value-mask and value-list specify
which components are to be changed. The values and restrictions are the same as
for CreateGC.

Changing the clip-mask also overrides any previous SetClipRectangles request on
the context. Changing dash-offset or dashes overrides any previous SetDashes
request on the context.

The order in which components are verified and altered is server-dependent. If
an error is generated, a subset of the components may have been altered.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['ChangeGC', 'ChangeGCChecked', ]


class ChangeGCAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xII'
    code = 56

    def _getbinary(self, gc, value_mask, value_list):
        buf = _StringIO()
        buf.write(_pack(self.fmt, gc, value_mask))
        buf.write(str(buffer(_array('I', value_list))))
        return buf.getvalue()

    def __call__(self, gc, value_mask, value_list):
        """Request ChangeGC X protocol.

        @Arguments:
        - `gc`:
        - `value_mask`:
        - `value_list`:

        @Return:
        VoidCookie

        @Error:
        BadAlloc, BadFont, BadGContext, BadMatch, BadPixmap, BadValue
        """
        return self.request(self._getbinary(gc, value_mask, value_list))


class ChangeGC(ChangeGCAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(gc, value_mask, value_list)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class ChangeGCChecked(ChangeGCAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(gc, value_mask, value_list)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# changegc.py ends here
