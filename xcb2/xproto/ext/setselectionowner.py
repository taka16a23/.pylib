#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: setselectionowner.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""setselectionowner -- a parts of xcb2

SetSelectionOwner

selection: ATOM
owner: WINDOW or None
time: TIMESTAMP or CurrentTime

Errors: Atom, Window

This request changes the owner, owner window, and last-change time of the
specified selection. This request has no effect if the specified time is earlier
than the current last-change time of the specified selection or is later than
the current server time. Otherwise, the last-change time is set to the specified
time with CurrentTime replaced by the current server time. If the owner window
is specified as None, then the owner of the selection becomes None (that is, no
owner). Otherwise, the owner of the selection becomes the client executing the
request. If the new owner (whether a client or None) is not the same as the
current owner and the current owner is not None, then the current owner is sent
a SelectionClear event.

If the client that is the owner of a selection is later terminated (that is, its
connection is closed) or if the owner window it has specified in the request is
later destroyed, then the owner of the selection automatically reverts to None,
but the last-change time is not affected.

The selection atom is uninterpreted by the server. The owner window is returned
by the GetSelectionOwner request and is reported in SelectionRequest and
SelectionClear events.

Selections are global to the server.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['SetSelectionOwner', 'SetSelectionOwnerChecked', ]


class SetSelectionOwnerAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """
    fmt = '=xx2xIII'
    code = 22

    def _getbinary(self, owner, selection, time):
        buf = _StringIO()
        buf.write(_pack(self.fmt, owner, selection, time))
        return buf.getvalue()

    def __call__(self, owner, selection, time):
        """Request SetSelectionOwner X protocol.

        @Arguments:
        - `owner`:
        - `selection`:
        - `time`:

        @Return:
        VoidCookie

        @Error:
        BadAtom, BadWindow
        """
        return self.request(self._getbinary(owner, selection, time))


class SetSelectionOwner(SetSelectionOwnerAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(owner, selection, time)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class SetSelectionOwnerChecked(SetSelectionOwnerAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(owner, selection, time)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# setselectionowner.py ends here
