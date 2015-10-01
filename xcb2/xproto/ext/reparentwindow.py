#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: reparentwindow.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""reparentwindow -- a parts of xcb2

ReparentWindow

window, parent: WINDOW
x, y: INT16

Errors: Match, Window

If the window is mapped, an UnmapWindow request is performed automatically
first. The window is then removed from its current position in the hierarchy and
is inserted as a child of the specified parent. The x and y coordinates are
relative to the parent's origin and specify the new position of the upper-left
outer corner of the window. The window is placed on top in the stacking order
with respect to siblings. A ReparentNotify event is then generated. The
override-redirect attribute of the window is passed on in this event; a value of
True indicates that a window manager should not tamper with this
window. Finally, if the window was originally mapped, a MapWindow request is
performed automatically.

Normal exposure processing on formerly obscured windows is performed. The server
might not generate exposure events for regions from the initial unmap that are
immediately obscured by the final map.

A Match error is generated if: The new parent is not on the same screen as the
old parent. The new parent is the window itself or an inferior of the
window. The new parent is InputOnly, and the window is not. The window has a
ParentRelative background, and the new parent is not the same depth as the
window.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['ReparentWindow', 'ReparentWindowChecked', ]


class ReparentWindowAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xIIhh'
    code = 7

    def _getbinary(self, window, parent, x, y):
        buf = _StringIO()
        buf.write(_pack(self.fmt, window, parent, x, y))
        return buf.getvalue()

    def __call__(self, window, parent, x, y):
        """ReparentWindow X protocol request.

        @Arguments:
        - `window`: (int)
        - `parent`:
        - `x`:
        - `y`:

        @Return:

        @Error:
        BadMatch, BadWindow
        """
        return self.request(self._getbinary(window, parent, x, y))


class ReparentWindow(ReparentWindowAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(window, parent, x, y)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class ReparentWindowChecked(ReparentWindowAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(window, parent, x, y)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# reparentwindow.py ends here
