#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""configurewindow -- a parts of xcb2

ConfigureWindow

window: WINDOW
value-mask: BITMASK
value-list: LISTofVALUE
Errors: Match, Value, Window
This request changes the configuration of the window. The value-mask and
value-list specify which values are to be given. The possible values are:

Attribute Type x INT16 y INT16 width CARD16 height CARD16 border-width CARD16
sibling WINDOW stack-mode { Above, Below, TopIf, BottomIf, Opposite } The x and
y coordinates are relative to the parent's origin and specify the position of
the upper-left outer corner of the window. The width and height specify the
inside size, not including the border, and must be nonzero (or a Value error
results). Those values not specified are taken from the existing geometry of the
window. Note that changing just the border-width leaves the outer-left corner of
the window in a fixed position but moves the absolute position of the window's
origin. It is a Match error to attempt to make the border-width of an InputOnly
window nonzero.

If the override-redirect attribute of the window is False and some other client
has selected SubstructureRedirect on the parent, a ConfigureRequest event is
generated, and no further processing is performed. Otherwise, the following is
performed:

If some other client has selected ResizeRedirect on the window and the inside
width or height of the window is being changed, a ResizeRequest event is
generated, and the current inside width and height are used instead. Note that
the override-redirect attribute of the window has no effect on ResizeRedirect
and that SubstructureRedirect on the parent has precedence over ResizeRedirect
on the window.

The geometry of the window is changed as specified, the window is restacked
among siblings, and a ConfigureNotify event is generated if the state of the
window actually changes. If the inside width or height of the window has
actually changed, then children of the window are affected, according to their
win-gravity. Exposure processing is performed on formerly obscured windows
(including the window itself and its inferiors if regions of them were obscured
but now are not). Exposure processing is also performed on any new regions of
the window (as a result of increasing the width or height) and on any regions
where window contents are lost.

If the inside width or height of a window is not changed but the window is moved
or its border is changed, then the contents of the window are not lost but move
with the window. Changing the inside width or height of the window causes its
contents to be moved or lost, depending on the bit-gravity of the window. It
also causes children to be reconfigured, depending on their win-gravity. For a
change of width and height of W and H, we define the [x, y] pairs as:

Direction Deltas NorthWest [0, 0] North [W/2, 0] NorthEast [W, 0] West [0, H/2]
Center [W/2, H/2] East [W, H/2] SouthWest [0, H] South [W/2, H] SouthEast [W, H]
When a window with one of these bit-gravities is resized, the corresponding pair
defines the change in position of each pixel in the window. When a window with
one of these win-gravities has its parent window resized, the corresponding pair
defines the change in position of the window within the parent. This
repositioning generates a GravityNotify event. GravityNotify events are
generated after the ConfigureNotify event is generated.

A gravity of Static indicates that the contents or origin should not move
relative to the origin of the root window. If the change in size of the window
is coupled with a change in position of [X, Y], then for bit-gravity the change
in position of each pixel is [-X, -Y] and for win-gravity the change in position
of a child when its parent is so resized is [-X, -Y]. Note that Static gravity
still only takes effect when the width or height of the window is changed, not
when the window is simply moved.

A bit-gravity of Forget indicates that the window contents are always discarded
after a size change, even if backing-store or save-under has been requested. The
window is tiled with its background (except, if no background is defined, the
existing screen contents are not altered) and zero or more exposure events are
generated.

The contents and borders of inferiors are not affected by their parent's
bit-gravity. A server is permitted to ignore the specified bit-gravity and use
Forget instead.

A win-gravity of Unmap is like NorthWest, but the child is also unmapped when
the parent is resized, and an UnmapNotify event is generated. UnmapNotify events
are generated after the ConfigureNotify event is generated.

If a sibling and a stack-mode are specified, the window is restacked as follows:

Above The window is placed just above the sibling.  Below The window is placed
just below the sibling.  TopIf If the sibling occludes the window, then the
window is placed at the top of the stack.  BottomIf If the window occludes the
sibling, then the window is placed at the bottom of the stack.  Opposite If the
sibling occludes the window, then the window is placed at the top of the
stack. Otherwise, if the window occludes the sibling, then the window is placed
at the bottom of the stack.  If a stack-mode is specified but no sibling is
specified, the window is restacked as follows:

Above The window is placed at the top of the stack.  Below The window is placed
at the bottom of the stack.  TopIf If any sibling occludes the window, then the
window is placed at the top of the stack.  BottomIf If the window occludes any
sibling, then the window is placed at the bottom of the stack.  Opposite If any
sibling occludes the window, then the window is placed at the top of the
stack. Otherwise, if the window occludes any sibling, then the window is placed
at the bottom of the stack.  It is a Match error if a sibling is specified
without a stack-mode or if the window is not actually a sibling.

Note that the computations for BottomIf, TopIf, and Opposite are performed with
respect to the window's final geometry (as controlled by the other arguments to
the request), not to its initial geometry.

Attempts to configure a root window have no effect.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['ConfigureWindow', 'ConfigureWindowChecked', ]


class ConfigureWindowAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """
    _head = _pack('=xx2x')
    _tail = _pack('2x')
    fmt = 'IH'
    code = 12

    def _getbinary(self, window, value_mask, value_list):
        buf = _StringIO()
        buf.write(self._head)
        buf.write(_pack(self.fmt, window, value_mask))
        buf.write(self._tail)
        buf.write(str(buffer(_array('I', value_list))))
        return buf.getvalue()

    def __call__(self, window, value_mask, value_list):
        """Request ConfigureWindow X protocol.

        @Arguments:
        - `window`: (int) Window's id
        - `value_mask`: (int) bit mask
        - `value_list`: (list of int) list of value

        @Return:
        VoidCookie

        @Error:
        BadMatch, BadValue, BadWindow
        """
        return self.request(self._getbinary(window, value_mask, value_list))


class ConfigureWindow(ConfigureWindowAbstract):
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


class ConfigureWindowChecked(ConfigureWindowAbstract):
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
# configurewindow.py ends here
