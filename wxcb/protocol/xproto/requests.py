#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""requests -- DESCRIPTION

"""
from enum import IntEnum as _IntEnum

from xcb import VoidCookie, xproto

import reply as _reply
import buffer as _buffer
import sendrequest



class Opcode(_IntEnum):
    r"""Opcode

    Opcode is a _IntEnum.
    Responsibility:
    """
    CreateWindow            = 1
    ChangeWindowAttributes  = 2
    GetWindowAttributes     = 3
    DestroyWindow           = 4
    DestroySubwindows       = 5
    ChangeSaveSet           = 6
    ReparentWindow          = 7
    MapWindow               = 8
    MapSubwindows           = 9
    UnmapWindow             = 10
    UnmapSubwindows         = 11
    ConfigureWindow         = 12
    CirculateWindow         = 13
    GetGeometry             = 14
    QueryTree               = 15
    InternAtom              = 16
    GetAtomName             = 17
    ChangeProperty          = 18
    DeleteProperty          = 19
    GetProperty             = 20
    ListProperties          = 21
    SetSelectionOwner       = 22
    GetSelectionOwner       = 23
    ConvertSelection        = 24
    SendEvent               = 25
    GrabPointer             = 26
    UngrabPointer           = 27
    GrabButton              = 28
    UngrabButton            = 29
    ChangeActivePointerGrab = 30
    GrabKeyboard            = 31
    UngrabKeyboard          = 32
    GrabKey                 = 33
    UngrabKey               = 34
    AllowEvents             = 35
    GrabServer              = 36
    UngrabServer            = 37
    QueryPointer            = 38
    GetMotionEvents         = 39
    TranslateCoordinates    = 40
    WarpPointer             = 41
    SetInputFocus           = 42
    GetInputFocus           = 43
    QueryKeymap             = 44
    OpenFont                = 45
    CloseFont               = 46
    QueryFont               = 47
    QueryTextExtents        = 48
    ListFonts               = 49
    ListFontsWithInfo       = 50
    SetFontPath             = 51
    GetFontPath             = 52
    CreatePixmap            = 53
    FreePixmap              = 54
    CreateGC                = 55
    ChangeGC                = 56
    CopyGC                  = 57
    SetDashes               = 58
    SetClipRectangles       = 59
    FreeGC                  = 60
    ClearArea               = 61
    CopyArea                = 62
    CopyPlane               = 63
    PolyPoint               = 64
    PolyLine                = 65
    PolySegment             = 66
    PolyRectangle           = 67
    PolyArc                 = 68
    FillPoly                = 69
    PolyFillRectangle       = 70
    PolyFillArc             = 71
    PutImage                = 72
    GetImage                = 73
    PolyText8               = 74
    PolyText16              = 75
    ImageText8              = 76
    ImageText16             = 77
    CreateColormap          = 78
    FreeColormap            = 79
    CopyColormapAndFree     = 80
    InstallColormap         = 81
    UninstallColormap       = 82
    ListInstalledColormaps  = 83
    AllocColor              = 84
    AllocNamedColor         = 85
    AllocColorCells         = 86
    AllocColorPlanes        = 87
    FreeColors              = 88
    StoreColors             = 89
    StoreNamedColor         = 90
    QueryColors             = 91
    LookupColor             = 92
    CreateCursor            = 93
    CreateGlyphCursor       = 94
    FreeCursor              = 95
    RecolorCursor           = 96
    QueryBestSize           = 97
    QueryExtension          = 98
    ListExtensions          = 99
    ChangeKeyboardMapping   = 100
    GetKeyboardMapping      = 101
    ChangeKeyboardControl   = 102
    GetKeyboardControl      = 103
    Bell                    = 104
    ChangePointerControl    = 105
    GetPointerControl       = 106
    SetScreenSaver          = 107
    GetScreenSaver          = 108
    ChangeHosts             = 109
    ListHosts               = 110
    SetAccessControl        = 111
    SetCloseDownMode        = 112
    KillClient              = 113
    RotateProperties        = 114
    ForceScreenSaver        = 115
    SetPointerMapping       = 116
    GetPointerMapping       = 117
    SetModifierMapping      = 118
    GetModifierMapping      = 119
    NoOperation             = 127


class Request(object):
    r"""Request

    Request is a object.
    Responsibility:
    """
    def __init__(self, opcode, cookietype, checked, display, reply=None):
        r"""

        @Arguments:
        - `display`:
        - `checked`:
        - `opcode`:
        - `cookietype`:
        """
        self._request = sendrequest.SendRequest(
            opcode, cookietype, checked, reply, display)

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self._request.get_display()

    def set_display(self, display):
        r"""SUMMARY

        set_display(display)

        @Arguments:
        - `display`:

        @Return:

        @Error:
        """
        self._request.set_display(display)

    display = property(get_display, set_display)

    def ischecked(self, ):
        r"""SUMMARY

        ischecked()

        @Return:

        @Error:
        """
        return self._request.ischecked()

    def set_checked(self, checked):
        r"""SUMMARY

        set_checked(checked)

        @Arguments:
        - `checked`:

        @Return:

        @Error:
        """
        self._request.set_checked(checked)

    checked = property(ischecked, set_checked)

    def flush(self, ):
        r"""SUMMARY

        flush()

        @Return:

        @Error:
        """
        self._request.flush()


class CreateWindow(Request):
    r"""CreateWindow

    CreateWindow is a object.
    Responsibility:
    """

    def __init__(self, depth, wid, parent, x, y, width, height,
                 border_width, _class, visual, value_mask, value_list,
                 checked=False, display=None):
        r"""

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
        """
        Request.__init__(
            self, Opcode.CreateWindow, VoidCookie, checked, display)
        self._buffer = _buffer.CreateWindow(
            depth, wid, parent, x, y, width, height, border_width,
            _class, visual, value_mask, value_list)

    def get_depth(self, ):
        r"""SUMMARY

        get_depth()

        @Return:

        @Error:
        """
        return self._buffer.get_depth()

    def set_depth(self, depth):
        r"""SUMMARY

        set_depth(depth)

        @Arguments:
        - `depth`:

        @Return:

        @Error:
        """
        self._buffer.set_depth(depth)

    depth = property(get_depth, set_depth)

    def get_id(self, ):
        r"""SUMMARY

        get_id()

        @Return:

        @Error:
        """
        return self._buffer.get_id()

    def set_id(self, wid):
        r"""SUMMARY

        set_id(wid)

        @Arguments:
        - `wid`:

        @Return:

        @Error:
        """
        self._buffer.set_id(wid)

    wid = property(get_id, set_id)

    def get_parent(self, ):
        r"""SUMMARY

        get_parent()

        @Return:

        @Error:
        """
        return self._buffer.get_parent()

    def set_parent(self, parent):
        r"""SUMMARY

        set_parent(parent)

        @Arguments:
        - `parent`:

        @Return:

        @Error:
        """
        self._buffer.set_parent(parent)

    parent = property(get_parent, set_parent)

    def get_x(self, ):
        r"""SUMMARY

        get_x()

        @Return:

        @Error:
        """
        return self._buffer.get_x()

    def set_x(self, newx):
        r"""SUMMARY

        set_x(newx)

        @Arguments:
        - `newx`:

        @Return:

        @Error:
        """
        self._buffer.set_x(newx)

    x = property(get_x, set_x)

    def get_y(self, ):
        r"""SUMMARY

        get_y()

        @Return:

        @Error:
        """
        return self._buffer.get_y()

    def set_y(self, newy):
        r"""SUMMARY

        set_y(newy)

        @Arguments:
        - `newy`:

        @Return:

        @Error:
        """
        self._buffer.set_y(newy)

    y = property(get_y, set_y)

    def get_width(self, ):
        r"""SUMMARY

        get_width()

        @Return:

        @Error:
        """
        return self._buffer.get_width()

    def set_width(self, width):
        r"""SUMMARY

        set_width(width)

        @Arguments:
        - `width`:

        @Return:

        @Error:
        """
        self._buffer.set_width(width)

    width = property(get_width, set_width)

    def get_height(self, ):
        r"""SUMMARY

        get_height()

        @Return:

        @Error:
        """
        return self._buffer.get_height()

    def set_height(self, height):
        r"""SUMMARY

        set_height(height)

        @Arguments:
        - `height`:

        @Return:

        @Error:
        """
        self._buffer.set_height(height)

    height = property(get_height, set_height)

    def get_border_width(self, ):
        r"""SUMMARY

        get_border_width()

        @Return:

        @Error:
        """
        return self._buffer.get_border_width()

    def set_border_width(self, border_width):
        r"""SUMMARY

        set_border_width(border_width)

        @Arguments:
        - `border_width`:

        @Return:

        @Error:
        """
        self._buffer.set_border_width(border_width)

    border_width = property(get_border_width, set_border_width)

    def get_class(self, ):
        r"""SUMMARY

        get_class()

        @Return:

        @Error:
        """
        return self._buffer.get_class()

    def set_class(self, _class):
        r"""SUMMARY

        set_class(_class)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_class(_class)

    class_ = property(get_class, set_class)

    def get_visual(self, ):
        r"""SUMMARY

        get_visual()

        @Return:

        @Error:
        """
        return self._buffer.get_visual()

    def set_visual(self, visual):
        r"""SUMMARY

        set_visual(_visual)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_visual(visual)

    visual = property(get_visual, set_visual)

    def get_value_mask(self, ):
        r"""SUMMARY

        get_value_mask()

        @Return:

        @Error:
        """
        return self._buffer.get_value_mask()

    def set_value_mask(self, value_mask):
        r"""SUMMARY

        set_value_mask(_value_mask)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_value_mask(value_mask)

    value_mask = property(get_value_mask, set_value_mask)

    def get_value_list(self, ):
        r"""SUMMARY

        get_value_list()

        @Return:

        @Error:
        """
        return self._buffer.get_value_list()

    def set_value_list(self, value_list):
        r"""SUMMARY

        set_value_list(_value_list)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_value_list(value_list)

    value_list = property(get_value_list, set_value_list)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class ChangeWindowAttributes(Request):
    r"""ChangeWindowAttributes

    ChangeWindowAttributes is a Request.
    Responsibility:
    """
    def __init__(self, window, value_mask, value_list, checked=False,
                 display=None):
        r"""

        @Arguments:
        - `window`:
        - `value_mask`:
        - `value_list`:
        - `display`:
        - `checked`:
        """
        Request.__init__(
            self, Opcode.ChangeWindowAttributes, VoidCookie, checked, display)
        self._buffer = _buffer.ChangeWindowAttributes(
            window, value_mask, value_list)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._buffer.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_window(window)

    window = property(get_window, set_window)

    def get_value_mask(self, ):
        r"""SUMMARY

        get_value_mask()

        @Return:

        @Error:
        """
        return self._buffer.get_value_mask()

    def set_value_mask(self, value_mask):
        r"""SUMMARY

        set_value_mask(_value_mask)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_value_mask(value_mask)

    value_mask = property(get_value_mask, set_value_mask)

    def get_value_list(self, ):
        r"""SUMMARY

        get_value_list()

        @Return:

        @Error:
        """
        return self._buffer.get_value_list()

    def set_value_list(self, value_list):
        r"""SUMMARY

        set_value_list(_value_list)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_value_list(value_list)

    value_list = property(get_value_list, set_value_list)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class GetWindowAttributes(Request):
    r"""GetWindowAttributes

    GetWindowAttributes is a Request.
    Responsibility:
    """
    def __init__(self, window, checked=True, display=None):
        r"""

        @Arguments:
        - `window`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.GetWindowAttributes,
                         xproto.GetWindowAttributesCookie, checked, display,
                         xproto.GetWindowAttributesReply)
        self._buffer = _buffer.GetWindowAttributes(window)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._buffer.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_window(window)

    window = property(get_window, set_window)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class DestroyWindow(Request):
    r"""DestroyWindow

    DestroyWindow is a Request.
    Responsibility:
    """
    def __init__(self, window, checked=False, display=None):
        r"""

        @Arguments:
        - `window`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.DestroyWindow, VoidCookie, checked, display)
        self._buffer = _buffer.DestroyWindow(window)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._buffer.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_window(window)

    window = property(get_window, set_window)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class DestroySubwindows(Request):
    r"""DestroySubwindows

    DestroySubwindows is a Request.
    Responsibility:
    """
    def __init__(self, window, checked=False, display=None):
        r"""

        @Arguments:
        - `window`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.DestroySubwindows, VoidCookie, checked, display)
        self._buffer = _buffer.DestroySubwindows(window)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._buffer.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_window(window)

    window = property(get_window, set_window)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class ChangeSaveSet(Request):
    r"""ChangeSaveSet

    ChangeSaveSet is a Request.
    Responsibility:
    """
    opcode = 6
    cookietype = VoidCookie

    def __init__(self, mode, window, checked=False, display=None):
        r"""

        @Arguments:
        - `mode`:
        - `window`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, 6, VoidCookie, checked, display)
        self._buffer = _buffer.ChangeSaveSet(mode, window)

    def get_mode(self, ):
        r"""SUMMARY

        get_mode()

        @Return:

        @Error:
        """
        return self._buffer.get_mode()

    def set_mode(self, mode):
        r"""SUMMARY

        set_mode(_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_mode(mode)

    mode = property(get_mode, set_mode)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._buffer.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_window(window)

    window = property(get_window, set_window)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class ReparentWindow(Request):
    r"""ReparentWindow

    ReparentWindow is a Request.
    Responsibility:
    """
    def __init__(self, window, parent, x, y, checked=False, display=None):
        r"""

        @Arguments:
        - `window`:
        - `parent`:
        - `x`:
        - `y`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.ReparentWindow, VoidCookie, checked, display)
        self._buffer = _buffer.ReparentWindow(window, parent, x, y)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._buffer.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_window(window)

    window = property(get_window, set_window)

    def get_parent(self, ):
        r"""SUMMARY

        get_parent()

        @Return:

        @Error:
        """
        return self._buffer.get_parent()

    def set_parent(self, parent):
        r"""SUMMARY

        set_parent(_parent)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_parent(parent)

    parent = property(get_parent, set_parent)

    def get_x(self, ):
        r"""SUMMARY

        get_x()

        @Return:

        @Error:
        """
        return self._buffer.get_x()

    def set_x(self, newx):
        r"""SUMMARY

        set_x(_x)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_x(newx)

    x = property(get_x, set_x)

    def get_y(self, ):
        r"""SUMMARY

        get_y()

        @Return:

        @Error:
        """
        return self._buffer.get_y()

    def set_y(self, newy):
        r"""SUMMARY

        set_y(_y)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_y(newy)

    y = property(get_y, set_y)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class MapWindow(Request):
    r"""MapWindow

    MapWindow is a Request.
    Responsibility:
    """
    def __init__(self, window, checked=False, display=None):
        r"""

        @Arguments:
        - `window`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.MapWindow, VoidCookie, checked, display)
        self._buffer = _buffer.MapWindow(window)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._buffer.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_window(window)

    window = property(get_window, set_window)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class MapSubwindows(Request):
    r"""MapSubwindows

    MapSubwindows is a Request.
    Responsibility:
    """
    def __init__(self, window, checked=False, display=None):
        r"""

        @Arguments:
        - `window`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.MapSubwindows, VoidCookie, checked, display)
        self._buffer = _buffer.MapSubwindows(window)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._buffer.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_window(window)

    window = property(get_window, set_window)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class UnmapWindow(Request):
    r"""UnmapWindow

    UnmapWindow is a Request.
    Responsibility:
    """
    def __init__(self, window, checked=False, display=None):
        r"""

        @Arguments:
        - `window`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.UnmapWindow, VoidCookie, checked, display)
        self._buffer = _buffer.UnmapWindow(window)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._buffer.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_window(window)

    window = property(get_window, set_window)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class UnmapSubwindows(Request):
    r"""UnmapSubwindows

    UnmapSubwindows is a Request.
    Responsibility:
    """
    def __init__(self, window, checked=False, display=None):
        r"""

        @Arguments:
        - `window`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.UnmapSubwindows, VoidCookie, checked, display)
        self._buffer = _buffer.UnmapSubwindows(window)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._buffer.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_window(window)

    window = property(get_window, set_window)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class ConfigureWindow(Request):
    r"""ConfigureWindow

    ConfigureWindow is a Request.
    Responsibility:
    """
    def __init__(self, window, value_mask, value_list, checked=False,
                 display=None):
        r"""

        @Arguments:
        - `window`:
        - `value_mask`:
        - `value_list`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.ConfigureWindow, VoidCookie, checked, display)
        self._buffer = _buffer.ConfigureWindow(window, value_mask, value_list)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._buffer.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_window(window)

    window = property(get_window, set_window)

    def get_value_mask(self, ):
        r"""SUMMARY

        get_value_mask()

        @Return:

        @Error:
        """
        return self._buffer.get_value_mask()

    def set_value_mask(self, value_mask):
        r"""SUMMARY

        set_value_mask(_value_mask)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_value_mask(value_mask)

    value_mask = property(get_value_mask, set_value_mask)

    def get_value_list(self, ):
        r"""SUMMARY

        get_value_list()

        @Return:

        @Error:
        """
        return self._buffer.get_value_list()

    def set_value_list(self, value_list):
        r"""SUMMARY

        set_value_list(_value_list)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_value_list(value_list)

    value_list = property(get_value_list, set_value_list)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class CirculateWindow(Request):
    r"""CirculateWindow

    CirculateWindow is a Request.
    Responsibility:
    """
    def __init__(self, direction, window, checked=False, display=None):
        r"""

        @Arguments:
        - `direction`:
        - `window`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.CirculateWindow, VoidCookie, checked, display)
        self._buffer = _buffer.CirculateWindow(direction, window)

    def get_direction(self, ):
        r"""SUMMARY

        get_direction()

        @Return:

        @Error:
        """
        return self._buffer.get_direction()

    def set_direction(self, direction):
        r"""SUMMARY

        set_direction(_direction)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_direction(direction)

    direction = property(get_direction, set_direction)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._buffer.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_window(window)

    window = property(get_window, set_window)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class GetGeometry(Request):
    r"""GetGeometry

    GetGeometry is a Request.
    Responsibility:
    """
    def __init__(self, drawable, checked=True, display=None):
        r"""

        @Arguments:
        - `drawable`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.GetGeometry, xproto.GetGeometryCookie,
                         checked, display, xproto.GetGeometryReply)
        self._buffer = _buffer.GetGeometry(drawable)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._buffer.get_drawable()

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(_drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_drawable(drawable)

    drawable = property(get_drawable, set_drawable)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class QueryTree(Request):
    r"""QueryTree

    QueryTree is a Request.
    Responsibility:
    """
    opcode = 15
    cookietype = xproto.QueryTreeCookie

    def __init__(self, window, checked=True, display=None):
        r"""

        @Arguments:
        - `window`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.QueryTree, xproto.QueryTreeCookie,
                         checked, display, xproto.QueryTreeReply)
        self._buffer = _buffer.QueryTree(window)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._buffer.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_window(window)

    window = property(get_window, set_window)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class InternAtom(Request):
    r"""InternAtom

    InternAtom is a Request.
    Responsibility:
    """
    def __init__(self, only_if_exists, name_len, name, checked=True,
                 display=None):
        r"""

        @Arguments:
        - `only_if_exists`:
        - `name_len`:
        - `name`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.InternAtom, xproto.InternAtomCookie,
                         checked, display, _reply.InternAtomReply)
        self._buffer = _buffer.InternAtom(only_if_exists, name_len, name)

    def get_only_if_exists(self, ):
        r"""SUMMARY

        get_only_if_exists()

        @Return:

        @Error:
        """
        return self._buffer.get_only_if_exists()

    def set_only_if_exists(self, only_if_exists):
        r"""SUMMARY

        set_only_if_exists(_only_if_exists)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_only_if_exists(only_if_exists)

    only_if_exists = property(get_only_if_exists, set_only_if_exists)

    def get_name_len(self, ):
        r"""SUMMARY

        get_name_len()

        @Return:

        @Error:
        """
        return self._buffer.get_name_len()

    def set_name_len(self, name_len):
        r"""SUMMARY

        set_name_len(name_len)

        @Arguments:
        - `name_len`:

        @Return:

        @Error:
        """
        self._buffer.set_name_len(name_len)

    name_len = property(get_name_len, set_name_len)

    def get_name(self, ):
        r"""SUMMARY

        get_name()

        @Return:

        @Error:
        """
        return self._buffer.get_name()

    def set_name(self, name):
        r"""SUMMARY

        set_name(_name)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_name(name)

    name = property(get_name, set_name)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class GetAtomName(Request):
    r"""GetAtomName

    GetAtomName is a Request.
    Responsibility:
    """
    def __init__(self, atom, checked=True, display=None):
        r"""

        @Arguments:
        - `atom`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.GetAtomName, xproto.GetAtomNameCookie,
                         checked, display, _reply.GetAtomNameReply)
        self._buffer = _buffer.GetAtomName(atom)

    def get_atom(self, ):
        r"""SUMMARY

        get_atom()

        @Return:

        @Error:
        """
        return self._buffer.get_atom()

    def set_atom(self, atom):
        r"""SUMMARY

        set_atom(_atom)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_atom(atom)

    atom = property(get_atom, set_atom)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class ChangeProperty(Request):
    r"""ChangeProperty

    ChangeProperty is a Request.
    Responsibility:
    """
    def __init__(self, mode, window, property_, type_, format_, data_len,
                 data, checked=False, display=None):
        r"""

        @Arguments:
        - `mode`:
        - `window`:
        - `property_`:
        - `type_`:
        - `format_`:
        - `data_len`:
        - `data`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.ChangeProperty, VoidCookie, checked, display)
        self._buffer = _buffer.ChangeProperty(
            mode, window, property_, type_, format_, data_len, data)

    def get_mode(self, ):
        r"""SUMMARY

        get_mode()

        @Return:

        @Error:
        """
        return self._buffer.get_mode()

    def set_mode(self, mode):
        r"""SUMMARY

        set_mode(_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_mode(mode)

    mode = property(get_mode, set_mode)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._buffer.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_window(window)

    window = property(get_window, set_window)

    def get_property(self, ):
        r"""SUMMARY

        get_property()

        @Return:

        @Error:
        """
        return self._buffer.get_property()

    def set_property(self, property_):
        r"""SUMMARY

        set_property(_property)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_property(property_)

    property_ = property(get_property, set_property)

    def get_type(self, ):
        r"""SUMMARY

        get_type()

        @Return:

        @Error:
        """
        return self._buffer.get_type()

    def set_type(self, type_):
        r"""SUMMARY

        set_type(_type)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_type(type_)

    type_ = property(get_type, set_type)

    def get_format(self, ):
        r"""SUMMARY

        get_format()

        @Return:

        @Error:
        """
        return self._buffer.get_format()

    def set_format(self, format_):
        r"""SUMMARY

        set_format(_format)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_format(format_)

    format = property(get_format, set_format)

    def get_data_len(self, ):
        r"""SUMMARY

        get_data_len()

        @Return:

        @Error:
        """
        return self._buffer.get_data_len()

    def set_data_len(self, data_len):
        r"""SUMMARY

        set_data_len(_data_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_data_len(data_len)

    data_len = property(get_data_len, set_data_len)

    def get_data(self, ):
        r"""SUMMARY

        get_data()

        @Return:

        @Error:
        """
        return self._buffer.get_data()

    def set_data(self, data):
        r"""SUMMARY

        set_data(_data)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_data(data)

    data = property(get_data, set_data)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class DeleteProperty(Request):
    r"""DeleteProperty

    DeleteProperty is a Request.
    Responsibility:
    """
    def __init__(self, window, property_, checked=False, display=None):
        r"""

        @Arguments:
        - `window`:
        - `property_`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.DeleteProperty, VoidCookie, checked, display)
        self._buffer = _buffer.DeleteProperty(window, property_)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._buffer.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_window(window)

    window = property(get_window, set_window)

    def get_property(self, ):
        r"""SUMMARY

        get_property()

        @Return:

        @Error:
        """
        return self._buffer.get_property()

    def set_property(self, property_):
        r"""SUMMARY

        set_property(_property)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_property(property_)

    property_ = property(get_property, set_property)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class GetProperty(Request):
    r"""GetProperty

    GetProperty is a Request.
    Responsibility:
    """
    def __init__(self, delete, window, property_, type_, long_offset,
                 long_length, checked=True, display=None):
        r"""

        @Arguments:
        - `delete`:
        - `window`:
        - `property_`:
        - `type_`:
        - `long_offset`:
        - `long_length`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.GetProperty, xproto.GetPropertyCookie,
                         checked, display, xproto.GetPropertyReply)
        self._buffer = _buffer.GetProperty(
            delete, window, property_, type_, long_offset, long_length)

    def get_delete(self, ):
        r"""SUMMARY

        get_delete()

        @Return:

        @Error:
        """
        return self._buffer.get_delete()

    def set_delete(self, delete):
        r"""SUMMARY

        set_delete(_delete)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_delete(delete)

    delete = property(get_delete, set_delete)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._buffer.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_window(window)

    window = property(get_window, set_window)

    def get_property(self, ):
        r"""SUMMARY

        get_property()

        @Return:

        @Error:
        """
        return self._buffer.get_property()

    def set_property(self, property_):
        r"""SUMMARY

        set_property(_property)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_property(property_)

    property_ = property(get_property, set_property)

    def get_type(self, ):
        r"""SUMMARY

        get_type()

        @Return:

        @Error:
        """
        return self._buffer.get_type()

    def set_type(self, type_):
        r"""SUMMARY

        set_type(_type)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_type(type_)

    type = property(get_type, set_type)

    def get_long_offset(self, ):
        r"""SUMMARY

        get_long_offset()

        @Return:

        @Error:
        """
        return self._buffer.get_long_offset()

    def set_long_offset(self, long_offset):
        r"""SUMMARY

        set_long_offset(_long_offset)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_long_offset(long_offset)

    long_offset = property(get_long_offset, set_long_offset)

    def get_long_length(self, ):
        r"""SUMMARY

        get_long_length()

        @Return:

        @Error:
        """
        return self._buffer.get_long_length()

    def set_long_length(self, long_length):
        r"""SUMMARY

        set_long_length(_long_length)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_long_length(long_length)

    long_length = property(get_long_length, set_long_length)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class ListProperties(Request):
    r"""ListProperties

    ListProperties is a Request.
    Responsibility:
    """
    def __init__(self, window, checked=True, display=None):
        r"""

        @Arguments:
        - `window`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.ListProperties,
                         xproto.ListPropertiesCookie, checked, display,
                         xproto.ListPropertiesReply)
        self._buffer = _buffer.ListProperties(window)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._buffer.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_window(window)

    window = property(get_window, set_window)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class SetSelectionOwner(Request):
    r"""SetSelectionOwner

    SetSelectionOwner is a Request.
    Responsibility:
    """
    def __init__(self, owner, selection, time, checked=False, display=None):
        r"""

        @Arguments:
        - `owner`:
        - `selection`:
        - `time`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.SetSelectionOwner, VoidCookie, checked, display)
        self._buffer = _buffer.SetSelectionOwner(owner, selection, time)

    def get_owner(self, ):
        r"""SUMMARY

        get_owner()

        @Return:

        @Error:
        """
        return self._buffer.get_owner()

    def set_owner(self, owner):
        r"""SUMMARY

        set_owner(_owner)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_owner(owner)

    owner = property(get_owner, set_owner)

    def get_selection(self, ):
        r"""SUMMARY

        get_selection()

        @Return:

        @Error:
        """
        return self._buffer.get_selection()

    def set_selection(self, selection):
        r"""SUMMARY

        set_selection(_selection)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_selection(selection)

    selection = property(get_selection, set_selection)

    def get_time(self, ):
        r"""SUMMARY

        get_time()

        @Return:

        @Error:
        """
        return self._buffer.get_time()

    def set_time(self, time):
        r"""SUMMARY

        set_time(_time)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_time(time)

    time = property(get_time, set_time)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class GetSelectionOwner(Request):
    r"""GetSelectionOwner

    GetSelectionOwner is a Request.
    Responsibility:
    """
    def __init__(self, selection, checked=True, display=None):
        r"""

        @Arguments:
        - `selection`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.GetSelectionOwner, xproto.GetSelectionOwnerCookie,
            checked, display, xproto.GetSelectionOwnerReply)
        self._buffer = _buffer.GetSelectionOwner(selection)

    def get_selection(self, ):
        r"""SUMMARY

        get_selection()

        @Return:

        @Error:
        """
        return self._buffer.get_selection()

    def set_selection(self, selection):
        r"""SUMMARY

        set_selection(_selection)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_selection(selection)

    selection = property(get_selection, set_selection)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class ConvertSelection(Request):
    r"""ConvertSelection

    ConvertSelection is a Request.
    Responsibility:
    """
    def __init__(self, requestor, selection, target, property_, time,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `requestor`:
        - `selection`:
        - `target`:
        - `property`:
        - `time`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.ConvertSelection, VoidCookie, checked, display)
        self._buffer = _buffer.ConvertSelection(
            requestor, selection, target, property_, time)

    def get_requestor(self, ):
        r"""SUMMARY

        get_requestor()

        @Return:

        @Error:
        """
        return self._buffer.get_requestor()

    def set_requestor(self, requestor):
        r"""SUMMARY

        set_requestor(_requestor)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_requestor(requestor)

    requestor = property(get_requestor, set_requestor)

    def get_selection(self, ):
        r"""SUMMARY

        get_selection()

        @Return:

        @Error:
        """
        return self._buffer.get_selection()

    def set_selection(self, selection):
        r"""SUMMARY

        set_selection(_selection)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_selection(selection)

    selection = property(get_selection, set_selection)

    def get_target(self, ):
        r"""SUMMARY

        get_target()

        @Return:

        @Error:
        """
        return self._buffer.get_target()

    def set_target(self, target):
        r"""SUMMARY

        set_target(_target)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_target(target)

    target = property(get_target, set_target)

    def get_property(self, ):
        r"""SUMMARY

        get_property()

        @Return:

        @Error:
        """
        return self._buffer.get_property()

    def set_property(self, property_):
        r"""SUMMARY

        set_property(_property)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_property(property_)

    property_ = property(get_property, set_property)

    def get_time(self, ):
        r"""SUMMARY

        get_time()

        @Return:

        @Error:
        """
        return self._buffer.get_time()

    def set_time(self, time):
        r"""SUMMARY

        set_time(_time)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_time(time)

    time = property(get_time, set_time)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class SendEvent(Request):
    r"""SendEvent

    SendEvent is a Request.
    Responsibility:
    """
    def __init__(self, propagate, destination, event_mask, event,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `propagate`:
        - `destination`:
        - `event_mask`:
        - `event`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.SendEvent, VoidCookie, checked, display)
        self._buffer = _buffer.SendEvent(
            propagate, destination, event_mask, event)

    def get_propagate(self, ):
        r"""SUMMARY

        get_propagate()

        @Return:

        @Error:
        """
        return self._buffer.get_propagate()

    def set_propagate(self, propagate):
        r"""SUMMARY

        set_propagate(_propagate)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_propagate(propagate)

    propagate = property(get_propagate, set_propagate)

    def get_destination(self, ):
        r"""SUMMARY

        get_destination()

        @Return:

        @Error:
        """
        return self._buffer.get_destination()

    def set_destination(self, destination):
        r"""SUMMARY

        set_destination(_destination)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_destination(destination)

    destination = property(get_destination, set_destination)

    def get_event_mask(self, ):
        r"""SUMMARY

        get_event_mask()

        @Return:

        @Error:
        """
        return self._buffer.get_event_mask()

    def set_event_mask(self, event_mask):
        r"""SUMMARY

        set_event_mask(_event_mask)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_event_mask(event_mask)

    event_mask = property(get_event_mask, set_event_mask)

    def get_event(self, ):
        r"""SUMMARY

        get_event()

        @Return:

        @Error:
        """
        return self._buffer.get_event()

    def set_event(self, event):
        r"""SUMMARY

        set_event(_event)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_event(event)

    event = property(get_event, set_event)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class GrabPointer(Request):
    r"""GrabPointer

    GrabPointer is a Request.
    Responsibility:
    """
    def __init__(self, owner_events, grab_window, event_mask, pointer_mode,
                 keyboard_mode, confine_to, cursor, time, checked=True,
                 display=None):
        r"""

        @Arguments:
        - `owner_events`:
        - `grab_window`:
        - `event_mask`:
        - `pointer_mode`:
        - `keyboard_mode`:
        - `confine_to`:
        - `cursor`:
        - `time`:
        """
        Request.__init__(self, Opcode.GrabPointer, xproto.GrabPointerCookie,
                         checked, display, xproto.GrabPointerReply)
        self._buffer = _buffer.GrabPointer(
            owner_events, grab_window, event_mask, pointer_mode,
            keyboard_mode, confine_to, cursor, time)

    def get_owner_events(self, ):
        r"""SUMMARY

        get_owner_events()

        @Return:

        @Error:
        """
        return self._buffer.get_owner_events()

    def set_owner_events(self, owner_events):
        r"""SUMMARY

        set_owner_events(_owner_events)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_owner_events(owner_events)

    owner_events = property(get_owner_events, set_owner_events)

    def get_grab_window(self, ):
        r"""SUMMARY

        get_grab_window()

        @Return:

        @Error:
        """
        return self._buffer.get_grab_window()

    def set_grab_window(self, grab_window):
        r"""SUMMARY

        set_grab_window(_grab_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_grab_window(grab_window)

    grab_window = property(get_grab_window, set_grab_window)

    def get_event_mask(self, ):
        r"""SUMMARY

        get_event_mask()

        @Return:

        @Error:
        """
        return self._buffer.get_event_mask()

    def set_event_mask(self, event_mask):
        r"""SUMMARY

        set_event_mask(_event_mask)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_event_mask(event_mask)

    event_mask = property(get_event_mask, set_event_mask)

    def get_pointer_mode(self, ):
        r"""SUMMARY

        get_pointer_mode()

        @Return:

        @Error:
        """
        return self._buffer.get_pointer_mode()

    def set_pointer_mode(self, pointer_mode):
        r"""SUMMARY

        set_pointer_mode(_pointer_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_pointer_mode(pointer_mode)

    pointer_mode = property(get_pointer_mode, set_pointer_mode)

    def get_keyboard_mode(self, ):
        r"""SUMMARY

        get_keyboard_mode()

        @Return:

        @Error:
        """
        return self._buffer.get_keyboard_mode()

    def set_keyboard_mode(self, keyboard_mode):
        r"""SUMMARY

        set_keyboard_mode(_keyboard_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_keyboard_mode(keyboard_mode)

    keyboard_mode = property(get_keyboard_mode, set_keyboard_mode)

    def get_confine_to(self, ):
        r"""SUMMARY

        get_confine_to()

        @Return:

        @Error:
        """
        return self._buffer.get_confine_to()

    def set_confine_to(self, confine_to):
        r"""SUMMARY

        set_confine_to(_confine_to)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_confine_to(confine_to)

    confine_to = property(get_confine_to, set_confine_to)

    def get_cursor(self, ):
        r"""SUMMARY

        get_cursor()

        @Return:

        @Error:
        """
        return self._buffer.get_cursor()

    def set_cursor(self, cursor):
        r"""SUMMARY

        set_cursor(_cursor)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_cursor(cursor)

    cursor = property(get_cursor, set_cursor)

    def get_time(self, ):
        r"""SUMMARY

        get_time()

        @Return:

        @Error:
        """
        return self._buffer.get_time()

    def set_time(self, time):
        r"""SUMMARY

        set_time(_time)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_time(time)

    time = property(get_time, set_time)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class UngrabPointer(Request):
    r"""UngrabPointer

    UngrabPointer is a Request.
    Responsibility:
    """
    def __init__(self, time, checked=False, display=None):
        r"""

        @Arguments:
        - `time`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.UngrabPointer, VoidCookie, checked, display)
        self._buffer = _buffer.UngrabPointer(time)

    def get_time(self, ):
        r"""SUMMARY

        get_time()

        @Return:

        @Error:
        """
        return self._buffer.get_time()

    def set_time(self, time):
        r"""SUMMARY

        set_time(_time)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_time(time)

    time = property(get_time, set_time)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class GrabButton(Request):
    r"""GrabButton

    GrabButton is a Request.
    Responsibility:
    """
    def __init__(self, owner_events, grab_window, event_mask, pointer_mode,
                 keyboard_mode, confine_to, cursor, button, modifiers,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `owner_events`:
        - `grab_window`:
        - `event_mask`:
        - `pointer_mode`:
        - `keyboard_mode`:
        - `confine_to`:
        - `cursor`:
        - `button`:
        - `modifiers`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.GrabButton, VoidCookie, checked, display)
        self._buffer = _buffer.GrabButton(
            owner_events, grab_window, event_mask, pointer_mode,
            keyboard_mode, confine_to, cursor, button, modifiers)

    def get_owner_events(self, ):
        r"""SUMMARY

        get_owner_events()

        @Return:

        @Error:
        """
        return self._buffer.get_owner_events()

    def set_owner_events(self, owner_events):
        r"""SUMMARY

        set_owner_events(_owner_events)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_owner_events(owner_events)

    owner_events = property(get_owner_events, set_owner_events)

    def get_grab_window(self, ):
        r"""SUMMARY

        get_grab_window()

        @Return:

        @Error:
        """
        return self._buffer.get_grab_window()

    def set_grab_window(self, grab_window):
        r"""SUMMARY

        set_grab_window(_grab_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_grab_window(grab_window)

    grab_window = property(get_grab_window, set_grab_window)

    def get_event_mask(self, ):
        r"""SUMMARY

        get_event_mask()

        @Return:

        @Error:
        """
        return self._buffer.get_event_mask()

    def set_event_mask(self, event_mask):
        r"""SUMMARY

        set_event_mask(_event_mask)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_event_mask(event_mask)

    event_mask = property(get_event_mask, set_event_mask)

    def get_pointer_mode(self, ):
        r"""SUMMARY

        get_pointer_mode()

        @Return:

        @Error:
        """
        return self._buffer.get_pointer_mode()

    def set_pointer_mode(self, pointer_mode):
        r"""SUMMARY

        set_pointer_mode(_pointer_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_pointer_mode(pointer_mode)

    pointer_mode = property(get_pointer_mode, set_pointer_mode)

    def get_keyboard_mode(self, ):
        r"""SUMMARY

        get_keyboard_mode()

        @Return:

        @Error:
        """
        return self._buffer.get_keyboard_mode()

    def set_keyboard_mode(self, keyboard_mode):
        r"""SUMMARY

        set_keyboard_mode(_keyboard_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_keyboard_mode(keyboard_mode)

    keyboard_mode = property(get_keyboard_mode, set_keyboard_mode)

    def get_confine_to(self, ):
        r"""SUMMARY

        get_confine_to()

        @Return:

        @Error:
        """
        return self._buffer.get_confine_to()

    def set_confine_to(self, confine_to):
        r"""SUMMARY

        set_confine_to(_confine_to)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_confine_to(confine_to)

    confine_to = property(get_confine_to, set_confine_to)

    def get_cursor(self, ):
        r"""SUMMARY

        get_cursor()

        @Return:

        @Error:
        """
        return self._buffer.get_cursor()

    def set_cursor(self, cursor):
        r"""SUMMARY

        set_cursor(_cursor)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_cursor(cursor)

    cursor = property(get_cursor, set_cursor)

    def get_button(self, ):
        r"""SUMMARY

        get_button()

        @Return:

        @Error:
        """
        return self._buffer.get_button()

    def set_button(self, button):
        r"""SUMMARY

        set_button(_button)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_button(button)

    button = property(get_button, set_button)

    def get_modifiers(self, ):
        r"""SUMMARY

        get_modifiers()

        @Return:

        @Error:
        """
        return self._buffer.get_modifiers()

    def set_modifiers(self, modifiers):
        r"""SUMMARY

        set_modifiers(_modifiers)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_modifiers(modifiers)

    modifiers = property(get_modifiers, set_modifiers)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class UngrabButton(Request):
    r"""UngrabButton

    UngrabButton is a Request.
    Responsibility:
    """
    def __init__(self, button, grab_window, modifiers,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `button`:
        - `grab_window`:
        - `modifiers`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.UngrabButton, VoidCookie, checked, display)
        self._buffer = _buffer.UngrabButton(button, grab_window, modifiers)

    def get_button(self, ):
        r"""SUMMARY

        get_button()

        @Return:

        @Error:
        """
        return self._buffer.get_button()

    def set_button(self, button):
        r"""SUMMARY

        set_button(_button)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_button(button)

    button = property(get_button, set_button)

    def get_grab_window(self, ):
        r"""SUMMARY

        get_grab_window()

        @Return:

        @Error:
        """
        return self._buffer.get_grab_window()

    def set_grab_window(self, grab_window):
        r"""SUMMARY

        set_grab_window(_grab_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_grab_window(grab_window)

    grab_window = property(get_grab_window, set_grab_window)

    def get_modifiers(self, ):
        r"""SUMMARY

        get_modifiers()

        @Return:

        @Error:
        """
        return self._buffer.get_modifiers()

    def set_modifiers(self, modifiers):
        r"""SUMMARY

        set_modifiers(_modifiers)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_modifiers(modifiers)

    modifiers = property(get_modifiers, set_modifiers)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class ChangeActivePointerGrab(Request):
    r"""ChangeActivePointerGrab

    ChangeActivePointerGrab is a Request.
    Responsibility:
    """
    def __init__(self, cursor, time, event_mask, checked=False, display=None):
        r"""

        @Arguments:
        - `cursor`:
        - `time`:
        - `event_mask`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.ChangeActivePointerGrab, VoidCookie, checked, display)
        self._buffer = _buffer.ChangeActivePointerGrab(
            cursor, time, event_mask)

    def get_cursor(self, ):
        r"""SUMMARY

        get_cursor()

        @Return:

        @Error:
        """
        return self._buffer.get_cursor()

    def set_cursor(self, cursor):
        r"""SUMMARY

        set_cursor(_cursor)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_cursor(cursor)

    cursor = property(get_cursor, set_cursor)

    def get_time(self, ):
        r"""SUMMARY

        get_time()

        @Return:

        @Error:
        """
        return self._buffer.get_time()

    def set_time(self, time):
        r"""SUMMARY

        set_time(_time)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_time(time)

    time = property(get_time, set_time)

    def get_event_mask(self, ):
        r"""SUMMARY

        get_event_mask()

        @Return:

        @Error:
        """
        return self._buffer.get_event_mask()

    def set_event_mask(self, event_mask):
        r"""SUMMARY

        set_event_mask(_event_mask)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_event_mask(event_mask)

    event_mask = property(get_event_mask, set_event_mask)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class GrabKeyboard(Request):
    r"""GrabKeyboard

    GrabKeyboard is a Request.
    Responsibility:
    """
    def __init__(self, owner_events, grab_window, time, pointer_mode,
                 keyboard_mode, checked=True, display=None):
        r"""

        @Arguments:
        - `owner_events`:
        - `grab_window`:
        - `time`:
        - `pointer_mode`:
        - `keyboard_mode`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.GrabKeyboard, xproto.GrabKeyboardCookie,
                         checked, display, xproto.GrabKeyboardReply)
        self._buffer = _buffer.GrabKeyboard(
            owner_events, grab_window, time, pointer_mode, keyboard_mode,)

    def get_owner_events(self, ):
        r"""SUMMARY

        get_owner_events()

        @Return:

        @Error:
        """
        return self._buffer.get_owner_events()

    def set_owner_events(self, owner_events):
        r"""SUMMARY

        set_owner_events(_owner_events)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_owner_events(owner_events)

    owner_events = property(get_owner_events, set_owner_events)

    def get_grab_window(self, ):
        r"""SUMMARY

        get_grab_window()

        @Return:

        @Error:
        """
        return self._buffer.get_grab_window()

    def set_grab_window(self, grab_window):
        r"""SUMMARY

        set_grab_window(_grab_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_grab_window(grab_window)

    grab_window = property(get_grab_window, set_grab_window)

    def get_time(self, ):
        r"""SUMMARY

        get_time()

        @Return:

        @Error:
        """
        return self._buffer.get_time()

    def set_time(self, time):
        r"""SUMMARY

        set_time(_time)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_time(time)

    time = property(get_time, set_time)

    def get_pointer_mode(self, ):
        r"""SUMMARY

        get_pointer_mode()

        @Return:

        @Error:
        """
        return self._buffer.get_pointer_mode()

    def set_pointer_mode(self, pointer_mode):
        r"""SUMMARY

        set_pointer_mode(_pointer_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_pointer_mode(pointer_mode)

    pointer_mode = property(get_pointer_mode, set_pointer_mode)

    def get_keyboard_mode(self, ):
        r"""SUMMARY

        get_keyboard_mode()

        @Return:

        @Error:
        """
        return self._buffer.get_keyboard_mode()

    def set_keyboard_mode(self, keyboard_mode):
        r"""SUMMARY

        set_keyboard_mode(_keyboard_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_keyboard_mode(keyboard_mode)

    keyboard_mode = property(get_keyboard_mode, set_keyboard_mode)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class UngrabKeyboard(Request):
    r"""UngrabKeyboard

    UngrabKeyboard is a Request.
    Responsibility:
    """
    def __init__(self, time, checked=False, display=None):
        r"""

        @Arguments:
        - `time`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, UngrabKeyboard, VoidCookie, checked, display)
        self._buffer = _buffer.UngrabKeyboard(time)

    def get_time(self, ):
        r"""SUMMARY

        get_time()

        @Return:

        @Error:
        """
        return self._buffer.get_time()

    def set_time(self, time):
        r"""SUMMARY

        set_time(_time)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_time(time)

    time = property(get_time, set_time)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class GrabKey(Request):
    r"""GrabKey

    GrabKey is a Request.
    Responsibility:
    """
    def __init__(self, owner_events, grab_window, modifiers, key,
                 pointer_mode,keyboard_mode, checked=False, display=None):
        r"""

        @Arguments:
        - `owner_events`:
        - `grab_window`:
        - `modifiers`:
        - `key`:
        - `pointer_mode`:
        - `keyboard_mode`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.GrabKey, VoidCookie, checked, display)
        self._buffer = _buffer.GrabKey(
            owner_events, grab_window, modifiers, key, pointer_mode,
            keyboard_mode)

    def get_owner_events(self, ):
        r"""SUMMARY

        get_owner_events()

        @Return:

        @Error:
        """
        return self._buffer.get_owner_events()

    def set_owner_events(self, owner_events):
        r"""SUMMARY

        set_owner_events(_owner_events)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_owner_events(owner_events)

    owner_events = property(get_owner_events, set_owner_events)

    def get_grab_window(self, ):
        r"""SUMMARY

        get_grab_window()

        @Return:

        @Error:
        """
        return self._buffer.get_grab_window()

    def set_grab_window(self, grab_window):
        r"""SUMMARY

        set_grab_window(_grab_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_grab_window(grab_window)

    grab_window = property(get_grab_window, set_grab_window)

    def get_modifiers(self, ):
        r"""SUMMARY

        get_modifiers()

        @Return:

        @Error:
        """
        return self._buffer.get_modifiers()

    def set_modifiers(self, modifiers):
        r"""SUMMARY

        set_modifiers(_modifiers)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_modifiers(modifiers)

    modifiers = property(get_modifiers, set_modifiers)

    def get_key(self, ):
        r"""SUMMARY

        get_key()

        @Return:

        @Error:
        """
        return self._buffer.get_key()

    def set_key(self, key):
        r"""SUMMARY

        set_key(_key)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_key(key)

    key = property(get_key, set_key)

    def get_pointer_mode(self, ):
        r"""SUMMARY

        get_pointer_mode()

        @Return:

        @Error:
        """
        return self._buffer.get_pointer_mode()

    def set_pointer_mode(self, pointer_mode):
        r"""SUMMARY

        set_pointer_mode(_pointer_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_pointer_mode(pointer_mode)

    pointer_mode = property(get_pointer_mode, set_pointer_mode)

    def get_keyboard_mode(self, ):
        r"""SUMMARY

        get_keyboard_mode()

        @Return:

        @Error:
        """
        return self._buffer.get_keyboard_mode()

    def set_keyboard_mode(self, keyboard_mode):
        r"""SUMMARY

        set_keyboard_mode(_keyboard_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_keyboard_mode(keyboard_mode)

    keyboard_mode = property(get_keyboard_mode, set_keyboard_mode)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class UngrabKey(Request):
    r"""UngrabKey

    UngrabKey is a Request.
    Responsibility:
    """
    def __init__(self, key, grab_window, modifiers, checked=False,
                 display=None):
        r"""

        @Arguments:
        - `key`:
        - `grab_window`:
        - `modifiers`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.UngrabKey, VoidCookie, checked, display)
        self._buffer = _buffer.UngrabKey(key, grab_window, modifiers)

    def get_key(self, ):
        r"""SUMMARY

        get_key()

        @Return:

        @Error:
        """
        return self._buffer.get_key()

    def set_key(self, key):
        r"""SUMMARY

        set_key(_key)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_key(key)

    key = property(get_key, set_key)

    def get_grab_window(self, ):
        r"""SUMMARY

        get_grab_window()

        @Return:

        @Error:
        """
        return self._buffer.get_grab_window()

    def set_grab_window(self, grab_window):
        r"""SUMMARY

        set_grab_window(_grab_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_grab_window(grab_window)

    grab_window = property(get_grab_window, set_grab_window)

    def get_modifiers(self, ):
        r"""SUMMARY

        get_modifiers()

        @Return:

        @Error:
        """
        return self._buffer.get_modifiers()

    def set_modifiers(self, modifiers):
        r"""SUMMARY

        set_modifiers(_modifiers)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_modifiers(modifiers)

    modifiers = property(get_modifiers, set_modifiers)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class AllowEvents(Request):
    r"""AllowEvents

    AllowEvents is a Request.
    Responsibility:
    """
    def __init__(self, mode, time, checked=False, display=None):
        r"""

        @Arguments:
        - `mode`:
        - `time`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.AllowEvents, VoidCookie, checked, display)
        self._buffer = _buffer.AllowEvents(mode, time)

    def get_mode(self, ):
        r"""SUMMARY

        get_mode()

        @Return:

        @Error:
        """
        return self._buffer.get_mode()

    def set_mode(self, mode):
        r"""SUMMARY

        set_mode(_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_mode(mode)

    mode = property(get_mode, set_mode)

    def get_time(self, ):
        r"""SUMMARY

        get_time()

        @Return:

        @Error:
        """
        return self._buffer.get_time()

    def set_time(self, time):
        r"""SUMMARY

        set_time(_time)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_time(time)

    time = property(get_time, set_time)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class GrabServer(Request):
    r"""GrabServer

    GrabServer is a Request.
    Responsibility:
    """
    def __init__(self, checked=False, display=None):
        r"""

        @Arguments:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.GrabServer, VoidCookie, checked, display)
        self._buffer = _buffer.GrabServer()

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class UngrabServer(Request):
    r"""UngrabServer

    UngrabServer is a Request.
    Responsibility:
    """
    def __init__(self, checked=False, display=None):
        r"""

        @Arguments:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.UngrabServer, VoidCookie, checked, display)
        self._buffer = _buffer.UngrabServer()

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class QueryPointer(Request):
    r"""QueryPointer

    QueryPointer is a Request.
    Responsibility:
    """
    def __init__(self, window, checked=True, display=None):
        r"""

        @Arguments:
        - `window`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.QueryPointer, xproto.QueryPointerCookie,
                         checked, display, xproto.QueryPointerReply)
        self._buffer = _buffer.QueryPointer(window)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._buffer.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_window(window)

    window = property(get_window, set_window)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()



class GetMotionEvents(Request):
    r"""GetMotionEvents

    GetMotionEvents is a Request.
    Responsibility:
    """
    def __init__(self, window, start, stop, checked=True, display=None):
        r"""

        @Arguments:
        - `window`:
        - `start`:
        - `stop`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.GetMotionEvents, xproto.GetMotionEventsCookie,
            checked, display, xproto.GetMotionEventsReply)
        self._buffer = _buffer.GetMotionEvents(window, start, stop)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._buffer.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_window(window)

    window = property(get_window, set_window)

    def get_start(self, ):
        r"""SUMMARY

        get_start()

        @Return:

        @Error:
        """
        return self._buffer.get_start()

    def set_start(self, start):
        r"""SUMMARY

        set_start(_start)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_start(start)

    start = property(get_start, set_start)

    def get_stop(self, ):
        r"""SUMMARY

        get_stop()

        @Return:

        @Error:
        """
        return self._buffer.get_stop()

    def set_stop(self, stop):
        r"""SUMMARY

        set_stop(_stop)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_stop(stop)

    stop = property(get_stop, set_stop)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class TranslateCoordinates(Request):
    r"""TranslateCoordinates

    TranslateCoordinates is a Request.
    Responsibility:
    """
    def __init__(self, src_window, dst_window, src_x, src_y,
                 checked=True, display=None):
        r"""

        @Arguments:
        - `src_window`:
        - `dst_window`:
        - `src_x`:
        - `src_y`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.TranslateCoordinates,
                         xproto.TranslateCoordinatesCookie, checked, display,
                         xproto.TranslateCoordinatesReply)
        self._buffer = _buffer.TranslateCoordinates(
            src_window, dst_window, src_x, src_y)

    def get_src_window(self, ):
        r"""SUMMARY

        get_src_window()

        @Return:

        @Error:
        """
        return self._buffer.get_src_window()

    def set_src_window(self, src_window):
        r"""SUMMARY

        set_src_window(_src_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_src_window(src_window)

    src_window = property(get_src_window, set_src_window)

    def get_dst_window(self, ):
        r"""SUMMARY

        get_dst_window()

        @Return:

        @Error:
        """
        return self._buffer.get_dst_window()

    def set_dst_window(self, dst_window):
        r"""SUMMARY

        set_dst_window(_dst_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_dst_window(dst_window)

    dst_window = property(get_dst_window, set_dst_window)

    def get_src_x(self, ):
        r"""SUMMARY

        get_src_x()

        @Return:

        @Error:
        """
        return self._buffer.get_src_x()

    def set_src_x(self, src_x):
        r"""SUMMARY

        set_src_x(_src_x)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_src_x(src_x)

    src_x = property(get_src_x, set_src_x)

    def get_src_y(self, ):
        r"""SUMMARY

        get_src_y()

        @Return:

        @Error:
        """
        return self._buffer.get_src_y()

    def set_src_y(self, src_y):
        r"""SUMMARY

        set_src_y(_src_y)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_src_y(src_y)

    src_y = property(get_src_y, set_src_y)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class WarpPointer(Request):
    r"""WarpPointer

    WarpPointer is a Request.
    Responsibility:
    """
    def __init__(self, src_window, dst_window, src_x, src_y,
                 src_width, src_height, dst_x, dst_y,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `src_window`:
        - `dst_window`:
        - `src_x`:
        - `src_y`:
        - `src_width`:
        - `src_height`:
        - `dst_x`:
        - `dst_y`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.WarpPointer, VoidCookie, checked, display)
        self._buffer = _buffer.WarpPointer(
            src_window, dst_window, src_x, src_y, src_width, src_height,
            dst_x, dst_y)

    def get_src_window(self, ):
        r"""SUMMARY

        get_src_window()

        @Return:

        @Error:
        """
        return self._buffer.get_src_window()

    def set_src_window(self, src_window):
        r"""SUMMARY

        set_src_window(_src_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_src_window(src_window)

    src_window = property(get_src_window, set_src_window)

    def get_dst_window(self, ):
        r"""SUMMARY

        get_dst_window()

        @Return:

        @Error:
        """
        return self._buffer.get_dst_window()

    def set_dst_window(self, dst_window):
        r"""SUMMARY

        set_dst_window(_dst_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_dst_window(dst_window)

    dst_window = property(get_dst_window, set_dst_window)

    def get_src_x(self, ):
        r"""SUMMARY

        get_src_x()

        @Return:

        @Error:
        """
        return self._buffer.get_src_x()

    def set_src_x(self, src_x):
        r"""SUMMARY

        set_src_x(_src_x)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_src_x(src_x)

    src_x = property(get_src_x, set_src_x)

    def get_src_y(self, ):
        r"""SUMMARY

        get_src_y()

        @Return:

        @Error:
        """
        return self._buffer.get_src_y()

    def set_src_y(self, src_y):
        r"""SUMMARY

        set_src_y(_src_y)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_src_y(src_y)

    src_y = property(get_src_y, set_src_y)

    def get_src_width(self, ):
        r"""SUMMARY

        get_src_width()

        @Return:

        @Error:
        """
        return self._buffer.get_src_width()

    def set_src_width(self, src_width):
        r"""SUMMARY

        set_src_width(_src_width)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_src_width(src_width)

    src_width = property(get_src_width, set_src_width)

    def get_src_width(self, ):
        r"""SUMMARY

        get_src_width()

        @Return:

        @Error:
        """
        return self._buffer.get_src_width()

    def set_src_width(self, src_width):
        r"""SUMMARY

        set_src_width(_src_width)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_src_width(src_width)

    src_width = property(get_src_width, set_src_width)

    def get_dst_x(self, ):
        r"""SUMMARY

        get_dst_x()

        @Return:

        @Error:
        """
        return self._buffer.get_dst_x()

    def set_dst_x(self, dst_x):
        r"""SUMMARY

        set_dst_x(_dst_x)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_dst_x(dst_x)

    dst_x = property(get_dst_x, set_dst_x)

    def get_dst_y(self, ):
        r"""SUMMARY

        get_dst_y()

        @Return:

        @Error:
        """
        return self._buffer.get_dst_y()

    def set_dst_y(self, dst_y):
        r"""SUMMARY

        set_dst_y(_dst_y)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_dst_y(dst_y)

    dst_y = property(get_dst_y, set_dst_y)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class SetInputFocus(Request):
    r"""SetInputFocus

    SetInputFocus is a Request.
    Responsibility:
    """
    def __init__(self, revert_to, focus, time, checked=False, display=None):
        r"""

        @Arguments:
        - `revert_to`:
        - `focus`:
        - `time`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.SetInputFocus, VoidCookie, checked, display)
        self._buffer = _buffer.SetInputFocus(revert_to, focus, time)

    def get_revert_to(self, ):
        r"""SUMMARY

        get_revert_to()

        @Return:

        @Error:
        """
        return self._buffer.get_revert_to()

    def set_revert_to(self, revert_to):
        r"""SUMMARY

        set_revert_to(_revert_to)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_revert_to(revert_to)

    revert_to = property(get_revert_to, set_revert_to)

    def get_focus(self, ):
        r"""SUMMARY

        get_focus()

        @Return:

        @Error:
        """
        return self._buffer.get_focus()

    def set_focus(self, focus):
        r"""SUMMARY

        set_focus(_focus)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_focus(focus)

    focus = property(get_focus, set_focus)

    def get_time(self, ):
        r"""SUMMARY

        get_time()

        @Return:

        @Error:
        """
        return self._buffer.get_time()

    def set_time(self, time):
        r"""SUMMARY

        set_time(_time)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_time(time)

    time = property(get_time, set_time)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class GetInputFocus(Request):
    r"""GetInputFocus

    GetInputFocus is a Request.
    Responsibility:
    """
    def __init__(self, checked=True, display=None):
        r"""

        @Arguments:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.GetInputFocus,
                         xproto.GetInputFocusCookie, checked, display,
                         xproto.GetInputFocusReply)
        self._buffer = _buffer.GetInputFocus()

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class QueryKeymap(Request):
    r"""QueryKeymap

    QueryKeymap is a Request.
    Responsibility:
    """
    def __init__(self, checked=True, display=None):
        r"""

        @Arguments:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.QueryKeymap, xproto.QueryKeymapCookie,
                         checked, display, xproto.QueryKeymapReply)
        self._buffer = _buffer.QueryKeymap()

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class OpenFont(Request):
    r"""OpenFont

    OpenFont is a Request.
    Responsibility:
    """
    def __init__(self, fid, name_len, name, checked=False, display=None):
        r"""

        @Arguments:
        - `fid`:
        - `name_len`:
        - `name`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.OpenFont, VoidCookie, checked, display)
        self._buffer = _buffer.OpenFont(fid, name)

    def get_fid(self, ):
        r"""SUMMARY

        get_fid()

        @Return:

        @Error:
        """
        return self._buffer.get_fid()

    def set_fid(self, fid):
        r"""SUMMARY

        set_fid(_fid)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_fid(fid)

    fid = property(get_fid, set_fid)

    def get_name(self, ):
        r"""SUMMARY

        get_name()

        @Return:

        @Error:
        """
        return self._buffer.get_name()

    def set_name(self, name):
        r"""SUMMARY

        set_name(_name)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_name(name)

    name = property(get_name, set_name)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class CloseFont(Request):
    r"""CloseFont

    CloseFont is a Request.
    Responsibility:
    """
    def __init__(self, font, checked=False, display=None):
        r"""

        @Arguments:
        - `font`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.CloseFont, VoidCookie, checked, display)
        self._buffer = _buffer.CloseFont(font)

    def get_font(self, ):
        r"""SUMMARY

        get_font()

        @Return:

        @Error:
        """
        return self._buffer.get_font()

    def set_font(self, font):
        r"""SUMMARY

        set_font(_font)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_font(font)

    font = property(get_font, set_font)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class QueryFont(Request):
    r"""QueryFont

    QueryFont is a Request.
    Responsibility:
    """
    def __init__(self, font, checked=True, display=None):
        r"""

        @Arguments:
        - `font`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.QueryFont, xproto.QueryFontCookie, checked, display)
        self._buffer = _buffer.QueryFont(font)

    def get_font(self, ):
        r"""SUMMARY

        get_font()

        @Return:

        @Error:
        """
        return self._buffer.get_font()

    def set_font(self, font):
        r"""SUMMARY

        set_font(_font)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_font(font)

    font = property(get_font, set_font)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class QueryTextExtents(Request):
    r"""QueryTextExtents

    QueryTextExtents is a Request.
    Responsibility:
    """
    def __init__(self, font, string_len, string, checked=True, display=None):
        r"""

        @Arguments:
        - `font`:
        - `string_len`:
        - `string`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.QueryTextExtents, xproto.QueryTextExtentsCookie,
            checked, display, xproto.QueryTextExtentsReply)
        self._buffer = _buffer.QueryTextExtents(font, string_len, string)

    def get_font(self, ):
        r"""SUMMARY

        get_font()

        @Return:

        @Error:
        """
        return self._buffer.get_font()

    def set_font(self, font):
        r"""SUMMARY

        set_font(_font)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_font(font)

    font = property(get_font, set_font)

    def get_string_len(self, ):
        r"""SUMMARY

        get_string_len()

        @Return:

        @Error:
        """
        return self._buffer.get_string_len()

    def set_string_len(self, string_len):
        r"""SUMMARY

        set_string_len(_string_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_string_len(string_len)

    string_len = property(get_string_len, set_string_len)

    def get_string(self, ):
        r"""SUMMARY

        get_string()

        @Return:

        @Error:
        """
        return self._buffer.get_string()

    def set_string(self, string):
        r"""SUMMARY

        set_string(_string)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_string(string)

    string = property(get_string, set_string)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class ListFonts(Request):
    r"""ListFonts

    ListFonts is a Request.
    Responsibility:
    """
    def __init__(self, max_names, pattern_len, pattern,
                 checked=True, display=None):
        r"""

        @Arguments:
        - `max_names`:
        - `pattern_len`:
        - `pattern`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.ListFonts, xproto.ListFontsCookie,
                         checked, display, xproto.ListFontsReply)
        self._buffer = _buffer.ListFonts(max_names, pattern_len, pattern)

    def get_max_names(self, ):
        r"""SUMMARY

        get_max_names()

        @Return:

        @Error:
        """
        return self._buffer.get_max_names()

    def set_max_names(self, max_names):
        r"""SUMMARY

        set_max_names(_max_names)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_max_names(max_names)

    max_names = property(get_max_names, set_max_names)

    def get_pattern_len(self, ):
        r"""SUMMARY

        get_pattern_len()

        @Return:

        @Error:
        """
        return self._buffer.get_pattern_len()

    def set_pattern_len(self, pattern_len):
        r"""SUMMARY

        set_pattern_len(_pattern_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_pattern_len(pattern_len)

    pattern_len = property(get_pattern_len, set_pattern_len)

    def get_pattern(self, ):
        r"""SUMMARY

        get_pattern()

        @Return:

        @Error:
        """
        return self._buffer.get_pattern()

    def set_pattern(self, pattern):
        r"""SUMMARY

        set_pattern(_pattern)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_pattern(pattern)

    pattern = property(get_pattern, set_pattern)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class ListFontsWithInfo(Request):
    r"""ListFontsWithInfo

    ListFontsWithInfo is a Request.
    Responsibility:
    """
    def __init__(self, max_names, pattern_len, pattern,
                 checked=True, display=None):
        r"""

        @Arguments:
        - `max_names`:
        - `pattern_len`:
        - `pattern`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.ListFontsWithInfo, xproto.ListFontsWithInfoCookie,
            checked, display, xproto.ListFontsWithInfoReply)
        self._buffer = _buffer.ListFontsWithInfo(
            max_names, pattern_len, pattern)

    def get_max_names(self, ):
        r"""SUMMARY

        get_max_names()

        @Return:

        @Error:
        """
        return self._buffer.get_max_names()

    def set_max_names(self, max_names):
        r"""SUMMARY

        set_max_names(_max_names)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_max_names(max_names)

    max_names = property(get_max_names, set_max_names)

    def get_pattern_len(self, ):
        r"""SUMMARY

        get_pattern_len()

        @Return:

        @Error:
        """
        return self._buffer.get_pattern_len()

    def set_pattern_len(self, pattern_len):
        r"""SUMMARY

        set_pattern_len(_pattern_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_pattern_len(pattern_len)

    pattern_len = property(get_pattern_len, set_pattern_len)

    def get_pattern(self, ):
        r"""SUMMARY

        get_pattern()

        @Return:

        @Error:
        """
        return self._buffer.get_pattern()

    def set_pattern(self, pattern):
        r"""SUMMARY

        set_pattern(_pattern)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_pattern(pattern)

    pattern = property(get_pattern, set_pattern)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class SetFontPath(Request):
    r"""SetFontPath

    SetFontPath is a Request.
    Responsibility:
    """
    def __init__(self, font_qty, font, checked=False, display=None):
        r"""

        @Arguments:
        - `font_qty`:
        - `font`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.SetFontPath, VoidCookie, checked, display)
        self._buffer = _buffer.SetFontPath(font_qty, font)

    def get_font_qty(self, ):
        r"""SUMMARY

        get_font_qty()

        @Return:

        @Error:
        """
        return self._buffer.get_font_qty()

    def set_font_qty(self, font_qty):
        r"""SUMMARY

        set_font_qty(_font_qty)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_font_qty(font_qty)

    font_qty = property(get_font_qty, set_font_qty)

    def get_font(self, ):
        r"""SUMMARY

        get_font()

        @Return:

        @Error:
        """
        return self._buffer.get_font()

    def set_font(self, font):
        r"""SUMMARY

        set_font(_font)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_font(font)

    font = property(get_font, set_font)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class GetFontPath(Request):
    r"""GetFontPath

    GetFontPath is a Request.
    Responsibility:
    """
    def __init__(self, checked=True, display=None):
        r"""

        @Arguments:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.GetFontPath, xproto.GetFontPathCookie,
                         checked, display, xproto.GetFontPathReply)
        self._buffer = _buffer.GetFontPath()

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class CreatePixmap(Request):
    r"""CreatePixmap

    CreatePixmap is a Request.
    Responsibility:
    """
    def __init__(self, depth, pid, drawable, width, height,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `depth`:
        - `pid`:
        - `drawable`:
        - `width`:
        - `height`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.CreatePixmap, VoidCookie, checked, display)
        self._buffer = _buffer.CreatePixmap(
            depth, pid, drawable, width, height)

    def get_depth(self, ):
        r"""SUMMARY

        get_depth()

        @Return:

        @Error:
        """
        return self._buffer.get_depth()

    def set_depth(self, depth):
        r"""SUMMARY

        set_depth(_depth)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_depth(depth)

    depth = property(get_depth, set_depth)

    def get_pid(self, ):
        r"""SUMMARY

        get_pid()

        @Return:

        @Error:
        """
        return self._buffer.get_pid()

    def set_pid(self, pid):
        r"""SUMMARY

        set_pid(_pid)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_pid(pid)

    pid = property(get_pid, set_pid)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._buffer.get_drawable()

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(_drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_drawable(drawable)

    drawable = property(get_drawable, set_drawable)

    def get_width(self, ):
        r"""SUMMARY

        get_width()

        @Return:

        @Error:
        """
        return self._buffer.get_width()

    def set_width(self, width):
        r"""SUMMARY

        set_width(_width)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_width(width)

    width = property(get_width, set_width)

    def get_height(self, ):
        r"""SUMMARY

        get_height()

        @Return:

        @Error:
        """
        return self._buffer.get_height()

    def set_height(self, height):
        r"""SUMMARY

        set_height(_height)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_height(height)

    height = property(get_height, set_height)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class FreePixmap(Request):
    r"""FreePixmap

    FreePixmap is a Request.
    Responsibility:
    """
    def __init__(self, pixmap, checked=False, display=None):
        r"""

        @Arguments:
        - `pixmap`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.FreePixmap, VoidCookie, checked, display)
        self._buffer = _buffer.FreePixmap(pixmap)

    def get_pixmap(self, ):
        r"""SUMMARY

        get_pixmap()

        @Return:

        @Error:
        """
        return self._buffer.get_pixmap()

    def set_pixmap(self, pixmap):
        r"""SUMMARY

        set_pixmap(_pixmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_pixmap(pixmap)

    pixmap = property(get_pixmap, set_pixmap)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class CreateGC(Request):
    r"""CreateGC

    CreateGC is a Request.
    Responsibility:
    """
    def __init__(self, cid, drawable, value_mask, value_list,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `cid`:
        - `drawable`:
        - `value_mask`:
        - `value_list`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.CreateGC, VoidCookie, checked, display)
        self._buffer = _buffer.CreateGC(cid, drawable, value_mask, value_list)

    def get_cid(self, ):
        r"""SUMMARY

        get_cid()

        @Return:

        @Error:
        """
        return self._buffer.get_cid()

    def set_cid(self, cid):
        r"""SUMMARY

        set_cid(_cid)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_cid(cid)

    cid = property(get_cid, set_cid)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._buffer.get_drawable()

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(_drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_drawable(drawable)

    drawable = property(get_drawable, set_drawable)

    def get_value_mask(self, ):
        r"""SUMMARY

        get_value_mask()

        @Return:

        @Error:
        """
        return self._buffer.get_value_mask()

    def set_value_mask(self, value_mask):
        r"""SUMMARY

        set_value_mask(_value_mask)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_value_mask(value_mask)

    value_mask = property(get_value_mask, set_value_mask)

    def get_value_list(self, ):
        r"""SUMMARY

        get_value_list()

        @Return:

        @Error:
        """
        return self._buffer.get_value_list()

    def set_value_list(self, value_list):
        r"""SUMMARY

        set_value_list(_value_list)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_value_list(value_list)

    value_list = property(get_value_list, set_value_list)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class ChangeGC(Request):
    r"""ChangeGC

    ChangeGC is a Request.
    Responsibility:
    """
    def __init__(self, gc, value_mask, value_list,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `gc`:
        - `value_mask`:
        - `value_list`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.ChangeGC, VoidCookie, checked, display)
        self._buffer = _buffer.ChangeGC(gc, value_mask, value_list)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._buffer.get_gc()

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(_gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_gc(gc)

    gc = property(get_gc, set_gc)

    def get_value_mask(self, ):
        r"""SUMMARY

        get_value_mask()

        @Return:

        @Error:
        """
        return self._buffer.get_value_mask()

    def set_value_mask(self, value_mask):
        r"""SUMMARY

        set_value_mask(_value_mask)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_value_mask(value_mask)

    value_mask = property(get_value_mask, set_value_mask)

    def get_value_list(self, ):
        r"""SUMMARY

        get_value_list()

        @Return:

        @Error:
        """
        return self._buffer.get_value_list()

    def set_value_list(self, value_list):
        r"""SUMMARY

        set_value_list(_value_list)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_value_list(value_list)

    value_list = property(get_value_list, set_value_list)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class CopyGC(Request):
    r"""CopyGC

    CopyGC is a Request.
    Responsibility:
    """
    def __init__(self, src_gc, dst_gc, value_mask, checked=False, display=None):
        r"""

        @Arguments:
        - `src_gc`:
        - `dst_gc`:
        - `value_mask`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.CopyGC, VoidCookie, checked, display)
        self._buffer = _buffer.CopyGC(src_gc, dst_gc, value_mask)

    def get_src_gc(self, ):
        r"""SUMMARY

        get_src_gc()

        @Return:

        @Error:
        """
        return self._buffer.get_src_gc()

    def set_src_gc(self, src_gc):
        r"""SUMMARY

        set_src_gc(_src_gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_src_gc(src_gc)

    src_gc = property(get_src_gc, set_src_gc)

    def get_dst_gc(self, ):
        r"""SUMMARY

        get_dst_gc()

        @Return:

        @Error:
        """
        return self._buffer.get_dst_gc()

    def set_dst_gc(self, dst_gc):
        r"""SUMMARY

        set_dst_gc(_dst_gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_dst_gc(dst_gc)

    dst_gc = property(get_dst_gc, set_dst_gc)

    def get_value_mask(self, ):
        r"""SUMMARY

        get_value_mask()

        @Return:

        @Error:
        """
        return self._buffer.get_value_mask()

    def set_value_mask(self, value_mask):
        r"""SUMMARY

        set_value_mask(_value_mask)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_value_mask(value_mask)

    value_mask = property(get_value_mask, set_value_mask)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class SetDashes(Request):
    r"""SetDashes

    SetDashes is a Request.
    Responsibility:
    """
    def __init__(self, gc, dash_offset, dashes_len, dashes,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `gc`:
        - `dash_offset`:
        - `dashes_len`:
        - `dashes`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.SetDashes, VoidCookie, checked, display)
        self._buffer = _buffer.SetDashes(gc, dash_offset, dashes_len, dashes)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._buffer.get_gc()

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(_gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_gc(gc)

    gc = property(get_gc, set_gc)

    def get_dash_offset(self, ):
        r"""SUMMARY

        get_dash_offset()

        @Return:

        @Error:
        """
        return self._buffer.get_dash_offset()

    def set_dash_offset(self, dash_offset):
        r"""SUMMARY

        set_dash_offset(_dash_offset)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_dash_offset(dash_offset)

    dash_offset = property(get_dash_offset, set_dash_offset)

    def get_dash_offset(self, ):
        r"""SUMMARY

        get_dash_offset()

        @Return:

        @Error:
        """
        return self._buffer.get_dash_offset()

    def set_dash_offset(self, dash_offset):
        r"""SUMMARY

        set_dash_offset(_dash_offset)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_dash_offset(dash_offset)

    dash_offset = property(get_dash_offset, set_dash_offset)

    def get_dashes_len(self, ):
        r"""SUMMARY

        get_dashes_len()

        @Return:

        @Error:
        """
        return self._buffer.get_dashes_len()

    def set_dashes_len(self, dashes_len):
        r"""SUMMARY

        set_dashes_len(_dashes_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_dashes_len(dashes_len)

    dashes_len = property(get_dashes_len, set_dashes_len)

    def get_dashes(self, ):
        r"""SUMMARY

        get_dashes()

        @Return:

        @Error:
        """
        return self._buffer.get_dashes()

    def set_dashes(self, dashes):
        r"""SUMMARY

        set_dashes(_dashes)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_dashes(dashes)

    dashes = property(get_dashes, set_dashes)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class SetClipRectangles(Request):
    r"""SetClipRectangles

    SetClipRectangles is a Request.
    Responsibility:
    """
    def __init__(self, ordering, gc, clip_x_origin, clip_y_origin,
                 rectangles_len, rectangles, checked=False, display=None):
        r"""

        @Arguments:
        - `ordering`:
        - `gc`:
        - `clip_x_origin`:
        - `clip_y_origin`:
        - `rectangles_len`:
        - `rectangles`:
        """
        Request.__init__(
            self, Opcode.SetClipRectangles, VoidCookie, checked, display)
        self._buffer = _buffer.SetClipRectangles(
            ordering, gc, clip_x_origin, clip_y_origin, rectangles_len,
            rectangles)

    def get_ordering(self, ):
        r"""SUMMARY

        get_ordering()

        @Return:

        @Error:
        """
        return self._buffer.get_ordering()

    def set_ordering(self, ordering):
        r"""SUMMARY

        set_ordering(_ordering)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_ordering(ordering)

    ordering = property(get_ordering, set_ordering)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._buffer.get_gc()

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(_gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_gc(gc)

    gc = property(get_gc, set_gc)

    def get_clip_x_origin(self, ):
        r"""SUMMARY

        get_clip_x_origin()

        @Return:

        @Error:
        """
        return self._buffer.get_clip_x_origin()

    def set_clip_x_origin(self, clip_x_origin):
        r"""SUMMARY

        set_clip_x_origin(_clip_x_origin)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_clip_x_origin(clip_x_origin)

    clip_x_origin = property(get_clip_x_origin, set_clip_x_origin)

    def get_clip_y_origin(self, ):
        r"""SUMMARY

        get_clip_y_origin()

        @Return:

        @Error:
        """
        return self._buffer.get_clip_y_origin()

    def set_clip_y_origin(self, clip_y_origin):
        r"""SUMMARY

        set_clip_y_origin(_clip_y_origin)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_clip_y_origin(clip_y_origin)

    clip_y_origin = property(get_clip_y_origin, set_clip_y_origin)

    def get_rectangles_len(self, ):
        r"""SUMMARY

        get_rectangles_len()

        @Return:

        @Error:
        """
        return self._buffer.get_rectangles_len()

    def set_rectangles_len(self, rectangles_len):
        r"""SUMMARY

        set_rectangles_len(_rectangles_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_rectangles_len(rectangles_len)

    rectangles_len = property(get_rectangles_len, set_rectangles_len)

    def get_rectangles(self, ):
        r"""SUMMARY

        get_rectangles()

        @Return:

        @Error:
        """
        return self._buffer.get_rectangles()

    def set_rectangles(self, rectangles):
        r"""SUMMARY

        set_rectangles(_rectangles)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_rectangles(rectangles)

    rectangles = property(get_rectangles, set_rectangles)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class FreeGC(Request):
    r"""FreeGC

    FreeGC is a Request.
    Responsibility:
    """
    def __init__(self, gc, checked=False, display=None):
        r"""

        @Arguments:
        - `gc`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.FreeGC, VoidCookie, checked, display)
        self._buffer = _buffer.FreeGC(gc)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._buffer.get_gc()

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(_gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_gc(gc)

    gc = property(get_gc, set_gc)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class ClearArea(Request):
    r"""ClearArea

    ClearArea is a Request.
    Responsibility:
    """
    def __init__(self, exposures, window, x, y, width, height,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `exposures`:
        - `window`:
        - `x`:
        - `y`:
        - `width`:
        - `height`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.ClearArea, VoidCookie, checked, display)
        self._buffer = _buffer.ClearArea(
            exposures, window, x, y, width, height)

    def get_exposures(self, ):
        r"""SUMMARY

        get_exposures()

        @Return:

        @Error:
        """
        return self._buffer.get_exposures()

    def set_exposures(self, exposures):
        r"""SUMMARY

        set_exposures(_exposures)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_exposures(exposures)

    exposures = property(get_exposures, set_exposures)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._buffer.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_window(window)

    window = property(get_window, set_window)

    def get_x(self, ):
        r"""SUMMARY

        get_x()

        @Return:

        @Error:
        """
        return self._buffer.get_x()

    def set_x(self, newx):
        r"""SUMMARY

        set_x(_x)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_x(newx)

    x = property(get_x, set_x)

    def get_y(self, ):
        r"""SUMMARY

        get_y()

        @Return:

        @Error:
        """
        return self._buffer.get_y()

    def set_y(self, newy):
        r"""SUMMARY

        set_y(_y)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_y(newy)

    y = property(get_y, set_y)

    def get_width(self, ):
        r"""SUMMARY

        get_width()

        @Return:

        @Error:
        """
        return self._buffer.get_width()

    def set_width(self, width):
        r"""SUMMARY

        set_width(_width)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_width(width)

    width = property(get_width, set_width)

    def get_height(self, ):
        r"""SUMMARY

        get_height()

        @Return:

        @Error:
        """
        return self._buffer.get_height()

    def set_height(self, height):
        r"""SUMMARY

        set_height(_height)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_height(height)

    height = property(get_height, set_height)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class CopyArea(Request):
    r"""CopyArea

    CopyArea is a Request.
    Responsibility:
    """
    def __init__(self, src_drawable, dst_drawable, gc, src_x, src_y,
                 dst_x, dst_y, width, height, checked=False, display=None):
        r"""

        @Arguments:
        - `src_drawable`:
        - `dst_drawable`:
        - `gc`:
        - `src_x`:
        - `src_y`:
        - `dst_x`:
        - `dst_y`:
        - `width`:
        - `height`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.CopyArea, VoidCookie, checked, display)
        self._buffer = _buffer.CopyArea(
            src_drawable, dst_drawable, gc, src_x, src_y, dst_x, dst_y,
            width, height)

    def get_src_drawable(self, ):
        r"""SUMMARY

        get_src_drawable()

        @Return:

        @Error:
        """
        return self._buffer.get_src_drawable()

    def set_src_drawable(self, src_drawable):
        r"""SUMMARY

        set_src_drawable(_src_drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_src_drawable(src_drawable)

    src_drawable = property(get_src_drawable, set_src_drawable)

    def get_dst_drawable(self, ):
        r"""SUMMARY

        get_dst_drawable()

        @Return:

        @Error:
        """
        return self._buffer.get_dst_drawable()

    def set_dst_drawable(self, dst_drawable):
        r"""SUMMARY

        set_dst_drawable(_dst_drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_dst_drawable(dst_drawable)

    dst_drawable = property(get_dst_drawable, set_dst_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._buffer.get_gc()

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(_gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_gc(gc)

    gc = property(get_gc, set_gc)

    def get_src_x(self, ):
        r"""SUMMARY

        get_src_x()

        @Return:

        @Error:
        """
        return self._buffer.get_src_x()

    def set_src_x(self, src_x):
        r"""SUMMARY

        set_src_x(_src_x)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_src_x(src_x)

    src_x = property(get_src_x, set_src_x)

    def get_src_y(self, ):
        r"""SUMMARY

        get_src_y()

        @Return:

        @Error:
        """
        return self._buffer.get_src_y()

    def set_src_y(self, src_y):
        r"""SUMMARY

        set_src_y(_src_y)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_src_y(src_y)

    src_y = property(get_src_y, set_src_y)

    def get_dst_x(self, ):
        r"""SUMMARY

        get_dst_x()

        @Return:

        @Error:
        """
        return self._buffer.get_dst_x()

    def set_dst_x(self, dst_x):
        r"""SUMMARY

        set_dst_x(_dst_x)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_dst_x(dst_x)

    dst_x = property(get_dst_x, set_dst_x)

    def get_dst_y(self, ):
        r"""SUMMARY

        get_dst_y()

        @Return:

        @Error:
        """
        return self._buffer.get_dst_y()

    def set_dst_y(self, dst_y):
        r"""SUMMARY

        set_dst_y(_dst_y)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_dst_y(dst_y)

    dst_y = property(get_dst_y, set_dst_y)

    def get_width(self, ):
        r"""SUMMARY

        get_width()

        @Return:

        @Error:
        """
        return self._buffer.get_width()

    def set_width(self, width):
        r"""SUMMARY

        set_width(_width)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_width(width)

    width = property(get_width, set_width)

    def get_height(self, ):
        r"""SUMMARY

        get_height()

        @Return:

        @Error:
        """
        return self._buffer.get_height()

    def set_height(self, height):
        r"""SUMMARY

        set_height(_height)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_height(height)

    height = property(get_height, set_height)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class CopyPlane(Request):
    r"""CopyPlane

    CopyPlane is a Request.
    Responsibility:
    """
    def __init__(self, src_drawable, dst_drawable, gc, src_x, src_y,
                 dst_x, dst_y, width, height, bit_plane,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `src_drawable`:
        - `dst_drawable`:
        - `gc`:
        - `src_x`:
        - `src_y`:
        - `dst_x`:
        - `dst_y`:
        - `width`:
        - `height`:
        - `bit_plane`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.CopyPlane, VoidCookie, checked, display)
        self._buffer = _buffer.CopyPlane(
            src_drawable, dst_drawable, gc, src_x, src_y, dst_x, dst_y,
            width, height, bit_plane)

    def get_src_drawable(self, ):
        r"""SUMMARY

        get_src_drawable()

        @Return:

        @Error:
        """
        return self._buffer.get_src_drawable()

    def set_src_drawable(self, src_drawable):
        r"""SUMMARY

        set_src_drawable(_src_drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_src_drawable(src_drawable)

    src_drawable = property(get_src_drawable, set_src_drawable)

    def get_dst_drawable(self, ):
        r"""SUMMARY

        get_dst_drawable()

        @Return:

        @Error:
        """
        return self._buffer.get_dst_drawable()

    def set_dst_drawable(self, dst_drawable):
        r"""SUMMARY

        set_dst_drawable(_dst_drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_dst_drawable(dst_drawable)

    dst_drawable = property(get_dst_drawable, set_dst_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._buffer.get_gc()

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(_gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_gc(gc)

    gc = property(get_gc, set_gc)

    def get_src_x(self, ):
        r"""SUMMARY

        get_src_x()

        @Return:

        @Error:
        """
        return self._buffer.get_src_x()

    def set_src_x(self, src_x):
        r"""SUMMARY

        set_src_x(_src_x)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_src_x(src_x)

    src_x = property(get_src_x, set_src_x)

    def get_src_y(self, ):
        r"""SUMMARY

        get_src_y()

        @Return:

        @Error:
        """
        return self._buffer.get_src_y()

    def set_src_y(self, src_y):
        r"""SUMMARY

        set_src_y(_src_y)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_src_y(src_y)

    src_y = property(get_src_y, set_src_y)

    def get_dst_x(self, ):
        r"""SUMMARY

        get_dst_x()

        @Return:

        @Error:
        """
        return self._buffer.get_dst_x()

    def set_dst_x(self, dst_x):
        r"""SUMMARY

        set_dst_x(_dst_x)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_dst_x(dst_x)

    dst_x = property(get_dst_x, set_dst_x)

    def get_dst_y(self, ):
        r"""SUMMARY

        get_dst_y()

        @Return:

        @Error:
        """
        return self._buffer.get_dst_y()

    def set_dst_y(self, dst_y):
        r"""SUMMARY

        set_dst_y(_dst_y)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_dst_y(dst_y)

    dst_y = property(get_dst_y, set_dst_y)

    def get_width(self, ):
        r"""SUMMARY

        get_width()

        @Return:

        @Error:
        """
        return self._buffer.get_width()

    def set_width(self, width):
        r"""SUMMARY

        set_width(_width)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_width(width)

    width = property(get_width, set_width)

    def get_height(self, ):
        r"""SUMMARY

        get_height()

        @Return:

        @Error:
        """
        return self._buffer.get_height()

    def set_height(self, height):
        r"""SUMMARY

        set_height(_height)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_height(height)

    height = property(get_height, set_height)

    def get_bit_plane(self, ):
        r"""SUMMARY

        get_bit_plane()

        @Return:

        @Error:
        """
        return self._buffer.get_bit_plane()

    def set_bit_plane(self, bit_plane):
        r"""SUMMARY

        set_bit_plane(_bit_plane)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_bit_plane(bit_plane)

    bit_plane = property(get_bit_plane, set_bit_plane)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class PolyPoint(Request):
    r"""PolyPoint

    PolyPoint is a Request.
    Responsibility:
    """
    def __init__(self, coordinate_mode, drawable, gc, points_len, points,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `coordinate_mode`:
        - `drawable`:
        - `gc`:
        - `points_len`:
        - `points`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.PolyPoint, VoidCookie, checked, display)
        self._buffer = _buffer.PolyPoint(
            coordinate_mode, drawable, gc, points_len, points)

    def get_coordinate_mode(self, ):
        r"""SUMMARY

        get_coordinate_mode()

        @Return:

        @Error:
        """
        return self._buffer.get_coordinate_mode()

    def set_coordinate_mode(self, coordinate_mode):
        r"""SUMMARY

        set_coordinate_mode(_coordinate_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_coordinate_mode(coordinate_mode)

    coordinate_mode = property(get_coordinate_mode, set_coordinate_mode)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._buffer.get_drawable()

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(_drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_drawable(drawable)

    drawable = property(get_drawable, set_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._buffer.get_gc()

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(_gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_gc(gc)

    gc = property(get_gc, set_gc)

    def get_points_len(self, ):
        r"""SUMMARY

        get_points_len()

        @Return:

        @Error:
        """
        return self._buffer.get_points_len()

    def set_points_len(self, points_len):
        r"""SUMMARY

        set_points_len(_points_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_points_len(points_len)

    points_len = property(get_points_len, set_points_len)

    def get_points(self, ):
        r"""SUMMARY

        get_points()

        @Return:

        @Error:
        """
        return self._buffer.get_points()

    def set_points(self, points):
        r"""SUMMARY

        set_points(_points)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_points(points)

    points = property(get_points, set_points)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class PolyLine(Request):
    r"""PolyLine

    PolyLine is a Request.
    Responsibility:
    """
    def __init__(self, coordinate_mode, drawable, gc, points_len, points,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `coordinate_mode`:
        - `drawable`:
        - `gc`:
        - `points_len`:
        - `points`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.PolyLine, VoidCookie, checked, display)
        self._buffer = _buffer.PolyLine(
            coordinate_mode, drawable, gc, points_len, points)

    def get_coordinate_mode(self, ):
        r"""SUMMARY

        get_coordinate_mode()

        @Return:

        @Error:
        """
        return self._buffer.get_coordinate_mode()

    def set_coordinate_mode(self, coordinate_mode):
        r"""SUMMARY

        set_coordinate_mode(_coordinate_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_coordinate_mode(coordinate_mode)

    coordinate_mode = property(get_coordinate_mode, set_coordinate_mode)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._buffer.get_drawable()

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(_drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_drawable(drawable)

    drawable = property(get_drawable, set_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._buffer.get_gc()

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(_gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_gc(gc)

    gc = property(get_gc, set_gc)

    def get_points_len(self, ):
        r"""SUMMARY

        get_points_len()

        @Return:

        @Error:
        """
        return self._buffer.get_points_len()

    def set_points_len(self, points_len):
        r"""SUMMARY

        set_points_len(_points_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_points_len(points_len)

    points_len = property(get_points_len, set_points_len)

    def get_points(self, ):
        r"""SUMMARY

        get_points()

        @Return:

        @Error:
        """
        return self._buffer.get_points()

    def set_points(self, points):
        r"""SUMMARY

        set_points(_points)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_points(points)

    points = property(get_points, set_points)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class PolySegment(Request):
    r"""PolySegment

    PolySegment is a Request.
    Responsibility:
    """
    def __init__(self, drawable, gc, segments_len, segments,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `drawable`:
        - `gc`:
        - `segments_len`:
        - `segments`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.PolySegment, VoidCookie, checked, display)
        self._buffer = _buffer.PolySegment(
            drawable, gc, segments_len, segments)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._buffer.get_drawable()

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(_drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_drawable(drawable)

    drawable = property(get_drawable, set_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._buffer.get_gc()

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(_gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_gc(gc)

    gc = property(get_gc, set_gc)

    def get_segments_len(self, ):
        r"""SUMMARY

        get_segments_len()

        @Return:

        @Error:
        """
        return self._buffer.get_segments_len()

    def set_segments_len(self, segments_len):
        r"""SUMMARY

        set_segments_len(_segments_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_segments_len(segments_len)

    segments_len = property(get_segments_len, set_segments_len)

    def get_segments(self, ):
        r"""SUMMARY

        get_segments()

        @Return:

        @Error:
        """
        return self._buffer.get_segments()

    def set_segments(self, segments):
        r"""SUMMARY

        set_segments(_segments)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_segments(segments)

    segments = property(get_segments, set_segments)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class PolyRectangle(Request):
    r"""PolyRectangle

    PolyRectangle is a Request.
    Responsibility:
    """
    def __init__(self, drawable, gc, rectangles_len, rectangles,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `drawable`:
        - `gc`:
        - `rectangles_len`:
        - `rectangles`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.PolyRectangle, VoidCookie, checked, display)
        self._buffer = _buffer.PolyRectangle(
            drawable, gc, rectangles_len, rectangles)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._buffer.get_drawable()

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(_drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_drawable(drawable)

    drawable = property(get_drawable, set_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._buffer.get_gc()

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(_gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_gc(gc)

    gc = property(get_gc, set_gc)

    def get_rectangles_len(self, ):
        r"""SUMMARY

        get_rectangles_len()

        @Return:

        @Error:
        """
        return self._buffer.get_rectangles_len()

    def set_rectangles_len(self, rectangles_len):
        r"""SUMMARY

        set_rectangles_len(_rectangles_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_rectangles_len(rectangles_len)

    rectangles_len = property(get_rectangles_len, set_rectangles_len)

    def get_rectangles(self, ):
        r"""SUMMARY

        get_rectangles()

        @Return:

        @Error:
        """
        return self._buffer.get_rectangles()

    def set_rectangles(self, rectangles):
        r"""SUMMARY

        set_rectangles(_rectangles)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_rectangles(rectangles)

    rectangles = property(get_rectangles, set_rectangles)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class PolyArc(Request):
    r"""PolyArc

    PolyArc is a Request.
    Responsibility:
    """
    def __init__(self, drawable, gc, arcs_len, arcs,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `drawable`:
        - `gc`:
        - `arcs_len`:
        - `arcs`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.PolyArc, VoidCookie, checked, display)
        self._buffer = _buffer.PolyArc(drawable, gc, arcs_len, arcs)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._buffer.get_drawable()

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(_drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_drawable(drawable)

    drawable = property(get_drawable, set_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._buffer.get_gc()

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(_gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_gc(gc)

    gc = property(get_gc, set_gc)

    def get_arcs_len(self, ):
        r"""SUMMARY

        get_arcs_len()

        @Return:

        @Error:
        """
        return self._buffer.get_arcs_len()

    def set_arcs_len(self, arcs_len):
        r"""SUMMARY

        set_arcs_len(_arcs_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_arcs_len(arcs_len)

    arcs_len = property(get_arcs_len, set_arcs_len)

    def get_arcs(self, ):
        r"""SUMMARY

        get_arcs()

        @Return:

        @Error:
        """
        return self._buffer.get_arcs()

    def set_arcs(self, arcs):
        r"""SUMMARY

        set_arcs(_arcs)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_arcs(arcs)

    arcs = property(get_arcs, set_arcs)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class FillPoly(Request):
    r"""FillPoly

    FillPoly is a Request.
    Responsibility:
    """
    def __init__(self, drawable, gc, shape, coordinate_mode, points_len,
                 points, checked=False, display=None):
        r"""

        @Arguments:
        - `drawable`:
        - `gc`:
        - `shape`:
        - `coordinate_mode`:
        - `points_len`:
        - `
points`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.FillPoly, VoidCookie, checked, display)
        self._buffer = _buffer.FillPoly(
            drawable, gc, shape, coordinate_mode, points_len, points)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._buffer.get_drawable()

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(_drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_drawable(drawable)

    drawable = property(get_drawable, set_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._buffer.get_gc()

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(_gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_gc(gc)

    gc = property(get_gc, set_gc)

    def get_shape(self, ):
        r"""SUMMARY

        get_shape()

        @Return:

        @Error:
        """
        return self._buffer.get_shape()

    def set_shape(self, shape):
        r"""SUMMARY

        set_shape(_shape)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_shape(shape)

    shape = property(get_shape, set_shape)

    def get_coordinate_mode(self, ):
        r"""SUMMARY

        get_coordinate_mode()

        @Return:

        @Error:
        """
        return self._buffer.get_coordinate_mode()

    def set_coordinate_mode(self, coordinate_mode):
        r"""SUMMARY

        set_coordinate_mode(_coordinate_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_coordinate_mode(coordinate_mode)

    coordinate_mode = property(get_coordinate_mode, set_coordinate_mode)

    def get_points_len(self, ):
        r"""SUMMARY

        get_points_len()

        @Return:

        @Error:
        """
        return self._buffer.get_points_len()

    def set_points_len(self, points_len):
        r"""SUMMARY

        set_points_len(_points_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_points_len(points_len)

    points_len = property(get_points_len, set_points_len)

    def get_points(self, ):
        r"""SUMMARY

        get_points()

        @Return:

        @Error:
        """
        return self._buffer.get_points()

    def set_points(self, points):
        r"""SUMMARY

        set_points(_points)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_points(points)

    points = property(get_points, set_points)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class PolyFillRectangle(Request):
    r"""PolyFillRectangle

    PolyFillRectangle is a Request.
    Responsibility:
    """
    def __init__(self, drawable, gc, rectangles_len, rectangles,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `drawable`:
        - `gc`:
        - `rectangles_len`:
        - `rectangles`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.PolyFillRectangle, VoidCookie, checked, display)
        self._buffer = _buffer.PolyFillRectangle(
            drawable, gc, rectangles_len, rectangles)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._buffer.get_drawable()

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(_drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_drawable(drawable)

    drawable = property(get_drawable, set_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._buffer.get_gc()

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(_gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_gc(gc)

    gc = property(get_gc, set_gc)

    def get_rectangles_len(self, ):
        r"""SUMMARY

        get_rectangles_len()

        @Return:

        @Error:
        """
        return self._buffer.get_rectangles_len()

    def set_rectangles_len(self, rectangles_len):
        r"""SUMMARY

        set_rectangles_len(_rectangles_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_rectangles_len(rectangles_len)

    rectangles_len = property(get_rectangles_len, set_rectangles_len)

    def get_rectangles(self, ):
        r"""SUMMARY

        get_rectangles()

        @Return:

        @Error:
        """
        return self._buffer.get_rectangles()

    def set_rectangles(self, rectangles):
        r"""SUMMARY

        set_rectangles(_rectangles)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_rectangles(rectangles)

    rectangles = property(get_rectangles, set_rectangles)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class PolyFillArc(Request):
    r"""PolyFillArc

    PolyFillArc is a Request.
    Responsibility:
    """
    def __init__(self, drawable, gc, arcs_len, arcs,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `drawable`:
        - `gc`:
        - `arcs_len`:
        - `arcs`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.PolyFillArc, VoidCookie, checked, display)
        self._buffer = _buffer.PolyFillArc(drawable, gc, arcs_len, arcs)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._buffer.get_drawable()

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(_drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_drawable(drawable)

    drawable = property(get_drawable, set_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._buffer.get_gc()

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(_gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_gc(gc)

    gc = property(get_gc, set_gc)

    def get_arcs_len(self, ):
        r"""SUMMARY

        get_arcs_len()

        @Return:

        @Error:
        """
        return self._buffer.get_arcs_len()

    def set_arcs_len(self, arcs_len):
        r"""SUMMARY

        set_arcs_len(_arcs_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_arcs_len(arcs_len)

    arcs_len = property(get_arcs_len, set_arcs_len)

    def get_arcs(self, ):
        r"""SUMMARY

        get_arcs()

        @Return:

        @Error:
        """
        return self._buffer.get_arcs()

    def set_arcs(self, arcs):
        r"""SUMMARY

        set_arcs(_arcs)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_arcs(arcs)

    arcs = property(get_arcs, set_arcs)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class PutImage(Request):
    r"""PutImage

    PutImage is a Request.
    Responsibility:
    """
    def __init__(self, format, drawable, gc, width, height, dst_x, dst_y,
                 left_pad, depth, data_len, data,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `format`:
        - `drawable`:
        - `gc`:
        - `width`:
        - `height`:
        - `dst_x`:
        - `dst_y`:
        - `left_pad`:
        - `depth`:
        - `data_len`:
        - `data`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.PutImage, VoidCookie, checked, display)
        self._buffer = _buffer.PutImage(
            format, drawable, gc, width, height, dst_x, dst_y, left_pad,
            depth, data_len, data)

    def get_format(self, ):
        r"""SUMMARY

        get_format()

        @Return:

        @Error:
        """
        return self._buffer.get_format()

    def set_format(self, format_):
        r"""SUMMARY

        set_format(_format)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_format(format_)

    format = property(get_format, set_format)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._buffer.get_drawable()

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(_drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_drawable(drawable)

    drawable = property(get_drawable, set_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._buffer.get_gc()

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(_gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_gc(gc)

    gc = property(get_gc, set_gc)

    def get_width(self, ):
        r"""SUMMARY

        get_width()

        @Return:

        @Error:
        """
        return self._buffer.get_width()

    def set_width(self, width):
        r"""SUMMARY

        set_width(_width)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_width(width)

    width = property(get_width, set_width)

    def get_height(self, ):
        r"""SUMMARY

        get_height()

        @Return:

        @Error:
        """
        return self._buffer.get_height()

    def set_height(self, height):
        r"""SUMMARY

        set_height(_height)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_height(height)

    height = property(get_height, set_height)

    def get_dst_x(self, ):
        r"""SUMMARY

        get_dst_x()

        @Return:

        @Error:
        """
        return self._buffer.get_dst_x()

    def set_dst_x(self, dst_x):
        r"""SUMMARY

        set_dst_x(_dst_x)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_dst_x(dst_x)

    dst_x = property(get_dst_x, set_dst_x)

    def get_dst_y(self, ):
        r"""SUMMARY

        get_dst_y()

        @Return:

        @Error:
        """
        return self._buffer.get_dst_y()

    def set_dst_y(self, dst_y):
        r"""SUMMARY

        set_dst_y(_dst_y)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_dst_y(dst_y)

    dst_y = property(get_dst_y, set_dst_y)

    def get_left_pad(self, ):
        r"""SUMMARY

        get_left_pad()

        @Return:

        @Error:
        """
        return self._buffer.get_left_pad()

    def set_left_pad(self, left_pad):
        r"""SUMMARY

        set_left_pad(_left_pad)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_left_pad(left_pad)

    left_pad = property(get_left_pad, set_left_pad)

    def get_depth(self, ):
        r"""SUMMARY

        get_depth()

        @Return:

        @Error:
        """
        return self._buffer.get_depth()

    def set_depth(self, depth):
        r"""SUMMARY

        set_depth(_depth)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_depth(depth)

    depth = property(get_depth, set_depth)

    def get_data_len(self, ):
        r"""SUMMARY

        get_data_len()

        @Return:

        @Error:
        """
        return self._buffer.get_data_len()

    def set_data_len(self, data_len):
        r"""SUMMARY

        set_data_len(_data_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_data_len(data_len)

    data_len = property(get_data_len, set_data_len)

    def get_data(self, ):
        r"""SUMMARY

        get_data()

        @Return:

        @Error:
        """
        return self._buffer.get_data()

    def set_data(self, data):
        r"""SUMMARY

        set_data(_data)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_data(data)

    data = property(get_data, set_data)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class GetImage(Request):
    r"""GetImage

    GetImage is a Request.
    Responsibility:
    """
    def __init__(self, format, drawable, x, y, width, height, plane_mask,
                 checked=True, display=None):
        r"""

        @Arguments:
        - `format`:
        - `drawable`:
        - `x`:
        - `y`:
        - `width`:
        - `height`:
        - `plane_mask`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.GetImage, xproto.GetImageCookie,
                         checked, display, xproto.GetImageReply)
        self._buffer = _buffer.GetImage(
            format, drawable, x, y, width, height, plane_mask)

    def get_format(self, ):
        r"""SUMMARY

        get_format()

        @Return:

        @Error:
        """
        return self._buffer.get_format()

    def set_format(self, format_):
        r"""SUMMARY

        set_format(_format)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_format(format_)

    format = property(get_format, set_format)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._buffer.get_drawable()

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(_drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_drawable(drawable)

    drawable = property(get_drawable, set_drawable)

    def get_x(self, ):
        r"""SUMMARY

        get_x()

        @Return:

        @Error:
        """
        return self._buffer.get_x()

    def set_x(self, newx):
        r"""SUMMARY

        set_x(_x)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_x(newx)

    x = property(get_x, set_x)

    def get_y(self, ):
        r"""SUMMARY

        get_y()

        @Return:

        @Error:
        """
        return self._buffer.get_y()

    def set_y(self, newy):
        r"""SUMMARY

        set_y(_y)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_y(newy)

    y = property(get_y, set_y)

    def get_width(self, ):
        r"""SUMMARY

        get_width()

        @Return:

        @Error:
        """
        return self._buffer.get_width()

    def set_width(self, width):
        r"""SUMMARY

        set_width(_width)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_width(width)

    width = property(get_width, set_width)

    def get_height(self, ):
        r"""SUMMARY

        get_height()

        @Return:

        @Error:
        """
        return self._buffer.get_height()

    def set_height(self, height):
        r"""SUMMARY

        set_height(_height)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_height(height)

    height = property(get_height, set_height)

    def get_plane_mask(self, ):
        r"""SUMMARY

        get_plane_mask()

        @Return:

        @Error:
        """
        return self._buffer.get_plane_mask()

    def set_plane_mask(self, plane_mask):
        r"""SUMMARY

        set_plane_mask(_plane_mask)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_plane_mask(plane_mask)

    plane_mask = property(get_plane_mask, set_plane_mask)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class PolyText8(Request):
    r"""PolyText8

    PolyText8 is a Request.
    Responsibility:
    """
    def __init__(self, drawable, gc, x, y, items_len, items,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `drawable`:
        - `gc`:
        - `x`:
        - `y`:
        - `items_len`:
        - `items`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.PolyText8, VoidCookie, checked, display)
        self._buffer = _buffer.PolyText8(
            drawable, gc, x, y, items_len, items)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._buffer.get_drawable()

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(_drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_drawable(drawable)

    drawable = property(get_drawable, set_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._buffer.get_gc()

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(_gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_gc(gc)

    gc = property(get_gc, set_gc)

    def get_x(self, ):
        r"""SUMMARY

        get_x()

        @Return:

        @Error:
        """
        return self._buffer.get_x()

    def set_x(self, newx):
        r"""SUMMARY

        set_x(_x)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_x(newx)

    x = property(get_x, set_x)

    def get_y(self, ):
        r"""SUMMARY

        get_y()

        @Return:

        @Error:
        """
        return self._buffer.get_y()

    def set_y(self, newy):
        r"""SUMMARY

        set_y(_y)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_y(newy)

    y = property(get_y, set_y)

    def get_items_len(self, ):
        r"""SUMMARY

        get_items_len()

        @Return:

        @Error:
        """
        return self._buffer.get_items_len()

    def set_items_len(self, items_len):
        r"""SUMMARY

        set_items_len(_items_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_items_len(items_len)

    items_len = property(get_items_len, set_items_len)

    def get_items(self, ):
        r"""SUMMARY

        get_items()

        @Return:

        @Error:
        """
        return self._buffer.get_items()

    def set_items(self, items):
        r"""SUMMARY

        set_items(_items)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_items(items)

    items = property(get_items, set_items)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class PolyText16(Request):
    r"""PolyText16

    PolyText16 is a Request.
    Responsibility:
    """
    def __init__(self, drawable, gc, x, y, items_len, items,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `drawable`:
        - `gc`:
        - `x`:
        - `y`:
        - `items_len`:
        - `items`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.PolyText16, VoidCookie, checked, display)
        self._buffer = _buffer.PolyText16(
            drawable, gc, x, y, items_len, items)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._buffer.get_drawable()

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(_drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_drawable(drawable)

    drawable = property(get_drawable, set_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._buffer.get_gc()

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(_gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_gc(gc)

    gc = property(get_gc, set_gc)

    def get_x(self, ):
        r"""SUMMARY

        get_x()

        @Return:

        @Error:
        """
        return self._buffer.get_x()

    def set_x(self, newx):
        r"""SUMMARY

        set_x(_x)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_x(newx)

    x = property(get_x, set_x)

    def get_y(self, ):
        r"""SUMMARY

        get_y()

        @Return:

        @Error:
        """
        return self._buffer.get_y()

    def set_y(self, newy):
        r"""SUMMARY

        set_y(_y)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_y(newy)

    y = property(get_y, set_y)

    def get_items_len(self, ):
        r"""SUMMARY

        get_items_len()

        @Return:

        @Error:
        """
        return self._buffer.get_items_len()

    def set_items_len(self, items_len):
        r"""SUMMARY

        set_items_len(_items_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_items_len(items_len)

    items_len = property(get_items_len, set_items_len)

    def get_items(self, ):
        r"""SUMMARY

        get_items()

        @Return:

        @Error:
        """
        return self._buffer.get_items()

    def set_items(self, items):
        r"""SUMMARY

        set_items(_items)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_items(items)

    items = property(get_items, set_items)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class ImageText8(Request):
    r"""ImageText8

    ImageText8 is a Request.
    Responsibility:
    """
    def __init__(self, string_len, drawable, gc, x, y, string,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `string_len`:
        - `drawable`:
        - `gc`:
        - `x`:
        - `y`:
        - `string`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.ImageText8, VoidCookie, checked, display)
        self._buffer = _buffer.ImageText8(
            string_len, drawable, gc, x, y, string)

    def get_string_len(self, ):
        r"""SUMMARY

        get_string_len()

        @Return:

        @Error:
        """
        return self._buffer.get_string_len()

    def set_string_len(self, string_len):
        r"""SUMMARY

        set_string_len(_string_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_string_len(string_len)

    string_len = property(get_string_len, set_string_len)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._buffer.get_drawable()

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(_drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_drawable(drawable)

    drawable = property(get_drawable, set_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._buffer.get_gc()

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(_gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_gc(gc)

    gc = property(get_gc, set_gc)

    def get_x(self, ):
        r"""SUMMARY

        get_x()

        @Return:

        @Error:
        """
        return self._buffer.get_x()

    def set_x(self, newx):
        r"""SUMMARY

        set_x(_x)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_x(newx)

    x = property(get_x, set_x)

    def get_y(self, ):
        r"""SUMMARY

        get_y()

        @Return:

        @Error:
        """
        return self._buffer.get_y()

    def set_y(self, newy):
        r"""SUMMARY

        set_y(_y)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_y(newy)

    y = property(get_y, set_y)

    def get_string(self, ):
        r"""SUMMARY

        get_string()

        @Return:

        @Error:
        """
        return self._buffer.get_string()

    def set_string(self, string):
        r"""SUMMARY

        set_string(_string)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_string(string)

    string = property(get_string, set_string)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class ImageText16(Request):
    r"""ImageText16

    ImageText16 is a Request.
    Responsibility:
    """
    def __init__(self, string_len, drawable, gc, x, y, string,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `string_len`:
        - `drawable`:
        - `gc`:
        - `x`:
        - `y`:
        - `string`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.ImageText16, VoidCookie, checked, display)
        self._buffer = _buffer.ImageText16(
            string_len, drawable, gc, x, y, string)

    def get_string_len(self, ):
        r"""SUMMARY

        get_string_len()

        @Return:

        @Error:
        """
        return self._buffer.get_string_len()

    def set_string_len(self, string_len):
        r"""SUMMARY

        set_string_len(_string_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_string_len(string_len)

    string_len = property(get_string_len, set_string_len)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._buffer.get_drawable()

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(_drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_drawable(drawable)

    drawable = property(get_drawable, set_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._buffer.get_gc()

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(_gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_gc(gc)

    gc = property(get_gc, set_gc)

    def get_x(self, ):
        r"""SUMMARY

        get_x()

        @Return:

        @Error:
        """
        return self._buffer.get_x()

    def set_x(self, newx):
        r"""SUMMARY

        set_x(_x)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_x(newx)

    x = property(get_x, set_x)

    def get_y(self, ):
        r"""SUMMARY

        get_y()

        @Return:

        @Error:
        """
        return self._buffer.get_y()

    def set_y(self, newy):
        r"""SUMMARY

        set_y(_y)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_y(newy)

    y = property(get_y, set_y)

    def get_string(self, ):
        r"""SUMMARY

        get_string()

        @Return:

        @Error:
        """
        return self._buffer.get_string()

    def set_string(self, string):
        r"""SUMMARY

        set_string(_string)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_string(string)

    string = property(get_string, set_string)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class CreateColormap(Request):
    r"""CreateColormap

    CreateColormap is a Request.
    Responsibility:
    """
    def __init__(self, alloc, mid, window, visual,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `alloc`:
        - `mid`:
        - `window`:
        - `visual`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.CreateColormap, VoidCookie, checked, display)
        self._buffer = _buffer.CreateColormap(
            alloc, mid, window, visual)

    def get_alloc(self, ):
        r"""SUMMARY

        get_alloc()

        @Return:

        @Error:
        """
        return self._buffer.get_alloc()

    def set_alloc(self, alloc):
        r"""SUMMARY

        set_alloc(_alloc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_alloc(alloc)

    alloc = property(get_alloc, set_alloc)

    def get_mid(self, ):
        r"""SUMMARY

        get_mid()

        @Return:

        @Error:
        """
        return self._buffer.get_mid()

    def set_mid(self, mid):
        r"""SUMMARY

        set_mid(_mid)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_mid(mid)

    mid = property(get_mid, set_mid)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._buffer.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_window(window)

    window = property(get_window, set_window)

    def get_visual(self, ):
        r"""SUMMARY

        get_visual()

        @Return:

        @Error:
        """
        return self._buffer.get_visual()

    def set_visual(self, visual):
        r"""SUMMARY

        set_visual(_visual)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_visual(visual)

    visual = property(get_visual, set_visual)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class FreeColormap(Request):
    r"""FreeColormap

    FreeColormap is a Request.
    Responsibility:
    """
    def __init__(self, cmap, checked=False, display=None):
        r"""

        @Arguments:
        - `cmap`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.FreeColormap, VoidCookie, checked, display)
        self._buffer = _buffer.FreeColormap(cmap)

    def get_cmap(self, ):
        r"""SUMMARY

        get_cmap()

        @Return:

        @Error:
        """
        return self._buffer.get_cmap()

    def set_cmap(self, cmap):
        r"""SUMMARY

        set_cmap(_cmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_cmap(cmap)

    cmap = property(get_cmap, set_cmap)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class CopyColormapAndFree(Request):
    r"""CopyColormapAndFree

    CopyColormapAndFree is a Request.
    Responsibility:
    """
    def __init__(self, mid, src_cmap, checked=False, display=None):
        r"""

        @Arguments:
        - `mid`:
        - `src_cmap`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.CopyColormapAndFree, VoidCookie, checked, display)
        self._buffer = _buffer.CopyColormapAndFree(mid, src_cmap)

    def get_mid(self, ):
        r"""SUMMARY

        get_mid()

        @Return:

        @Error:
        """
        return self._buffer.get_mid()

    def set_mid(self, mid):
        r"""SUMMARY

        set_mid(_mid)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_mid(mid)

    mid = property(get_mid, set_mid)

    def get_src_cmap(self, ):
        r"""SUMMARY

        get_src_cmap()

        @Return:

        @Error:
        """
        return self._buffer.get_src_cmap()

    def set_src_cmap(self, src_cmap):
        r"""SUMMARY

        set_src_cmap(_src_cmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_src_cmap(src_cmap)

    src_cmap = property(get_src_cmap, set_src_cmap)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class InstallColormap(Request):
    r"""InstallColormap

    InstallColormap is a Request.
    Responsibility:
    """
    def __init__(self, cmap, checked=False, display=None):
        r"""

        @Arguments:
        - `cmap`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.InstallColormap, VoidCookie, checked, display)
        self._buffer = _buffer.InstallColormap(cmap)

    def get_cmap(self, ):
        r"""SUMMARY

        get_cmap()

        @Return:

        @Error:
        """
        return self._buffer.get_cmap()

    def set_cmap(self, cmap):
        r"""SUMMARY

        set_cmap(_cmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_cmap(cmap)

    cmap = property(get_cmap, set_cmap)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class UninstallColormap(Request):
    r"""UninstallColormap

    UninstallColormap is a Request.
    Responsibility:
    """
    def __init__(self, cmap, checked=False, display=None):
        r"""

        @Arguments:
        - `cmap`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.UninstallColormap, VoidCookie, checked, display)
        self._buffer = _buffer.UninstallColormap(cmap)

    def get_cmap(self, ):
        r"""SUMMARY

        get_cmap()

        @Return:

        @Error:
        """
        return self._buffer.get_cmap()

    def set_cmap(self, cmap):
        r"""SUMMARY

        set_cmap(_cmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_cmap(cmap)

    cmap = property(get_cmap, set_cmap)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class ListInstalledColormaps(Request):
    r"""ListInstalledColormaps

    ListInstalledColormaps is a Request.
    Responsibility:
    """
    def __init__(self, window, checked=True, display=None):
        r"""

        @Arguments:
        - `window`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.ListInstalledColormaps,
                         xproto.ListInstalledColormapsCookie,
                         checked, display, xproto.ListInstalledColormapsReply)
        self._buffer = _buffer.ListInstalledColormaps(window)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._buffer.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_window(window)

    window = property(get_window, set_window)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class AllocColor(Request):
    r"""AllocColor

    AllocColor is a Request.
    Responsibility:
    """
    def __init__(self, cmap, red, green, blue, checked=True, display=None):
        r"""

        @Arguments:
        - `cmap`:
        - `red`:
        - `green`:
        - `blue`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.AllocColor, xproto.AllocColorCookie,
                         checked, display, xproto.AllocColorReply)
        self._buffer = _buffer.AllocColor(cmap, red, green, blue)

    def get_cmap(self, ):
        r"""SUMMARY

        get_cmap()

        @Return:

        @Error:
        """
        return self._buffer.get_cmap()

    def set_cmap(self, cmap):
        r"""SUMMARY

        set_cmap(_cmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_cmap(cmap)

    cmap = property(get_cmap, set_cmap)

    def get_red(self, ):
        r"""SUMMARY

        get_red()

        @Return:

        @Error:
        """
        return self._buffer.get_red()

    def set_red(self, red):
        r"""SUMMARY

        set_red(_red)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_red(red)

    red = property(get_red, set_red)

    def get_green(self, ):
        r"""SUMMARY

        get_green()

        @Return:

        @Error:
        """
        return self._buffer.get_green()

    def set_green(self, green):
        r"""SUMMARY

        set_green(_green)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_green(green)

    green = property(get_green, set_green)

    def get_blue(self, ):
        r"""SUMMARY

        get_blue()

        @Return:

        @Error:
        """
        return self._buffer.get_blue()

    def set_blue(self, blue):
        r"""SUMMARY

        set_blue(_blue)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_blue(blue)

    blue = property(get_blue, set_blue)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class AllocNamedColor(Request):
    r"""AllocNamedColor

    AllocNamedColor is a Request.
    Responsibility:
    """
    def __init__(self, cmap, name_len, name, checked=True, display=None):
        r"""

        @Arguments:
        - `cmap`:
        - `name_len`:
        - `name`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.AllocNamedColor,
                         xproto.AllocNamedColorCookie, checked, display,
                         xproto.AllocNamedColorReply)
        self._buffer = _buffer.AllocNamedColor(cmap, name_len, name)

    def get_cmap(self, ):
        r"""SUMMARY

        get_cmap()

        @Return:

        @Error:
        """
        return self._buffer.get_cmap()

    def set_cmap(self, cmap):
        r"""SUMMARY

        set_cmap(_cmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_cmap(cmap)

    cmap = property(get_cmap, set_cmap)

    def get_name_len(self, ):
        r"""SUMMARY

        get_name_len()

        @Return:

        @Error:
        """
        return self._buffer.get_name_len()

    def set_name_len(self, name_len):
        r"""SUMMARY

        set_name_len(_name_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_name_len(name_len)

    name_len = property(get_name_len, set_name_len)

    def get_name(self, ):
        r"""SUMMARY

        get_name()

        @Return:

        @Error:
        """
        return self._buffer.get_name()

    def set_name(self, name):
        r"""SUMMARY

        set_name(_name)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_name(name)

    name = property(get_name, set_name)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class AllocColorCells(Request):
    r"""AllocColorCells

    AllocColorCells is a Request.
    Responsibility:
    """
    def __init__(self, contiguous, cmap, colors, planes,
                 checked=True, display=None):
        r"""

        @Arguments:
        - `contiguous`:
        - `cmap`:
        - `colors`:
        - `planes`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.AllocColorCells, xproto.AllocColorCellsCookie,
            checked, display, xproto.AllocColorCellsReply)
        self._buffer = _buffer.AllocColorCells(
            contiguous, cmap, colors, planes)

    def get_contiguous(self, ):
        r"""SUMMARY

        get_contiguous()

        @Return:

        @Error:
        """
        return self._buffer.get_contiguous()

    def set_contiguous(self, contiguous):
        r"""SUMMARY

        set_contiguous(_contiguous)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_contiguous(contiguous)

    contiguous = property(get_contiguous, set_contiguous)

    def get_cmap(self, ):
        r"""SUMMARY

        get_cmap()

        @Return:

        @Error:
        """
        return self._buffer.get_cmap()

    def set_cmap(self, cmap):
        r"""SUMMARY

        set_cmap(_cmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_cmap(cmap)

    cmap = property(get_cmap, set_cmap)

    def get_colors(self, ):
        r"""SUMMARY

        get_colors()

        @Return:

        @Error:
        """
        return self._buffer.get_colors()

    def set_colors(self, colors):
        r"""SUMMARY

        set_colors(_colors)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_colors(colors)

    colors = property(get_colors, set_colors)

    def get_planes(self, ):
        r"""SUMMARY

        get_planes()

        @Return:

        @Error:
        """
        return self._buffer.get_planes()

    def set_planes(self, planes):
        r"""SUMMARY

        set_planes(_planes)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_planes(planes)

    planes = property(get_planes, set_planes)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class AllocColorPlanes(Request):
    r"""AllocColorPlanes

    AllocColorPlanes is a Request.
    Responsibility:
    """
    def __init__(self, contiguous, cmap, colors, reds, greens, blues,
                 checked=True, display=None):
        r"""

        @Arguments:
        - `contiguous`:
        - `cmap`:
        - `colors`:
        - `reds`:
        - `greens`:
        - `blues`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.AllocColorPlanes,
                         xproto.AllocColorPlanesCookie, checked, display,
                         xproto.AllocColorPlanesReply)
        self._buffer = _buffer.AllocColorPlanes(
            contiguous, cmap, colors, reds, greens, blues)

    def get_contiguous(self, ):
        r"""SUMMARY

        get_contiguous()

        @Return:

        @Error:
        """
        return self._buffer.get_contiguous()

    def set_contiguous(self, contiguous):
        r"""SUMMARY

        set_contiguous(_contiguous)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_contiguous(contiguous)

    contiguous = property(get_contiguous, set_contiguous)

    def get_cmap(self, ):
        r"""SUMMARY

        get_cmap()

        @Return:

        @Error:
        """
        return self._buffer.get_cmap()

    def set_cmap(self, cmap):
        r"""SUMMARY

        set_cmap(_cmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_cmap(cmap)

    cmap = property(get_cmap, set_cmap)

    def get_colors(self, ):
        r"""SUMMARY

        get_colors()

        @Return:

        @Error:
        """
        return self._buffer.get_colors()

    def set_colors(self, colors):
        r"""SUMMARY

        set_colors(_colors)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_colors(colors)

    colors = property(get_colors, set_colors)

    def get_reds(self, ):
        r"""SUMMARY

        get_reds()

        @Return:

        @Error:
        """
        return self._buffer.get_reds()

    def set_reds(self, reds):
        r"""SUMMARY

        set_reds(_reds)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_reds(reds)

    reds = property(get_reds, set_reds)

    def get_greens(self, ):
        r"""SUMMARY

        get_greens()

        @Return:

        @Error:
        """
        return self._buffer.get_greens()

    def set_greens(self, greens):
        r"""SUMMARY

        set_greens(_greens)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_greens(greens)

    greens = property(get_greens, set_greens)

    def get_blues(self, ):
        r"""SUMMARY

        get_blues()

        @Return:

        @Error:
        """
        return self._buffer.get_blues()

    def set_blues(self, blues):
        r"""SUMMARY

        set_blues(_blues)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_blues(blues)

    blues = property(get_blues, set_blues)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class FreeColors(Request):
    r"""FreeColors

    FreeColors is a Request.
    Responsibility:
    """
    def __init__(self, cmap, plane_mask, pixels_len, pixels,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `cmap`:
        - `plane_mask`:
        - `pixels_len`:
        - `pixels`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.FreeColors, VoidCookie, checked, display)
        self._buffer = _buffer.FreeColors(
            cmap, plane_mask, pixels_len, pixels)

    def get_cmap(self, ):
        r"""SUMMARY

        get_cmap()

        @Return:

        @Error:
        """
        return self._buffer.get_cmap()

    def set_cmap(self, cmap):
        r"""SUMMARY

        set_cmap(_cmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_cmap(cmap)

    cmap = property(get_cmap, set_cmap)

    def get_plane_mask(self, ):
        r"""SUMMARY

        get_plane_mask()

        @Return:

        @Error:
        """
        return self._buffer.get_plane_mask()

    def set_plane_mask(self, plane_mask):
        r"""SUMMARY

        set_plane_mask(_plane_mask)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_plane_mask(plane_mask)

    plane_mask = property(get_plane_mask, set_plane_mask)

    def get_pixels_len(self, ):
        r"""SUMMARY

        get_pixels_len()

        @Return:

        @Error:
        """
        return self._buffer.get_pixels_len()

    def set_pixels_len(self, pixels_len):
        r"""SUMMARY

        set_pixels_len(_pixels_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_pixels_len(pixels_len)

    pixels_len = property(get_pixels_len, set_pixels_len)

    def get_pixels(self, ):
        r"""SUMMARY

        get_pixels()

        @Return:

        @Error:
        """
        return self._buffer.get_pixels()

    def set_pixels(self, pixels):
        r"""SUMMARY

        set_pixels(_pixels)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_pixels(pixels)

    pixels = property(get_pixels, set_pixels)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class StoreColors(Request):
    r"""StoreColors

    StoreColors is a Request.
    Responsibility:
    """
    def __init__(self, cmap, items_len, items, checked=False, display=None):
        r"""

        @Arguments:
        - `cmap`:
        - `items_len`:
        - `items`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.StoreColors, VoidCookie, checked, display)
        self._buffer = _buffer.StoreColors(cmap, items_len, items)

    def get_cmap(self, ):
        r"""SUMMARY

        get_cmap()

        @Return:

        @Error:
        """
        return self._buffer.get_cmap()

    def set_cmap(self, cmap):
        r"""SUMMARY

        set_cmap(_cmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_cmap(cmap)

    cmap = property(get_cmap, set_cmap)

    def get_items_len(self, ):
        r"""SUMMARY

        get_items_len()

        @Return:

        @Error:
        """
        return self._buffer.get_items_len()

    def set_items_len(self, items_len):
        r"""SUMMARY

        set_items_len(_items_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_items_len(items_len)

    items_len = property(get_items_len, set_items_len)

    def get_items(self, ):
        r"""SUMMARY

        get_items()

        @Return:

        @Error:
        """
        return self._buffer.get_items()

    def set_items(self, items):
        r"""SUMMARY

        set_items(_items)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_items(items)

    items = property(get_items, set_items)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class StoreNamedColor(Request):
    r"""StoreNamedColor

    StoreNamedColor is a Request.
    Responsibility:
    """
    def __init__(self, flags, cmap, pixel, name_len, name,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `flags`:
        - `cmap`:
        - `pixel`:
        - `name_len`:
        - `name`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.StoreNamedColor, VoidCookie, checked, display)
        self._buffer = _buffer.StoreNamedColor(
            flags, cmap, pixel, name_len, name)

    def get_flags(self, ):
        r"""SUMMARY

        get_flags()

        @Return:

        @Error:
        """
        return self._buffer.get_flags()

    def set_flags(self, flags):
        r"""SUMMARY

        set_flags(_flags)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_flags(flags)

    flags = property(get_flags, set_flags)

    def get_cmap(self, ):
        r"""SUMMARY

        get_cmap()

        @Return:

        @Error:
        """
        return self._buffer.get_cmap()

    def set_cmap(self, cmap):
        r"""SUMMARY

        set_cmap(_cmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_cmap(cmap)

    cmap = property(get_cmap, set_cmap)

    def get_pixel(self, ):
        r"""SUMMARY

        get_pixel()

        @Return:

        @Error:
        """
        return self._buffer.get_pixel()

    def set_pixel(self, pixel):
        r"""SUMMARY

        set_pixel(_pixel)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_pixel(pixel)

    pixel = property(get_pixel, set_pixel)

    def get_name_len(self, ):
        r"""SUMMARY

        get_name_len()

        @Return:

        @Error:
        """
        return self._buffer.get_name_len()

    def set_name_len(self, name_len):
        r"""SUMMARY

        set_name_len(_name_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_name_len(name_len)

    name_len = property(get_name_len, set_name_len)

    def get_name(self, ):
        r"""SUMMARY

        get_name()

        @Return:

        @Error:
        """
        return self._buffer.get_name()

    def set_name(self, name):
        r"""SUMMARY

        set_name(_name)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_name(name)

    name = property(get_name, set_name)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class QueryColors(Request):
    r"""QueryColors

    QueryColors is a Request.
    Responsibility:
    """
    def __init__(self, cmap, pixels_len, pixels, checked=True, display=None):
        r"""

        @Arguments:
        - `cmap`:
        - `pixels_len`:
        - `pixels`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.QueryColors, xproto.QueryColorsCookie,
                         checked, display, xproto.QueryColorsReply)
        self._buffer = _buffer.QueryColors(cmap, pixels_len, pixels)

    def get_cmap(self, ):
        r"""SUMMARY

        get_cmap()

        @Return:

        @Error:
        """
        return self._buffer.get_cmap()

    def set_cmap(self, cmap):
        r"""SUMMARY

        set_cmap(_cmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_cmap(cmap)

    cmap = property(get_cmap, set_cmap)

    def get_pixels_len(self, ):
        r"""SUMMARY

        get_pixels_len()

        @Return:

        @Error:
        """
        return self._buffer.get_pixels_len()

    def set_pixels_len(self, pixels_len):
        r"""SUMMARY

        set_pixels_len(_pixels_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_pixels_len(pixels_len)

    pixels_len = property(get_pixels_len, set_pixels_len)

    def get_pixels(self, ):
        r"""SUMMARY

        get_pixels()

        @Return:

        @Error:
        """
        return self._buffer.get_pixels()

    def set_pixels(self, pixels):
        r"""SUMMARY

        set_pixels(_pixels)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_pixels(pixels)

    pixels = property(get_pixels, set_pixels)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class LookupColor(Request):
    r"""LookupColor

    LookupColor is a Request.
    Responsibility:
    """
    def __init__(self, cmap, name_len, name, checked=True, display=None):
        r"""

        @Arguments:
        - `cmap`:
        - `name_len`:
        - `name`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.LookupColor, xproto.LookupColorCookie,
                         checked, display, xproto.LookupColorReply)
        self._buffer = _buffer.LookupColor(cmap, name_len, name)

    def get_cmap(self, ):
        r"""SUMMARY

        get_cmap()

        @Return:

        @Error:
        """
        return self._buffer.get_cmap()

    def set_cmap(self, cmap):
        r"""SUMMARY

        set_cmap(_cmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_cmap(cmap)

    cmap = property(get_cmap, set_cmap)

    def get_name_len(self, ):
        r"""SUMMARY

        get_name_len()

        @Return:

        @Error:
        """
        return self._buffer.get_name_len()

    def set_name_len(self, name_len):
        r"""SUMMARY

        set_name_len(_name_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_name_len(name_len)

    name_len = property(get_name_len, set_name_len)

    def get_name(self, ):
        r"""SUMMARY

        get_name()

        @Return:

        @Error:
        """
        return self._buffer.get_name()

    def set_name(self, name):
        r"""SUMMARY

        set_name(_name)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_name(name)

    name = property(get_name, set_name)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class CreateCursor(Request):
    r"""CreateCursor

    CreateCursor is a Request.
    Responsibility:
    """
    def __init__(self, cid, source, mask, fore_red, fore_green, fore_blue,
                 back_red, back_green, back_blue, x, y,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `cid`:
        - `source`:
        - `mask`:
        - `fore_red`:
        - `fore_green`:
        - `fore_blue`:
        - `back_red`:
        - `back_green`:
        - `back_blue`:
        - `x`:
        - `y`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.CreateCursor, VoidCookie, checked, display)
        self._buffer = _buffer.CreateCursor(
            cid, source, mask, fore_red, fore_green, fore_blue, back_red,
            back_green, back_blue, x, y)

    def get_cid(self, ):
        r"""SUMMARY

        get_cid()

        @Return:

        @Error:
        """
        return self._buffer.get_cid()

    def set_cid(self, cid):
        r"""SUMMARY

        set_cid(_cid)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_cid(cid)

    cid = property(get_cid, set_cid)

    def get_source(self, ):
        r"""SUMMARY

        get_source()

        @Return:

        @Error:
        """
        return self._buffer.get_source()

    def set_source(self, source):
        r"""SUMMARY

        set_source(_source)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_source(source)

    source = property(get_source, set_source)

    def get_mask(self, ):
        r"""SUMMARY

        get_mask()

        @Return:

        @Error:
        """
        return self._buffer.get_mask()

    def set_mask(self, mask):
        r"""SUMMARY

        set_mask(_mask)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_mask(mask)

    mask = property(get_mask, set_mask)

    def get_fore_red(self, ):
        r"""SUMMARY

        get_fore_red()

        @Return:

        @Error:
        """
        return self._buffer.get_fore_red()

    def set_fore_red(self, fore_red):
        r"""SUMMARY

        set_fore_red(_fore_red)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_fore_red(fore_red)

    fore_red = property(get_fore_red, set_fore_red)

    def get_fore_green(self, ):
        r"""SUMMARY

        get_fore_green()

        @Return:

        @Error:
        """
        return self._buffer.get_fore_green()

    def set_fore_green(self, fore_green):
        r"""SUMMARY

        set_fore_green(_fore_green)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_fore_green(fore_green)

    fore_green = property(get_fore_green, set_fore_green)

    def get_fore_blue(self, ):
        r"""SUMMARY

        get_fore_blue()

        @Return:

        @Error:
        """
        return self._buffer.get_fore_blue()

    def set_fore_blue(self, fore_blue):
        r"""SUMMARY

        set_fore_blue(_fore_blue)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_fore_blue(fore_blue)

    fore_blue = property(get_fore_blue, set_fore_blue)

    def get_back_red(self, ):
        r"""SUMMARY

        get_back_red()

        @Return:

        @Error:
        """
        return self._buffer.get_back_red()

    def set_back_red(self, back_red):
        r"""SUMMARY

        set_back_red(_back_red)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_back_red(back_red)

    back_red = property(get_back_red, set_back_red)

    def get_back_green(self, ):
        r"""SUMMARY

        get_back_green()

        @Return:

        @Error:
        """
        return self._buffer.get_back_green()

    def set_back_green(self, back_green):
        r"""SUMMARY

        set_back_green(_back_green)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_back_green(back_green)

    back_green = property(get_back_green, set_back_green)

    def get_back_blue(self, ):
        r"""SUMMARY

        get_back_blue()

        @Return:

        @Error:
        """
        return self._buffer.get_back_blue()

    def set_back_blue(self, back_blue):
        r"""SUMMARY

        set_back_blue(_back_blue)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_back_blue(back_blue)

    back_blue = property(get_back_blue, set_back_blue)

    def get_x(self, ):
        r"""SUMMARY

        get_x()

        @Return:

        @Error:
        """
        return self._buffer.get_x()

    def set_x(self, newx):
        r"""SUMMARY

        set_x(_x)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_x(newx)

    x = property(get_x, set_x)

    def get_y(self, ):
        r"""SUMMARY

        get_y()

        @Return:

        @Error:
        """
        return self._buffer.get_y()

    def set_y(self, newy):
        r"""SUMMARY

        set_y(_y)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_y(newy)

    y = property(get_y, set_y)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class CreateGlyphCursor(Request):
    r"""CreateGlyphCursor

    CreateGlyphCursor is a Request.
    Responsibility:
    """
    def __init__(self, cid, source_font, mask_font, source_char, mask_char,
                 fore_red, fore_green, fore_blue, back_red, back_green,
                 back_blue, checked=False, display=None):
        r"""

        @Arguments:
        - `cid`:
        - `source_font`:
        - `mask_font`:
        - `source_char`:
        - `mask_char`:
        - `fore_red`:
        - `fore_green`:
        - `fore_blue`:
        - `back_red`:
        - `back_green`:
        - `back_blue`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.CreateGlyphCursor, VoidCookie, checked, display)
        self._buffer = _buffer.CreateGlyphCursor(
            cid, source_font, mask_font, source_char, mask_char, fore_red,
            fore_green, fore_blue, back_red, back_green, back_blue)

    def get_cid(self, ):
        r"""SUMMARY

        get_cid()

        @Return:

        @Error:
        """
        return self._buffer.get_cid()

    def set_cid(self, cid):
        r"""SUMMARY

        set_cid(_cid)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_cid(cid)

    cid = property(get_cid, set_cid)

    def get_source_font(self, ):
        r"""SUMMARY

        get_source_font()

        @Return:

        @Error:
        """
        return self._buffer.get_source_font()

    def set_source_font(self, source_font):
        r"""SUMMARY

        set_source_font(_source_font)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_source_font(source_font)

    source_font = property(get_source_font, set_source_font)

    def get_mask_font(self, ):
        r"""SUMMARY

        get_mask_font()

        @Return:

        @Error:
        """
        return self._buffer.get_mask_font()

    def set_mask_font(self, mask_font):
        r"""SUMMARY

        set_mask_font(_mask_font)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_mask_font(mask_font)

    mask_font = property(get_mask_font, set_mask_font)

    def get_source_char(self, ):
        r"""SUMMARY

        get_source_char()

        @Return:

        @Error:
        """
        return self._buffer.get_source_char()

    def set_source_char(self, source_char):
        r"""SUMMARY

        set_source_char(_source_char)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_source_char(source_char)

    source_char = property(get_source_char, set_source_char)

    def get_mask_char(self, ):
        r"""SUMMARY

        get_mask_char()

        @Return:

        @Error:
        """
        return self._buffer.get_mask_char()

    def set_mask_char(self, mask_char):
        r"""SUMMARY

        set_mask_char(_mask_char)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_mask_char(mask_char)

    mask_char = property(get_mask_char, set_mask_char)

    def get_fore_red(self, ):
        r"""SUMMARY

        get_fore_red()

        @Return:

        @Error:
        """
        return self._buffer.get_fore_red()

    def set_fore_red(self, fore_red):
        r"""SUMMARY

        set_fore_red(_fore_red)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_fore_red(fore_red)

    fore_red = property(get_fore_red, set_fore_red)

    def get_fore_green(self, ):
        r"""SUMMARY

        get_fore_green()

        @Return:

        @Error:
        """
        return self._buffer.get_fore_green()

    def set_fore_green(self, fore_green):
        r"""SUMMARY

        set_fore_green(_fore_green)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_fore_green(fore_green)

    fore_green = property(get_fore_green, set_fore_green)

    def get_fore_blue(self, ):
        r"""SUMMARY

        get_fore_blue()

        @Return:

        @Error:
        """
        return self._buffer.get_fore_blue()

    def set_fore_blue(self, fore_blue):
        r"""SUMMARY

        set_fore_blue(_fore_blue)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_fore_blue(fore_blue)

    fore_blue = property(get_fore_blue, set_fore_blue)

    def get_back_red(self, ):
        r"""SUMMARY

        get_back_red()

        @Return:

        @Error:
        """
        return self._buffer.get_back_red()

    def set_back_red(self, back_red):
        r"""SUMMARY

        set_back_red(_back_red)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_back_red(back_red)

    back_red = property(get_back_red, set_back_red)

    def get_back_green(self, ):
        r"""SUMMARY

        get_back_green()

        @Return:

        @Error:
        """
        return self._buffer.get_back_green()

    def set_back_green(self, back_green):
        r"""SUMMARY

        set_back_green(_back_green)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_back_green(back_green)

    back_green = property(get_back_green, set_back_green)

    def get_back_blue(self, ):
        r"""SUMMARY

        get_back_blue()

        @Return:

        @Error:
        """
        return self._buffer.get_back_blue()

    def set_back_blue(self, back_blue):
        r"""SUMMARY

        set_back_blue(_back_blue)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_back_blue(back_blue)

    back_blue = property(get_back_blue, set_back_blue)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class FreeCursor(Request):
    r"""FreeCursor

    FreeCursor is a Request.
    Responsibility:
    """
    def __init__(self, cursor, checked=False, display=None):
        r"""

        @Arguments:
        - `cursor`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.FreeCursor, VoidCookie, checked, display)
        self._buffer = _buffer.FreeCursor(cursor)

    def get_cursor(self, ):
        r"""SUMMARY

        get_cursor()

        @Return:

        @Error:
        """
        return self._buffer.get_cursor()

    def set_cursor(self, cursor):
        r"""SUMMARY

        set_cursor(_cursor)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_cursor(cursor)

    cursor = property(get_cursor, set_cursor)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class RecolorCursor(Request):
    r"""RecolorCursor

    RecolorCursor is a Request.
    Responsibility:
    """
    def __init__(self, cursor, fore_red, fore_green, fore_blue, back_red,
                 back_green, back_blue, checked=False, display=None):
        r"""

        @Arguments:
        - `cursor`:
        - `fore_red`:
        - `fore_green`:
        - `fore_blue`:
        - `back_red`:
        - `back_green`:
        - `back_blue`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.RecolorCursor, VoidCookie, checked, display)
        self._buffer = _buffer.RecolorCursor(
            cursor, fore_red, fore_green, fore_blue, back_red, back_green,
            back_blue)

    def get_cursor(self, ):
        r"""SUMMARY

        get_cursor()

        @Return:

        @Error:
        """
        return self._buffer.get_cursor()

    def set_cursor(self, cursor):
        r"""SUMMARY

        set_cursor(_cursor)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_cursor(cursor)

    cursor = property(get_cursor, set_cursor)

    def get_fore_red(self, ):
        r"""SUMMARY

        get_fore_red()

        @Return:

        @Error:
        """
        return self._buffer.get_fore_red()

    def set_fore_red(self, fore_red):
        r"""SUMMARY

        set_fore_red(_fore_red)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_fore_red(fore_red)

    fore_red = property(get_fore_red, set_fore_red)

    def get_fore_green(self, ):
        r"""SUMMARY

        get_fore_green()

        @Return:

        @Error:
        """
        return self._buffer.get_fore_green()

    def set_fore_green(self, fore_green):
        r"""SUMMARY

        set_fore_green(_fore_green)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_fore_green(fore_green)

    fore_green = property(get_fore_green, set_fore_green)

    def get_fore_blue(self, ):
        r"""SUMMARY

        get_fore_blue()

        @Return:

        @Error:
        """
        return self._buffer.get_fore_blue()

    def set_fore_blue(self, fore_blue):
        r"""SUMMARY

        set_fore_blue(_fore_blue)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_fore_blue(fore_blue)

    fore_blue = property(get_fore_blue, set_fore_blue)

    def get_back_red(self, ):
        r"""SUMMARY

        get_back_red()

        @Return:

        @Error:
        """
        return self._buffer.get_back_red()

    def set_back_red(self, back_red):
        r"""SUMMARY

        set_back_red(_back_red)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_back_red(back_red)

    back_red = property(get_back_red, set_back_red)

    def get_back_green(self, ):
        r"""SUMMARY

        get_back_green()

        @Return:

        @Error:
        """
        return self._buffer.get_back_green()

    def set_back_green(self, back_green):
        r"""SUMMARY

        set_back_green(_back_green)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_back_green(back_green)

    back_green = property(get_back_green, set_back_green)

    def get_back_blue(self, ):
        r"""SUMMARY

        get_back_blue()

        @Return:

        @Error:
        """
        return self._buffer.get_back_blue()

    def set_back_blue(self, back_blue):
        r"""SUMMARY

        set_back_blue(_back_blue)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_back_blue(back_blue)

    back_blue = property(get_back_blue, set_back_blue)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class QueryBestSize(Request):
    r"""QueryBestSize

    QueryBestSize is a Request.
    Responsibility:
    """
    def __init__(self, _class, drawable, width, height,
                 checked=True, display=None):
        r"""

        @Arguments:
        - `_class`:
        - `drawable`:
        - `width`:
        - `height`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.QueryBestSize,
                         xproto.QueryBestSizeCookie, checked, display,
            xproto.QueryBestSizeReply)
        self._buffer = _buffer.QueryBestSize(_class, drawable, width, height)

    def get_class(self, ):
        r"""SUMMARY

        get_class()

        @Return:

        @Error:
        """
        return self._buffer.get_class()

    def set_class(self, _class):
        r"""SUMMARY

        set_class(_class)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_class(_class)

    class_ = property(get_class, set_class)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._buffer.get_drawable()

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(_drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_drawable(drawable)

    drawable = property(get_drawable, set_drawable)

    def get_width(self, ):
        r"""SUMMARY

        get_width()

        @Return:

        @Error:
        """
        return self._buffer.get_width()

    def set_width(self, width):
        r"""SUMMARY

        set_width(_width)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_width(width)

    width = property(get_width, set_width)

    def get_height(self, ):
        r"""SUMMARY

        get_height()

        @Return:

        @Error:
        """
        return self._buffer.get_height()

    def set_height(self, height):
        r"""SUMMARY

        set_height(_height)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_height(height)

    height = property(get_height, set_height)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class QueryExtension(Request):
    r"""QueryExtension

    QueryExtension is a Request.
    Responsibility:
    """
    def __init__(self, name_len, name, checked=True, display=None):
        r"""

        @Arguments:
        - `name_len`:
        - `name`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.QueryExtension,
                         xproto.QueryExtensionCookie, checked, display,
                         xproto.QueryExtensionReply)
        self._buffer = _buffer.QueryExtension(name_len, name)

    def get_name_len(self, ):
        r"""SUMMARY

        get_name_len()

        @Return:

        @Error:
        """
        return self._buffer.get_name_len()

    def set_name_len(self, name_len):
        r"""SUMMARY

        set_name_len(_name_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_name_len(name_len)

    name_len = property(get_name_len, set_name_len)

    def get_name(self, ):
        r"""SUMMARY

        get_name()

        @Return:

        @Error:
        """
        return self._buffer.get_name()

    def set_name(self, name):
        r"""SUMMARY

        set_name(_name)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_name(name)

    name = property(get_name, set_name)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class ListExtensions(Request):
    r"""ListExtensions

    ListExtensions is a Request.
    Responsibility:
    """
    def __init__(self, checked=True, display=None):
        r"""

        @Arguments:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.ListExtensions,
                         xproto.ListExtensionsCookie, checked, display,
                         xproto.ListExtensionsReply)
        self._buffer = _buffer.ListExtensions()

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class ChangeKeyboardMapping(Request):
    r"""ChangeKeyboardMapping

    ChangeKeyboardMapping is a Request.
    Responsibility:
    """
    def __init__(self, keycode_count, first_keycode, keysyms_per_keycode,
                 keysyms, checked=False, display=None):
        r"""

        @Arguments:
        - `keycode_count`:
        - `first_keycode`:
        - `keysyms_per_keycode`:
        - `keysyms`:
        """
        Request.__init__(
            self, Opcode.ChangeKeyboardMapping, VoidCookie, checked, display)
        self._buffer = _buffer.ChangeKeyboardMapping(
            keycode_count, first_keycode, keysyms_per_keycode, keysyms)

    def get_keycode_count(self, ):
        r"""SUMMARY

        get_keycode_count()

        @Return:

        @Error:
        """
        return self._buffer.get_keycode_count()

    def set_keycode_count(self, keycode_count):
        r"""SUMMARY

        set_keycode_count(_keycode_count)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_keycode_count(keycode_count)

    keycode_count = property(get_keycode_count, set_keycode_count)

    def get_first_keycode(self, ):
        r"""SUMMARY

        get_first_keycode()

        @Return:

        @Error:
        """
        return self._buffer.get_first_keycode()

    def set_first_keycode(self, first_keycode):
        r"""SUMMARY

        set_first_keycode(_first_keycode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_first_keycode(first_keycode)

    first_keycode = property(get_first_keycode, set_first_keycode)

    def get_keysyms_per_keycode(self, ):
        r"""SUMMARY

        get_keysyms_per_keycode()

        @Return:

        @Error:
        """
        return self._buffer.get_keysyms_per_keycode()

    def set_keysyms_per_keycode(self, keysyms_per_keycode):
        r"""SUMMARY

        set_keysyms_per_keycode(_keysyms_per_keycode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_keysyms_per_keycode(keysyms_per_keycode)

    keysyms_per_keycode = property(
        get_keysyms_per_keycode, set_keysyms_per_keycode)

    def get_keysyms(self, ):
        r"""SUMMARY

        get_keysyms()

        @Return:

        @Error:
        """
        return self._buffer.get_keysyms()

    def set_keysyms(self, keysyms):
        r"""SUMMARY

        set_keysyms(_keysyms)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_keysyms(keysyms)

    keysyms = property(get_keysyms, set_keysyms)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class GetKeyboardMapping(Request):
    r"""GetKeyboardMapping

    GetKeyboardMapping is a Request.
    Responsibility:
    """
    def __init__(self, first_keycode, count, checked=True, display=None):
        r"""

        @Arguments:
        - `first_keycode`:
        - `count`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.GetKeyboardMapping,
                         xproto.GetKeyboardMappingCookie, checked, display,
                         _reply.GetKeyboardMappingReply)
        self._buffer = _buffer.GetKeyboardMapping(
            first_keycode, count)

    def get_first_keycode(self, ):
        r"""SUMMARY

        get_first_keycode()

        @Return:

        @Error:
        """
        return self._buffer.get_first_keycode()

    def set_first_keycode(self, count):
        r"""SUMMARY

        set_first_keycode(_first_keycode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_first_keycode(count)

    first_keycode = property(get_first_keycode, set_first_keycode)

    def get_count(self, ):
        r"""SUMMARY

        get_count()

        @Return:

        @Error:
        """
        return self._buffer.get_count()

    def set_count(self, count):
        r"""SUMMARY

        set_count(_count)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_count(count)

    count = property(get_count, set_count)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class ChangeKeyboardControl(Request):
    r"""ChangeKeyboardControl

    ChangeKeyboardControl is a Request.
    Responsibility:
    """
    def __init__(self, value_mask, value_list, checked=False, display=None):
        r"""

        @Arguments:
        - `value_mask`:
        - `value_list`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.ChangeKeyboardControl, VoidCookie, checked, display)
        self._buffer = _buffer.ChangeKeyboardControl(
            value_mask, value_list)

    def get_value_mask(self, ):
        r"""SUMMARY

        get_value_mask()

        @Return:

        @Error:
        """
        return self._buffer.get_value_mask()

    def set_value_mask(self, value_mask):
        r"""SUMMARY

        set_value_mask(_value_mask)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_value_mask(value_mask)

    value_mask = property(get_value_mask, set_value_mask)

    def get_value_list(self, ):
        r"""SUMMARY

        get_value_list()

        @Return:

        @Error:
        """
        return self._buffer.get_value_list()

    def set_value_list(self, value_list):
        r"""SUMMARY

        set_value_list(_value_list)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_value_list(value_list)

    value_list = property(get_value_list, set_value_list)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class GetKeyboardControl(Request):
    r"""GetKeyboardControl

    GetKeyboardControl is a Request.
    Responsibility:
    """
    def __init__(self, checked=True, display=None):
        r"""

        @Arguments:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.GetKeyboardControl,
                         xproto.GetKeyboardControlCookie, checked, display,
                         xproto.GetKeyboardControlReply)
        self._buffer = _buffer.GetKeyboardControl()

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class Bell(Request):
    r"""Bell

    Bell is a Request.
    Responsibility:
    """
    def __init__(self, percent, checked=False, display=None):
        r"""

        @Arguments:
        - `parent`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.Bell, VoidCookie, checked, display)
        self._buffer = _buffer.Bell(percent)

    def get_percent(self, ):
        r"""SUMMARY

        get_percent()

        @Return:

        @Error:
        """
        return self._buffer.get_percent()

    def set_percent(self, percent):
        r"""SUMMARY

        set_percent(_percent)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_percent(percent)

    percent = property(get_percent, set_percent)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class ChangePointerControl(Request):
    r"""ChangePointerControl

    ChangePointerControl is a Request.
    Responsibility:
    """
    def __init__(self, acceleration_numerator, acceleration_denominator,
                 threshold, do_acceleration, do_threshold,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `acceleration_numerator`:
        - `acceleration_denominator`:
        - `threshold`:
        - `do_acceleration`:
        - `do_threshold`:
        """
        Request.__init__(
            self, Opcode.ChangePointerControl, VoidCookie, checked, display)
        self._buffer = _buffer.ChangePointerControl(
            acceleration_numerator, acceleration_denominator, threshold,
            do_acceleration, do_threshold)

    def get_acceleration_numerator(self, ):
        r"""SUMMARY

        get_acceleration_numerator()

        @Return:

        @Error:
        """
        return self._buffer.get_acceleration_numerator()

    def set_acceleration_numerator(self, acceleration_numerator):
        r"""SUMMARY

        set_acceleration_numerator(_acceleration_numerator)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_acceleration_numerator(acceleration_numerator)

    acceleration_numerator = property(
        get_acceleration_numerator, set_acceleration_numerator)

    def get_acceleration_denominator(self, ):
        r"""SUMMARY

        get_acceleration_denominator()

        @Return:

        @Error:
        """
        return self._buffer.get_acceleration_denominator()

    def set_acceleration_denominator(self, acceleration_denominator):
        r"""SUMMARY

        set_acceleration_denominator(_acceleration_denominator)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_acceleration_denominator(acceleration_denominator)

    acceleration_denominator = property(
        get_acceleration_denominator, set_acceleration_denominator)

    def get_threshold(self, ):
        r"""SUMMARY

        get_threshold()

        @Return:

        @Error:
        """
        return self._buffer.get_threshold()

    def set_threshold(self, threshold):
        r"""SUMMARY

        set_threshold(_threshold)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_threshold(threshold)

    threshold = property(get_threshold, set_threshold)

    def get_do_acceleration(self, ):
        r"""SUMMARY

        get_do_acceleration()

        @Return:

        @Error:
        """
        return self._buffer.get_do_acceleration()

    def set_do_acceleration(self, do_acceleration):
        r"""SUMMARY

        set_do_acceleration(_do_acceleration)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_do_acceleration(do_acceleration)

    do_acceleration = property(get_do_acceleration, set_do_acceleration)

    def get_do_threshold(self, ):
        r"""SUMMARY

        get_do_threshold()

        @Return:

        @Error:
        """
        return self._buffer.get_do_threshold()

    def set_do_threshold(self, do_threshold):
        r"""SUMMARY

        set_do_threshold(_do_threshold)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_do_threshold(do_threshold)

    do_threshold = property(get_do_threshold, set_do_threshold)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class GetPointerControl(Request):
    r"""GetPointerControl

    GetPointerControl is a Request.
    Responsibility:
    """
    def __init__(self, checked=True, display=None):
        r"""

        @Arguments:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.GetPointerControl,
                         xproto.GetPointerControlCookie, checked, display,
                         xproto.GetPointerControlReply)
        self._buffer = _buffer.GetPointerControl()

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class SetScreenSaver(Request):
    r"""SetScreenSaver

    SetScreenSaver is a Request.
    Responsibility:
    """
    def __init__(self, timeout, interval, prefer_blanking, allow_exposures,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `timeout`:
        - `interval`:
        - `prefer_blanking`:
        - `allow_exposures`:
        """
        Request.__init__(
            self, Opcode.SetScreenSaver, VoidCookie, checked, display)
        self._buffer = _buffer.SetScreenSaver(
            timeout, interval, prefer_blanking, allow_exposures)

    def get_timeout(self, ):
        r"""SUMMARY

        get_timeout()

        @Return:

        @Error:
        """
        return self._buffer.get_timeout()

    def set_timeout(self, timeout):
        r"""SUMMARY

        set_timeout(_timeout)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_timeout(timeout)

    timeout = property(get_timeout, set_timeout)

    def get_interval(self, ):
        r"""SUMMARY

        get_interval()

        @Return:

        @Error:
        """
        return self._buffer.get_interval()

    def set_interval(self, interval):
        r"""SUMMARY

        set_interval(_interval)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_interval(interval)

    interval = property(get_interval, set_interval)

    def get_prefer_blanking(self, ):
        r"""SUMMARY

        get_prefer_blanking()

        @Return:

        @Error:
        """
        return self._buffer.get_prefer_blanking()

    def set_prefer_blanking(self, prefer_blanking):
        r"""SUMMARY

        set_prefer_blanking(_prefer_blanking)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_prefer_blanking(prefer_blanking)

    prefer_blanking = property(get_prefer_blanking, set_prefer_blanking)

    def get_allow_exposures(self, ):
        r"""SUMMARY

        get_allow_exposures()

        @Return:

        @Error:
        """
        return self._buffer.get_allow_exposures()

    def set_allow_exposures(self, allow_exposures):
        r"""SUMMARY

        set_allow_exposures(_allow_exposures)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_allow_exposures(allow_exposures)

    allow_exposures = property(get_allow_exposures, set_allow_exposures)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class GetScreenSaver(Request):
    r"""GetScreenSaver

    GetScreenSaver is a Request.
    Responsibility:
    """
    def __init__(self, checked=True, display=None):
        r"""

        @Arguments:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.GetScreenSaver,
                         xproto.GetScreenSaverCookie, checked, display,
                         xproto.GetScreenSaverReply)
        self._buffer = _buffer.GetScreenSaver()

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class ChangeHosts(Request):
    r"""ChangeHosts

    ChangeHosts is a Request.
    Responsibility:
    """
    def __init__(self, mode, family, address_len, address,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `mode`:
        - `family`:
        - `address_len`:
        - `address`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.ChangeHosts, VoidCookie, checked, display)
        self._buffer = _buffer.ChangeHosts(mode, family, address_len, address)

    def get_mode(self, ):
        r"""SUMMARY

        get_mode()

        @Return:

        @Error:
        """
        return self._buffer.get_mode()

    def set_mode(self, mode):
        r"""SUMMARY

        set_mode(_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_mode(mode)

    mode = property(get_mode, set_mode)

    def get_family(self, ):
        r"""SUMMARY

        get_family()

        @Return:

        @Error:
        """
        return self._buffer.get_family()

    def set_family(self, family):
        r"""SUMMARY

        set_family(_family)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_family(family)

    family = property(get_family, set_family)

    def get_address_len(self, ):
        r"""SUMMARY

        get_addresss_len()

        @Return:

        @Error:
        """
        return self._buffer.get_address_len()

    def set_address_len(self, address_len):
        r"""SUMMARY

        set_addresss_len(_addresss_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_address_len(address_len)

    address_len = property(get_address_len, set_address_len)

    def get_address(self, ):
        r"""SUMMARY

        get_address()

        @Return:

        @Error:
        """
        return self._buffer.get_address()

    def set_address(self, address):
        r"""SUMMARY

        set_address(_address)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_address(address)

    address = property(get_address, set_address)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class ListHosts(Request):
    r"""ListHosts

    ListHosts is a Request.
    Responsibility:
    """
    def __init__(self, checked=True, display=None):
        r"""

        @Arguments:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.ListHosts, xproto.ListHostsCookie,
                         checked, display, xproto.ListHostsReply)
        self._buffer = _buffer.ListHosts()

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class SetAccessControl(Request):
    r"""SetAccessControl

    SetAccessControl is a Request.
    Responsibility:
    """
    def __init__(self, mode, checked=False, display=None):
        r"""

        @Arguments:
        - `mode`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.SetAccessControl, VoidCookie, checked, display)
        self._buffer = _buffer.SetAccessControl(mode)

    def get_mode(self, ):
        r"""SUMMARY

        get_mode()

        @Return:

        @Error:
        """
        return self._buffer.get_mode()

    def set_mode(self, mode):
        r"""SUMMARY

        set_mode(_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_mode(mode)

    mode = property(get_mode, set_mode)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class SetCloseDownMode(Request):
    r"""SetCloseDownMode

    SetCloseDownMode is a Request.
    Responsibility:
    """
    def __init__(self, mode, checked=False, display=None):
        r"""

        @Arguments:
        - `mode`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.SetCloseDownMode, VoidCookie, checked, display)
        self._buffer = _buffer.SetCloseDownMode(mode)

    def get_mode(self, ):
        r"""SUMMARY

        get_mode()

        @Return:

        @Error:
        """
        return self._buffer.get_mode()

    def set_mode(self, mode):
        r"""SUMMARY

        set_mode(_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_mode(mode)

    mode = property(get_mode, set_mode)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class KillClient(Request):
    r"""KillClient

    KillClient is a Request.
    Responsibility:
    """
    def __init__(self, resource, checked=False, display=None):
        r"""

        @Arguments:
        - `resource`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.KillClient, VoidCookie, checked, display)
        self._buffer = _buffer.KillClient(resource)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class RotateProperties(Request):
    r"""RotateProperties

    RotateProperties is a Request.
    Responsibility:
    """
    def __init__(self, window, atoms_len, delta, atoms,
                 checked=False, display=None):
        r"""

        @Arguments:
        - `window`:
        - `atoms_len`:
        - `delta`:
        - `atoms`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.RotateProperties, VoidCookie, checked, display)
        self._buffer = _buffer.RotateProperties(
            window, atoms_len, delta, atoms)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._buffer.get_window()

    def set_window(self, window):
        r"""SUMMARY

        set_window(_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_window(window)

    window = property(get_window, set_window)

    def get_atoms_len(self, ):
        r"""SUMMARY

        get_atoms_len()

        @Return:

        @Error:
        """
        return self._buffer.get_atoms_len()

    def set_atoms_len(self, atoms_len):
        r"""SUMMARY

        set_atoms_len(_atoms_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_atoms_len(atoms_len)

    atoms_len = property(get_atoms_len, set_atoms_len)

    def get_delta(self, ):
        r"""SUMMARY

        get_delta()

        @Return:

        @Error:
        """
        return self._buffer.get_delta()

    def set_delta(self, delta):
        r"""SUMMARY

        set_delta(_delta)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_delta(delta)

    delta = property(get_delta, set_delta)

    def get_atoms(self, ):
        r"""SUMMARY

        get_atoms()

        @Return:

        @Error:
        """
        return self._buffer.get_atoms()

    def set_atoms(self, atoms):
        r"""SUMMARY

        set_atoms(_atoms)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_atoms(atoms)

    atoms = property(get_atoms, set_atoms)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class ForceScreenSaver(Request):
    r"""ForceScreenSaver

    ForceScreenSaver is a Request.
    Responsibility:
    """
    def __init__(self, mode, checked=False, display=None):
        r"""

        @Arguments:
        - `mode`:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.ForceScreenSaver, VoidCookie, checked, display)
        self._buffer = _buffer.ForceScreenSaver(mode)

    def get_mode(self, ):
        r"""SUMMARY

        get_mode()

        @Return:

        @Error:
        """
        return self._buffer.get_mode()

    def set_mode(self, mode):
        r"""SUMMARY

        set_mode(_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_mode(mode)

    mode = property(get_mode, set_mode)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class SetPointerMapping(Request):
    r"""SetPointerMapping

    SetPointerMapping is a Request.
    Responsibility:
    """
    def __init__(self, map_len, map, checked=True, display=None):
        r"""

        @Arguments:
        - `map_len`:
        - `map`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.SetPointerMapping,
                         xproto.SetPointerMappingCookie, checked, display,
                         xproto.SetPointerMappingReply)
        self._buffer = _buffer.SetPointerMapping(map_len, map)

    def get_map_len(self, ):
        r"""SUMMARY

        get_map_len()

        @Return:

        @Error:
        """
        return self._buffer.get_map_len()

    def set_map_len(self, map_len):
        r"""SUMMARY

        set_map_len(_map_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_map_len(map_len)

    map_len = property(get_map_len, set_map_len)

    def get_map(self, ):
        r"""SUMMARY

        get_map()

        @Return:

        @Error:
        """
        return self._buffer.get_map()

    def set_map(self, map):
        r"""SUMMARY

        set_map(_map)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_map(map)

    map = property(get_map, set_map)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class GetPointerMapping(Request):
    r"""GetPointerMapping

    GetPointerMapping is a Request.
    Responsibility:
    """
    def __init__(self, checked=True, display=None):
        r"""

        @Arguments:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.GetPointerMapping,
                         xproto.GetPointerMappingCookie, checked, display,
                         xproto.GetPointerMappingReply)
        self._buffer = _buffer.GetPointerMapping()

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class SetModifierMapping(Request):
    r"""SetModifierMapping

    SetModifierMapping is a Request.
    Responsibility:
    """
    def __init__(self, keycodes_per_modifier, keycodes, checked=True,
                 display=None):
        r"""

        @Arguments:
        - `keycodes_per_modifier`:
        - `keycodes`:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.SetModifierMapping,
                         xproto.SetModifierMappingCookie, checked, display,
                         xproto.SetModifierMappingReply)
        self._buffer = _buffer.SetModifierMapping(
            keycodes_per_modifier, keycodes)

    def get_keycodes_per_modifier(self, ):
        r"""SUMMARY

        get_keycodes_per_modifier()

        @Return:

        @Error:
        """
        return self._buffer.get_keycodes_per_modifier()

    def set_keycodes_per_modifier(self, keycodes_per_modifier):
        r"""SUMMARY

        set_keycodes_per_modifier(_keycodes_per_modifier)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_keycodes_per_modifier(keycodes_per_modifier)

    keycodes_per_modifier = property(
        get_keycodes_per_modifier, set_keycodes_per_modifier)

    def get_keycodes(self, ):
        r"""SUMMARY

        get_keycodes()

        @Return:

        @Error:
        """
        return self._buffer.get_keycodes()

    def set_keycodes(self, keycodes):
        r"""SUMMARY

        set_keycodes(_keycodes)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._buffer.set_keycodes(keycodes)

    keycodes = property(get_keycodes, set_keycodes)

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class GetModifierMapping(Request):
    r"""GetModifierMapping

    GetModifierMapping is a Request.
    Responsibility:
    """
    def __init__(self, checked=True, display=None):
        r"""

        @Arguments:
        - `checked`:
        - `display`:
        """
        Request.__init__(self, Opcode.GetModifierMapping,
                         xproto.GetModifierMappingCookie, checked, display,
                         xproto.GetModifierMappingReply)
        self._buffer = _buffer.GetModifierMapping()

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()


class NoOperation(Request):
    r"""NoOperation

    NoOperation is a Request.
    Responsibility:
    """
    def __init__(self, checked=False, display=None):
        r"""

        @Arguments:
        - `checked`:
        - `display`:
        """
        Request.__init__(
            self, Opcode.NoOperation, VoidCookie, checked, display)
        self._buffer = _buffer.NoOperation()

    def request(self, ):
        r"""SUMMARY

        request()

        @Return:

        @Error:
        """
        return self._request.send(self._buffer.get_buffer())

    def __call__(self):
        return self.request()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# requests.py ends here
