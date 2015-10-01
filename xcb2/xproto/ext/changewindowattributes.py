#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: changewindowattributes.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""ChangeWindowAttributes -- a parts of xcb2

ChangeWindowAttributes
window: WINDOW
value-mask: BITMASK
value-list: LISTofVALUE

Errors: Access, Colormap, Cursor, Match, Pixmap, Value, Window

The value-mask and value-list specify which attributes are to be changed.
The values and restrictions  are the same as for CreateWindow.
Setting a new background, whether by background-pixmap or background-pixel,
overrides any previous background.
Setting a new border, whether by border-pixel or border-pixmap, overrides any
previous border.
Changing the background does not cause the window contents to be changed.
Setting the border or changing the background such that the border tile origin changes causes the border to be repainted.
Changing the background of a root window to None or ParentRelative restores the
default background pixmap. Changing the border of a root window to CopyFromParent
restores the default border pixmap.
Changing the win-gravity does not affect the current position of the window.
Changing the backing-store of an obscured window to WhenMapped or Always or
changing the backing-planes, backing-pixel, or save-under of a mapped window may
have no immediate effect.
Multiple clients can select input on the same window;
their event-masks are disjoint. When an event is generated, it will be reported
to all interested clients. However, only one client at a time can select for
SubstructureRedirect, only one client at a time can select for ResizeRedirect,
and only one client at a time can select for ButtonPress.
An attempt to violate these restrictions results in an Access error.
There is only one do-not-propagate-mask for a window, not one per client.
Changing the colormap of a window (by deﬁning a new map, not by changing the
contents of the existing map) generates a ColormapNotify ev ent.
Changing the colormap of a visible window might have no immediate effect on
the screen (see InstallColormap request).
Changing the cursor of a root window to None restores the default cursor.
The order in which attributes are veriﬁed and altered is server-dependent.
If an error is generated, a subset of the attributes may have been altered.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['ChangeWindowAttributes', 'ChangeWindowAttributesChecked', ]


class ChangeWindowAttributesAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """
    _head = _pack('=xx2x')
    fmt = 'II'
    code = 2

    def _getbinary(self, window, value_mask, value_list):
        buf = _StringIO()
        buf.write(self._head)
        buf.write(_pack(self.fmt, window, value_mask))
        buf.write(str(buffer(_array('I', value_list))))
        return buf.getvalue()

    def __call__(self, window, value_mask, value_list):
        """ChangeWindowAttributes X protocol request.

        @Arguments:
        - `window`: (int)
        - `value_mask`: (int)
        - `value_list`: (list)

        @Return:
        VoidCookie

        @Error:
        BadAccess, BadColormap, BadCursor, BadMatch, BadPixmap, BadValue,
        BadWindow
        """
        return self.request(self._getbinary(window, value_mask, value_list))


class ChangeWindowAttributes(ChangeWindowAttributesAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(window, value_mask, value_list)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class ChangeWindowAttributesChecked(ChangeWindowAttributesAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(window, value_mask, value_list)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# changewindowattributes.py ends here
