#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""querytree -- a parts of xcb2

QueryTree

window: WINDOW

root: WINDOW
parent: WINDOW or None
children: LISTofWINDOW

Errors: Window

This request returns the root, the parent, and the children of the window.
The children are listed in bottom-to-top stacking order.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import QueryTreeCookie, QueryTreeReply
from xcb2.xproto.wcookie import WrapQueryTreeCookie
from xcb2.xobj import Window


__all__ = ['QueryTree', 'QueryTreeUnchecked', ]


class QueryTreeAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """
    fmt = '=xx2xI'
    code = 15

    def _getbinary(self, window):
        buf = _StringIO()
        buf.write(_pack(self.fmt, window))
        return buf.getvalue()

    def __call__(self, window):
        """Request QueryTree X protocol.

        @Arguments:
        - `window`: (int)

        @Return:
        WrapQueryTreeCookie

        @Error:
        BadWindow
        """
        return WrapQueryTreeCookie(
            self._connection, self.request(self._getbinary(window)))

    def recursive(self, window):
        r"""SUMMARY

        recursive(window)

        @Arguments:
        - `window`:

        @Return:
        """
        yield Window(self._connection, window)
        for win in self(window).reply().children:
            for win2 in self.recursive(win):
                yield Window(self._connection, win2)


class QueryTree(QueryTreeAbstract):
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
            QueryTreeCookie(), QueryTreeReply)


class QueryTreeUnchecked(QueryTreeAbstract):
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
            QueryTreeCookie(), QueryTreeReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# querytree.py ends here
