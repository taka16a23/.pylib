#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: getproperty.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""getproperty -- a parts of xcb2

GetProperty

window: WINDOW
property: ATOM
type: ATOM or AnyPropertyType
long-offset, long-length: CARD32
delete: BOOL

type: ATOM or None
format: {0, 8, 16, 32}
bytes-after: CARD32
value: LISTofINT8 or LISTofINT16 or LISTofINT32

Errors: Atom, Value, Window

If the specified property does not exist for the specified window, then the
return type is None, the format and bytes-after are zero, and the value is
empty. The delete argument is ignored in this case. If the specified property
exists but its type does not match the specified type, then the return type is
the actual type of the property, the format is the actual format of the property
(never zero), the bytes-after is the length of the property in bytes (even if
the format is 16 or 32), and the value is empty. The delete argument is ignored
in this case. If the specified property exists and either AnyPropertyType is
specified or the specified type matches the actual type of the property, then
the return type is the actual type of the property, the format is the actual
format of the property (never zero), and the bytes-after and value are as
follows, given:

    N = actual length of the stored property in bytes
        (even if the format is 16 or 32)
    I = 4 * long-offset
    T = N - I
    L = MINIMUM(T, 4 * long-length)
    A = N - (I + L)
The returned value starts at byte index I in the property (indexing from 0), and
its length in bytes is L. However, it is a Value error if long-offset is given
such that L is negative. The value of bytes-after is A, giving the number of
trailing unread bytes in the stored property. If delete is True and the
bytes-after is zero, the property is also deleted from the window, and a
PropertyNotify event is generated on the window.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract, CoreSubMethodAbstract
from xcb2.xproto import GetPropertyCookie, GetPropertyReply
from xcb2.xproto.wcookie import WrapGetPropertyCookie


__all__ = ['GetProperty', 'GetPropertyUnchecked', ]


class GetPropertyMethodAbstract(CoreSubMethodAbstract):
    r"""SUMMARY
    """
    atomname = None

    def __init__(self, parent):
        r"""

        @Arguments:
        - `connection`:
        """
        CoreSubMethodAbstract.__init__(self, parent)

        self.atom = self._connection.core.InternAtom.usecache(self.atomname)
        self.types = self.atom.gettypeatom()
        self._atom = self.atom.pack()
        self._types = self.types.pack()

    def _getbinary(self, window, delete=False, long_offset=0, long_length=10):
        buf = _StringIO()
        buf.write(_pack('=xB2xI', delete, window))
        buf.write(self._atom)
        buf.write(self._types)
        buf.write(_pack('II', long_offset, long_length))
        return buf.getvalue()

    def __call__(self, window, delete=False, long_offset=0, long_length=10):
        """Request GetProperty X protocol.

        @Arguments:
        - `window`:
        - `delete`:
        - `long_offset`:
        - `long_length`:

        @Return:
        """
        cookie = self._parent.request(
            self._getbinary(window, delete, long_offset, long_length))
        cookie.window, cookie.property = window, self.atom
        return WrapGetPropertyCookie(self._connection, cookie)


