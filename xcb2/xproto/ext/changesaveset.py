#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: changesaveset.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""changesaveset -- a parts of xcb2

ChangeSaveSet

window: WINDOW
mode: { Insert, Delete}

Errors: Match, Value, Window

This request adds or removes the specified window from the client's
save-set. The window must have been created by some other client (or a Match
error results). For further information about the use of the save-set, see
section 10.

When windows are destroyed, the server automatically removes them from the
save-set.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['ChangeSaveSet', 'ChangeSaveSetChecked', ]


class ChangeSaveSetAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xI'
    code = 6

    def _getbinary(self, mode, window):
        buf = _StringIO()
        buf.write(_pack(self.fmt, mode, window))
        return buf.getvalue()

    def __call__(self, mode, window):
        """ChangeSaveSet

        @Arguments:
        - `mode`:
        - `window`: (int)

        @Return:
        VoidCookie

        @Error:
        BadMatch, BadValue, BadWindow
        """
        return self.request(self._getbinary(mode, window))


class ChangeSaveSet(ChangeSaveSetAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(mode, window)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class ChangeSaveSetChecked(ChangeSaveSetAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(mode, window)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# changesaveset.py ends here
