#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: createwindow.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""createwindow -- a parts of xcb2

CreateWindow

wid, parent: WINDOW
class: { InputOutput, InputOnly, CopyFromParent}
depth: CARD8
visual: VISUALID or CopyFromParent
x, y: INT16
width, height, border-width: CARD16
value-mask: BITMASK
value-list: LISTofVALUE

Errors: Alloc, Colormap, Cursor, IDChoice, Match, Pixmap, Value, Window

This request creates an unmapped window and assigns the identifier wid to it.

A class of CopyFromParent means the class is taken from the parent. A depth of
zero for class InputOutput or CopyFromParent means the depth is taken from the
parent. A visual of CopyFromParent means the visual type is taken from the
parent. For class InputOutput, the visual type and depth must be a combination
supported for the screen (or a Match error results). The depth need not be the
same as the parent, but the parent must not be of class InputOnly (or a Match
error results). For class InputOnly, the depth must be zero (or a Match error
results), and the visual must be one supported for the screen (or a Match error
results). However, the parent can have any depth and class.

The server essentially acts as if InputOnly windows do not exist for the
purposes of graphics requests, exposure processing, and VisibilityNotify
events. An InputOnly window cannot be used as a drawable (as a source or
destination for graphics requests). InputOnly and InputOutput windows act
identically in other respects-properties, grabs, input control, and so on.

The coordinate system has the X axis horizontal and the Y axis vertical with the
origin [0, 0] at the upper-left corner. Coordinates are integral, in terms of
pixels, and coincide with pixel centers. Each window and pixmap has its own
coordinate system. For a window, the origin is inside the border at the inside,
upper-left corner.

The x and y coordinates for the window are relative to the parent's origin and
specify the position of the upper-left outer corner of the window (not the
origin). The width and height specify the inside size (not including the border)
and must be nonzero (or a Value error results). The border-width for an
InputOnly window must be zero (or a Match error results).

The window is placed on top in the stacking order with respect to siblings.

The value-mask and value-list specify attributes of the window that are to be
explicitly initialized. The possible values are:

Attribute	Type
background-pixmap	 PIXMAP or None or ParentRelative
background-pixel	CARD32
border-pixmap	 PIXMAP or CopyFromParent
border-pixel	CARD32
bit-gravity	BITGRAVITY
win-gravity	WINGRAVITY
backing-store	 { NotUseful, WhenMapped, Always }
backing-planes	CARD32
backing-pixel	CARD32
save-under	BOOL
event-mask	SETofEVENT
do-not-propagate-mask	SETofDEVICEEVENT
override-redirect	BOOL
colormap	 COLORMAP or CopyFromParent
cursor	 CURSOR or None
The default values when attributes are not explicitly initialized are:

Attribute	Default
background-pixmap	None
border-pixmap	CopyFromParent
bit-gravity	Forget
win-gravity	NorthWest
backing-store	NotUseful
backing-planes	all ones
backing-pixel	zero
save-under	False
event-mask	{} (empty set)
do-not-propagate-mask	{} (empty set)
override-redirect	False
colormap	CopyFromParent
cursor	None
Only the following attributes are defined for InputOnly windows:
win-gravity
event-mask
do-not-propagate-mask
override-redirect
cursor

It is a Match error to specify any other attributes for InputOnly windows.
If background-pixmap is given, it overrides the default background-pixmap. The
background pixmap and the window must have the same root and the same depth (or
a Match error results). Any size pixmap can be used, although some sizes may be
faster than others. If background None is specified, the window has no defined
background. If background ParentRelative is specified, the parent's background
is used, but the window must have the same depth as the parent (or a Match error
results). If the parent has background None, then the window will also have
background None. A copy of the parent's background is not made. The parent's
background is reexamined each time the window background is required. If
background-pixel is given, it overrides the default background-pixmap and any
background-pixmap given explicitly, and a pixmap of undefined size filled with
background-pixel is used for the background. Range checking is not performed on
the background-pixel value; it is simply truncated to the appropriate number of
bits. For a ParentRelative background, the background tile origin always aligns
with the parent's background tile origin. Otherwise, the background tile origin
is always the window origin.

When no valid contents are available for regions of a window and the regions are
either visible or the server is maintaining backing store, the server
automatically tiles the regions with the window's background unless the window
has a background of None. If the background is None, the previous screen
contents from other windows of the same depth as the window are simply left in
place if the contents come from the parent of the window or an inferior of the
parent; otherwise, the initial contents of the exposed regions are
undefined. Exposure events are then generated for the regions, even if the
background is None.

