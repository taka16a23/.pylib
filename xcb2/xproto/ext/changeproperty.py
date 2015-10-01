#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: changeproperty.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""changeproperty -- a parts of xcb2

ChangeProperty

window: WINDOW
property, type: ATOM
format: {8, 16, 32}
mode: { Replace, Prepend, Append}
data: LISTofINT8 or LISTofINT16 or LISTofINT32

Errors: Alloc, Atom, Match, Value, Window

This request alters the property for the specified window. The type is
uninterpreted by the server. The format specifies whether the data should be
viewed as a list of 8-bit, 16-bit, or 32-bit quantities so that the server can
correctly byte-swap as necessary.

If the mode is Replace, the previous property value is discarded. If the mode is
Prepend or Append, then the type and format must match the existing property
value (or a Match error results). If the property is undefined, it is treated as
defined with the correct type and format with zero-length data. For Prepend, the
data is tacked on to the beginning of the existing data, and for Append, it is
tacked on to the end of the existing data.

This request generates a PropertyNotify event on the window.

The lifetime of a property is not tied to the storing client. Properties remain
until explicitly deleted, until the window is destroyed, or until server reset
(see section 10).

The maximum size of a property is server-dependent and may vary dynamically.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

from xcb2 import Request, VoidCookie
from xcb2.xproto import Property
from xcb2.xproto.ext.abstract import CoreMethodAbstract, CoreSubMethodAbstract


__all__ = ['ChangeProperty', 'ChangePropertyChecked', ]


class ChangePropertyMethodAbstract(CoreSubMethodAbstract):
    r"""SUMMARY
    """
    atomname = None

    def __init__(self, parent):
        r"""

        @Arguments:
        - `parent`:
        """
        CoreSubMethodAbstract.__init__(self, parent)
        self.atom = self._connection.core.InternAtom.usecache(self.atomname)
        self.types = self.atom.gettypeatom()
        self.format = self.atom.getformat()
        self.property_newvalue = Property.NewValue
        self.property_delete = Property.Delete
        self._atom = self.atom.pack()
        self._types = self.types.pack()
        self._format = _pack('B', self.format)
        self._newvalue = _pack('=B3x', self.property_newvalue)
        self._delete = _pack('=B3x', self.property_delete)

    def _getbinary(self, mode, window, data):
        r"""SUMMARY

        _getbinary(mode, window, data)

        @Arguments:
        - `mode`:
        - `window`:
        - `data`:

        @Return:
        """
        buf = _StringIO()
        buf.write(_pack('=B3x', mode))
        buf.write(_pack('I', window))
        buf.write(self._atom)
        buf.write(self._types)
        buf.write(self._format)
        buf.write(_pack('3x'))
        buf.write(_pack('I', len(data)))
        buf.write(str(buffer(_array('B', data))))
        return buf.getvalue()

    def _get_newvalue_binary(self, window, data):
        r"""SUMMARY

        _get_newvalue_binary(window, data)

        @Arguments:
        - `window`:
        - `data`:

        @Return:
        """
        buf = _StringIO()
        buf.write(self._newvalue)
        buf.write(_pack('I', window))
        buf.write(self._atom)
        buf.write(self._types)
        buf.write(self._format)
        buf.write(_pack('3x'))
        buf.write(_pack('I', len(data)))
        buf.write(str(buffer(_array('B', data))))
        return buf.getvalue()

    def _get_delete_binary(self, window, data):
        r"""SUMMARY

        _get_delete_binary()

        @Return:
        """
        buf = _StringIO()
        buf.write(self._delete)
        buf.write(_pack('I', window))
        buf.write(self._atom)
        buf.write(self._types)
        buf.write(self._format)
        buf.write(_pack('3x'))
        buf.write(_pack('I', len(data)))
        buf.write(str(buffer(_array('B', data))))
        return buf.getvalue()

    def newvalue(self, window, data):
        r"""SUMMARY

        newvalue()

        @Return:
        """
        return self._parent.request(
            self._get_newvalue_binary(window, data))

    def delete(self, window, data):
        r"""SUMMARY

        delete(window, data)

        @Arguments:
        - `window`:
        - `data`:

        @Return:
        """
        return self._parent.request(
            self._get_delete_binary(window, data))

    def __call__(self, window, data, mode=Property.NewValue):
        r"""SUMMARY

        __call__(window, data, mode=Property.NewValue)

        @Arguments:
        - `window`:
        - `data`:
        - `mode`:

        @Return:
        """
        return self._parent.request(self._getbinary(mode, window, data))


