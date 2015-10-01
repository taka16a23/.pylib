#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: deleteproperty.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""deleteproperty -- a parts of xcb2

DeleteProperty

window: WINDOW
property: ATOM
Errors: Atom, Window

This request deletes the property from the specified window if the property
exists and generates a PropertyNotify event on the window unless the property
does not exist.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['DeleteProperty', 'DeletePropertyChecked', ]


class DeletePropertyAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xII'
    code = 19

    def _getbinary(self, window, property):
        buf = _StringIO()
        buf.write(_pack(self.fmt, window, property))
        return buf.getvalue()


    def __call__(self, window, property):
        """Request DeleteProperty X protocol.

        @Arguments:
        - `window`:
        - `property`:

        @Return:
        VoidCookie

        @Error:
        BadAtom, BadWindow
        """
        return self.request(self._getbinary(window, property))


class DeleteProperty(DeletePropertyAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(window, property)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class DeletePropertyChecked(DeletePropertyAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(window, property)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# deleteproperty.py ends here