class GetWM_NAME(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = 'WM_NAME'


class GetWM_LOCALE_NAME(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = 'WM_LOCALE_NAME'


class GetWM_ICON_NAME(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = 'WM_ICON_NAME'


class GetWM_CLASS(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = 'WM_CLASS'


class GetWM_TRANSIENT_FOR(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = 'WM_TRANSIENT_FOR'


class GetWM_PROTOCOLS(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = 'WM_PROTOCOLS'


class GetWM_COLORMAP_WINDOWS(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = 'WM_COLORMAP_WINDOWS'


class GetWM_CLIENT_MACHINE(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = 'WM_CLIENT_MACHINE'


class GetWM_STATE(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = 'WM_STATE'


class Get_WIN_WORKSPACE(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_WIN_WORKSPACE'


class Get_WIN_STATE(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_WIN_STATE'


class Get_NET_SUPPORTED(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_SUPPORTED'


class Get_NET_CLIENT_LIST(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_CLIENT_LIST'


class Get_NET_CLIENT_LIST_STACKING(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_CLIENT_LIST_STACKING'


class Get_NET_NUMBER_OF_DESKTOPS(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_NUMBER_OF_DESKTOPS'


class Get_NET_DESKTOP_GEOMETRY(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_DESKTOP_GEOMETRY'


class Get_NET_DESKTOP_VIEWPORT(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_DESKTOP_VIEWPORT'


class Get_NET_CURRENT_DESKTOP(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_CURRENT_DESKTOP'


class Get_NET_DESKTOP_NAMES(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_DESKTOP_NAMES'


class Get_NET_ACTIVE_WINDOW(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_ACTIVE_WINDOW'


class Get_NET_WORKAREA(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WORKAREA'


class Get_NET_SUPPORTING_WM_CHECK(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_SUPPORTING_WM_CHECK'


class Get_NET_VIRTUAL_ROOTS(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_VIRTUAL_ROOTS'


class Get_NET_DESKTOP_LAYOUT(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_DESKTOP_LAYOUT'


class Get_NET_SHOWING_DESKTOP(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_SHOWING_DESKTOP'


class Get_NET_CLOSE_WINDOW(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_CLOSE_WINDOW'


class Get_NET_MOVERESIZE_WINDOW(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_MOVERESIZE_WINDOW'


class Get_NET_WM_MORERESIZE(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_MORERESIZE'


class Get_NET_RESTACK_WINDOW(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_RESTACK_WINDOW'


class Get_NET_REQUEST_FRAME_EXTENTS(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_REQUEST_FRAME_EXTENTS'


class Get_NET_WM_NAME(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_NAME'


class Get_NET_WM_VISIBLE_NAME(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_VISIBLE_NAME'


class Get_NET_WM_ICON_NAME(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_ICON_NAME'


class Get_NET_WM_VISIBLE_ICON_NAME(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_VISIBLE_ICON_NAME'


class Get_NET_WM_DESKTOP(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_DESKTOP'


class Get_NET_WM_WINDOW_TYPE(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_WINDOW_TYPE'


class Get_NET_WM_STATE(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_STATE'


class Get_NET_WM_ALLOWED_ACTIONS(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_ALLOWED_ACTIONS'


class Get_NET_WM_STRUT(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_STRUT'


class Get_NET_WM_STRUT_PARTIAL(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_STRUT_PARTIAL'


class Get_NET_WM_ICON_GEOMETRY(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_ICON_GEOMETRY'


class Get_NET_WM_ICON(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_ICON'


class Get_NET_WM_PID(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_PID'


class Get_NET_WM_HANDLED_ICONS(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_HANDLED_ICONS'


class Get_NET_WM_USER_TIME(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_USER_TIME'


class Get_NET_WM_USER_TIME_WINDOW(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_USER_TIME_WINDOW'


class Get_NET_FRAME_EXTENTS(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_FRAME_EXTENTS'


class Get_OB_APP_TYPE(GetPropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_OB_APP_TYPE'


class GetPropertyMethod(CoreSubMethodAbstract):
    r"""SUMMARY
    """
    # TODO: (Atami) [2014/05/27]
    # split head
    delete = _pack('=xB2x', False)

    def set_delete(self, bool_):
        r"""SUMMARY

        set_delete(bool_)

        @Arguments:
        - `bool_`:

        @Return:
        """
        if not isinstance(bool_, bool):
            # TODO: (Atami) [2014/05/27]
            raise StandardError()
        self.delete = _pack('=xB2x', bool_)

    def _getbinary(self, window, property, long_offset, long_length):
        r"""SUMMARY

        _getbinary(atom, window, long_offset, long_length)

        @Arguments:
        - `atom`:
        - `window`:
        - `long_offset`:
        - `long_length`:

        @Return:
        """
        buf = _StringIO()
        buf.write(self.delete)
        buf.write(_pack('5I', window, property, property.gettypeatom(),
                        long_offset, long_length))
        return buf.getvalue()

    def __call__(self, atom, window, long_offset=0, long_length=0):
        r"""SUMMARY

        __call__(atom, window, delete=False, long_offset, long_length=0)

        @Arguments:
        - `atom`:
        - `window`:
        - `delete`:
        - `long_offset`:
        - `long_length`:

        @Return:
        """
        atom = self._connection.core.atomidentify(atom)
        cookie = self._parent.request(
            self._getbinary(window, atom, long_offset, long_length))
        cookie.window, cookie.property = window, atom
        return WrapGetPropertyCookie(self._connection, cookie)


## CoreMethod
#
class GetPropertyAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xIIIII'
    code = 20

    def __init__(self, connection):
        r"""SUMMARY

        __init__(connection)

        @Arguments:
        - `connection`:

        @Return:
        """
        CoreMethodAbstract.__init__(self, connection)
        self.getproperty                = GetPropertyMethod(self)
        self.WM_NAME                    = GetWM_NAME(self)
        self.WM_LOCALE_NAME             = GetWM_LOCALE_NAME(self)
        self.WM_ICON_NAME               = GetWM_ICON_NAME(self)
        self.WM_CLASS                   = GetWM_CLASS(self)
        self.WM_TRANSIENT_FOR           = GetWM_TRANSIENT_FOR(self)
        self.WM_PROTOCOLS               = GetWM_PROTOCOLS(self)
        self.WM_COLORMAP_WINDOWS        = GetWM_COLORMAP_WINDOWS(self)
        self.WM_CLIENT_MACHINE          = GetWM_CLIENT_MACHINE(self)
        self.WM_STATE                   = GetWM_STATE(self)
        self._WIN_WORKSPACE             = Get_WIN_WORKSPACE(self)
        self._WIN_STATE                 = Get_WIN_STATE(self)
        self._NET_SUPPORTED             = Get_NET_SUPPORTED(self)
        self._NET_CLIENT_LIST           = Get_NET_CLIENT_LIST(self)
        self._NET_CLIENT_LIST_STACKING  = Get_NET_CLIENT_LIST_STACKING(self)
        self._NET_NUMBER_OF_DESKTOPS    = Get_NET_NUMBER_OF_DESKTOPS(self)
        self._NET_DESKTOP_GEOMETRY      = Get_NET_DESKTOP_GEOMETRY(self)
        self._NET_DESKTOP_VIEWPORT      = Get_NET_DESKTOP_VIEWPORT(self)
        self._NET_CURRENT_DESKTOP       = Get_NET_CURRENT_DESKTOP(self)
        self._NET_DESKTOP_NAMES         = Get_NET_DESKTOP_NAMES(self)
        self._NET_ACTIVE_WINDOW         = Get_NET_ACTIVE_WINDOW(self)
        self._NET_WORKAREA              = Get_NET_WORKAREA(self)
        self._NET_SUPPORTING_WM_CHECK   = Get_NET_SUPPORTING_WM_CHECK(self)
        self._NET_VIRTUAL_ROOTS         = Get_NET_VIRTUAL_ROOTS(self)
        self._NET_DESKTOP_LAYOUT        = Get_NET_DESKTOP_LAYOUT(self)
        self._NET_SHOWING_DESKTOP       = Get_NET_SHOWING_DESKTOP(self)
        self._NET_CLOSE_WINDOW          = Get_NET_CLOSE_WINDOW(self)
        self._NET_MOVERESIZE_WINDOW     = Get_NET_MOVERESIZE_WINDOW(self)
        self._NET_WM_MORERESIZE         = Get_NET_WM_MORERESIZE(self)
        self._NET_RESTACK_WINDOW        = Get_NET_RESTACK_WINDOW(self)
        self._NET_REQUEST_FRAME_EXTENTS = Get_NET_REQUEST_FRAME_EXTENTS(self)
        self._NET_WM_NAME               = Get_NET_WM_NAME(self)
        self._NET_WM_STATE              = Get_NET_WM_STATE(self)
        self._NET_WM_VISIBLE_NAME       = Get_NET_WM_VISIBLE_NAME(self)
        self._NET_WM_ICON_NAME          = Get_NET_WM_ICON_NAME(self)
        self._NET_WM_VISIBLE_ICON_NAME  = Get_NET_WM_VISIBLE_ICON_NAME(self)
        self._NET_WM_DESKTOP            = Get_NET_WM_DESKTOP(self)
        self._NET_WM_WINDOW_TYPE        = Get_NET_WM_WINDOW_TYPE(self)
        self._NET_WM_ALLOWED_ACTIONS    = Get_NET_WM_ALLOWED_ACTIONS(self)
        self._NET_WM_STRUT              = Get_NET_WM_STRUT(self)
        self._NET_WM_STRUT_PARTIAL      = Get_NET_WM_STRUT_PARTIAL(self)
        self._NET_WM_ICON_GEOMETRY      = Get_NET_WM_ICON_GEOMETRY(self)
        self._NET_WM_ICON               = Get_NET_WM_ICON(self)
        self._NET_WM_PID                = Get_NET_WM_PID(self)
        self._NET_WM_HANDLED_ICONS      = Get_NET_WM_HANDLED_ICONS(self)
        self._NET_WM_USER_TIME          = Get_NET_WM_USER_TIME(self)
        self._NET_WM_USER_TIME_WINDOW   = Get_NET_WM_USER_TIME_WINDOW(self)
        self._NET_FRAME_EXTENTS         = Get_NET_FRAME_EXTENTS(self)
        self._OB_APP_TYPE               = Get_OB_APP_TYPE(self)

    def _getbinary(
            self, delete, window, property, type, long_offset, long_length):
        r"""SUMMARY

        _getbinary(delete, window, property, type, long_offset, long_length)

        @Arguments:
        - `delete`:
        - `window`:
        - `property`:
        - `type`:
        - `long_offset`:
        - `long_length`:
        """
        buf = _StringIO()
        buf.write(_pack(self.fmt, delete, window, property, type,
                              long_offset, long_length))
        return buf.getvalue()

    def __call__(
            self, delete, window, property, type, long_offset, long_length):
        """Request GetProperty X protocol.

        @Arguments:
        - `delete`:
        - `window`:
        - `property`:
        - `type`:
        - `long_offset`:
        - `long_length`:

        @Return:
        GetPropertyCookie

        @Error:
        BadAtom, BadValue, BadWindow
        """
        cookie = self.request(
            self._getbinary(
                delete, window, property, type, long_offset, long_length))
        cookie.window, cookie.property = window, property
        return WrapGetPropertyCookie(self._connection, cookie)


class GetProperty(GetPropertyAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(delete, window, property, type, long_offset, long_length)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            GetPropertyCookie(), GetPropertyReply)


class GetPropertyUnchecked(GetPropertyAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(delete, window, property, type, long_offset, long_length)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            GetPropertyCookie(), GetPropertyReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# getproperty.py ends here