class ChangeWM_NAME(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = 'WM_NAME'


class ChangeWM_LOCALE_NAME(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = 'WM_LOCALE_NAME'


class ChangeWM_ICON_NAME(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = 'WM_ICON_NAME'


class ChangeWM_CLASS(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = 'WM_CLASS'


class ChangeWM_TRANSIENT_FOR(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = 'WM_TRANSIENT_FOR'


class ChangeWM_PROTOCOLS(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = 'WM_PROTOCOLS'


class ChangeWM_COLORMAP_WINDOWS(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = 'WM_COLORMAP_WINDOWS'


class ChangeWM_CLIENT_MACHINE(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = 'WM_CLIENT_MACHINE'


class ChangeWM_STATE(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = 'WM_STATE'


class Change_WIN_WORKSPACE(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_WIN_WORKSPACE'


class Change_WIN_STATE(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_WIN_STATE'


class Change_NET_SUPPORTED(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_SUPPORTED'


class Change_NET_CLIENT_LIST(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_CLIENT_LIST'


class Change_NET_CLIENT_LIST_STACKING(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_CLIENT_LIST_STACKING'


class Change_NET_NUMBER_OF_DESKTOPS(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_NUMBER_OF_DESKTOPS'


class Change_NET_DESKTOP_GEOMETRY(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_DESKTOP_GEOMETRY'


class Change_NET_DESKTOP_VIEWPORT(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_DESKTOP_VIEWPORT'


class Change_NET_CURRENT_DESKTOP(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_CURRENT_DESKTOP'


class Change_NET_DESKTOP_NAMES(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_DESKTOP_NAMES'


class Change_NET_ACTIVE_WINDOW(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_ACTIVE_WINDOW'


class Change_NET_WORKAREA(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WORKAREA'


class Change_NET_SUPPORTING_WM_CHECK(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_SUPPORTING_WM_CHECK'


class Change_NET_VIRTUAL_ROOTS(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_VIRTUAL_ROOTS'


class Change_NET_DESKTOP_LAYOUT(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_DESKTOP_LAYOUT'


class Change_NET_SHOWING_DESKTOP(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_SHOWING_DESKTOP'


class Change_NET_CLOSE_WINDOW(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_CLOSE_WINDOW'


class Change_NET_MOVERESIZE_WINDOW(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_MOVERESIZE_WINDOW'


class Change_NET_WM_MORERESIZE(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_MORERESIZE'


class Change_NET_RESTACK_WINDOW(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_RESTACK_WINDOW'


class Change_NET_REQUEST_FRAME_EXTENTS(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_REQUEST_FRAME_EXTENTS'


class Change_NET_WM_NAME(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_NAME'


class Change_NET_WM_VISIBLE_NAME(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_VISIBLE_NAME'


class Change_NET_WM_ICON_NAME(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_ICON_NAME'


class Change_NET_WM_VISIBLE_ICON_NAME(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_VISIBLE_ICON_NAME'


class Change_NET_WM_DESKTOP(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_DESKTOP'


class Change_NET_WM_WINDOW_TYPE(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_WINDOW_TYPE'


class Change_NET_WM_STATE(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_STATE'


class Change_NET_WM_ALLOWED_ACTIONS(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_ALLOWED_ACTIONS'


class Change_NET_WM_STRUT(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_STRUT'


class Change_NET_WM_STRUT_PARTIAL(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_STRUT_PARTIAL'


class Change_NET_WM_ICON_GEOMETRY(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_ICON_GEOMETRY'


class Change_NET_WM_ICON(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_ICON'


class Change_NET_WM_PID(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_PID'


class Change_NET_WM_HANDLED_ICONS(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_HANDLED_ICONS'


class Change_NET_WM_USER_TIME(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_USER_TIME'


class Change_NET_WM_USER_TIME_WINDOW(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_WM_USER_TIME_WINDOW'


class Change_NET_FRAME_EXTENTS(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_FRAME_EXTENTS'


class Change_OB_APP_TYPE(ChangePropertyMethodAbstract):
    r"""SUMMARY
    """
    atomname = '_OB_APP_TYPE'


class ChangePropertyAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """
    fmt = '=xB2xIIIB3xI'
    code = 18

    def __init__(self, connection):
        r"""SUMMARY

        __init__(connection)

        @Arguments:
        - `connection`:

        @Return:
        """
        CoreMethodAbstract.__init__(self, connection)
        self.WM_NAME                    = ChangeWM_NAME(self)
        self.WM_LOCALE_NAME             = ChangeWM_LOCALE_NAME(self)
        self.WM_ICON_NAME               = ChangeWM_ICON_NAME(self)
        self.WM_CLASS                   = ChangeWM_CLASS(self)
        self.WM_TRANSIENT_FOR           = ChangeWM_TRANSIENT_FOR(self)
        self.WM_PROTOCOLS               = ChangeWM_PROTOCOLS(self)
        self.WM_COLORMAP_WINDOWS        = ChangeWM_COLORMAP_WINDOWS(self)
        self.WM_CLIENT_MACHINE          = ChangeWM_CLIENT_MACHINE(self)
        self.WM_STATE                   = ChangeWM_STATE(self)
        self._WIN_WORKSPACE             = Change_WIN_WORKSPACE(self)
        self._WIN_STATE                 = Change_WIN_STATE(self)
        self._NET_SUPPORTED             = Change_NET_SUPPORTED(self)
        self._NET_CLIENT_LIST           = Change_NET_CLIENT_LIST(self)
        self._NET_CLIENT_LIST_STACKING  = Change_NET_CLIENT_LIST_STACKING(self)
        self._NET_NUMBER_OF_DESKTOPS    = Change_NET_NUMBER_OF_DESKTOPS(self)
        self._NET_DESKTOP_GEOMETRY      = Change_NET_DESKTOP_GEOMETRY(self)
        self._NET_DESKTOP_VIEWPORT      = Change_NET_DESKTOP_VIEWPORT(self)
        self._NET_CURRENT_DESKTOP       = Change_NET_CURRENT_DESKTOP(self)
        self._NET_DESKTOP_NAMES         = Change_NET_DESKTOP_NAMES(self)
        self._NET_ACTIVE_WINDOW         = Change_NET_ACTIVE_WINDOW(self)
        self._NET_WORKAREA              = Change_NET_WORKAREA(self)
        self._NET_SUPPORTING_WM_CHECK   = Change_NET_SUPPORTING_WM_CHECK(self)
        self._NET_VIRTUAL_ROOTS         = Change_NET_VIRTUAL_ROOTS(self)
        self._NET_DESKTOP_LAYOUT        = Change_NET_DESKTOP_LAYOUT(self)
        self._NET_SHOWING_DESKTOP       = Change_NET_SHOWING_DESKTOP(self)
        self._NET_CLOSE_WINDOW          = Change_NET_CLOSE_WINDOW(self)
        self._NET_MOVERESIZE_WINDOW     = Change_NET_MOVERESIZE_WINDOW(self)
        self._NET_WM_MORERESIZE         = Change_NET_WM_MORERESIZE(self)
        self._NET_RESTACK_WINDOW        = Change_NET_RESTACK_WINDOW(self)
        self._NET_REQUEST_FRAME_EXTENTS = Change_NET_REQUEST_FRAME_EXTENTS(self)
        self._NET_WM_NAME               = Change_NET_WM_NAME(self)
        self._NET_WM_STATE              = Change_NET_WM_STATE(self)
        self._NET_WM_VISIBLE_NAME       = Change_NET_WM_VISIBLE_NAME(self)
        self._NET_WM_ICON_NAME          = Change_NET_WM_ICON_NAME(self)
        self._NET_WM_VISIBLE_ICON_NAME  = Change_NET_WM_VISIBLE_ICON_NAME(self)
        self._NET_WM_DESKTOP            = Change_NET_WM_DESKTOP(self)
        self._NET_WM_WINDOW_TYPE        = Change_NET_WM_WINDOW_TYPE(self)
        self._NET_WM_ALLOWED_ACTIONS    = Change_NET_WM_ALLOWED_ACTIONS(self)
        self._NET_WM_STRUT              = Change_NET_WM_STRUT(self)
        self._NET_WM_STRUT_PARTIAL      = Change_NET_WM_STRUT_PARTIAL(self)
        self._NET_WM_ICON_GEOMETRY      = Change_NET_WM_ICON_GEOMETRY(self)
        self._NET_WM_ICON               = Change_NET_WM_ICON(self)
        self._NET_WM_PID                = Change_NET_WM_PID(self)
        self._NET_WM_HANDLED_ICONS      = Change_NET_WM_HANDLED_ICONS(self)
        self._NET_WM_USER_TIME          = Change_NET_WM_USER_TIME(self)
        self._NET_WM_USER_TIME_WINDOW   = Change_NET_WM_USER_TIME_WINDOW(self)
        self._NET_FRAME_EXTENTS         = Change_NET_FRAME_EXTENTS(self)
        self._OB_APP_TYPE               = Change_OB_APP_TYPE(self)

    def _getbinary(self, mode, window, property, type, format, data_len, data):
        buf = _StringIO()
        buf.write(_pack(self.fmt, mode, window, property, type, format,
                        data_len))
        buf.write(str(buffer(_array('B', data))))
        return buf.getvalue()

    def __call__(self, mode, window, property, type, format, data_len, data):
        """Request ChangeProperty X protocol.

        @Arguments:
        - `mode`:
        - `window`:
        - `property`:
        - `type`:
        - `format`:
        - `data_len`:
        - `data`:

        @Return:
        VoidCookie

        @Error:
        BadAlloc, BadAtom, BadMatch, BadValue, BadWindow
        """
        return self.request(self._getbinary(
            mode, window, property, type, format, data_len, data))

    def _get_changeproperty_binary(self, window, property_, data_len, data, mode):
        r"""SUMMARY

        changeproperty(window, property_, data, mode=Property.NewValue)

        @Arguments:
        - `window`:
        - `property_`:
        - `data`:
        - `mode`:

        @Return:
        """
        atom = self._connection.core.atomidentify(property_)
        types = atom.gettypeatom()
        format = atom.getformat()
        buf = _StringIO()
        buf.write(_pack('=B3x', mode))
        buf.write(_pack('I', window))
        buf.write(atom.pack())
        buf.write(types.pack())
        buf.write(_pack('B', format))
        buf.write(_pack('3x'))
        buf.write(_pack('I', data_len))
        buf.write(str(buffer(_array('B', data))))
        return buf.getvalue()

    def changeproperty(self, window, property_, data_len, data, mode=Property.NewValue):
        r"""SUMMARY

        changeproperty(window, property_, data, mode=Property.NewValue)

        @Arguments:
        - `window`:
        - `property_`:
        - `data`:
        - `mode`:

        @Return:
        """
        return self.request(self._get_changeproperty_binary(
            window, property_, data_len, data, mode))


class ChangeProperty(ChangePropertyAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(mode, window, property, type, format, data_len, data)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class ChangePropertyChecked(ChangePropertyAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(mode, window, property, type, format, data_len, data)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# changeproperty.py ends here
