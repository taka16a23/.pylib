#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""installcolormap -- a parts of xcb2

InstallColormap

cmap: COLORMAP

Errors: Colormap

This request makes this colormap an installed map for its screen. All windows
associated with this colormap immediately display with true colors. As a side
effect, additional colormaps might be implicitly installed or uninstalled by the
server. Which other colormaps get installed or uninstalled is server-dependent
except that the required list must remain installed.

If cmap is not already an installed map, a ColormapNotify event is generated on
every window having cmap as an attribute. In addition, for every other colormap
that is installed or uninstalled as a result of the request, a ColormapNotify
event is generated on every window having that colormap as an attribute.

At any time, there is a subset of the installed maps that are viewed as an
ordered list and are called the required list. The length of the required list
is at most M, where M is the min-installed-maps specified for the screen in the
connection setup. The required list is maintained as follows. When a colormap is
an explicit argument to InstallColormap, it is added to the head of the list;
the list is truncated at the tail, if necessary, to keep the length of the list
to at most M. When a colormap is an explicit argument to UninstallColormap and
it is in the required list, it is removed from the list. A colormap is not added
to the required list when it is installed implicitly by the server, and the
server cannot implicitly uninstall a colormap that is in the required list.

Initially the default colormap for a screen is installed (but is not in the
required list).
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['InstallColormap', 'InstallColormapChecked', ]


class InstallColormapAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xI'
    code = 81

    def _getbinary(self, cmap):
        buf = _StringIO()
        buf.write(_pack(self.fmt, cmap))
        return buf.getvalue()

    def __call__(self, cmap):
        """Request InstallColormap X protocol.

        @Arguments:
        - `cmap`:

        @Return:
        VoidCookie

        @Error:
        BadColormap
        """
        return self.request(self._getbinary(cmap))


class InstallColormap(InstallColormapAbstract):
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


class InstallColormapChecked(InstallColormapAbstract):
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
# installcolormap.py ends here
