#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: listproperties.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""listproperties -- a parts of xcb2

ListProperties

window: WINDOW

atoms: LISTofATOM
Errors: Window

This request returns the atoms of properties currently defined on the window.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import ListPropertiesCookie, ListPropertiesReply
from xcb2.xproto.wcookie import WrapListPropertyCookie


__all__ = ['ListProperties', 'ListPropertiesUnchecked', ]


class ListPropertiesAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xI'
    code = 21

    def _getbinary(self, window):
        buf = _StringIO()
        buf.write(_pack(self.fmt, window))
        return buf.getvalue()

    def __call__(self, window):
        """Request ListProperties X protocol.

        @Arguments:
        - `window`: (int)

        @Return:
        WrapListPropertyCookie

        @Error:
        BadWindow
        """
        return WrapListPropertyCookie(
            self._connection, self.request(self._getbinary(window)))


class ListProperties(ListPropertiesAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(window)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            ListPropertiesCookie(), ListPropertiesReply)


class ListPropertiesUnchecked(ListPropertiesAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(window)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            ListPropertiesCookie(), ListPropertiesReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# listproperties.py ends here
