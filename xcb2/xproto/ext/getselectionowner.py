#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: getselectionowner.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""getselectionowner -- a parts of xcb2

GetSelectionOwner

selection: ATOM

owner: WINDOW or None
Errors: Atom
This request returns the current owner window of the specified selection, if
any. If None is returned, then there is no owner for the selection.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import GetSelectionOwnerCookie, GetSelectionOwnerReply


__all__ = ['GetSelectionOwner', 'GetSelectionOwnerUnchecked', ]


class GetSelectionOwnerAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xI'
    code = 23

    def _getbinary(self, selection):
        buf = _StringIO()
        buf.write(_pack(self.fmt, selection))
        return buf.getvalue()

    def __call__(self, selection):
        """Request GetSelectionOwner X protocol.

        @Arguments:
        - `selection`:

        @Return:
        GetSelectionOwnerCookie

        @Error:
        BadAtom
        """
        return self.request(self._getbinary(selection))


class GetSelectionOwner(GetSelectionOwnerAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(selection)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            GetSelectionOwnerCookie(), GetSelectionOwnerReply)


class GetSelectionOwnerUnchecked(GetSelectionOwnerAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(selection)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            GetSelectionOwnerCookie(), GetSelectionOwnerReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# getselectionowner.py ends here
