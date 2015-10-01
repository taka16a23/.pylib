#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""destroywindow -- a parts of xcb2

DestroyWindow

window: WINDOW
Errors: Window

If the argument window is mapped, an UnmapWindow request is performed
automatically. The window and all inferiors are then destroyed, and a
DestroyNotify event is generated for each window. The ordering of the
DestroyNotify events is such that for any given window, DestroyNotify is
generated on all inferiors of the window before being generated on the window
itself. The ordering among siblings and across subhierarchies is not otherwise
constrained.

Normal exposure processing on formerly obscured windows is performed.

If the window is a root window, this request has no effect.

"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['DestroyWindow', 'DestroyWindowChecked', ]


class DestroyWindowAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xI'
    code = 4

    def _getbinary(self, window):
        buf = _StringIO()
        buf.write(_pack(self.fmt, window))
        return buf.getvalue()

    def __call__(self, window):
        """DestroyWindow

        @Arguments:
        - `window`: (int)

        @Return:
        VoidCookie

        @Errors:
        BadWindow
        """
        return self.request(self._getbinary(window))


class DestroyWindow(DestroyWindowAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(window)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class DestroyWindowChecked(DestroyWindowAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(window)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# destroywindow.py ends here
