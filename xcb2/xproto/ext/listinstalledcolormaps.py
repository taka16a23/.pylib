#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""listinstalledcolormaps -- a parts of xcb2

ListInstalledColormaps

window: WINDOW

cmaps: LISTofCOLORMAP

Errors: Window

This request returns a list of the currently installed colormaps for the screen
of the specified window. The order of colormaps is not significant, and there is
no explicit indication of the required list (see InstallColormap request).
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import ListInstalledColormapsCookie, ListInstalledColormapsReply


__all__ = ['ListInstalledColormaps', 'ListInstalledColormapsUnchecked', ]


class ListInstalledColormapsAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xI'
    code = 83

    def _getbinary(self, window):
        buf = _StringIO()
        buf.write(_pack(self.fmt, window))
        return buf.getvalue()

    def __call__(self, window):
        """Request ListInstalledColormaps X protocol.

        @Arguments:
        - `window`:

        @Return:
        ListInstalledColormapsCookie

        @Error:
        BadWindow
        """
        return self.request(self._getbinary(window))


class ListInstalledColormaps(ListInstalledColormapsAbstract):
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
            ListInstalledColormapsCookie(), ListInstalledColormapsReply)


class ListInstalledColormapsUnchecked(ListInstalledColormapsAbstract):
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
            ListInstalledColormapsCookie(), ListInstalledColormapsReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# listinstalledcolormaps.py ends here
