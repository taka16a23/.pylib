#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""getwindowattributes -- a parts of xcb2

window: WINDOW

Return:
visual: VISUALID
class: { InputOutput, InputOnly}
bit-gravity: BITGRAVITY
win-gravity: WINGRAVITY
backing-store: { NotUseful, WhenMapped, Always}
backing-planes: CARD32
backing-pixel: CARD32
save-under: BOOL
colormap: COLORMAP or None
map-is-installed: BOOL
map-state: { Unmapped, Unviewable, Viewable}
all-event-masks, your-event-mask: SETofEVENT
do-not-propagate-mask: SETofDEVICEEVENT
override-redirect: BOOL

Errors: Window

This request returns the current attributes of the window. A window is Unviewable if it is mapped but some ancestor is unmapped. All-event-masks is the inclusive-OR of all event masks selected on the window by clients. Your-event-mask is the event mask selected by the querying client.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import GetWindowAttributesCookie, GetWindowAttributesReply


__all__ = ['GetWindowAttributes', 'GetWindowAttributesUnchecked', ]


class GetWindowAttributesAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xI'
    code = 3

    def _getbinary(self, window):
        buf = _StringIO()
        buf.write(_pack(self.fmt, window))
        return buf.getvalue()

    def __call__(self, window):
        """GetWindowAttributes X protocol request.

        @Arguments:
        - `window`: (int)

        @Return:
        GetWindowAttributesCookie
        visual                           : VISUALID
        class                            : { InputOutput, InputOnly}
        bit-gravity                      : BITGRAVITY
        win-gravity                      : WINGRAVITY
        backing-store                    : { NotUseful, WhenMapped, Always}
        backing-planes                   : CARD32
        backing-pixel                    : CARD32
        save-under                       : BOOL
        colormap                         : COLORMAP or None
        map-is-installed                 : BOOL
        map-state                        : { Unmapped, Unviewable, Viewable}
        all-event-masks, your-event-mask : SETofEVENT
        do-not-propagate-mask            : SETofDEVICEEVENT
        override-redirect                : BOOL

        @Error:
        BadWindow
        """
        return self.request(self._getbinary(window))


class GetWindowAttributes(GetWindowAttributesAbstract):
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
            GetWindowAttributesCookie(), GetWindowAttributesReply)


class GetWindowAttributesUnchecked(GetWindowAttributesAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(window)

        @Arguments:
        - [yas] elisp error!:
        - [yas] elisp error!:
        - [yas] elisp error!:
        - [yas] elisp error!:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            GetWindowAttributesCookie(), GetWindowAttributesReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# getwindowattributes.py ends here
