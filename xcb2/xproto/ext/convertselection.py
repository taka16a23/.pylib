#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: convertselection.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""convertselection -- a parts of xcb2

ConvertSelection

selection, target: ATOM
property: ATOM or None
requestor: WINDOW
time: TIMESTAMP or CurrentTime

Errors: Atom, Window

If the specified selection has an owner, the server sends a SelectionRequest
event to that owner. If no owner for the specified selection exists, the server
generates a SelectionNotify event to the requestor with property None. The
arguments are passed on unchanged in either of the events.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['ConvertSelection', 'ConvertSelectionChecked', ]


class ConvertSelectionAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xIIIII'
    code = 24

    def _getbinary(self, requestor, selection, target, property, time):
        buf = _StringIO()
        buf.write(_pack(self.fmt, requestor, selection, target, property, time))
        return buf.getvalue()


    def __call__(self, requestor, selection, target, property, time):
        """Request ConvertSelection X protocol.

        @Arguments:
        - `requestor`:
        - `selection`:
        - `target`:
        - `property`:
        - `time`:

        @Return:
        VoidCookie

        @Error:
        BadAtom, BadWindow
        """
        return self.request(
            self._getbinary(requestor, selection, target, property, time))


class ConvertSelection(ConvertSelectionAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(requestor, selection, target, property, time)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class ConvertSelectionChecked(ConvertSelectionAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(requestor, selection, target, property, time)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# convertselection.py ends here