The border tile origin is always the same as the background tile origin. If
border-pixmap is given, it overrides the default border-pixmap. The border
pixmap and the window must have the same root and the same depth (or a Match
error results). Any size pixmap can be used, although some sizes may be faster
than others. If CopyFromParent is given, the parent's border pixmap is copied
(subsequent changes to the parent's border attribute do not affect the child),
but the window must have the same depth as the parent (or a Match error
results). The pixmap might be copied by sharing the same pixmap object between
the child and parent or by making a complete copy of the pixmap contents. If
border-pixel is given, it overrides the default border-pixmap and any
border-pixmap given explicitly, and a pixmap of undefined size filled with
border-pixel is used for the border. Range checking is not performed on the
border-pixel value; it is simply truncated to the appropriate number of bits.

Output to a window is always clipped to the inside of the window, so that the
border is never affected.

The bit-gravity defines which region of the window should be retained if the
window is resized, and win-gravity defines how the window should be repositioned
if the parent is resized (see ConfigureWindow request).

A backing-store of WhenMapped advises the server that maintaining contents of
obscured regions when the window is mapped would be beneficial. A backing-store
of Always advises the server that maintaining contents even when the window is
unmapped would be beneficial. In this case, the server may generate an exposure
event when the window is created. A value of NotUseful advises the server that
maintaining contents is unnecessary, although a server may still choose to
maintain contents while the window is mapped. Note that if the server maintains
contents, then the server should maintain complete contents not just the region
within the parent boundaries, even if the window is larger than its
parent. While the server maintains contents, exposure events will not normally
be generated, but the server may stop maintaining contents at any time.

If save-under is True, the server is advised that when this window is mapped,
saving the contents of windows it obscures would be beneficial.

When the contents of obscured regions of a window are being maintained, regions
obscured by noninferior windows are included in the destination (and source,
when the window is the source) of graphics requests, but regions obscured by
inferior windows are not included.

The backing-planes indicates (with bits set to 1) which bit planes of the window
hold dynamic data that must be preserved in backing-stores and during
save-unders. The backing-pixel specifies what value to use in planes not covered
by backing-planes. The server is free to save only the specified bit planes in
the backing-store or save-under and regenerate the remaining planes with the
specified pixel value. Any bits beyond the specified depth of the window in
these values are simply ignored.

The event-mask defines which events the client is interested in for this window
(or for some event types, inferiors of the window). The do-not-propagate-mask
defines which events should not be propagated to ancestor windows when no client
has the event type selected in this window.

The override-redirect specifies whether map and configure requests on this
window should override a SubstructureRedirect on the parent, typically to inform
a window manager not to tamper with the window.

The colormap specifies the colormap that best reflects the true colors of the
window. Servers capable of supporting multiple hardware colormaps may use this
information, and window managers may use it for InstallColormap requests. The
colormap must have the same visual type and root as the window (or a Match error
results). If CopyFromParent is specified, the parent's colormap is copied
(subsequent changes to the parent's colormap attribute do not affect the
child). However, the window must have the same visual type as the parent (or a
Match error results), and the parent must not have a colormap of None (or a
Match error results). For an explanation of None, see FreeColormap request. The
colormap is copied by sharing the colormap object between the child and the
parent, not by making a complete copy of the colormap contents.

If a cursor is specified, it will be used whenever the pointer is in the
window. If None is specified, the parent's cursor will be used when the pointer
is in the window, and any change in the parent's cursor will cause an immediate
change in the displayed cursor.

This request generates a CreateNotify event.

The background and border pixmaps and the cursor may be freed immediately if no
further explicit references to them are to be made.

Subsequent drawing into the background or border pixmap has an undefined effect
on the window state. The server might or might not make a copy of the pixmap.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['CreateWindow', 'CreateWindowChecked', ]


class CreateWindowAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xIIhhHHHHII'
    code = 1

    def _getbinary(self, depth, wid, parent, x, y, width, height,
                            border_width, _class, visual, value_mask,
                            value_list):
        buf = _StringIO()
        buf.write(_pack(self.fmt, depth, wid, parent, x, y, width, height,
                        border_width, _class, visual, value_mask))
        buf.write(str(buffer(_array('I', value_list))))
        return buf.getvalue()

    def __call__(self, depth, wid, parent, x, y, width, height, border_width,
                 _class, visual, value_mask, value_list):
        """CreateWindow

        @Arguments:
        - `depth`:
        - `wid`:
        - `parent`:
        - `x`:
        - `y`:
        - `width`:
        - `height`:
        - `border_width`:
        - `_class`:
        - `visual`:
        - `value_mask`:
        - `value_list`:

        @Return:
        VoidCookie

        @Errors:
        BadAlloc, BadColormap, BadCursor, BadIDChoice, BadMatch, BadPixmap,
        BadValue, BadWindow
        """
        return self.request(
            self._getbinary(depth, wid, parent, x, y, width, height,
                            border_width, _class, visual, value_mask, value_list))


class CreateWindow(CreateWindowAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(depth, wid, parent, x, y, width, height, border_width,
        _class, visual, value_mask, value_list)

        @Arguments:
        - [yas] elisp error!:
        - [yas] elisp error!:
        - [yas] elisp error!:
        - [yas] elisp error!:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class CreateWindowChecked(CreateWindowAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(depth, wid, parent, x, y, width, height,
        border_width, _class, visual, value_mask, value_list)

        @Arguments:
        - [yas] elisp error!:
        - [yas] elisp error!:
        - [yas] elisp error!:
        - [yas] elisp error!:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# createwindow.py ends here
