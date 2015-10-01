#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: uninstallcolormap.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""uninstallcolormap -- a parts of xcb2

UninstallColormap

cmap: COLORMAP

Errors: Colormap

If cmap is on the required list for its screen (see InstallColormap request), it
is removed from the list. As a side effect, cmap might be uninstalled, and
additional colormaps might be implicitly installed or uninstalled. Which
colormaps get installed or uninstalled is server-dependent except that the
required list must remain installed.

If cmap becomes uninstalled, a ColormapNotify event is generated on every window
having cmap as an attribute. In addition, for every other colormap that is
installed or uninstalled as a result of the request, a ColormapNotify event is
generated on every window having that colormap as an attribute.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['UninstallColormap', 'UninstallColormapChecked', ]


class UninstallColormapAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xI'
    code = 82

    def _getbinary(self, cmap):
        buf = _StringIO()
        buf.write(_pack(self.fmt, cmap))
        return buf.getvalue()

    def __call__(self, cmap):
        """Request UninstallColormap X protocol.

        @Arguments:
        - `cmap`:

        @Return:
        VoidCookie

        @Error:
        BadColormap
        """
        return self.request(self._getbinary(cmap))


class UninstallColormap(UninstallColormapAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cmap)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class UninstallColormapChecked(UninstallColormapAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(cmap)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# uninstallcolormap.py ends here
