#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""buffer -- DESCRIPTION

"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

import xcb

import wxcb.xobj.atom
import wxcb.xobj.atomname as _atomname
import wxcb.xobj.rectangle as _rectangle
import wxcb.xobj.point as _point
import wxcb.xobj.dimension as _dimension


class CreateWindow(object):
    r"""CreateWindow

    CreateWindow is a object.
    Responsibility:
    """
    def __init__(self, depth, wid, parent, x, y, width, height,
                 border_width, _class, visual, value_mask, value_list):
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
        self._depth = depth
        self._wid = wid
        self._parent = parent
        self._rectangle = _rectangle.Rectangle(x, y, width, height)
        self._border_width = border_width
        self._class = _class
        self._visual = visual
        self._value_mask = value_mask
        self._value_list = value_list

    def get_depth(self, ):
        r"""SUMMARY

        get_depth()

        @Return:

        @Error:
        """
        return self._depth

    def set_depth(self, depth):
        r"""SUMMARY

        set_depth(depth)

        @Arguments:
        - `depth`:

        @Return:

        @Error:
        """
        self._depth = int(depth)

    depth = property(get_depth, set_depth)

    def get_id(self, ):
        r"""SUMMARY

        get_id()

        @Return:

        @Error:
        """
        return self._wid

    def set_id(self, wid):
        r"""SUMMARY

        set_window(window)

        @Arguments:
        - `wid`:

        @Return:

        @Error:
        """
        self._wid = int(wid)

    id = property(get_id, set_id)

    def get_parent(self, ):
        r"""SUMMARY

        get_parent()

        @Return:

        @Error:
        """
        return self._parent

    def set_parent(self, parent):
        r"""SUMMARY

        set_parent(parent)

        @Arguments:
        - `parent`:

        @Return:

        @Error:
        """
        self._parent = int(parent)

    parent = property(get_parent, set_parent)

    def get_x(self, ):
        r"""SUMMARY

        get_x()

        @Return:

        @Error:
        """
        return self._rectangle.get_x()

    def set_x(self, newx):
        r"""SUMMARY

        set_x(newx)

        @Arguments:
        - `newx`:

        @Return:

        @Error:
        """
        self._rectangle.set_x(newx)

    x = property(get_x, set_x)

    def get_y(self, ):
        r"""SUMMARY

        get_y()

        @Return:

        @Error:
        """
        return self._rectangle.get_y()

    def set_y(self, newy):
        r"""SUMMARY

        set_y(newy)

        @Arguments:
        - `newy`:

        @Return:

        @Error:
        """
        self._rectangle.set_y(newy)

    y = property(get_y, set_y)

    def get_width(self, ):
        r"""SUMMARY

        get_width()

        @Return:

        @Error:
        """
        return self._rectangle.get_width()

    def set_width(self, width):
        r"""SUMMARY

        set_width(width)

        @Arguments:
        - `width`:

        @Return:

        @Error:
        """
        self._rectangle.set_width(width)

    width = property(get_width, set_width)

    def get_height(self, ):
        r"""SUMMARY

        get_height()

        @Return:

        @Error:
        """
        return self._rectangle.get_height()

    def set_height(self, height):
        r"""SUMMARY

        set_height(height)

        @Arguments:
        - `height`:

        @Return:

        @Error:
        """
        self._rectangle.set_height(height)

    height = property(get_height, set_height)

    def get_border_width(self, ):
        r"""SUMMARY

        get_border_width()

        @Return:

        @Error:
        """
        return self._border_width

    def set_border_width(self, border_width):
        r"""SUMMARY

        set_border_width(border_width)

        @Arguments:
        - `border_width`:

        @Return:

        @Error:
        """
        self._border_width = int(border_width)

    border_width = property(get_border_width, set_border_width)

    def get_class(self, ):
        r"""SUMMARY

        get_class()

        @Return:

        @Error:
        """
        return self._class

    def set_class(self, _class):
        r"""SUMMARY

        set_class(_class)

        @Arguments:
        - `_class`:

        @Return:

        @Error:
        """
        self._class = int(_class)

    class_ = property(get_class, set_class)

    def get_visual(self, ):
        r"""SUMMARY

        get_visual()

        @Return:

        @Error:
        """
        return self._visual

    def set_visual(self, visual):
        r"""SUMMARY

        set_visual(visual)

        @Arguments:
        - `visual`:

        @Return:

        @Error:
        """
        self._visual = int(visual)

    visual = property(get_visual, set_visual)

    def get_value_mask(self, ):
        r"""SUMMARY

        get_value_mask()

        @Arguments:
        - `mask`:

        @Return:

        @Error:
        """
        return self._value_mask

    def set_value_mask(self, value_mask):
        r"""SUMMARY

        set_value_mask(value_mask)

        @Arguments:
        - `value_mask`:

        @Return:

        @Error:
        """
        self._value_mask = int(value_mask)

    value_mask = property(get_value_mask, set_value_mask)

    def get_value_list(self, ):
        r"""SUMMARY

        get_value_list()

        @Return:

        @Error:
        """
        return self._value_list

    def set_value_list(self, value_list):
        r"""SUMMARY

        set_value_list(value_list)

        @Arguments:
        - `value_list`:

        @Return:

        @Error:
        """
        self._value_list = list(value_list)

    value_list = property(get_value_list, set_value_list)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(
            _pack('=xB2xIIhhHHHHII', self.depth, self.id, self.parent,
                  self.x, self.y, self.width, self.height, self.border_width,
                  self.class_, self.visual, self.value_mask))
        buf.write(str(buffer(_array('I', self.value_list))))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class ChangeWindowAttributes(object):
    r"""ChangeWindowAttributes

    ChangeWindowAttributes is a object.
    Responsibility:
    """
    def __init__(self, window, value_mask, value_list):
        r"""

        @Arguments:
        - `window`:
        - `value_mask`:
        - `value_list`:
        """
        self._window = window
        self._value_mask = value_mask
        self._value_list = value_list

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._window

    def set_window(self, window):
        r"""SUMMARY

        set_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        self._window = int(window)

    window = property(get_window, set_window)

    def get_value_mask(self, ):
        r"""SUMMARY

        get_value_mask()

        @Return:

        @Error:
        """
        return self._value_mask

    def set_value_mask(self, value_mask):
        r"""SUMMARY

        set_value_mask(value_mask)

        @Arguments:
        - `value_mask`:

        @Return:

        @Error:
        """
        self._value_mask = int(value_mask)

    value_mask = property(get_value_mask, set_value_mask)

    def get_value_list(self, ):
        r"""SUMMARY

        get_value_list()

        @Return:

        @Error:
        """
        return self._value_list

    def set_value_list(self, value_list):
        r"""SUMMARY

        set_value_list(value_list)

        @Arguments:
        - `value_list`:

        @Return:

        @Error:
        """
        self._value_list = list(value_list)

    value_list = property(get_value_list, set_value_list)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xII', self.window, self.value_mask))
        buf.write(str(buffer(_array('I', self.value_list))))
        return buf.getvalue()


class _Window(object):
    r"""_Window

    _Window is a object.
    Responsibility:
    """
    def __init__(self, window):
        r"""

        @Arguments:
        - `window`:
        """
        self._window = window

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._window

    def set_window(self, window):
        r"""SUMMARY

        set_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        self._window = int(window)

    window = property(get_window, set_window)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xI', self.window))
        return buf.get_value()

    def __str__(self):
        return self.get_buffer()


class GetWindowAttributes(_Window):
    r"""GetWindowAttributes

    GetWindowAttributes is a object.
    Responsibility:
    """


class DestroyWindow(_Window):
    r"""DestroyWindow

    DestroyWindow is a object.
    Responsibility:
    """


class DestroySubwindows(_Window):
    r"""DestroySubwindows

    DestroySubwindows is a _Window.
    Responsibility:
    """


class ChangeSaveSet(object):
    r"""ChangeSaveSet

    ChangeSaveSet is a object.
    Responsibility:
    """
    def __init__(self, mode, window):
        r"""

        @Arguments:
        - `mode`:
        - `window`:
        """
        self._mode = mode
        self._window = window

    def get_mode(self, ):
        r"""SUMMARY

        get_mode()

        @Return:

        @Error:
        """
        return self._mode

    def set_mode(self, mode):
        r"""SUMMARY

        set_mode(mode)

        @Arguments:
        - `mode`:

        @Return:

        @Error:
        """
        self._mode = int(mode)

    mode = property(get_mode, set_mode)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._window

    def set_window(self, window):
        r"""SUMMARY

        set_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        self._window = int(window)

    window = property(get_window, set_window)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xI', self.mode, self.window))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class ReparentWindow(object):
    r"""ReparentWindow

    ReparentWindow is a object.
    Responsibility:
    """
    def __init__(self, window, parent, x, y):
        r"""

        @Arguments:
        - `window`:
        - `parent`:
        - `x`:
        - `y`:
        """
        self._window = window
        self._parent = parent
        self._point = _point.Point(x, y)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._window

    def set_window(self, window):
        r"""SUMMARY

        set_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        self._window = int(window)

    window = property(get_window, set_window)

    def get_parent(self, ):
        r"""SUMMARY

        get_parent()

        @Return:

        @Error:
        """
        return self._parent

    def set_parent(self, parent):
        r"""SUMMARY

        set_parent(parent)

        @Arguments:
        - `parent`:

        @Return:

        @Error:
        """
        self._parent = int(parent)

    parent = property(get_parent, set_parent)

    def get_x(self, ):
        r"""SUMMARY

        get_x()

        @Return:

        @Error:
        """
        return self._point.get_x()

    def set_x(self, newx):
        r"""SUMMARY

        set_x(newx)

        @Arguments:
        - `newx`:

        @Return:

        @Error:
        """
        self._point.set_x(newx)

    x = property(get_x, set_x)

    def get_y(self, ):
        r"""SUMMARY

        get_y()

        @Return:

        @Error:
        """
        return self._point.get_y()

    def set_y(self, newy):
        r"""SUMMARY

        set_y(newy)

        @Arguments:
        - `newy`:

        @Return:

        @Error:
        """
        return self._point.set_y(newy)

    y = property(get_y, set_y)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xIIhh', self.window, self.parent, self.x, self.y))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class MapWindow(_Window):
    r"""MapWindow

    MapWindow is a _Window.
    Responsibility:
    """


class MapSubwindows(_Window):
    r"""MapSubwindows

    MapSubwindows is a _Window.
    Responsibility:
    """


class UnmapWindow(_Window):
    r"""UnmapWindow

    UnmapWindow is a _Window.
    Responsibility:
    """


class UnmapSubwindows(_Window):
    r"""UnmapSubwindows

    UnmapSubwindows is a _Window.
    Responsibility:
    """


class ConfigureWindow(object):
    r"""ConfigureWindow

    ConfigureWindow is a object.
    Responsibility:
    """
    def __init__(self, window, value_mask, value_list):
        r"""

        @Arguments:
        - `window`:
        - `value_mask`:
        - `value_list`:
        """
        self._window = window
        self._value_mask = value_mask
        self._value_list = value_list

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._window

    def set_window(self, window):
        r"""SUMMARY

        set_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        self._window = int(window)

    window = property(get_window, set_window)

    def get_value_mask(self, ):
        r"""SUMMARY

        get_value_mask()

        @Return:

        @Error:
        """
        return self._value_mask

    def set_value_mask(self, value_mask):
        r"""SUMMARY

        set_value_mask(value_mask)

        @Arguments:
        - `value_mask`:

        @Return:

        @Error:
        """
        self._value_mask = int(value_mask)

    value_mask = property(get_value_mask, set_value_mask)

    def get_value_list(self, ):
        r"""SUMMARY

        get_value_list()

        @Return:

        @Error:
        """
        return self._value_list

    def set_value_list(self, value_list):
        r"""SUMMARY

        set_value_list(value_list)

        @Arguments:
        - `value_list`:

        @Return:

        @Error:
        """
        self._value_list = list(value_list)

    value_list = property(get_value_list, set_value_list)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xIH2x', self.window, self.value_mask))
        buf.write(str(buffer(_array('I', self.value_list))))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class CirculateWindow(object):
    r"""CirculateWindow

    CirculateWindow is a object.
    Responsibility:
    """
    def __init__(self, direction, window):
        r"""

        @Arguments:
        - `direction`:
        - `window`:
        """
        self._direction = direction
        self._window = window

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._window

    def set_window(self, window):
        r"""SUMMARY

        set_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        self._window = int(window)

    window = property(get_window, set_window)

    def get_direction(self, ):
        r"""SUMMARY

        get_direction()

        @Return:

        @Error:
        """
        return self._direction

    def set_direction(self, direction):
        r"""SUMMARY

        set_direction(direction)

        @Arguments:
        - `direction`:

        @Return:

        @Error:
        """
        self._direction = direction

    direction = property(get_direction, set_direction)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xI', self.direction, self.window))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class GetGeometry(object):
    r"""GetGeometry

    GetGeometry is a object.
    Responsibility:
    """
    def __init__(self, drawable):
        r"""

        @Arguments:
        - `drawable`:
        """
        self._drawable = drawable

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._drawable

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(drawable)

        @Arguments:
        - `drawable`:

        @Return:

        @Error:
        """
        self._drawable = drawable

    drawable = property(get_drawable, set_drawable)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xI', self.drawable))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class QueryTree(_Window):
    r"""QueryTree

    QueryTree is a _Window.
    Responsibility:
    """


class InternAtom(object):
    r"""InternAtom

    InternAtom is a object.
    Responsibility:

    option code: 16
    """
    def __init__(self, only_if_exists, name_len, name):
        r"""

        @Arguments:
        - `only_if_exists`:
        - `atomname`:
        """
        self._only_if_exists = None
        self._name_len = None
        self._name = None
        self.set_only_if_exists(only_if_exists)
        self.set_name_len(name_len)
        self.set_name(name)

    def get_only_if_exists(self, ):
        r"""SUMMARY

        get_only_if_exists()

        @Return:

        @Error:
        """
        return self._only_if_exists

    def set_only_if_exists(self, val):
        r"""SUMMARY

        set_only_if_exists(val)

        @Arguments:
        - `val`:

        @Return:

        @Error:
        """
        self._only_if_exists = bool(val)

    only_if_exists = property(get_only_if_exists, set_only_if_exists)

    def get_name(self, ):
        r"""SUMMARY

        get()

        @Return:

        @Error:
        """
        return self._name

    def set_name(self, name):
        r"""SUMMARY

        set(atom)

        @Arguments:
        - `atom`:

        @Return:

        @Error:
        """
        self._name = _atomname.AtomName(name)

    name = property(get_name, set_name)

    def get_name_len(self, ):
        r"""SUMMARY

        get_length()

        @Return:

        @Error:
        """
        return self._name_len

    def set_name_len(self, name_len):
        r"""SUMMARY

        set_name_len(name_len)

        @Arguments:
        - `name_len`:

        @Return:

        @Error:
        """
        self._name_len = int(name_len)

    name_len = property(get_name_len, set_name_len)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:

        '\x00\x00\x00\x00\x06\x00\x00\x00BITMAP'
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xH2x', self.only_if_exists, self.name_len))
        buf.write(self.name.pack())
        return buf.getvalue()

    def __len__(self):
        return self.name_len

    def __str__(self):
        return self.get_buffer()


class GetAtomName(object):
    r"""GetAtomName

    GetAtomName is a object.
    Responsibility:

    option code: 17
    """
    def __init__(self, atom):
        r"""

        @Arguments:
        - `atom`:
        """
        self._atom = None
        self.set_atom(atom)

    def get_atom(self, ):
        r"""SUMMARY

        get_atom()

        @Return:

        @Error:
        """
        return self._atom

    def set_atom(self, atom):
        r"""SUMMARY

        set_atom(atom)

        @Arguments:
        - `atom`:

        @Return:

        @Error:
        """
        self._atom = wxcb.xobj.atom.Atom(atom)

    atom = property(get_atom, set_atom)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2x'))
        buf.write(self.atom.pack())
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class ChangeProperty(object):
    r"""ChangeProperty

    ChangeProperty is a object.
    Responsibility:
    """
    def __init__(self, mode, window, property_, type_, format_, data_len, data):
        r"""

        @Arguments:
        - `mode`:
        - `window`:
        - `property_`:
        - `type_`:
        - `format_`:
        - `data_len`:
        - `data`:
        """
        self._mode = mode
        self._window = window
        self._property = property_
        self._type = type_
        self._format = format_
        self._data_len = data_len
        self._data = data

    def get_mode(self, ):
        r"""SUMMARY

        get_mode()

        @Return:

        @Error:
        """
        return self._mode

    def set_mode(self, mode):
        r"""SUMMARY

        set_mode(mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._mode = int(mode)

    mode = property(get_mode, set_mode)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._window

    def set_window(self, window):
        r"""SUMMARY

        set_window(window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._window = int(window)

    window = property(get_window, set_window)

    def get_property(self, ):
        r"""SUMMARY

        get_property()

        @Return:

        @Error:
        """
        return self._property

    def set_property(self, property_):
        r"""SUMMARY

        set_property(property_)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._property = int(property_)

    property_ = property(get_property, set_property)

    def get_type(self, ):
        r"""SUMMARY

        get_type()

        @Return:

        @Error:
        """
        return self._type

    def set_type(self, type_):
        r"""SUMMARY

        set_type(type_)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._type = int(type_)

    type = property(get_type, set_type)

    def get_format(self, ):
        r"""SUMMARY

        get_format()

        @Return:

        @Error:
        """
        return self._format

    def set_format(self, format_):
        r"""SUMMARY

        set_format(format_)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._format = int(format_)

    format = property(get_format, set_format)

    def get_data_len(self, ):
        r"""SUMMARY

        get_data_len()

        @Return:

        @Error:
        """
        return self._data_len

    def set_data_len(self, data_len):
        r"""SUMMARY

        set_data_len(data_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._data_len = int(data_len)

    data_len = property(get_data_len, set_data_len)

    def get_data(self, ):
        r"""SUMMARY

        get_data()

        @Return:

        @Error:
        """
        return self._data

    def set_data(self, data):
        r"""SUMMARY

        set_data(data)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._data = data

    data = property(get_data, set_data)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xIIIB3xI', self.mode, self.window, self.property_,
                        self.type, self.format, self.data_len))
        buf.write(str(buffer(_array('B', self.data))))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class DeleteProperty(object):
    r"""DeleteProperty

    DeleteProperty is a object.
    Responsibility:
    """
    def __init__(self, window, property_):
        r"""

        @Arguments:
        - `window`:
        - `property_`:
        """
        self._window = window
        self._property = property_

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._window

    def set_window(self, window):
        r"""SUMMARY

        set_window(window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._window = int(window)

    window = property(get_window, set_window)

    def get_property(self, ):
        r"""SUMMARY

        get_property()

        @Return:

        @Error:
        """
        return self._property

    def set_property(self, property_):
        r"""SUMMARY

        set_property(property_)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._property = int(property_)

    property_ = property(get_property, set_property)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xII', self.window, self.property_))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class GetProperty(object):
    r"""GetProperty

    GetProperty is a object.
    Responsibility:
    """
    def __init__(self, delete, window, property_, type_, long_offset, long_length):
        r"""

        @Arguments:
        - `delete`:
        - `window`:
        - `property_`:
        - `type_`:
        - `long_offset`:
        - `long_length`:
        """
        self._delete = delete
        self._window = window
        self._property = property_
        self._type = type_
        self._long_offset = long_offset
        self._long_length = long_length

    def get_delete(self, ):
        r"""SUMMARY

        get_delete()

        @Return:

        @Error:
        """
        return self._delete

    def set_delete(self, delete):
        r"""SUMMARY

        set_delete(delete)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._delete = bool(delete)

    delete = property(get_delete, set_delete)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._window

    def set_window(self, window):
        r"""SUMMARY

        set_window(window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._window = int(window)

    window = property(get_window, set_window)

    def get_property(self, ):
        r"""SUMMARY

        get_property()

        @Return:

        @Error:
        """
        return self._property

    def set_property(self, property_):
        r"""SUMMARY

        set_property(property_)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._property = int(property_)

    property_ = property(get_property, set_property)

    def get_type(self, ):
        r"""SUMMARY

        get_type()

        @Return:

        @Error:
        """
        return self._type

    def set_type(self, type_):
        r"""SUMMARY

        set_type(type_)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._type = int(type_)

    type = property(get_type, set_type)

    def get_long_offset(self, ):
        r"""SUMMARY

        get_long_offset()

        @Return:

        @Error:
        """
        return self._long_offset

    def set_long_offset(self, long_offset):
        r"""SUMMARY

        set_long_offset(long_offset)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._long_offset = int(long_offset)

    long_offset = property(get_long_offset, set_long_offset)

    def get_long_length(self, ):
        r"""SUMMARY

        get_long_length()

        @Return:

        @Error:
        """
        return self._long_length

    def set_long_length(self, long_length):
        r"""SUMMARY

        set_long_length(long_length)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._long_length = int(long_length)

    long_length = property(get_long_length, set_long_length)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xIIIII', self.delete, self.window, self.property_,
                        self.type, self.long_offset, self.long_length))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class ListProperties(_Window):
    r"""ListProperties

    ListProperties is a _Window.
    Responsibility:
    """


class SetSelectionOwner(object):
    r"""SetSelectionOwner

    SetSelectionOwner is a object.
    Responsibility:
    """
    def __init__(self, owner, selection, time):
        r"""

        @Arguments:
        - `owner`:
        - `selection`:
        - `time`:
        """
        self._owner = owner
        self._selection = selection
        self._time = time

    def get_owner(self, ):
        r"""SUMMARY

        get_owner()

        @Return:

        @Error:
        """
        return self._owner

    def set_owner(self, owner):
        r"""SUMMARY

        set_owner(owner)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._owner = owner

    owner = property(get_owner, set_owner)

    def get_selection(self, ):
        r"""SUMMARY

        get_selection()

        @Return:

        @Error:
        """
        return self._selection

    def set_selection(self, selection):
        r"""SUMMARY

        set_selection(selection)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._selection = selection

    selection = property(get_selection, set_selection)

    def get_time(self, ):
        r"""SUMMARY

        get_time()

        @Return:

        @Error:
        """
        return self._time

    def set_time(self, time):
        r"""SUMMARY

        set_time(time)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._time = time

    time = property(get_time, set_time)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xIII', self.owner, self.selection, self.time))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class GetSelectionOwner(object):
    r"""GetSelectionOwner

    GetSelectionOwner is a object.
    Responsibility:
    """
    def __init__(self, selection):
        r"""

        @Arguments:
        - `selection`:
        """
        self._selection = selection

    def get_selection(self, ):
        r"""SUMMARY

        get_selection()

        @Return:

        @Error:
        """
        return self._selection

    def set_selection(self, selection):
        r"""SUMMARY

        set_selection(selection)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._selection = selection

    selection = property(get_selection, set_selection)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xI', self.selection))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class ConvertSelection(object):
    r"""ConvertSelection

    ConvertSelection is a object.
    Responsibility:
    """
    def __init__(self, requestor, selection, target, property_, time):
        r"""

        @Arguments:
        - `requestor`:
        - `selection`:
        - `target`:
        - `property_`:
        - `time`:
        """
        self._requestor = requestor
        self._selection = selection
        self._target = target
        self._property_ = property_
        self._time = time

    def get_requestor(self, ):
        r"""SUMMARY

        get_requestor()

        @Return:

        @Error:
        """
        return self._requestor

    def set_requestor(self, requestor):
        r"""SUMMARY

        set_requestor(requestor)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._requestor = requestor

    requestor = property(get_requestor, set_requestor)

    def get_selection(self, ):
        r"""SUMMARY

        get_selection()

        @Return:

        @Error:
        """
        return self._selection

    def set_selection(self, selection):
        r"""SUMMARY

        set_selection(selection)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._selection = selection

    selection = property(get_selection, set_selection)

    def get_target(self, ):
        r"""SUMMARY

        get_target()

        @Return:

        @Error:
        """
        return self._target

    def set_target(self, target):
        r"""SUMMARY

        set_target(target)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._target = target

    target = property(get_target, set_target)

    def get_property(self, ):
        r"""SUMMARY

        get_property()

        @Return:

        @Error:
        """
        return self._property

    def set_property(self, property_):
        r"""SUMMARY

        set_property(property_)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._property = property_

    property_ = property(get_property, set_property)

    def get_time(self, ):
        r"""SUMMARY

        get_time()

        @Return:

        @Error:
        """
        return self._time

    def set_time(self, time):
        r"""SUMMARY

        set_time(time)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._time = time

    time = property(get_time, set_time)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xIIIII', self.requestor, self.selection,
                        self.target, self.property_, self.time))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class SendEvent(object):
    r"""SendEvent

    SendEvent is a object.
    Responsibility:
    """
    def __init__(self, propagate, destination, event_mask, event):
        r"""

        @Arguments:
        - `propagate`:
        - `destination`:
        - `event_mask`:
        - `event`:
        """
        self._propagate = propagate
        self._destination = destination
        self._event_mask = event_mask
        self._event = event

    def get_propagate(self, ):
        r"""SUMMARY

        get_propagate()

        @Return:

        @Error:
        """
        return self._propagate

    def set_propagate(self, propagate):
        r"""SUMMARY

        set_propagate(propagate)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._propagate = bool(propagate)

    propagate = property(get_propagate, set_propagate)

    def get_destination(self, ):
        r"""SUMMARY

        get_destination()

        @Return:

        @Error:
        """
        return self._destination

    def set_destination(self, destination):
        r"""SUMMARY

        set_destination(destination)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._destination = destination

    destination = property(get_destination, set_destination)

    def get_event_mask(self, ):
        r"""SUMMARY

        get_event_mask()

        @Return:

        @Error:
        """
        return self._event_mask

    def set_event_mask(self, event_mask):
        r"""SUMMARY

        set_event_mask(event_mask)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._event_mask = int(event_mask)

    event_mask = property(get_event_mask, set_event_mask)

    def get_event(self, ):
        r"""SUMMARY

        get_event()

        @Return:

        @Error:
        """
        return self._event

    def set_event(self, event):
        r"""SUMMARY

        set_event(event)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._event = event

    event = property(get_event, set_event)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack(
            '=xB2xII', self.propagate, self.destination, self.event_mask))
        buf.write(str(buffer(_array('b', self.event))))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class GrabPointer(object):
    r"""GrabPointer

    GrabPointer is a object.
    Responsibility:
    """
    def __init__(self, owner_events, grab_window, event_mask, pointer_mode,
                 keyboard_mode, confine_to, cursor, time):
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
        self._owner_events = owner_events
        self._grab_window = grab_window
        self._event_mask = event_mask
        self._pointer_mode = pointer_mode
        self._keyboard_mode = keyboard_mode
        self._confine_to = confine_to
        self._cursor = cursor
        self._time = time

    def get_owner_events(self, ):
        r"""SUMMARY

        get_owner_events()

        @Return:

        @Error:
        """
        return self._owner_events

    def set_owner_events(self, owner_events):
        r"""SUMMARY

        set_owner_events(owner_events)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._owner_events = owner_events

    owner_events = property(get_owner_events, set_owner_events)

    def get_grab_window(self, ):
        r"""SUMMARY

        get_grab_window()

        @Return:

        @Error:
        """
        return self._grab_window

    def set_grab_window(self, grab_window):
        r"""SUMMARY

        set_grab_window(grab_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._grab_window = grab_window

    grab_window = property(get_grab_window, set_grab_window)

    def get_event_mask(self, ):
        r"""SUMMARY

        get_event_mask()

        @Return:

        @Error:
        """
        return self._event_mask

    def set_event_mask(self, event_mask):
        r"""SUMMARY

        set_event_mask(event_mask)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._event_mask = event_mask

    event_mask = property(get_event_mask, set_event_mask)

    def get_pointer_mode(self, ):
        r"""SUMMARY

        get_pointer_mode()

        @Return:

        @Error:
        """
        return self._pointer_mode

    def set_pointer_mode(self, pointer_mode):
        r"""SUMMARY

        set_pointer_mode(pointer_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._pointer_mode = pointer_mode

    pointer_mode = property(get_pointer_mode, set_pointer_mode)

    def get_keyboard_mode(self, ):
        r"""SUMMARY

        get_keyboard_mode()

        @Return:

        @Error:
        """
        return self._keyboard_mode

    def set_keyboard_mode(self, keyboard_mode):
        r"""SUMMARY

        set_keyboard_mode(keyboard_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._keyboard_mode = keyboard_mode

    keyboard_mode = property(get_keyboard_mode, set_keyboard_mode)

    def get_confine_to(self, ):
        r"""SUMMARY

        get_confine_to()

        @Return:

        @Error:
        """
        return self._confine_to

    def set_confine_to(self, confine_to):
        r"""SUMMARY

        set_confine_to(confine_to)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._confine_to = confine_to

    confine_to = property(get_confine_to, set_confine_to)

    def get_cursor(self, ):
        r"""SUMMARY

        get_cursor()

        @Return:

        @Error:
        """
        return self._cursor

    def set_cursor(self, cursor):
        r"""SUMMARY

        set_cursor(cursor)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._cursor = cursor

    cursor = property(get_cursor, set_cursor)

    def get_time(self, ):
        r"""SUMMARY

        get_time()

        @Return:

        @Error:
        """
        return self._time

    def set_time(self, time):
        r"""SUMMARY

        set_time(time)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._time = time

    time = property(get_time, set_time)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xIHBBIII', self.owner_events, self.grab_window,
                        self.event_mask, self.pointer_mode, self.keyboard_mode,
                        self.confine_to, self.cursor, self.time))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class UngrabPointer(object):
    r"""UngrabPointer

    UngrabPointer is a object.
    Responsibility:
    """
    def __init__(self, time):
        r"""

        @Arguments:
        - `time`:
        """
        self._time = time

    def get_time(self, ):
        r"""SUMMARY

        get_time()

        @Return:

        @Error:
        """
        return self._time

    def set_time(self, time):
        r"""SUMMARY

        set_time(time)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._time = time

    time = property(get_time, set_time)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xI', self.time))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class GrabButton(object):
    r"""GrabButton

    GrabButton is a object.
    Responsibility:
    """
    def __init__(self, owner_events, grab_window, event_mask, pointer_mode, keyboard_mode, confine_to, cursor, button, modifiers):
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
        """
        self._owner_events = owner_events
        self._grab_window = grab_window
        self._event_mask = event_mask
        self._pointer_mode = pointer_mode
        self._keyboard_mode = keyboard_mode
        self._confine_to = confine_to
        self._cursor = cursor
        self._button = button
        self._modifiers = modifiers

    def get_owner_events(self, ):
        r"""SUMMARY

        get_owner_events()

        @Return:

        @Error:
        """
        return self._owner_events

    def set_owner_events(self, owner_events):
        r"""SUMMARY

        set_owner_events(owner_events)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._owner_events = owner_events

    owner_events = property(get_owner_events, set_owner_events)

    def get_grab_window(self, ):
        r"""SUMMARY

        get_grab_window()

        @Return:

        @Error:
        """
        return self._grab_window

    def set_grab_window(self, grab_window):
        r"""SUMMARY

        set_grab_window(grab_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._grab_window = int(grab_window)

    grab_window = property(get_grab_window, set_grab_window)

    def get_event_mask(self, ):
        r"""SUMMARY

        get_event_mask()

        @Return:

        @Error:
        """
        return self._event_mask

    def set_event_mask(self, event_mask):
        r"""SUMMARY

        set_event_mask(event_mask)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._event_mask = int(event_mask)

    event_mask = property(get_event_mask, set_event_mask)

    def get_pointer_mode(self, ):
        r"""SUMMARY

        get_pointer_mode()

        @Return:

        @Error:
        """
        return self._pointer_mode

    def set_pointer_mode(self, pointer_mode):
        r"""SUMMARY

        set_pointer_mode(pointer_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._pointer_mode = pointer_mode

    pointer_mode = property(get_pointer_mode, set_pointer_mode)

    def get_keyboard_mode(self, ):
        r"""SUMMARY

        get_keyboard_mode()

        @Return:

        @Error:
        """
        return self._keyboard_mode

    def set_keyboard_mode(self, keyboard_mode):
        r"""SUMMARY

        set_keyboard_mode(keyboard_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._keyboard_mode = int(keyboard_mode)

    keyboard_mode = property(get_keyboard_mode, set_keyboard_mode)

    def get_confine_to(self, ):
        r"""SUMMARY

        get_confine_to()

        @Return:

        @Error:
        """
        return self._confine_to

    def set_confine_to(self, confine_to):
        r"""SUMMARY

        set_confine_to(confine_to)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._confine_to = confine_to

    confine_to = property(get_confine_to, set_confine_to)

    def get_cursor(self, ):
        r"""SUMMARY

        get_cursor()

        @Return:

        @Error:
        """
        return self._cursor

    def set_cursor(self, cursor):
        r"""SUMMARY

        set_cursor(cursor)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._cursor = cursor

    cursor = property(get_cursor, set_cursor)

    def get_button(self, ):
        r"""SUMMARY

        get_button()

        @Return:

        @Error:
        """
        return self._button

    def set_button(self, button):
        r"""SUMMARY

        set_button(button)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._button = button

    button = property(get_button, set_button)

    def get_modifiers(self, ):
        r"""SUMMARY

        get_modifiers()

        @Return:

        @Error:
        """
        return self._modifiers

    def set_modifiers(self, modifiers):
        r"""SUMMARY

        set_modifiers(modifiers)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._modifiers = modifiers

    modifiers = property(get_modifiers, set_modifiers)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xIHBBIIBxH', self.owner_events, self.grab_window,
                        self.event_mask, self.pointer_mode, self.keyboard_mode,
                        self.confine_to, self.cursor, self.button,
                        self.modifiers))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class UngrabButton(object):
    r"""UngrabButton

    UngrabButton is a object.
    Responsibility:
    """
    def __init__(self, button, grab_window, modifiers):
        r"""

        @Arguments:
        - `button`:
        - `grab_window`:
        - `modifiers`:
        """
        self._button = button
        self._grab_window = grab_window
        self._modifiers = modifiers

    def get_button(self, ):
        r"""SUMMARY

        get_button()

        @Return:

        @Error:
        """
        return self._button

    def set_button(self, button):
        r"""SUMMARY

        set_button(button)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._button = button

    button = property(get_button, set_button)

    def get_grab_window(self, ):
        r"""SUMMARY

        get_grab_window()

        @Return:

        @Error:
        """
        return self._grab_window

    def set_grab_window(self, window):
        r"""SUMMARY

        set_grab_window(window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._grab_window = window

    grab_window = property(get_grab_window, set_grab_window)

    def get_modifiers(self, ):
        r"""SUMMARY

        get_modifiers()

        @Return:

        @Error:
        """
        return self._modifiers

    def set_modifiers(self, modifiers):
        r"""SUMMARY

        set_modifiers(modifiers)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._modifiers = modifiers

    modifiers = property(get_modifiers, set_modifiers)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xIH2x', self.button, self.grab_window,
                        self.modifiers))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class ChangeActivePointerGrab(object):
    r"""ChangeActivePointerGrab

    ChangeActivePointerGrab is a object.
    Responsibility:
    """
    def __init__(self, cursor, time, event_mask):
        r"""

        @Arguments:
        - `cursor`:
        - `time`:
        - `event_mask`:
        """
        self._cursor = cursor
        self._time = time
        self._event_mask = event_mask

    def get_cursor(self, ):
        r"""SUMMARY

        get_cursor()

        @Return:

        @Error:
        """
        return self._cursor

    def set_cursor(self, cursor):
        r"""SUMMARY

        set_cursor(cursor)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._cursor = cursor

    cursor = property(get_cursor, set_cursor)

    def get_time(self, ):
        r"""SUMMARY

        get_time()

        @Return:

        @Error:
        """
        return self._time

    def set_time(self, time):
        r"""SUMMARY

        set_time(time)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._time = time

    time = property(get_time, set_time)

    def get_event_mask(self, ):
        r"""SUMMARY

        get_event_mask()

        @Return:

        @Error:
        """
        return self._event_mask

    def set_event_mask(self, event_mask):
        r"""SUMMARY

        set_event_mask(event_mask)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._event_mask = int(event_mask)

    event_mask = property(get_event_mask, set_event_mask)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xIIH2x', self.cursor, self.time, self.event_mask))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class GrabKeyboard(object):
    r"""GrabKeyboard

    GrabKeyboard is a object.
    Responsibility:
    """
    def __init__(self, owner_events, grab_window, time, pointer_mode,
                 keyboard_mode):
        r"""

        @Arguments:
        - `owner_events`:
        - `grab_window`:
        - `time`:
        - `pointer_mode`:
        - `keyboard_mode`:
        """
        self._owner_events = owner_events
        self._grab_window = grab_window
        self._time = time
        self._pointer_mode = pointer_mode
        self._keyboard_mode = keyboard_mode

    def get_owner_events(self, ):
        r"""SUMMARY

        get_owner_events()

        @Return:

        @Error:
        """
        return self._owner_events

    def set_owner_events(self, owner_events):
        r"""SUMMARY

        set_owner_events(owner_events)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._owner_events = owner_events

    owner_events = property(get_owner_events, set_owner_events)

    def get_grab_window(self, ):
        r"""SUMMARY

        get_grab_window()

        @Return:

        @Error:
        """
        return self._grab_window

    def set_grab_window(self, grab_window):
        r"""SUMMARY

        set_grab_window(grab_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._grab_window = grab_window

    grab_window = property(get_grab_window, set_grab_window)

    def get_time(self, ):
        r"""SUMMARY

        get_time()

        @Return:

        @Error:
        """
        return self._time

    def set_time(self, time):
        r"""SUMMARY

        set_time(time)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._time = time

    time = property(get_time, set_time)

    def get_pointer_mode(self, ):
        r"""SUMMARY

        get_pointer_mode()

        @Return:

        @Error:
        """
        return self._pointer_mode

    def set_pointer_mode(self, pointer_mode):
        r"""SUMMARY

        set_pointer_mode(pointer_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._pointer_mode = pointer_mode

    pointer_mode = property(get_pointer_mode, set_pointer_mode)

    def get_keyboard_mode(self, ):
        r"""SUMMARY

        get_keyboard_mode()

        @Return:

        @Error:
        """
        return self._keyboard_mode

    def set_keyboard_mode(self, keyboard_mode):
        r"""SUMMARY

        set_keyboard_mode(keyboard_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._keyboard_mode = keyboard_mode

    keyboard_mode = property(get_keyboard_mode, set_keyboard_mode)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xIIBB2x', self.owner_events, self.grab_window,
                        self.time, self.pointer_mode, self.keyboard_mode))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class UngrabKeyboard(object):
    r"""UngrabKeyboard

    UngrabKeyboard is a object.
    Responsibility:
    """
    def __init__(self, time):
        r"""

        @Arguments:
        - `time`:
        """
        self._time = time

    def get_time(self, ):
        r"""SUMMARY

        get_time()

        @Return:

        @Error:
        """
        return self._time

    def set_time(self, time):
        r"""SUMMARY

        set_time(time)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._time = time

    time = property(get_time, set_time)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xI', self.time))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class GrabKey(object):
    r"""GrabKey

    GrabKey is a object.
    Responsibility:
    """
    def __init__(self, owner_events, grab_window, modifiers, key,
                 pointer_mode, keyboard_mode):
        r"""

        @Arguments:
        - `owner_events`:
        - `grab_window`:
        - `modifiers`:
        - `key`:
        - `pointer_mode`:
        - `keyboard_mode`:
        """
        self._owner_events = owner_events
        self._grab_window = grab_window
        self._modifiers = modifiers
        self._key = key
        self._pointer_mode = pointer_mode
        self._keyboard_mode = keyboard_mode

    def get_owner_events(self, ):
        r"""SUMMARY

        get_owner_events()

        @Return:

        @Error:
        """
        return self._owner_events

    def set_owner_events(self, owner_events):
        r"""SUMMARY

        set_owner_events(owner_events)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._owner_events = owner_events

    owner_events = property(get_owner_events, set_owner_events)

    def get_grab_window(self, ):
        r"""SUMMARY

        get_grab_window()

        @Return:

        @Error:
        """
        return self._grab_window

    def set_grab_window(self, grab_window):
        r"""SUMMARY

        set_grab_window(grab_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._grab_window = grab_window

    grab_window = property(get_grab_window, set_grab_window)

    def get_modifiers(self, ):
        r"""SUMMARY

        get_modifiers()

        @Return:

        @Error:
        """
        return self._modifiers

    def set_modifiers(self, modifiers):
        r"""SUMMARY

        set_modifiers(modifiers)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._modifiers = modifiers

    modifiers = property(get_modifiers, set_modifiers)

    def get_key(self, ):
        r"""SUMMARY

        get_key()

        @Return:

        @Error:
        """
        return self._key

    def set_key(self, key):
        r"""SUMMARY

        set_key(key)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._key = key

    key = property(get_key, set_key)

    def get_pointer_mode(self, ):
        r"""SUMMARY

        get_pointer_mode()

        @Return:

        @Error:
        """
        return self._pointer_mode

    def set_pointer_mode(self, pointer_mode):
        r"""SUMMARY

        set_pointer_mode(pointer_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._pointer_mode = pointer_mode

    pointer_mode = property(get_pointer_mode, set_pointer_mode)

    def get_keyboard_mode(self, ):
        r"""SUMMARY

        get_keyboard_mode()

        @Return:

        @Error:
        """
        return self._keyboard_mode

    def set_keyboard_mode(self, keyboard_mode):
        r"""SUMMARY

        set_keyboard_mode(keyboard_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._keyboard_mode = keyboard_mode

    keyboard_mode = property(get_keyboard_mode, set_keyboard_mode)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xIHBBB3x', self.owner_events, self.grab_window,
                        self.modifiers, self.key, self.pointer_mode,
                        self.keyboard_mode))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class UngrabKey(object):
    r"""UngrabKey

    UngrabKey is a object.
    Responsibility:
    """
    def __init__(self, key, grab_window, modifiers):
        r"""

        @Arguments:
        - `key`:
        - `grab_window`:
        - `modifiers`:
        """
        self._key = key
        self._grab_window = grab_window
        self._modifiers = modifiers

    def get_key(self, ):
        r"""SUMMARY

        get_key()

        @Return:

        @Error:
        """
        return self._key

    def set_key(self, key):
        r"""SUMMARY

        set_key(key)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._key = key

    key = property(get_key, set_key)

    def get_grab_window(self, ):
        r"""SUMMARY

        get_grab_window()

        @Return:

        @Error:
        """
        return self._grab_window

    def set_grab_window(self, grab_window):
        r"""SUMMARY

        set_grab_window(grab_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._grab_window = grab_window

    grab_window = property(get_grab_window, set_grab_window)

    def get_modifiers(self, ):
        r"""SUMMARY

        get_modifiers()

        @Return:

        @Error:
        """
        return self._modifiers

    def set_modifiers(self, modifiers):
        r"""SUMMARY

        set_modifiers(modifiers)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._modifiers = modifiers

    modifiers = property(get_modifiers, set_modifiers)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xIH2x', self.key, self.grab_window, self.modifiers))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class AllowEvents(object):
    r"""AllowEvents

    AllowEvents is a object.
    Responsibility:
    """
    def __init__(self, mode, time):
        r"""

        @Arguments:
        - `mode`:
        - `time`:
        """
        self._mode = mode
        self._time = time

    def get_mode(self, ):
        r"""SUMMARY

        get_mode()

        @Return:

        @Error:
        """
        return self._mode

    def set_mode(self, mode):
        r"""SUMMARY

        set_mode(mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._mode = mode

    mode = property(get_mode, set_mode)

    def get_time(self, ):
        r"""SUMMARY

        get_time()

        @Return:

        @Error:
        """
        return self._time

    def set_time(self, time):
        r"""SUMMARY

        set_time(time)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._time = time

    time = property(get_time, set_time)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xI', self.mode, self.time))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class GrabServer(object):
    r"""GrabServer

    GrabServer is a object.
    Responsibility:
    """
    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class UngrabServer(object):
    r"""UngrabServer

    UngrabServer is a object.
    Responsibility:
    """
    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class QueryPointer(_Window):
    r"""QueryPointer

    QueryPointer is a _Window.
    Responsibility:
    """


class GetMotionEvents(object):
    r"""GetMotionEvents

    GetMotionEvents is a object.
    Responsibility:
    """
    def __init__(self, window, start, stop):
        r"""

        @Arguments:
        - `window`:
        - `start`:
        - `stop`:
        """
        self._window = window
        self._start = start
        self._stop = stop

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._window

    def set_window(self, window):
        r"""SUMMARY

        set_window(window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._window = window

    window = property(get_window, set_window)

    def get_start(self, ):
        r"""SUMMARY

        get_start()

        @Return:

        @Error:
        """
        return self._start

    def set_start(self, start):
        r"""SUMMARY

        set_start(start)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._start = start

    start = property(get_start, set_start)

    def get_stop(self, ):
        r"""SUMMARY

        get_stop()

        @Return:

        @Error:
        """
        return self._stop

    def set_stop(self, stop):
        r"""SUMMARY

        set_stop(stop)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._stop = stop

    stop = property(get_stop, set_stop)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xIII', self.window, self.start, self.stop))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class TranslateCoordinates(object):
    r"""TranslateCoordinates

    TranslateCoordinates is a object.
    Responsibility:
    """
    def __init__(self, src_window, dst_window, src_x, src_y):
        r"""

        @Arguments:
        - `src_window`:
        - `dst_window`:
        - `src_x`:
        - `src_y`:
        """
        self._src_window = src_window
        self._dst_window = dst_window
        self._src_point = _point.Point(src_x, src_y)

    def get_src_window(self, ):
        r"""SUMMARY

        get_src_window()

        @Return:

        @Error:
        """
        return self._src_window

    def set_src_window(self, src_window):
        r"""SUMMARY

        set_src_window(src_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._src_window = src_window

    src_window = property(get_src_window, set_src_window)

    def get_dst_window(self, ):
        r"""SUMMARY

        get_dst_window()

        @Return:

        @Error:
        """
        return self._dst_window

    def set_dst_window(self, dst_window):
        r"""SUMMARY

        set_dst_window(dst_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._dst_window = dst_window

    dst_window = property(get_dst_window, set_dst_window)

    def get_src_x(self, ):
        r"""SUMMARY

        get_src_x()

        @Return:

        @Error:
        """
        return self._src_point.get_x()

    def set_src_x(self, src_x):
        r"""SUMMARY

        set_src_x(src_x)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._src_point.set_x(src_x)

    src_x = property(get_src_x, set_src_x)

    def get_src_y(self, ):
        r"""SUMMARY

        get_src_y()

        @Return:

        @Error:
        """
        return self._src_point.get_y()

    def set_src_y(self, src_y):
        r"""SUMMARY

        set_src_y(src_y)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._src_point.set_y(src_y)

    src_y = property(get_src_y, set_src_y)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xIIhh', self.src_window, self.dst_window,
                        self.src_x, self.src_y))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class WarpPointer(object):
    r"""WarpPointer

    WarpPointer is a object.
    Responsibility:
    """
    def __init__(self, src_window, dst_window, src_x, src_y,
                 src_width, src_height, dst_x, dst_y):
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
        """
        self._src_window = src_window
        self._dst_window = dst_window
        self._src_rect = _rectangle.Rectangle(
            src_x, src_y, src_width, src_height)
        self._dst_point = _point.Point(dst_x, dst_y)

    def get_src_window(self, ):
        r"""SUMMARY

        get_src_window()

        @Return:

        @Error:
        """
        return self._src_window

    def set_src_window(self, src_window):
        r"""SUMMARY

        set_src_window(src_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._src_window = src_window

    src_window = property(get_src_window, set_src_window)

    def get_dst_window(self, ):
        r"""SUMMARY

        get_dst_window()

        @Return:

        @Error:
        """
        return self._dst_window

    def set_dst_window(self, dst_window):
        r"""SUMMARY

        set_dst_window(dst_window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._dst_window = dst_window

    dst_window = property(get_dst_window, set_dst_window)

    def get_src_x(self, ):
        r"""SUMMARY

        get_src_x()

        @Return:

        @Error:
        """
        return self._src_rect.get_x()

    def set_src_x(self, src_x):
        r"""SUMMARY

        set_src_x(src_x)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._src_rect.set_x(src_x)

    src_x = property(get_src_x, set_src_x)

    def get_src_y(self, ):
        r"""SUMMARY

        get_src_y()

        @Return:

        @Error:
        """
        return self._src_rect.get_y()

    def set_src_y(self, src_y):
        r"""SUMMARY

        set_src_y(src_y)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._src_rect.set_y(src_y)

    src_y = property(get_src_y, set_src_y)

    def get_src_width(self, ):
        r"""SUMMARY

        get_src_width()

        @Return:

        @Error:
        """
        return self._src_rect.get_width()

    def set_src_width(self, src_width):
        r"""SUMMARY

        set_src_width(src_width)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._src_rect.set_width(src_width)

    src_width = property(get_src_width, set_src_width)

    def get_src_height(self, ):
        r"""SUMMARY

        get_src_height()

        @Return:

        @Error:
        """
        return self._src_rect.get_height()

    def set_src_height(self, src_height):
        r"""SUMMARY

        set_src_height(src_height)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._src_rect.set_height(src_height)

    src_height = property(get_src_height, set_src_height)

    def get_dst_x(self, ):
        r"""SUMMARY

        get_dst_x()

        @Return:

        @Error:
        """
        return self._dst_point.get_x()

    def set_dst_x(self, dst_x):
        r"""SUMMARY

        set_dst_x(dst_x)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._dst_point.set_x(dst_x)

    dst_x = property(get_dst_x, set_dst_x)

    def get_dst_y(self, ):
        r"""SUMMARY

        get_dst_y()

        @Return:

        @Error:
        """
        return self._dst_point.get_y()

    def set_dst_y(self, dst_y):
        r"""SUMMARY

        set_dst_y(dst_y)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._dst_point.set_y(dst_y)

    dst_y = property(get_dst_y, set_dst_y)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xIIhhHHhh', self.src_window, self.dst_window,
                        self.src_x, self.src_y, self.src_width, self.src_height,
                        self.dst_x, self.dst_y))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class SetInputFocus(object):
    r"""SetInputFocus

    SetInputFocus is a object.
    Responsibility:
    """
    def __init__(self, revert_to, focus, time):
        r"""

        @Arguments:
        - `revert_to`:
        - `focus`:
        - `time`:
        """
        self._revert_to = revert_to
        self._focus = focus
        self._time = time

    def get_revert_to(self, ):
        r"""SUMMARY

        get_revert_to()

        @Return:

        @Error:
        """
        return self._revert_to

    def set_revert_to(self, revert_to):
        r"""SUMMARY

        set_revert_to(revert_to)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._revert_to = revert_to

    revert_to = property(get_revert_to, set_revert_to)

    def get_focus(self, ):
        r"""SUMMARY

        get_focus()

        @Return:

        @Error:
        """
        return self._focus

    def set_focus(self, focus):
        r"""SUMMARY

        set_focus(focus)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._focus = focus

    focus = property(get_focus, set_focus)

    def get_time(self, ):
        r"""SUMMARY

        get_time()

        @Return:

        @Error:
        """
        return self._time

    def set_time(self, time):
        r"""SUMMARY

        set_time(time)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._time = time

    time = property(get_time, set_time)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xII', self.revert_to, self.focus, self.time))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class GetInputFocus(object):
    r"""GetInputFocus

    GetInputFocus is a object.
    Responsibility:
    """
    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        return _pack('=xx2x', )

    def __str__(self):
        return self.get_buffer()


class QueryKeymap(object):
    r"""QueryKeymap

    QueryKeymap is a object.
    Responsibility:
    """
    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        return _pack('=xx2x', )

    def __str__(self):
        return self.get_buffer()


class OpenFont(object):
    r"""OpenFont

    OpenFont is a object.
    Responsibility:
    """
    def __init__(self, fid, name):
        r"""

        @Arguments:
        - `fid`:
        - `name_len`:
        - `name`:
        """
        self._fid = fid
        self._name = name

    def get_fid(self, ):
        r"""SUMMARY

        get_fid()

        @Return:

        @Error:
        """
        return self._fid

    def set_fid(self, fid):
        r"""SUMMARY

        set_fid(fid)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._fid = fid

    fid = property(get_fid, set_fid)

    def get_name(self, ):
        r"""SUMMARY

        get_name()

        @Return:

        @Error:
        """
        return self._name

    def set_name(self, name):
        r"""SUMMARY

        set_name(name)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._name = name

    name = property(get_name, set_name)

    def get_length(self, ):
        r"""SUMMARY

        get_length()

        @Return:

        @Error:
        """
        return len(self.name)

    name_len = property(get_length)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xIH2x', self.fid, self.name_len))
        buf.write(str(buffer(_array('b', self.name))))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class CloseFont(object):
    r"""CloseFont

    CloseFont is a object.
    Responsibility:
    """
    def __init__(self, font):
        r"""

        @Arguments:
        - `font`:
        """
        self._font = font

    def get_font(self, ):
        r"""SUMMARY

        get_font()

        @Return:

        @Error:
        """
        return self._font

    def set_font(self, font):
        r"""SUMMARY

        set_font(font)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._font = font

    font = property(get_font, set_font)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xI', self.font))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class QueryFont(CloseFont):
    r"""QueryFont

    QueryFont is a CloseFont.
    Responsibility:
    """


class QueryTextExtents(object):
    r"""QueryTextExtents

    QueryTextExtents is a object.
    Responsibility:
    """
    def __init__(self, font, string_len, string):
        r"""

        @Arguments:
        - `font`:
        - `string_len`:
        - `string`:
        """
        self._font = font
        self._string_len = string_len
        self._string = string

    def get_font(self, ):
        r"""SUMMARY

        get_font()

        @Return:

        @Error:
        """
        return self._font

    def set_font(self, font):
        r"""SUMMARY

        set_font(font)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._font = font

    font = property(get_font, set_font)

    def get_string_len(self, ):
        r"""SUMMARY

        get_string_len()

        @Return:

        @Error:
        """
        return self._string_len

    def set_string_len(self, string_len):
        r"""SUMMARY

        set_string_len(string_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._string_len = string_len

    string_len = property(get_string_len, set_string_len)

    def get_string(self, ):
        r"""SUMMARY

        get_string()

        @Return:

        @Error:
        """
        return self._string

    def set_string(self, string):
        r"""SUMMARY

        set_string(string)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._string = string

    string = property(get_string, set_string)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=x', ))
        buf.write(_pack('=B', (self.string_len & 1)))
        buf.write(_pack('=2xI', self.font))
        # TODO: (Atami) [2015/01/15]
        for elt in xcb.Iterator(self.string, 2, 'string', True):
            buf.write(_pack('=BB', *elt))

    def __str__(self):
        return self.get_buffer()


class ListFonts(object):
    r"""ListFonts

    ListFonts is a object.
    Responsibility:
    """
    def __init__(self, max_names, pattern_len, pattern):
        r"""

        @Arguments:
        - `max_names`:
        - `pattern_len`:
        - `pattern`:
        """
        self._max_names = max_names
        self._pattern_len = pattern_len
        self._pattern = pattern

    def get_max_names(self, ):
        r"""SUMMARY

        get_max_names()

        @Return:

        @Error:
        """
        return self._max_names

    def set_max_names(self, max_names):
        r"""SUMMARY

        set_max_names(max_names)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._max_names = max_names

    max_names = property(get_max_names, set_max_names)

    def get_pattern_len(self, ):
        r"""SUMMARY

        get_pattern_len()

        @Return:

        @Error:
        """
        return self._pattern_len

    def set_pattern_len(self, pattern_len):
        r"""SUMMARY

        set_pattern_len(pattern_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._pattern_len = pattern_len

    pattern_len = property(get_pattern_len, set_pattern_len)

    def get_pattern(self, ):
        r"""SUMMARY

        get_pattern()

        @Return:

        @Error:
        """
        return self._pattern

    def set_pattern(self, pattern):
        r"""SUMMARY

        set_pattern(pattern)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._pattern = pattern

    pattern = property(get_pattern, set_pattern)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xHH', self.max_names, self.pattern_len))
        buf.write(str(buffer(_array('b', self.pattern))))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class ListFontsWithInfo(ListFonts):
    r"""ListFontsWithInfo

    ListFontsWithInfo is a ListFonts.
    Responsibility:
    """


class SetFontPath(object):
    r"""SetFontPath

    SetFontPath is a object.
    Responsibility:
    """
    def __init__(self, font_qty, font):
        r"""

        @Arguments:
        - `font_qty`:
        - `font`:
        """
        self._font_qty = font_qty
        self._font = font

    def get_font_qty(self, ):
        r"""SUMMARY

        get_font_qty()

        @Return:

        @Error:
        """
        return self._font_qty

    def set_font_qty(self, font_qty):
        r"""SUMMARY

        set_font_qty(font_qty)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._font_qty = font_qty

    font_qty = property(get_font_qty, set_font_qty)

    def get_font(self, ):
        r"""SUMMARY

        get_font()

        @Return:

        @Error:
        """
        return self._font

    def set_font(self, font):
        r"""SUMMARY

        set_font(font)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._font = font

    font = property(get_font, set_font)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer_()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xH2x', self.font_qty))
        for elt in xcb.Iterator(self.font, -1, 'font', True):
            buf.write(_pack('=None', *elt))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()



class GetFontPath(object):
    r"""GetFontPath

    GetFontPath is a object.
    Responsibility:
    """
    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class CreatePixmap(object):
    r"""CreatePixmap

    CreatePixmap is a object.
    Responsibility:
    """
    def __init__(self, depth, pid, drawable, width, height):
        r"""

        @Arguments:
        - `depth`:
        - `pid`:
        - `drawable`:
        - `width`:
        - `height`:
        """
        self._depth = depth
        self._pid = pid
        self._drawable = drawable
        self._dimension = _dimension.Dimension(width, height)

    def get_depth(self, ):
        r"""SUMMARY

        get_depth()

        @Return:

        @Error:
        """
        return self._depth

    def set_depth(self, depth):
        r"""SUMMARY

        set_depth(depth)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._depth = depth

    depth = property(get_depth, set_depth)

    def get_pid(self, ):
        r"""SUMMARY

        get_pid()

        @Return:

        @Error:
        """
        return self._pid

    def set_pid(self, pid):
        r"""SUMMARY

        set_pid(pid)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._pid = pid

    pid = property(get_pid, set_pid)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._drawable

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._drawable = drawable

    drawable = property(get_drawable, set_drawable)

    def get_width(self, ):
        r"""SUMMARY

        get_width()

        @Return:

        @Error:
        """
        return self._dimension.get_width()

    def set_width(self, width):
        r"""SUMMARY

        set_width(width)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._dimension.set_width(width)

    width = property(get_width, set_width)

    def get_height(self, ):
        r"""SUMMARY

        get_height()

        @Return:

        @Error:
        """
        return self._dimension.get_height()

    def set_height(self, height):
        r"""SUMMARY

        set_height(height)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._dimension.set_height(height)

    height = property(get_height, set_height)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xIIHH', self.depth, self.pid, self.drawable,
                        self.width, self.height))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class FreePixmap(object):
    r"""FreePixmap

    FreePixmap is a object.
    Responsibility:
    """
    def __init__(self, pixmap):
        r"""

        @Arguments:
        - `pixmap`:
        """
        self._pixmap = pixmap

    def get_pixmap(self, ):
        r"""SUMMARY

        get_pixmap()

        @Return:

        @Error:
        """
        return self._pixmap

    def set_pixmap(self, pixmap):
        r"""SUMMARY

        set_pixmap(pixmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._pixmap = pixmap

    pixmap = property(get_pixmap, set_pixmap)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xI', self.pixmap))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class CreateGC(object):
    r"""CreateGC

    CreateGC is a object.
    Responsibility:
    """
    def __init__(self, cid, drawable, value_mask, value_list):
        r"""

        @Arguments:
        - `cid`:
        - `drawable`:
        - `value_mask`:
        - `value_list`:
        """
        self._cid = cid
        self._drawable = drawable
        self._value_mask = value_mask
        self._value_list = value_list

    def get_cid(self, ):
        r"""SUMMARY

        get_cid()

        @Return:

        @Error:
        """
        return self._cid

    def set_cid(self, cid):
        r"""SUMMARY

        set_cid(cid)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._cid = cid

    cid = property(get_cid, set_cid)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._drawable

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._drawable = drawable

    drawable = property(get_drawable, set_drawable)

    def get_value_mask(self, ):
        r"""SUMMARY

        get_value_mask()

        @Return:

        @Error:
        """
        return self._value_mask

    def set_value_mask(self, value_mask):
        r"""SUMMARY

        set_value_mask(value_mask)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._value_mask = value_mask

    value_mask = property(get_value_mask, set_value_mask)

    def get_value_list(self, ):
        r"""SUMMARY

        get_value_list()

        @Return:

        @Error:
        """
        return self._value_list

    def set_value_list(self, value_list):
        r"""SUMMARY

        set_value_list(value_list)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._value_list = value_list

    value_list = property(get_value_list, set_value_list)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xIII', self.cid, self.drawable, self.value_mask))
        buf.write(str(buffer(_array('I', self.value_list))))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class ChangeGC(object):
    r"""ChangeGC

    ChangeGC is a object.
    Responsibility:
    """
    def __init__(self, gc, value_mask, value_list):
        r"""

        @Arguments:
        - `gc`:
        - `value_mask`:
        - `value_list`:
        """
        self._gc = gc
        self._value_mask = value_mask
        self._value_list = value_list

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._gc

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._gc = gc

    gc = property(get_gc, set_gc)

    def get_value_mask(self, ):
        r"""SUMMARY

        get_value_mask()

        @Return:

        @Error:
        """
        return self._value_mask

    def set_value_mask(self, value_mask):
        r"""SUMMARY

        set_value_mask(value_mask)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._value_mask = value_mask

    value_mask = property(get_value_mask, set_value_mask)

    def get_value_list(self, ):
        r"""SUMMARY

        get_value_list()

        @Return:

        @Error:
        """
        return self._value_list

    def set_value_list(self, value_list):
        r"""SUMMARY

        set_value_list(value_list)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._value_list = value_list

    value_list = property(get_value_list, set_value_list)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xII', self.gc, self.value_mask))
        buf.write(str(buffer(_array('I', self.value_list))))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class CopyGC(object):
    r"""CopyGC

    CopyGC is a object.
    Responsibility:
    """
    def __init__(self, src_gc, dst_gc, value_mask):
        r"""

        @Arguments:
        - `src_gc`:
        - `dst_gc`:
        - `value_mask`:
        """
        self._src_gc = src_gc
        self._dst_gc = dst_gc
        self._value_mask = value_mask

    def get_src_gc(self, ):
        r"""SUMMARY

        get_src_gc()

        @Return:

        @Error:
        """
        return self._src_gc

    def set_src_gc(self, src_gc):
        r"""SUMMARY

        set_src_gc(src_gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._src_gc = src_gc

    src_gc = property(get_src_gc, set_src_gc)

    def get_dst_gc(self, ):
        r"""SUMMARY

        get_dst_gc()

        @Return:

        @Error:
        """
        return self._dst_gc

    def set_dst_gc(self, dst_gc):
        r"""SUMMARY

        set_dst_gc(dst_gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._dst_gc = dst_gc

    dst_gc = property(get_dst_gc, set_dst_gc)

    def get_value_mask(self, ):
        r"""SUMMARY

        get_value_mask()

        @Return:

        @Error:
        """
        return self._value_mask

    def set_value_mask(self, value_mask):
        r"""SUMMARY

        set_value_mask(value_mask)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._value_mask = value_mask

    value_mask = property(get_value_mask, set_value_mask)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xIII', self.src_gc, self.dst_gc, self.value_mask))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class SetDashes(object):
    r"""SetDashes

    SetDashes is a object.
    Responsibility:
    """
    def __init__(self, gc, dash_offset, dashes_len, dashes):
        r"""

        @Arguments:
        - `gc`:
        - `dash_offset`:
        - `dashes_len`:
        - `dashes`:
        """
        self._gc = gc
        self._dash_offset = dash_offset
        self._dashes_len = dashes_len
        self._dashes = dashes

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._gc

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._gc = gc

    gc = property(get_gc, set_gc)

    def get_dash_offset(self, ):
        r"""SUMMARY

        get_dash_offset()

        @Return:

        @Error:
        """
        return self._dash_offset

    def set_dash_offset(self, dash_offset):
        r"""SUMMARY

        set_dash_offset(dash_offset)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._dash_offset = dash_offset

    dash_offset = property(get_dash_offset, set_dash_offset)

    def get_dashes_len(self, ):
        r"""SUMMARY

        get_dash_len()

        @Return:

        @Error:
        """
        return self._dashes_len

    def set_dashes_len(self, dashes_len):
        r"""SUMMARY

        set_dash_len(dash_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._dashes_len = dashes_len

    dashes_len = property(get_dashes_len, set_dashes_len)

    def get_dashes(self, ):
        r"""SUMMARY

        get_dashes()

        @Return:

        @Error:
        """
        return self._dashes

    def set_dashes(self, dashes):
        r"""SUMMARY

        set_dashes(dashes)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._dashes = dashes

    dashes = property(get_dashes, set_dashes)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xIHH', self.gc, self.dash_offset, self.dashes_len))
        buf.write(str(buffer(_array('B', self.dashes))))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class SetClipRectangles(object):
    r"""SetClipRectangles

    SetClipRectangles is a object.
    Responsibility:
    """
    def __init__(self, ordering, gc, clip_x_origin, clip_y_origin,
                 rectangles_len, rectangles):
        r"""

        @Arguments:
        - `ordering`:
        - `gc`:
        - `clip_x_origin`:
        - `clip_y_origin`:
        - `rectangles_len`:
        - `rectangles`:
        """
        self._ordering = ordering
        self._gc = gc
        self._clip_x_origin = clip_x_origin
        self._clip_y_origin = clip_y_origin
        self._rectangles_len = rectangles_len
        self._rectangles = rectangles

    def get_ordering(self, ):
        r"""SUMMARY

        get_ordering()

        @Return:

        @Error:
        """
        return self._ordering

    def set_ordering(self, ordering):
        r"""SUMMARY

        set_ordering(ordering)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._ordering = ordering

    ordering = property(get_ordering, set_ordering)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._gc

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._gc = gc

    gc = property(get_gc, set_gc)

    def get_clip_x_origin(self, ):
        r"""SUMMARY

        get_clip_x_origin()

        @Return:

        @Error:
        """
        return self._clip_x_origin

    def set_clip_x_origin(self, clip_x_origin):
        r"""SUMMARY

        set_clip_x_origin(clip_x_origin)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._clip_x_origin = clip_x_origin

    clip_x_origin = property(get_clip_x_origin, set_clip_x_origin)

    def get_clip_y_origin(self, ):
        r"""SUMMARY

        get_clip_y_origin()

        @Return:

        @Error:
        """
        return self._clip_y_origin

    def set_clip_y_origin(self, clip_y_origin):
        r"""SUMMARY

        set_clip_y_origin(clip_y_origin)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._clip_y_origin = clip_y_origin

    clip_y_origin = property(get_clip_y_origin, set_clip_y_origin)

    def get_rectangles_len(self, ):
        r"""SUMMARY

        get_rectangles_len()

        @Return:

        @Error:
        """
        return self._rectangles_len

    def set_rectangles_len(self, rectangles_len):
        r"""SUMMARY

        set_rectangles_len(rectangles_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._rectangles_len = rectangles_len

    rectangles_len = property(get_rectangles_len, set_rectangles_len)

    def get_rectangles(self, ):
        r"""SUMMARY

        get_rectangles()

        @Return:

        @Error:
        """
        return self._rectangles

    def set_rectangles(self, rectangles):
        r"""SUMMARY

        set_rectangles(rectangles)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._rectangles = rectangles

    rectangles = property(get_rectangles, set_rectangles)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xIhh', self.ordering, self.gc,
                        self.clip_x_origin, self.clip_y_origin))
        for elt in xcb.Iterator(self.rectangles, 4, 'rectangles', True):
            buf.write(_pack('=hhHH', *elt))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class FreeGC(object):
    r"""FreeGC

    FreeGC is a object.
    Responsibility:
    """
    def __init__(self, gc):
        r"""

        @Arguments:
        - `gc`:
        """
        self._gc = gc

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._gc

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._gc = gc

    gc = property(get_gc, set_gc)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xI', self.gc))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class ClearArea(object):
    r"""ClearArea

    ClearArea is a object.
    Responsibility:
    """
    def __init__(self, exposures, window, x, y, width, height):
        r"""

        @Arguments:
        - `exposures`:
        - `window`:
        - `x`:
        - `y`:
        - `width`:
        - `height`:
        """
        self._exposures = exposures
        self._window = window
        self._rect = _rectangle.Rectangle(x, y, width, height)

    def get_exposures(self, ):
        r"""SUMMARY

        get_exposures()

        @Return:

        @Error:
        """
        return self._exposures

    def set_exposures(self, exposures):
        r"""SUMMARY

        set_exposures(exposures)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._exposures = exposures

    exposures = property(get_exposures, set_exposures)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._window

    def set_window(self, window):
        r"""SUMMARY

        set_window(window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._window = window

    window = property(get_window, set_window)

    def get_x(self, ):
        r"""SUMMARY

        get_x()

        @Return:

        @Error:
        """
        return self._rect.get_x()

    def set_x(self, newx):
        r"""SUMMARY

        set_x(newx)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._rect.set_x(newx)

    x = property(get_x, set_x)

    def get_y(self, ):
        r"""SUMMARY

        get_y()

        @Return:

        @Error:
        """
        return self._rect.get_y()

    def set_y(self, newy):
        r"""SUMMARY

        set_y(newy)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._rect.set_y(newy)

    y = property(get_y, set_y)

    def get_width(self, ):
        r"""SUMMARY

        get_width()

        @Return:

        @Error:
        """
        return self._rect.get_width()

    def set_width(self, width):
        r"""SUMMARY

        set_width(width)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._rect.set_width(width)

    width = property(get_width, set_width)

    def get_height(self, ):
        r"""SUMMARY

        get_height()

        @Return:

        @Error:
        """
        return self._rect.get_height()

    def set_height(self, height):
        r"""SUMMARY

        set_height(height)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._rect.set_height(height)

    height = property(get_height, set_height)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xIhhHH', self.exposures, self.window,
                        self.x, self.y, self.width, self.height))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class CopyArea(object):
    r"""CopyArea

    CopyArea is a object.
    Responsibility:
    """
    def __init__(self, src_drawable, dst_drawable, gc, src_x, src_y,
                 dst_x, dst_y, width, height):
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
        """
        self._src_drawable = src_drawable
        self._dst_drawable = dst_drawable
        self._gc = gc
        self._src_point = _point.Point(src_x, src_y)
        self._dst_point = _point.Point(dst_x, dst_y)
        self._dimension = _dimension.Dimension(width, height)

    def get_src_drawable(self, ):
        r"""SUMMARY

        get_src_drawable()

        @Return:

        @Error:
        """
        return self._src_drawable

    def set_src_drawable(self, src_drawable):
        r"""SUMMARY

        set_src_drawable(src_drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._src_drawable = src_drawable

    src_drawable = property(get_src_drawable, set_src_drawable)

    def get_dst_drawable(self, ):
        r"""SUMMARY

        get_dst_drawable()

        @Return:

        @Error:
        """
        return self._dst_drawable

    def set_dst_drawable(self, dst_drawable):
        r"""SUMMARY

        set_dst_drawable(dst_drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._dst_drawable = dst_drawable

    dst_drawable = property(get_dst_drawable, set_dst_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._gc

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._gc = gc

    gc = property(get_gc, set_gc)

    def get_src_x(self, ):
        r"""SUMMARY

        get_src_x()

        @Return:

        @Error:
        """
        return self._src_point.get_x()

    def set_src_x(self, src_x):
        r"""SUMMARY

        set_src_x(src_x)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._src_point.set_x(src_x)

    src_x = property(get_src_x, set_src_x)

    def get_src_y(self, ):
        r"""SUMMARY

        get_src_y()

        @Return:

        @Error:
        """
        return self._src_point.get_y()

    def set_src_y(self, src_y):
        r"""SUMMARY

        set_src_y(src_y)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._src_point.set_y(src_y)

    src_y = property(get_src_y, set_src_y)

    def get_dst_x(self, ):
        r"""SUMMARY

        get_dst_x()

        @Return:

        @Error:
        """
        return self._dst_point.get_x()

    def set_dst_x(self, dst_x):
        r"""SUMMARY

        set_dst_x(dst_x)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._dst_point.set_x(dst_x)

    dst_x = property(get_dst_x, set_dst_x)

    def get_dst_y(self, ):
        r"""SUMMARY

        get_dst_y()

        @Return:

        @Error:
        """
        return self._dst_point.get_y()

    def set_dst_y(self, dst_y):
        r"""SUMMARY

        set_dst_y(dst_y)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._dst_point.set_y(dst_y)

    dst_y = property(get_dst_y, set_dst_y)

    def get_width(self, ):
        r"""SUMMARY

        get_width()

        @Return:

        @Error:
        """
        return self._dimension.get_width()

    def set_width(self, width):
        r"""SUMMARY

        set_width(width)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._dimension.set_width(width)

    width = property(get_width, set_width)

    def get_height(self, ):
        r"""SUMMARY

        get_height()

        @Return:

        @Error:
        """
        return self._dimension.get_height()

    def set_height(self, height):
        r"""SUMMARY

        set_height(height)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._dimension.set_height(height)

    height = property(get_height, set_height)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xIIIhhhhHH', self.src_drawable, self.dst_drawable,
                        self.gc, self.src_x, self.src_y, self.dst_x, self.dst_y,
                        self.width, self.height))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class CopyPlane(CopyArea):
    r"""CopyPlane

    CopyPlane is a object.
    Responsibility:
    """
    def __init__(self, src_drawable, dst_drawable, gc, src_x, src_y,
                 dst_x, dst_y, width, height, bit_plane):
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
        """
        CopyArea.__init__(self, src_drawable, dst_drawable, gc, src_x, src_y,
                          dst_x, dst_y, width, height)
        self._bit_plane = bit_plane

    def get_bit_plane(self, ):
        r"""SUMMARY

        get_bit_plane()

        @Return:

        @Error:
        """
        return self._bit_plane

    def set_bit_plane(self, bit_plane):
        r"""SUMMARY

        set_bit_plane(bit_plane)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._bit_plane = bit_plane

    bit_plane = property(get_bit_plane, set_bit_plane)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(super(CopyPlane, self).get_buffer())
        buf.write('I', self.bit_plane)
        return buf.getvalue()


class PolyPoint(object):
    r"""PolyPoint

    PolyPoint is a object.
    Responsibility:
    """
    def __init__(self, coordinate_mode, drawable, gc, points_len, points):
        r"""

        @Arguments:
        - `coordinate_mode`:
        - `drawable`:
        - `gc`:
        - `points_len`:
        - `points`:
        """
        self._coordinate_mode = coordinate_mode
        self._drawable = drawable
        self._gc = gc
        self._points_len = points_len
        self._points = points

    def get_coordinate_mode(self, ):
        r"""SUMMARY

        get_coordinate_mode()

        @Return:

        @Error:
        """
        return self._coordinate_mode

    def set_coordinate_mode(self, coordinate_mode):
        r"""SUMMARY

        set_coordinate_mode(coordinate_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._coordinate_mode = coordinate_mode

    coordinate_mode = property(get_coordinate_mode, set_coordinate_mode)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._drawable

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._drawable = drawable

    drawable = property(get_drawable, set_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._gc

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._gc = gc

    gc = property(get_gc, set_gc)

    def get_points_len(self, ):
        r"""SUMMARY

        get_points_len()

        @Return:

        @Error:
        """
        return self._points_len

    def set_points_len(self, points_len):
        r"""SUMMARY

        set_points_len(points_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._points_len = points_len

    points_len = property(get_points_len, set_points_len)

    def get_points(self, ):
        r"""SUMMARY

        get_points()

        @Return:

        @Error:
        """
        return self._points

    def set_points(self, points):
        r"""SUMMARY

        set_points(points)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._points = points

    points = property(get_points, set_points)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xII', self.coordinate_mode, self.drawable,
                        self.gc))
        for elt in xcb.Iterator(self.points, 2, 'points', True):
            buf.write(_pack('=hh', *elt))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class PolyLine(PolyPoint):
    r"""PolyLine

    PolyLine is a PolyPoint.
    Responsibility:
    """


class PolySegment(object):
    r"""PolySegment

    PolySegment is a object.
    Responsibility:
    """
    def __init__(self, drawable, gc, segments_len, segments):
        r"""

        @Arguments:
        - `drawable`:
        - `gc`:
        - `segments_len`:
        - `segments`:
        """
        self._drawable = drawable
        self._gc = gc
        self._segments_len = segments_len
        self._segments = segments

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._drawable

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._drawable = drawable

    drawable = property(get_drawable, set_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._gc

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._gc = gc

    gc = property(get_gc, set_gc)

    def get_segments_len(self, ):
        r"""SUMMARY

        get_segments_len()

        @Return:

        @Error:
        """
        return self._segments_len

    def set_segments_len(self, segments_len):
        r"""SUMMARY

        set_segments_len(segments_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._segments_len = segments_len

    segments_len = property(get_segments_len, set_segments_len)

    def get_segments(self, ):
        r"""SUMMARY

        get_segments()

        @Return:

        @Error:
        """
        return self._segments

    def set_segments(self, segments):
        r"""SUMMARY

        set_segments(segments)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._segments = segments

    segments = property(get_segments, set_segments)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xII', self.drawable, self.gc))
        for elt in xcb.Iterator(self.segments, 4, 'segments', True):
            buf.write(_pack('=hhhh', *elt))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class PolyRectangle(object):
    r"""PolyRectangle

    PolyRectangle is a object.
    Responsibility:
    """
    def __init__(self, drawable, gc, rectangles_len, rectangles):
        r"""

        @Arguments:
        - `drawable`:
        - `gc`:
        - `rectangles_len`:
        - `rectangles`:
        """
        self._drawable = drawable
        self._gc = gc
        self._rectangles_len = rectangles_len
        self._rectangles = rectangles

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._drawable

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._drawable = drawable

    drawable = property(get_drawable, set_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._gc

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._gc = gc

    gc = property(get_gc, set_gc)

    def get_rectangles_len(self, ):
        r"""SUMMARY

        get_rectangles_len()

        @Return:

        @Error:
        """
        return self._rectangles_len

    def set_rectangles_len(self, rectangles_len):
        r"""SUMMARY

        set_rectangles_len(rectangles_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._rectangles_len = rectangles_len

    rectangles_len = property(get_rectangles_len, set_rectangles_len)

    def get_rectangles(self, ):
        r"""SUMMARY

        get_rectangles()

        @Return:

        @Error:
        """
        return self._rectangles

    def set_rectangles(self, rectangles):
        r"""SUMMARY

        set_rectangles(rectangles)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._rectangles = rectangles

    rectangles = property(get_rectangles, set_rectangles)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xII', self.drawable, self.gc))
        for elt in xcb.Iterator(self.rectangles, 4, 'rectangles', True):
            buf.write(_pack('=hhHH', *elt))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class PolyArc(object):
    r"""PolyArc

    PolyArc is a object.
    Responsibility:
    """
    def __init__(self, drawable, gc, arcs_len, arcs):
        r"""

        @Arguments:
        - `drawable`:
        - `gc`:
        - `arcs_len`:
        - `arcs`:
        """
        self._drawable = drawable
        self._gc = gc
        self._arcs_len = arcs_len
        self._arcs = arcs

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._drawable

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._drawable = drawable

    drawable = property(get_drawable, set_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._gc

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._gc = gc

    gc = property(get_gc, set_gc)

    def get_arcs_len(self, ):
        r"""SUMMARY

        get_arcs_len()

        @Return:

        @Error:
        """
        return self._arcs_len

    def set_arcs_len(self, arcs_len):
        r"""SUMMARY

        set_arcs_len(arcs_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._arcs_len = arcs_len

    arcs_len = property(get_arcs_len, set_arcs_len)

    def get_arcs(self, ):
        r"""SUMMARY

        get_arcs()

        @Return:

        @Error:
        """
        return self._arcs

    def set_arcs(self, arcs):
        r"""SUMMARY

        set_arcs(arcs)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._arcs = arcs

    arcs = property(get_arcs, set_arcs)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xII', self.drawable, self.gc))
        for elt in xcb.Iterator(self.arcs, 6, 'arcs', True):
            buf.write(_pack('=hhHHhh', *elt))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class FillPoly(object):
    r"""FillPoly

    FillPoly is a object.
    Responsibility:
    """
    def __init__(self, drawable, gc, shape, coordinate_mode, points_len,
                 points):
        r"""

        @Arguments:
        - `drawable`:
        - `gc`:
        - `shape`:
        - `coordinate_mode`:
        - `points_len`:
        - `points`:
        """
        self._drawable = drawable
        self._gc = gc
        self._shape = shape
        self._coordinate_mode = coordinate_mode
        self._points_len = points_len
        self._points = points

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._drawable

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._drawable = drawable

    drawable = property(get_drawable, set_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._gc

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._gc = gc

    gc = property(get_gc, set_gc)

    def get_shape(self, ):
        r"""SUMMARY

        get_shape()

        @Return:

        @Error:
        """
        return self._shape

    def set_shape(self, shape):
        r"""SUMMARY

        set_shape(shape)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._shape = shape

    shape = property(get_shape, set_shape)

    def get_coordinate_mode(self, ):
        r"""SUMMARY

        get_coordinate_mode()

        @Return:

        @Error:
        """
        return self._coordinate_mode

    def set_coordinate_mode(self, coordinate_mode):
        r"""SUMMARY

        set_coordinate_mode(coordinate_mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._coordinate_mode = coordinate_mode

    coordinate_mode = property(get_coordinate_mode, set_coordinate_mode)

    def get_points_len(self, ):
        r"""SUMMARY

        get_points_len()

        @Return:

        @Error:
        """
        return self._points_len

    def set_points_len(self, points_len):
        r"""SUMMARY

        set_points_len(points_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._points_len = points_len

    points_len = property(get_points_len, set_points_len)

    def get_points(self, ):
        r"""SUMMARY

        get_points()

        @Return:

        @Error:
        """
        return self._points

    def set_points(self, points):
        r"""SUMMARY

        set_points(points)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._points = points

    points = property(get_points, set_points)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xIIBB2x', self.drawable, self.gc, self.shape,
                        self.coordinate_mode))
        for elt in xcb.Iterator(self.points, 2, 'points', True):
            buf.write(_pack('=hh', *elt))

    def __str__(self):
        return self.get_buffer()


class PolyFillRectangle(object):
    r"""PolyFillRectangle

    PolyFillRectangle is a object.
    Responsibility:
    """
    def __init__(self, drawable, gc, rectangles_len, rectangles):
        r"""

        @Arguments:
        - `drawable`:
        - `gc`:
        - `rectangles_len`:
        - `rectangles`:
        """
        self._drawable = drawable
        self._gc = gc
        self._rectangles_len = rectangles_len
        self._rectangles = rectangles

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._drawable

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._drawable = drawable

    drawable = property(get_drawable, set_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._gc

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._gc = gc

    gc = property(get_gc, set_gc)

    def get_rectangles_len(self, ):
        r"""SUMMARY

        get_rectangles_len()

        @Return:

        @Error:
        """
        return self._rectangles_len

    def set_rectangles_len(self, rectangles_len):
        r"""SUMMARY

        set_rectangles_len(rectangles_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._rectangles_len = rectangles_len

    rectangles_len = property(get_rectangles_len, set_rectangles_len)

    def get_rectangles(self, ):
        r"""SUMMARY

        get_rectangles()

        @Return:

        @Error:
        """
        return self._rectangles

    def set_rectangles(self, rectangles):
        r"""SUMMARY

        set_rectangles(rectangles)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._rectangles = rectangles

    rectangles = property(get_rectangles, set_rectangles)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xII', self.drawable, self.gc))
        for elt in xcb.Iterator(self.rectangles, 4, 'rectangles', True):
            buf.write(_pack('=hhHH', *elt))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class PolyFillArc(object):
    r"""PolyFillArc

    PolyFillArc is a object.
    Responsibility:
    """
    def __init__(self, drawable, gc, arcs_len, arcs):
        r"""

        @Arguments:
        - `drawable`:
        - `gc`:
        - `arcs_len`:
        - `arcs`:
        """
        self._drawable = drawable
        self._gc = gc
        self._arcs_len = arcs_len
        self._arcs = arcs

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._drawable

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._drawable = drawable

    drawable = property(get_drawable, set_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._gc

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._gc = gc

    gc = property(get_gc, set_gc)

    def get_arcs_len(self, ):
        r"""SUMMARY

        get_arcs_len()

        @Return:

        @Error:
        """
        return self._arcs_len

    def set_arcs_len(self, arcs_len):
        r"""SUMMARY

        set_arcs_len(arcs_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._arcs_len = arcs_len

    arcs_len = property(get_arcs_len, set_arcs_len)

    def get_arcs(self, ):
        r"""SUMMARY

        get_arcs()

        @Return:

        @Error:
        """
        return self._arcs

    def set_arcs(self, arcs):
        r"""SUMMARY

        set_arcs(arcs)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._arcs = arcs

    arcs = property(get_arcs, set_arcs)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xII', self.drawable, self.gc))
        for elt in xcb.Iterator(self.arcs, 6, 'arcs', True):
            buf.write(_pack('=hhHHhh', *elt))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class PutImage(object):
    r"""PutImage

    PutImage is a object.
    Responsibility:
    """
    def __init__(self, format_, drawable, gc, width, height, dst_x, dst_y,
                 left_pad, depth, data_len, data):
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
        """
        self._format = format_
        self._drawable = drawable
        self._gc = gc
        self._dst_rect = _rectangle.Rectangle(dst_x, dst_y, width, height)
        self._left_pad = left_pad
        self._depth = depth
        self._data_len = data_len
        self._data = data

    def get_format(self, ):
        r"""SUMMARY

        get_format()

        @Return:

        @Error:
        """
        return self._format

    def set_format(self, format_):
        r"""SUMMARY

        set_format(format_)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._format = format_

    format = property(get_format, set_format)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._drawable

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._drawable = drawable

    drawable = property(get_drawable, set_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._gc

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._gc = gc

    gc = property(get_gc, set_gc)

    def get_width(self, ):
        r"""SUMMARY

        get_width()

        @Return:

        @Error:
        """
        return self._dst_rect.get_width()

    def set_width(self, width):
        r"""SUMMARY

        set_width(width)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._dst_rect.set_width(width)

    width = property(get_width, set_width)

    def get_height(self, ):
        r"""SUMMARY

        get_height()

        @Return:

        @Error:
        """
        return self._dst_rect.get_height()

    def set_height(self, height):
        r"""SUMMARY

        set_height(height)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._dst_rect.set_height(height)

    height = property(get_height, set_height)

    def get_dst_x(self, ):
        r"""SUMMARY

        get_x()

        @Return:

        @Error:
        """
        return self._dst_rect.get_x()

    def set_dst_x(self, newx):
        r"""SUMMARY

        set_x(newx)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._dst_rect.set_x(newx)

    x = property(get_dst_x, set_dst_x)

    def get_dst_y(self, ):
        r"""SUMMARY

        get_y()

        @Return:

        @Error:
        """
        return self._dst_rect.get_y()

    def set_dst_y(self, newy):
        r"""SUMMARY

        set_y(newy)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._dst_rect.set_y(newy)

    y = property(get_dst_y, set_dst_y)

    def get_left_pad(self, ):
        r"""SUMMARY

        get_left_pad()

        @Return:

        @Error:
        """
        return self._left_pad

    def set_left_pad(self, left_pad):
        r"""SUMMARY

        set_left_pad(left_pad)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._left_pad = left_pad

    left_pad = property(get_left_pad, set_left_pad)

    def get_depth(self, ):
        r"""SUMMARY

        get_depth()

        @Return:

        @Error:
        """
        return self._depth

    def set_depth(self, depth):
        r"""SUMMARY

        set_depth(depth)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._depth = depth

    depth = property(get_depth, set_depth)

    def get_data_len(self, ):
        r"""SUMMARY

        get_data_len()

        @Return:

        @Error:
        """
        return self._data_len

    def set_data_len(self, data_len):
        r"""SUMMARY

        set_data_len(data_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._data_len = data_len

    data_len = property(get_data_len, set_data_len)

    def get_data(self, ):
        r"""SUMMARY

        get_data()

        @Return:

        @Error:
        """
        return self._data

    def set_data(self, data):
        r"""SUMMARY

        set_data(data)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._data = data

    data = property(get_data, set_data)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xIIHHhhBB2x', self.format, self.drawable, self.gc,
                        self.width, self.height, self.x, self.y,
                        self.left_pad, self.depth))
        buf.write(str(buffer(_array('B', self.data))))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class GetImage(object):
    r"""GetImage

    GetImage is a object.
    Responsibility:
    """
    def __init__(self, format_, drawable, x, y, width, height, plane_mask):
        r"""

        @Arguments:
        - `format_`:
        - `drawable`:
        - `x`:
        - `y`:
        - `width`:
        - `height`:
        - `plane_mask`:
        """
        self._format_ = format_
        self._drawable = drawable
        self._rect = _rectangle.Rectangle(x, y, width, height)
        self._plane_mask = plane_mask

    def get_format(self, ):
        r"""SUMMARY

        get_format()

        @Return:

        @Error:
        """
        return self._format

    def set_format(self, format_):
        r"""SUMMARY

        set_format(format_)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._format = format_

    format = property(get_format, set_format)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._drawable

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._drawable = drawable

    drawable = property(get_drawable, set_drawable)

    def get_x(self, ):
        r"""SUMMARY

        get_x()

        @Return:

        @Error:
        """
        return self._rect.get_x()

    def set_x(self, newx):
        r"""SUMMARY

        set_x(newx)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._rect.set_x(newx)

    x = property(get_x, set_x)

    def get_y(self, ):
        r"""SUMMARY

        get_y()

        @Return:

        @Error:
        """
        return self._rect.get_y()

    def set_y(self, newy):
        r"""SUMMARY

        set_y(newy)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._rect.set_y(newy)

    y = property(get_y, set_y)

    def get_width(self, ):
        r"""SUMMARY

        get_width()

        @Return:

        @Error:
        """
        return self._rect.get_width()

    def set_width(self, width):
        r"""SUMMARY

        set_width(width)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._rect.set_width(width)

    width = property(get_width, set_width)

    def get_height(self, ):
        r"""SUMMARY

        get_height()

        @Return:

        @Error:
        """
        return self._rect.get_height()

    def set_height(self, height):
        r"""SUMMARY

        set_height(height)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._rect.set_height(height)

    height = property(get_height, set_height)

    def get_plane_mask(self, ):
        r"""SUMMARY

        get_plane_mask()

        @Return:

        @Error:
        """
        return self._plane_mask

    def set_plane_mask(self, plane_mask):
        r"""SUMMARY

        set_plane_mask(plane_mask)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._plane_mask = plane_mask

    plane_mask = property(get_plane_mask, set_plane_mask)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xIhhHHI', self.format, self.drawable, self.x,
                        self.y, self.width, self.height, self.plane_mask))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class PolyText8(object):
    r"""PolyText8

    PolyText8 is a object.
    Responsibility:
    """
    def __init__(self, drawable, gc, x, y, items_len, items):
        r"""

        @Arguments:
        - `drawable`:
        - `gc`:
        - `x`:
        - `y`:
        - `items_len`:
        - `items`:
        """
        self._drawable = drawable
        self._gc = gc
        self._point = _point.Point(x, y)
        self._items_len = items_len
        self._items = items

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._drawable

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._drawable = drawable

    drawable = property(get_drawable, set_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._gc

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._gc = gc

    gc = property(get_gc, set_gc)

    def get_x(self, ):
        r"""SUMMARY

        get_x()

        @Return:

        @Error:
        """
        return self._point.get_x()

    def set_x(self, newx):
        r"""SUMMARY

        set_x(newx)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._point.set_x(newx)

    x = property(get_x, set_x)

    def get_y(self, ):
        r"""SUMMARY

        get_y()

        @Return:

        @Error:
        """
        return self._point.get_y()

    def set_y(self, newy):
        r"""SUMMARY

        set_y(newy)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._point.set_y(newy)

    y = property(get_y, set_y)

    def get_items_len(self, ):
        r"""SUMMARY

        get_items_len()

        @Return:

        @Error:
        """
        return self._items_len

    def set_items_len(self, items_len):
        r"""SUMMARY

        set_items_len(items_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._items_len = items_len

    items_len = property(get_items_len, set_items_len)

    def get_items(self, ):
        r"""SUMMARY

        get_items()

        @Return:

        @Error:
        """
        return self._items

    def set_items(self, items):
        r"""SUMMARY

        set_items(items)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._items = items

    items = property(get_items, set_items)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xIIhh', self.drawable, self.gc, self.x, self.y))
        buf.write(str(buffer(_array('B', self.items))))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class PolyText16(PolyText8):
    r"""PolyText16

    PolyText16 is a PolyText8.
    Responsibility:
    """


class ImageText8(object):
    r"""ImageText8

    ImageText8 is a object.
    Responsibility:
    """
    def __init__(self, string_len, drawable, gc, x, y, string):
        r"""

        @Arguments:
        - `string_len`:
        - `drawable`:
        - `gc`:
        - `x`:
        - `y`:
        - `string`:
        """
        self._string_len = string_len
        self._drawable = drawable
        self._gc = gc
        self._pont = _point.Point(x, y)
        self._string = string

    def get_string_len(self, ):
        r"""SUMMARY

        get_string_len()

        @Return:

        @Error:
        """
        return self._string_len

    def set_string_len(self, string_len):
        r"""SUMMARY

        set_string_len(string_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._string_len = string_len

    string_len = property(get_string_len, set_string_len)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._drawable

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._drawable = drawable

    drawable = property(get_drawable, set_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._gc

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._gc = gc

    gc = property(get_gc, set_gc)

    def get_x(self, ):
        r"""SUMMARY

        get_x()

        @Return:

        @Error:
        """
        return self._point.get_x()

    def set_x(self, newx):
        r"""SUMMARY

        set_x(newx)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._point.set_x(newx)

    x = property(get_x, set_x)

    def get_y(self, ):
        r"""SUMMARY

        get_y()

        @Return:

        @Error:
        """
        return self._point.get_y()

    def set_y(self, newy):
        r"""SUMMARY

        set_y(newy)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._point.set_y(newy)

    y = property(get_y, set_y)

    def get_string(self, ):
        r"""SUMMARY

        get_string()

        @Return:

        @Error:
        """
        return self._string

    def set_string(self, string):
        r"""SUMMARY

        set_string(string)

        @Arguments:
        - `string`:

        @Return:

        @Error:
        """
        self._string = string

    string = property(get_string, set_string)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xIIhh', self.string_len, self.drawable, self.gc,
                        self.x, self.y))
        buf.write(str(buffer(_array('b', self.string))))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class ImageText16(object):
    r"""ImageText16

    ImageText16 is a ImageText8.
    Responsibility:
    """
    def __init__(self, string_len, drawable, gc, x, y, string):
        r"""

        @Arguments:
        - `string_len`:
        - `drawable`:
        - `gc`:
        - `x`:
        - `y`:
        - `string`:
        """
        self._string_len = string_len
        self._drawable = drawable
        self._gc = gc
        self._point = _point.Point(x, y)
        self._string = string

    def get_string_len(self, ):
        r"""SUMMARY

        get_string_len()

        @Return:

        @Error:
        """
        return self._string_len

    def set_string_len(self, string_len):
        r"""SUMMARY

        set_string_len(string_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._string_len = string_len

    string_len = property(get_string_len, set_string_len)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._drawable

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._drawable = drawable

    drawable = property(get_drawable, set_drawable)

    def get_gc(self, ):
        r"""SUMMARY

        get_gc()

        @Return:

        @Error:
        """
        return self._gc

    def set_gc(self, gc):
        r"""SUMMARY

        set_gc(gc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._gc = gc

    gc = property(get_gc, set_gc)

    def get_x(self, ):
        r"""SUMMARY

        get_x()

        @Return:

        @Error:
        """
        return self._point.get_x()

    def set_x(self, newx):
        r"""SUMMARY

        set_x(newx)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._point.set_x(newx)

    x = property(get_x, set_x)

    def get_y(self, ):
        r"""SUMMARY

        get_y()

        @Return:

        @Error:
        """
        return self._point.get_y()

    def set_y(self, newy):
        r"""SUMMARY

        set_y(newy)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._point.set_y(newy)

    y = property(get_y, set_y)

    def get_string(self, ):
        r"""SUMMARY

        get_string()

        @Return:

        @Error:
        """
        return self._string

    def set_string(self, string):
        r"""SUMMARY

        set_string(string)

        @Arguments:
        - `string`:

        @Return:

        @Error:
        """
        self._string = string

    string = property(get_string, set_string)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xIIhh', self.string_len, self.drawable, self.gc,
                        self.x, self.y))
        buf.write(str(buffer(_array('b', self.string))))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class CreateColormap(object):
    r"""CreateColormap

    CreateColormap is a object.
    Responsibility:
    """
    def __init__(self, alloc, mid, window, visual):
        r"""

        @Arguments:
        - `alloc`:
        - `mid`:
        - `window`:
        - `visual`:
        """
        self._alloc = alloc
        self._mid = mid
        self._window = window
        self._visual = visual

    def get_alloc(self, ):
        r"""SUMMARY

        get_alloc()

        @Return:

        @Error:
        """
        return self._alloc

    def set_alloc(self, alloc):
        r"""SUMMARY

        set_alloc(alloc)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._alloc = alloc

    alloc = property(get_alloc, set_alloc)

    def get_mid(self, ):
        r"""SUMMARY

        get_mid()

        @Return:

        @Error:
        """
        return self._mid

    def set_mid(self, mid):
        r"""SUMMARY

        set_mid()

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._mid = mid

    mid = property(get_mid, set_mid)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._window

    def set_window(self, window):
        r"""SUMMARY

        set_window(window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._window = window

    window = property(get_window, set_window)

    def get_visual(self, ):
        r"""SUMMARY

        get_visual()

        @Return:

        @Error:
        """
        return self._visual

    def set_visual(self, visual):
        r"""SUMMARY

        set_visual(visual)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._visual = visual

    visual = property(get_visual, set_visual)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xIII', self.alloc, self.mid, self.window,
                        self.visual))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class FreeColormap(object):
    r"""FreeColormap

    FreeColormap is a object.
    Responsibility:
    """
    def __init__(self, cmap):
        r"""

        @Arguments:
        - `cmap`:
        """
        self._cmap = cmap

    def get_cmap(self, ):
        r"""SUMMARY

        get_cmap()

        @Return:

        @Error:
        """
        return self._cmap

    def set_cmap(self, cmap):
        r"""SUMMARY

        set_cmap(cmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._cmap = cmap

    cmap = property(get_cmap, set_cmap)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xI', self.cmap))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class CopyColormapAndFree(object):
    r"""CopyColormapAndFree

    CopyColormapAndFree is a object.
    Responsibility:
    """
    def __init__(self, mid, src_cmap):
        r"""

        @Arguments:
        - `mid`:
        - `src_cmap`:
        """
        self._mid = mid
        self._src_cmap = src_cmap

    def get_mid(self, ):
        r"""SUMMARY

        get_mid()

        @Return:

        @Error:
        """
        return self._mid

    def set_mid(self, mid):
        r"""SUMMARY

        set_mid(mid)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._mid = mid

    mid = property(get_mid, set_mid)

    def get_src_cmap(self, ):
        r"""SUMMARY

        get_src_cmap()

        @Return:

        @Error:
        """
        return self._src_cmap

    def set_src_cmap(self, src_cmap):
        r"""SUMMARY

        set_src_cmap(src_cmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._src_cmap = src_cmap

    src_cmap = property(get_src_cmap, set_src_cmap)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xII', self.mid, self.src_cmap))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class InstallColormap(FreeColormap):
    r"""InstallColormap

    InstallColormap is a FreeColormap.
    Responsibility:
    """


class UninstallColormap(FreeColormap):
    r"""UninstallColormap

    UninstallColormap is a FreeColormap.
    Responsibility:
    """


class ListInstalledColormaps(_Window):
    r"""ListInstalledColormaps

    ListInstalledColormaps is a _Window.
    Responsibility:
    """


class AllocColor(object):
    r"""AllocColor

    AllocColor is a object.
    Responsibility:
    """
    def __init__(self, cmap, red, green, blue):
        r"""

        @Arguments:
        - `cmap`:
        - `red`:
        - `green`:
        - `blue`:
        """
        self._cmap = cmap
        self._red = red
        self._green = green
        self._blue = blue

    def get_cmap(self, ):
        r"""SUMMARY

        get_cmap()

        @Return:

        @Error:
        """
        return self._cmap

    def set_cmap(self, cmap):
        r"""SUMMARY

        set_cmap(cmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._cmap = cmap

    cmap = property(get_cmap, set_cmap)

    def get_red(self, ):
        r"""SUMMARY

        get_red()

        @Return:

        @Error:
        """
        return self._red

    def set_red(self, red):
        r"""SUMMARY

        set_red(red)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._red = red

    red = property(get_red, set_red)

    def get_green(self, ):
        r"""SUMMARY

        get_green()

        @Return:

        @Error:
        """
        return self._green

    def set_green(self, green):
        r"""SUMMARY

        set_green(green)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._green = green

    green = property(get_green, set_green)

    def get_blue(self, ):
        r"""SUMMARY

        get_blue()

        @Return:

        @Error:
        """
        return self._blue

    def set_blue(self, blue):
        r"""SUMMARY

        set_blue(blue)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._blue = blue

    blue = property(get_blue, set_blue)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xIHHH2x', self.cmap, self.red, self.green,
                        self.blue))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class AllocNamedColor(object):
    r"""AllocNamedColor

    AllocNamedColor is a object.
    Responsibility:
    """
    def __init__(self, cmap, name_len, name):
        r"""

        @Arguments:
        - `cmap`:
        - `name_len`:
        - `name`:
        """
        self._cmap = cmap
        self._name_len = name_len
        self._name = name

    def get_cmap(self, ):
        r"""SUMMARY

        get_cmap()

        @Return:

        @Error:
        """
        return self._cmap

    def set_cmap(self, cmap):
        r"""SUMMARY

        set_cmap(cmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._cmap = cmap

    cmap = property(get_cmap, set_cmap)

    def get_name_len(self, ):
        r"""SUMMARY

        get_name_len()

        @Return:

        @Error:
        """
        return self._name_len

    def set_name_len(self, name_len):
        r"""SUMMARY

        set_name_len(name_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._name_len = name_len

    name_len = property(get_name_len, set_name_len)

    def get_name(self, ):
        r"""SUMMARY

        get_name()

        @Return:

        @Error:
        """
        return self._name

    def set_name(self, name):
        r"""SUMMARY

        set_name(name)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._name = name

    name = property(get_name, set_name)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xIH2x', self.cmap, self.name_len))
        buf.write(str(buffer(_array('b', self.name))))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class AllocColorCells(object):
    r"""AllocColorCells

    AllocColorCells is a object.
    Responsibility:
    """
    def __init__(self, contiguous, cmap, colors, planes):
        r"""

        @Arguments:
        - `contiguous`:
        - `cmap`:
        - `colors`:
        - `planes`:
        """
        self._contiguous = contiguous
        self._cmap = cmap
        self._colors = colors
        self._planes = planes

    def get_contiguous(self, ):
        r"""SUMMARY

        get_contiguous()

        @Return:

        @Error:
        """
        return self._contiguous

    def set_contiguous(self, contiguous):
        r"""SUMMARY

        set_contiguous(contiguous)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._contiguous = contiguous

    contiguous = property(get_contiguous, set_contiguous)

    def get_cmap(self, ):
        r"""SUMMARY

        get_cmap()

        @Return:

        @Error:
        """
        return self._cmap

    def set_cmap(self, cmap):
        r"""SUMMARY

        set_cmap(cmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._cmap = cmap

    cmap = property(get_cmap, set_cmap)

    def get_colors(self, ):
        r"""SUMMARY

        get_colors()

        @Return:

        @Error:
        """
        return self._colors

    def set_colors(self, colors):
        r"""SUMMARY

        set_colors(colors)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._colors = colors

    colors = property(get_colors, set_colors)

    def get_planes(self, ):
        r"""SUMMARY

        get_planes()

        @Return:

        @Error:
        """
        return self._planes

    def set_planes(self, planes):
        r"""SUMMARY

        set_planes(planes)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._planes = planes

    planes = property(get_planes, set_planes)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xIHH', self.contiguous, self.cmap,
                        self.colors, self.planes))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class AllocColorPlanes(object):
    r"""AllocColorPlanes

    AllocColorPlanes is a object.
    Responsibility:
    """
    def __init__(self, contiguous, cmap, colors, reds, greens, blues):
        r"""

        @Arguments:
        - `contiguous`:
        - `cmap`:
        - `colors`:
        - `reds`:
        - `greens`:
        - `blues`:
        """
        self._contiguous = contiguous
        self._cmap = cmap
        self._colors = colors
        self._reds = reds
        self._greens = greens
        self._blues = blues

    def get_contiguous(self, ):
        r"""SUMMARY

        get_cointiguous()

        @Return:

        @Error:
        """
        return self._contiguous

    def set_contiguous(self, contiguous):
        r"""SUMMARY

        set_cointiguous(contiguous)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._contiguous = contiguous

    contiguous = property(get_contiguous, set_contiguous)

    def get_cmap(self, ):
        r"""SUMMARY

        get_cmap()

        @Return:

        @Error:
        """
        return self._cmap

    def set_cmap(self, cmap):
        r"""SUMMARY

        set_cmap(cmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._cmap = cmap

    cmap = property(get_cmap, set_cmap)

    def get_colors(self, ):
        r"""SUMMARY

        get_colors()

        @Return:

        @Error:
        """
        return self._colors

    def set_colors(self, colors):
        r"""SUMMARY

        set_colors(colors)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._colors = colors

    colors = property(get_colors, set_colors)

    def get_reds(self, ):
        r"""SUMMARY

        get_reds()

        @Return:

        @Error:
        """
        return self._reds

    def set_reds(self, reds):
        r"""SUMMARY

        set_reds(reds)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._reds = reds

    reds = property(get_reds, set_reds)

    def get_greens(self, ):
        r"""SUMMARY

        get_greens()

        @Return:

        @Error:
        """
        return self._greens

    def set_greens(self, greens):
        r"""SUMMARY

        set_greens(greens)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._greens = greens

    greens = property(get_greens, set_greens)

    def get_blues(self, ):
        r"""SUMMARY

        get_blues()

        @Return:

        @Error:
        """
        return self._blues

    def set_blues(self, blues):
        r"""SUMMARY

        set_blues(blues)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._blues = blues

    blues = property(get_blues, set_blues)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xIHHHH', self.contiguous, self.cmap, self.colors,
                        self.reds, self.greens, self.blues))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class FreeColors(object):
    r"""FreeColors

    FreeColors is a object.
    Responsibility:
    """
    def __init__(self, cmap, plane_mask, pixels_len, pixels):
        r"""

        @Arguments:
        - `cmap`:
        - `plane_mask`:
        - `pixels_len`:
        - `pixels`:
        """
        self._cmap = cmap
        self._plane_mask = plane_mask
        self._pixels_len = pixels_len
        self._pixels = pixels

    def get_cmap(self, ):
        r"""SUMMARY

        get_cmap()

        @Return:

        @Error:
        """
        return self._cmap

    def set_cmap(self, cmap):
        r"""SUMMARY

        set_cmap(cmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._cmap = cmap

    cmap = property(get_cmap, set_cmap)

    def get_plane_mask(self, ):
        r"""SUMMARY

        get_plane_mask()

        @Return:

        @Error:
        """
        return self._plane_mask

    def set_plane_mask(self, plane_mask):
        r"""SUMMARY

        set_plane_mask(plane_mask)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._plane_mask = plane_mask

    plane_mask = property(get_plane_mask, set_plane_mask)

    def get_pixels_len(self, ):
        r"""SUMMARY

        get_pixels_len()

        @Return:

        @Error:
        """
        return self._pixels_len

    def set_pixels_len(self, pixels_len):
        r"""SUMMARY

        set_pixels_len(pixels_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._pixels_len = pixels_len

    pixels_len = property(get_pixels_len, set_pixels_len)

    def get_pixels(self, ):
        r"""SUMMARY

        get_pixels()

        @Return:

        @Error:
        """
        return self._pixels

    def set_pixels(self, pixels):
        r"""SUMMARY

        set_pixels(pixels)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._pixels = pixels

    pixels = property(get_pixels, set_pixels)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xII', slfe.cmap, self.plane_mask))
        buf.write(str(buffer(_array('I', self.pixels))))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class StoreColors(object):
    r"""StoreColors

    StoreColors is a object.
    Responsibility:
    """
    def __init__(self, cmap, items_len, items):
        r"""

        @Arguments:
        - `cmap`:
        - `items_len`:
        - `items`:
        """
        self._cmap = cmap
        self._items_len = items_len
        self._items = items

    def get_cmap(self, ):
        r"""SUMMARY

        get_cmap()

        @Return:

        @Error:
        """
        return self._cmap

    def set_cmap(self, cmap):
        r"""SUMMARY

        set_cmap(cmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._cmap = cmap

    cmap = property(get_cmap, set_cmap)

    def get_items_len(self, ):
        r"""SUMMARY

        get_items_len()

        @Return:

        @Error:
        """
        return self._items_len

    def set_items_len(self, items_len):
        r"""SUMMARY

        set_items_len(items_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._items_len = items_len

    items_len = property(get_items_len, set_items_len)

    def get_items(self, ):
        r"""SUMMARY

        get_items()

        @Return:

        @Error:
        """
        return self._items

    def set_items(self, items):
        r"""SUMMARY

        set_items(items)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._items = items

    items = property(get_items, set_items)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xI', self.cmap))
        for elt in xcb.Iterator(self.items, 5, 'items', True):
            buf.write(_pack('=IHHHBx', *elt))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class StoreNamedColor(object):
    r"""StoreNamedColor

    StoreNamedColor is a object.
    Responsibility:
    """
    def __init__(self, flags, cmap, pixel, name_len, name):
        r"""

        @Arguments:
        - `flags`:
        - `cmap`:
        - `pixel`:
        - `name_len`:
        - `name`:
        """
        self._flags = flags
        self._cmap = cmap
        self._pixel = pixel
        self._name_len = name_len
        self._name = name

    def get_flags(self, ):
        r"""SUMMARY

        get_flags()

        @Return:

        @Error:
        """
        return self._flags

    def set_flags(self, flags):
        r"""SUMMARY

        set_flags(flags)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._flags = flags

    flags = property(get_flags, set_flags)

    def get_cmap(self, ):
        r"""SUMMARY

        get_cmap()

        @Return:

        @Error:
        """
        return self._cmap

    def set_cmap(self, cmap):
        r"""SUMMARY

        set_cmap(cmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._cmap = cmap

    cmap = property(get_cmap, set_cmap)

    def get_pixel(self, ):
        r"""SUMMARY

        get_pixel()

        @Return:

        @Error:
        """
        return self._pixel

    def set_pixel(self, pixel):
        r"""SUMMARY

        set_pixel(pixel)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._pixel = pixel

    pixel = property(get_pixel, set_pixel)

    def get_name_len(self, ):
        r"""SUMMARY

        get_name_len()

        @Return:

        @Error:
        """
        return self._name_len

    def set_name_len(self, name_len):
        r"""SUMMARY

        set_name_len(name_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._name_len = name_len

    name_len = property(get_name_len, set_name_len)

    def get_name(self, ):
        r"""SUMMARY

        get_name()

        @Return:

        @Error:
        """
        return self._name

    def set_name(self, name):
        r"""SUMMARY

        set_name(name)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._name = name

    name = property(get_name, set_name)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xIIH2x', self.flags, self.cmap, self.pixel,
                        self.name_len))
        buf.write(str(buffer(_array('b', self.name))))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class QueryColors(object):
    r"""QueryColors

    QueryColors is a object.
    Responsibility:
    """
    def __init__(self, cmap, pixels_len, pixels):
        r"""

        @Arguments:
        - `cmap`:
        - `pixels_len`:
        - `pixels`:
        """
        self._cmap = cmap
        self._pixels_len = pixels_len
        self._pixels = pixels

    def get_cmap(self, ):
        r"""SUMMARY

        get_cmap()

        @Return:

        @Error:
        """
        return self._cmap

    def set_cmap(self, cmap):
        r"""SUMMARY

        set_cmap(cmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._cmap = cmap

    cmap = property(get_cmap, set_cmap)

    def get_pixels_len(self, ):
        r"""SUMMARY

        get_pixels_len()

        @Return:

        @Error:
        """
        return self._pixels_len

    def set_pixels_len(self, pixels_len):
        r"""SUMMARY

        set_pixels_len(pixels_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._pixels_len = pixels_len

    pixels_len = property(get_pixels_len, set_pixels_len)

    def get_pixels(self, ):
        r"""SUMMARY

        get_pixels()

        @Return:

        @Error:
        """
        return self._pixels

    def set_pixels(self, pixels):
        r"""SUMMARY

        set_pixels(pixels)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._pixels = pixels

    pixels = property(get_pixels, set_pixels)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xI', self.cmap))
        buf.write(str(buffer(_array('I', self.pixels))))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class LookupColor(object):
    r"""LookupColor

    LookupColor is a object.
    Responsibility:
    """
    def __init__(self, cmap, name_len, name):
        r"""

        @Arguments:
        - `cmap`:
        - `name_len`:
        - `name`:
        """
        self._cmap = cmap
        self._name_len = name_len
        self._name = name

    def get_cmap(self, ):
        r"""SUMMARY

        get_cmap()

        @Return:

        @Error:
        """
        return self._cmap

    def set_cmap(self, cmap):
        r"""SUMMARY

        set_cmap(cmap)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._cmap = cmap

    cmap = property(get_cmap, set_cmap)

    def get_name_len(self, ):
        r"""SUMMARY

        get_name_len()

        @Return:

        @Error:
        """
        return self._name_len

    def set_name_len(self, name_len):
        r"""SUMMARY

        set_name_len(name_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._name_len = name_len

    name_len = property(get_name_len, set_name_len)

    def get_name(self, ):
        r"""SUMMARY

        get_name()

        @Return:

        @Error:
        """
        return self._name

    def set_name(self, name):
        r"""SUMMARY

        set_name(name)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._name = name

    name = property(get_name, set_name)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xIH2x', self.cmap, self.name_len))
        buf.write(str(buffer(_array('b', self.name))))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class CreateCursor(object):
    r"""CreateCursor

    CreateCursor is a object.
    Responsibility:
    """
    def __init__(self, cid, source, mask, fore_red, fore_green,
                 fore_blue, back_red, back_green, back_blue, x, y):
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
        """
        self._cid = cid
        self._source = source
        self._mask = mask
        self._fore_red = fore_red
        self._fore_green = fore_green
        self._fore_blue = fore_blue
        self._back_red = back_red
        self._back_green = back_green
        self._back_blue = back_blue
        self._point = _point.Point(x, y)

    def get_cid(self, ):
        r"""SUMMARY

        get_cid()

        @Return:

        @Error:
        """
        return self._cid

    def set_cid(self, cid):
        r"""SUMMARY

        set_cid(cid)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._cid = cid

    cid = property(get_cid, set_cid)

    def get_source(self, ):
        r"""SUMMARY

        get_source()

        @Return:

        @Error:
        """
        return self._source

    def set_source(self, source):
        r"""SUMMARY

        set_source(source)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._source = source

    source = property(get_source, set_source)

    def get_mask(self, ):
        r"""SUMMARY

        get_mask()

        @Return:

        @Error:
        """
        return self._mask

    def set_mask(self, mask):
        r"""SUMMARY

        set_mask(mask)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._mask = mask

    mask = property(get_mask, set_mask)

    def get_fore_red(self, ):
        r"""SUMMARY

        get_fore_red()

        @Return:

        @Error:
        """
        return self._fore_red

    def set_fore_red(self, fore_red):
        r"""SUMMARY

        set_fore_red(fore_red)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._fore_red = fore_red

    fore_red = property(get_fore_red, set_fore_red)

    def get_fore_green(self, ):
        r"""SUMMARY

        get_fore_green()

        @Return:

        @Error:
        """
        return self._fore_green

    def set_fore_green(self, fore_green):
        r"""SUMMARY

        set_fore_green(fore_green)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._fore_green = fore_green

    fore_green = property(get_fore_green, set_fore_green)

    def get_fore_blue(self, ):
        r"""SUMMARY

        get_fore_blue()

        @Return:

        @Error:
        """
        return self._fore_blue

    def set_fore_blue(self, fore_blue):
        r"""SUMMARY

        set_fore_blue(fore_blue)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._fore_blue = fore_blue

    fore_blue = property(get_fore_blue, set_fore_blue)

    def get_back_red(self, ):
        r"""SUMMARY

        get_back_red()

        @Return:

        @Error:
        """
        return self._back_red

    def set_back_red(self, back_red):
        r"""SUMMARY

        set_back_red(back_red)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._back_red = back_red

    back_red = property(get_back_red, set_back_red)

    def get_back_green(self, ):
        r"""SUMMARY

        get_back_green()

        @Return:

        @Error:
        """
        return self._back_green

    def set_back_green(self, back_green):
        r"""SUMMARY

        set_back_green(back_green)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._back_green = back_green

    back_green = property(get_back_green, set_back_green)

    def get_back_blue(self, ):
        r"""SUMMARY

        get_back_blue()

        @Return:

        @Error:
        """
        return self._back_blue

    def set_back_blue(self, back_blue):
        r"""SUMMARY

        set_back_blue(back_blue)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._back_blue = back_blue

    back_blue = property(get_back_blue, set_back_blue)

    def get_x(self, ):
        r"""SUMMARY

        get_x()

        @Return:

        @Error:
        """
        return self._point.get_x()

    def set_x(self, newx):
        r"""SUMMARY

        set_x(newx)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._point.set_x(newx)

    x = property(get_x, set_x)

    def get_y(self, ):
        r"""SUMMARY

        get_y()

        @Return:

        @Error:
        """
        return self._point.get_y()

    def set_y(self, newy):
        r"""SUMMARY

        set_y(newy)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._point.set_y(newy)

    y = property(get_y, set_y)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xIIIHHHHHHHH', self.cid, self.source, self.mask,
                        self.fore_red, self.fore_green, self.fore_blue,
                        self.back_red, self.back_green, self.back_blue,
                        self.x, self.y))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class CreateGlyphCursor(object):
    r"""CreateGlyphCursor

    CreateGlyphCursor is a object.
    Responsibility:
    """
    def __init__(self, cid, source_font, mask_font, source_char, mask_char,
                 fore_red, fore_green, fore_blue, back_red, back_green,
                 back_blue):
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
        """
        self._cid = cid
        self._source_font = source_font
        self._mask_font = mask_font
        self._source_char = source_char
        self._mask_char = mask_char
        self._fore_red = fore_red
        self._fore_green = fore_green
        self._fore_blue = fore_blue
        self._back_red = back_red
        self._back_green = back_green
        self._back_blue = back_blue

    def get_cid(self, ):
        r"""SUMMARY

        get_cid()

        @Return:

        @Error:
        """
        return self._cid

    def set_cid(self, cid):
        r"""SUMMARY

        set_cid(cid)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._cid = cid

    cid = property(get_cid, set_cid)

    def get_source_font(self, ):
        r"""SUMMARY

        get_source_font()

        @Return:

        @Error:
        """
        return self._source_font

    def set_source_font(self, source_font):
        r"""SUMMARY

        set_source_font(source_font)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._source_font = source_font

    source_font = property(get_source_font, set_source_font)

    def get_mask_font(self, ):
        r"""SUMMARY

        get_mask_font()

        @Return:

        @Error:
        """
        return self._mask_font

    def set_mask_font(self, mask_font):
        r"""SUMMARY

        set_mask_font(mask_font)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._mask_font = mask_font

    mask_font = property(get_mask_font, set_mask_font)

    def get_source_char(self, ):
        r"""SUMMARY

        get_source_char()

        @Return:

        @Error:
        """
        return self._source_char

    def set_source_char(self, source_char):
        r"""SUMMARY

        set_source_char(source_char)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._source_char = source_char

    source_char = property(get_source_char, set_source_char)

    def get_mask_char(self, ):
        r"""SUMMARY

        get_mask_char()

        @Return:

        @Error:
        """
        return self._mask_char

    def set_mask_char(self, mask_char):
        r"""SUMMARY

        set_mask_char(mask_char)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._mask_char = mask_char

    mask_char = property(get_mask_char, set_mask_char)

    def get_fore_red(self, ):
        r"""SUMMARY

        get_fore_red()

        @Return:

        @Error:
        """
        return self._fore_red

    def set_fore_red(self, fore_red):
        r"""SUMMARY

        set_fore_red(fore_red)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._fore_red = fore_red

    fore_red = property(get_fore_red, set_fore_red)

    def get_fore_green(self, ):
        r"""SUMMARY

        get_fore_green()

        @Return:

        @Error:
        """
        return self._fore_green

    def set_fore_green(self, fore_green):
        r"""SUMMARY

        set_fore_green(fore_green)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._fore_green = fore_green

    fore_green = property(get_fore_green, set_fore_green)

    def get_fore_blue(self, ):
        r"""SUMMARY

        get_fore_blue()

        @Return:

        @Error:
        """
        return self._fore_blue

    def set_fore_blue(self, fore_blue):
        r"""SUMMARY

        set_fore_blue(fore_blue)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._fore_blue = fore_blue

    fore_blue = property(get_fore_blue, set_fore_blue)

    def get_back_red(self, ):
        r"""SUMMARY

        get_back_red()

        @Return:

        @Error:
        """
        return self._back_red

    def set_back_red(self, back_red):
        r"""SUMMARY

        set_back_red(back_red)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._back_red = back_red

    back_red = property(get_back_red, set_back_red)

    def get_back_green(self, ):
        r"""SUMMARY

        get_back_green()

        @Return:

        @Error:
        """
        return self._back_green

    def set_back_green(self, back_green):
        r"""SUMMARY

        set_back_green(back_green)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._back_green = back_green

    back_green = property(get_back_green, set_back_green)

    def get_back_blue(self, ):
        r"""SUMMARY

        get_back_blue()

        @Return:

        @Error:
        """
        return self._back_blue

    def set_back_blue(self, back_blue):
        r"""SUMMARY

        set_back_blue(back_blue)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._back_blue = back_blue

    back_blue = property(get_back_blue, set_back_blue)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xIIIHHHHHHHH', self.cid, self.source_font,
                        self.mask_font, self.source_char, self.mask_char,
                        self.fore_red, self.fore_green, self.fore_blue,
                        self.back_red, self.back_green, self.back_blue))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class FreeCursor(object):
    r"""FreeCursor

    FreeCursor is a object.
    Responsibility:
    """
    def __init__(self, cursor):
        r"""

        @Arguments:
        - `cursor`:
        """
        self._cursor = cursor

    def get_cursor(self, ):
        r"""SUMMARY

        get_cursor()

        @Return:

        @Error:
        """
        return self._cursor

    def set_cursor(self, cursor):
        r"""SUMMARY

        set_cursor(cursor)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._cursor = cursor

    cursor = property(get_cursor, set_cursor)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xI', self.cursor))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class RecolorCursor(object):
    r"""RecolorCursor

    RecolorCursor is a object.
    Responsibility:
    """
    def __init__(self, cursor, fore_red, fore_green, fore_blue,
                 back_red, back_green, back_blue):
        r"""

        @Arguments:
        - `cursor`:
        - `fore_red`:
        - `fore_green`:
        - `fore_blue`:
        - `back_red`:
        - `back_green`:
        - `back_blue`:
        """
        self._cursor = cursor
        self._fore_red = fore_red
        self._fore_green = fore_green
        self._fore_blue = fore_blue
        self._back_red = back_red
        self._back_green = back_green
        self._back_blue = back_blue

    def get_cursor(self, ):
        r"""SUMMARY

        get_cursor()

        @Return:

        @Error:
        """
        return self._cursor

    def set_cursor(self, cursor):
        r"""SUMMARY

        set_cursor(cursor)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._cursor = cursor

    cursor = property(get_cursor, set_cursor)

    def get_fore_red(self, ):
        r"""SUMMARY

        get_fore_red()

        @Return:

        @Error:
        """
        return self._fore_red

    def set_fore_red(self, fore_red):
        r"""SUMMARY

        set_fore_red(fore_red)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._fore_red = fore_red

    fore_red = property(get_fore_red, set_fore_red)

    def get_fore_green(self, ):
        r"""SUMMARY

        get_fore_green()

        @Return:

        @Error:
        """
        return self._fore_green

    def set_fore_green(self, fore_green):
        r"""SUMMARY

        set_fore_green(fore_green)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._fore_green = fore_green

    fore_green = property(get_fore_green, set_fore_green)

    def get_fore_blue(self, ):
        r"""SUMMARY

        get_fore_blue()

        @Return:

        @Error:
        """
        return self._fore_blue

    def set_fore_blue(self, fore_blue):
        r"""SUMMARY

        set_fore_blue(fore_blue)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._fore_blue = fore_blue

    fore_blue = property(get_fore_blue, set_fore_blue)

    def get_back_red(self, ):
        r"""SUMMARY

        get_back_red()

        @Return:

        @Error:
        """
        return self._back_red

    def set_back_red(self, back_red):
        r"""SUMMARY

        set_back_red(back_red)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._back_red = back_red

    back_red = property(get_back_red, set_back_red)

    def get_back_green(self, ):
        r"""SUMMARY

        get_back_green()

        @Return:

        @Error:
        """
        return self._back_green

    def set_back_green(self, back_green):
        r"""SUMMARY

        set_back_green(back_green)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._back_green = back_green

    back_green = property(get_back_green, set_back_green)

    def get_back_blue(self, ):
        r"""SUMMARY

        get_back_blue()

        @Return:

        @Error:
        """
        return self._back_blue

    def set_back_blue(self, back_blue):
        r"""SUMMARY

        set_back_blue(back_blue)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._back_blue = back_blue

    back_blue = property(get_back_blue, set_back_blue)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xIHHHHHH', self.cursor, self.fore_red,
                        self.fore_green, self.fore_blue, self.back_red,
                        self.back_green, self.back_blue))
        return buf.getvaue()

    def __str__(self):
        return self.get_buffer()


class QueryBestSize(object):
    r"""QueryBestSize

    QueryBestSize is a object.
    Responsibility:
    """
    def __init__(self, _class, drawable, width, height):
        r"""

        @Arguments:
        - `_class`:
        - `drawable`:
        - `width`:
        - `height`:
        """
        self._class = _class
        self._drawable = drawable
        self._dimension = _dimension.Dimension(width, height)

    def get_class(self, ):
        r"""SUMMARY

        get_class()

        @Return:

        @Error:
        """
        return self._class

    def set_class(self, class_):
        r"""SUMMARY

        set_class(class_)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._class = class_

    class_ = property(get_class, set_class)

    def get_drawable(self, ):
        r"""SUMMARY

        get_drawable()

        @Return:

        @Error:
        """
        return self._drawable

    def set_drawable(self, drawable):
        r"""SUMMARY

        set_drawable(drawable)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._drawable = drawable

    drawable = property(get_drawable, set_drawable)

    def get_width(self, ):
        r"""SUMMARY

        get_width()

        @Return:

        @Error:
        """
        return self._dimension.get_width()

    def set_width(self, width):
        r"""SUMMARY

        set_width(width)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._dimension.set_width(width)

    width = property(get_width, set_width)

    def get_height(self, ):
        r"""SUMMARY

        get_height()

        @Return:

        @Error:
        """
        return self._dimension.get_height()

    def set_height(self, height):
        r"""SUMMARY

        set_height(height)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._dimension.set_height(height)

    height = property(get_height, set_height)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xIHH', self._class, self.drawable, self.width,
                        self.height))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class QueryExtension(object):
    r"""QueryExtension

    QueryExtension is a object.
    Responsibility:
    """
    def __init__(self, name_len, name):
        r"""

        @Arguments:
        - `name_len`:
        - `name`:
        """
        self._name_len = name_len
        self._name = name

    def get_name_len(self, ):
        r"""SUMMARY

        get_name_len()

        @Return:

        @Error:
        """
        return self._name_len

    def set_name_len(self, name_len):
        r"""SUMMARY

        set_name_len(name_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._name_len = name_len

    name_len = property(get_name_len, set_name_len)

    def get_name(self, ):
        r"""SUMMARY

        get_name()

        @Return:

        @Error:
        """
        return self._name

    def set_name(self, name):
        r"""SUMMARY

        set_name(name)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._name = name

    name = property(get_name, set_name)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xH2x', self.name_len))
        buf.write(str(buffer(_array('b', self.name))))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class ListExtensions(object):
    r"""ListExtensions

    ListExtensions is a object.
    Responsibility:
    """
    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class ChangeKeyboardMapping(object):
    r"""ChangeKeyboardMapping

    ChangeKeyboardMapping is a object.
    Responsibility:
    """
    def __init__(self, keycode_count, first_keycode, keysyms_per_keycode,
                 keysyms):
        r"""

        @Arguments:
        - `keycode_count`:
        - `first_keycode`:
        - `keysyms_per_keycode`:
        - `keysyms`:
        """
        self._keycode_count = keycode_count
        self._first_keycode = first_keycode
        self._keysyms_per_keycode = keysyms_per_keycode
        self._keysyms = keysyms

    def get_keycode_count(self, ):
        r"""SUMMARY

        get_keycode_count()

        @Return:

        @Error:
        """
        return self._keycode_count

    def set_keycode_count(self, keycode_count):
        r"""SUMMARY

        set_keycode_count(keycode_count)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._keycode_count = keycode_count

    keycode_count = property(get_keycode_count, set_keycode_count)

    def get_first_keycode(self, ):
        r"""SUMMARY

        get_first_keycode()

        @Return:

        @Error:
        """
        return self._first_keycode

    def set_first_keycode(self, first_keycode):
        r"""SUMMARY

        set_first_keycode(first_keycode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._first_keycode = first_keycode

    first_keycode = property(get_first_keycode, set_first_keycode)

    def get_keysyms_per_keycode(self, ):
        r"""SUMMARY

        get_keysyms_per_keycode()

        @Return:

        @Error:
        """
        return self._keysyms_per_keycode

    def set_keysyms_per_keycode(self, keysym_per_keycode):
        r"""SUMMARY

        set_keysyms_per_keycode(keysym_per_keycode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._keysyms_per_keycode = keysym_per_keycode

    keysyms_per_keycode = property(
        get_keysyms_per_keycode, set_keysyms_per_keycode)

    def get_keysyms(self, ):
        r"""SUMMARY

        get_keysyms()

        @Return:

        @Error:
        """
        return self._keysyms

    def set_keysyms(self, keysyms):
        r"""SUMMARY

        set_keysyms(keysyms)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._keysyms = keysyms

    keysyms = property(get_keysyms, set_keysyms)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xBB2x', self.keycode_count, self.first_keycode,
                        self.keysyms_per_keycode))
        buf.write(str(buffer(_array('I', self.keysyms))))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class GetKeyboardMapping(object):
    r"""GetKeyboardMapping

    GetKeyboardMapping is a object.
    Responsibility:
    """
    def __init__(self, first_keycode, count):
        r"""

        @Arguments:
        - `first_keycode`:
        - `count`:
        """
        self._first_keycode = first_keycode
        self._count = count

    def get_first_keycode(self, ):
        r"""SUMMARY

        get_first_keycode()

        @Return:

        @Error:
        """
        return self._first_keycode

    def set_first_keycode(self, first_keycode):
        r"""SUMMARY

        set_first_keycode(first_keycode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._first_keycode = first_keycode

    first_keycode = property(get_first_keycode, set_first_keycode)

    def get_count(self, ):
        r"""SUMMARY

        get_count()

        @Return:

        @Error:
        """
        return self._count

    def set_count(self, count):
        r"""SUMMARY

        set_count(count)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._count = count

    count = property(get_count, set_count)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xBB', self.first_keycode, self.count))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class ChangeKeyboardControl(object):
    r"""ChangeKeyboardControl

    ChangeKeyboardControl is a object.
    Responsibility:
    """
    def __init__(self, value_mask, value_list):
        r"""

        @Arguments:
        - `value_mask`:
        - `value_list`:
        """
        self._value_mask = value_mask
        self._value_list = value_list

    def get_value_mask(self, ):
        r"""SUMMARY

        get_value_mask()

        @Return:

        @Error:
        """
        return self._value_mask

    def set_value_mask(self, value_mask):
        r"""SUMMARY

        set_value_mask(value_mask)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._value_mask = value_mask

    value_mask = property(get_value_mask, set_value_mask)

    def get_value_list(self, ):
        r"""SUMMARY

        get_value_list()

        @Return:

        @Error:
        """
        return self._value_list

    def set_value_list(self, value_list):
        r"""SUMMARY

        set_value_list(value_list)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._value_list = value_list

    value_list = property(get_value_list, set_value_list)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xI', self.value_mask))
        buf.write(str(buffer(_array('I', self.value_list))))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class GetKeyboardControl(object):
    r"""GetKeyboardControl

    GetKeyboardControl is a object.
    Responsibility:
    """
    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class Bell(object):
    r"""Bell

    Bell is a object.
    Responsibility:
    """
    def __init__(self, percent):
        r"""

        @Arguments:
        - `percent`:
        """
        self._percent = percent

    def get_percent(self, ):
        r"""SUMMARY

        get_percent()

        @Return:

        @Error:
        """
        return self._percent

    def set_percent(self, percent):
        r"""SUMMARY

        set_percent(percent)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._percent = percent

    percent = property(get_percent, set_percent)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xb2x', self.percent))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class ChangePointerControl(object):
    r"""ChangePointerControl

    ChangePointerControl is a object.
    Responsibility:
    """
    def __init__(self, acceleration_numerator, acceleration_denominator,
                 threshold, do_acceleration, do_threshold):
        r"""

        @Arguments:
        - `acceleration_numerator`:
        - `acceleration_denominator`:
        - `threshold`:
        - `do_acceleration`:
        - `do_threshold`:
        """
        self._acceleration_numerator = acceleration_numerator
        self._acceleration_denominator = acceleration_denominator
        self._threshold = threshold
        self._do_acceleration = do_acceleration
        self._do_threshold = do_threshold

    def get_acceleration_numerator(self, ):
        r"""SUMMARY

        get_acceleration_numerator()

        @Return:

        @Error:
        """
        return self._acceleration_numerator

    def set_acceleration_numerator(self, acceleration_numerator):
        r"""SUMMARY

        set_acceleration_numerator(acceleration_numerator)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._acceleration_numerator = acceleration_numerator

    acceleration_numerator = property(
        get_acceleration_numerator, set_acceleration_numerator)

    def get_acceleration_denominator(self, ):
        r"""SUMMARY

        get_acceleration_denominator()

        @Return:

        @Error:
        """
        return self._acceleration_denominator

    def set_acceleration_denominator(self, acceleration_denominator):
        r"""SUMMARY

        set_acceleration_denominator(acceleration_denominator)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._acceleration_denominator = acceleration_denominator

    acceleration_denominator = property(
        get_acceleration_denominator, set_acceleration_denominator)

    def get_threshold(self, ):
        r"""SUMMARY

        get_threshold()

        @Return:

        @Error:
        """
        return self._threshold

    def set_threshold(self, threshold):
        r"""SUMMARY

        set_threshold(threshold)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._threshold = threshold

    threshold = property(get_threshold, set_threshold)

    def get_do_acceleration(self, ):
        r"""SUMMARY

        get_do_acceleration()

        @Return:

        @Error:
        """
        return self._do_acceleration

    def set_do_acceleration(self, do_acceleration):
        r"""SUMMARY

        set_do_acceleration(do_acceleration)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._do_acceleration = do_acceleration

    do_acceleration = property(get_do_acceleration, set_do_acceleration)

    def get_do_threshold(self, ):
        r"""SUMMARY

        get_do_threshold()

        @Return:

        @Error:
        """
        return self._do_threshold

    def set_do_threshold(self, do_threshold):
        r"""SUMMARY

        set_do_threshold(do_threshold)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._do_threshold = do_threshold

    do_threshold = property(get_do_threshold, set_do_threshold)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xhhhBB', self.acceleration_numerator,
                        self.acceleration_denominator, self.threshold,
                        self.do_acceleration, self.do_threshold))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class GetPointerControl(object):
    r"""GetPointerControl

    GetPointerControl is a object.
    Responsibility:
    """
    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class SetScreenSaver(object):
    r"""SetScreenSaver

    SetScreenSaver is a object.
    Responsibility:
    """
    def __init__(self, timeout, interval, prefer_blanking, allow_exposures):
        r"""

        @Arguments:
        - `timeout`:
        - `interval`:
        - `prefer_blanking`:
        - `allow_exposures`:
        """
        self._timeout = timeout
        self._interval = interval
        self._prefer_blanking = prefer_blanking
        self._allow_exposures = allow_exposures

    def get_timeout(self, ):
        r"""SUMMARY

        get_timeout()

        @Return:

        @Error:
        """
        return self._timeout

    def set_timeout(self, timeout):
        r"""SUMMARY

        set_timeout(timeout)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._timeout = timeout

    timeout = property(get_timeout, set_timeout)

    def get_interval(self, ):
        r"""SUMMARY

        get_interval()

        @Return:

        @Error:
        """
        return self._interval

    def set_interval(self, interval):
        r"""SUMMARY

        set_interval(interval)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._interval = interval

    interval = property(get_interval, set_interval)

    def get_prefer_blanking(self, ):
        r"""SUMMARY

        get_prefer_blanking()

        @Return:

        @Error:
        """
        return self._prefer_blanking

    def set_prefer_blanking(self, prefer_blanking):
        r"""SUMMARY

        set_prefer_blanking(prefer_blanking)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._prefer_blanking = prefer_blanking

    prefer_blanking = property(get_prefer_blanking, set_prefer_blanking)

    def get_allow_exposures(self, ):
        r"""SUMMARY

        get_allow_exposures()

        @Return:

        @Error:
        """
        return self._allow_exposures

    def set_allow_exposures(self, allow_exposures):
        r"""SUMMARY

        set_allow_exposures(allow_exposures)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._allow_exposures = allow_exposures

    allow_exposures = property(get_allow_exposures, set_allow_exposures)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xhhBB', self.timeout, self.interval,
                        self.prefer_blanking, self.allow_exposures))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class GetScreenSaver(object):
    r"""GetScreenSaver

    GetScreenSaver is a object.
    Responsibility:
    """
    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class ChangeHosts(object):
    r"""ChangeHosts

    ChangeHosts is a object.
    Responsibility:
    """
    def __init__(self, mode, family, address_len, address):
        r"""

        @Arguments:
        - `mode`:
        - `family`:
        - `address_len`:
        - `address`:
        """
        self._mode = mode
        self._family = family
        self._address_len = address_len
        self._address = address

    def get_mode(self, ):
        r"""SUMMARY

        get_mode()

        @Return:

        @Error:
        """
        return self._mode

    def set_mode(self, mode):
        r"""SUMMARY

        set_mode(mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._mode = mode

    mode = property(get_mode, set_mode)

    def get_family(self, ):
        r"""SUMMARY

        get_family()

        @Return:

        @Error:
        """
        return self._family

    def set_family(self, family):
        r"""SUMMARY

        set_family(family)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._family = family

    family = property(get_family, set_family)

    def get_address_len(self, ):
        r"""SUMMARY

        get_address_len()

        @Return:

        @Error:
        """
        return self._address_len

    def set_address_len(self, address_len):
        r"""SUMMARY

        set_address_len(address_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._address_len = address_len

    address_len = property(get_address_len, set_address_len)

    def get_address(self, ):
        r"""SUMMARY

        get_address()

        @Return:

        @Error:
        """
        return self._address

    def set_address(self, address):
        r"""SUMMARY

        set_address(address)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._address = address

    address = property(get_address, set_address)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xBxH', self.mode, self.family, self.address_len))
        buf.write(str(buffer(_array('B', self.address))))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class ListHosts(object):
    r"""ListHosts

    ListHosts is a object.
    Responsibility:
    """
    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()



class SetAccessControl(object):
    r"""SetAccessControl

    SetAccessControl is a object.
    Responsibility:
    """
    def __init__(self, mode):
        r"""

        @Arguments:
        - `mode`:
        """
        self._mode = mode

    def get_mode(self, ):
        r"""SUMMARY

        get_mode()

        @Return:

        @Error:
        """
        return self._mode

    def set_mode(self, mode):
        r"""SUMMARY

        set_mode(mode)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._mode = mode

    mode = property(get_mode, set_mode)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2x', self.mode))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class SetCloseDownMode(SetAccessControl):
    r"""SetCloseDownMode

    SetCloseDownMode is a SetAccessControl.
    Responsibility:
    """


class KillClient(object):
    r"""KillClient

    KillClient is a object.
    Responsibility:
    """
    def __init__(self, resource):
        r"""

        @Arguments:
        - `resource`:
        """
        self._resource = resource

    def get_resource(self, ):
        r"""SUMMARY

        get_resource()

        @Return:

        @Error:
        """
        return self._resource

    def set_resource(self, resource):
        r"""SUMMARY

        set_resource(resource)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._resource = resource

    resource = property(get_resource, set_resource)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xI', self.resource))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class RotateProperties(object):
    r"""RotateProperties

    RotateProperties is a object.
    Responsibility:
    """
    def __init__(self, window, atoms_len, delta, atoms):
        r"""

        @Arguments:
        - `window`:
        - `atoms_len`:
        - `delta`:
        - `atoms`:
        """
        self._window = window
        self._atoms_len = atoms_len
        self._delta = delta
        self._atoms = atoms

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._window

    def set_window(self, window):
        r"""SUMMARY

        set_window(window)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._window = window

    window = property(get_window, set_window)

    def get_atoms_len(self, ):
        r"""SUMMARY

        get_atoms_len()

        @Return:

        @Error:
        """
        return self._atoms_len

    def set_atoms_len(self, atoms_len):
        r"""SUMMARY

        set_atoms_len(atoms_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._atoms_len = atoms_len

    atoms_len = property(get_atoms_len, set_atoms_len)

    def get_delta(self, ):
        r"""SUMMARY

        get_delta()

        @Return:

        @Error:
        """
        return self._delta

    def set_delta(self, delta):
        r"""SUMMARY

        set_delta(delta)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._delta = delta

    delta = property(get_delta, set_delta)

    def get_atoms(self, ):
        r"""SUMMARY

        get_atoms()

        @Return:

        @Error:
        """
        return self._atoms

    def set_atoms(self, atoms):
        r"""SUMMARY

        set_atoms(atoms)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._atoms = atoms

    atoms = property(get_atoms, set_atoms)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2xIHh', self.window, self.atoms_len, self.delta))
        buf.write(str(buffer(_array('I', self.atoms))))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class ForceScreenSaver(SetAccessControl):
    r"""ForceScreenSaver

    ForceScreenSaver is a object.
    Responsibility:
    """


class SetPointerMapping(object):
    r"""SetPointerMapping

    SetPointerMapping is a object.
    Responsibility:
    """
    def __init__(self, map_len, map):
        r"""

        @Arguments:
        - `map_len`:
        - `map`:
        """
        self._map_len = map_len
        self._map = map

    def get_map_len(self, ):
        r"""SUMMARY

        get_map_len()

        @Return:

        @Error:
        """
        return self._map_len

    def set_map_len(self, map_len):
        r"""SUMMARY

        set_map_len(map_len)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._map_len = map_len

    map_len = property(get_map_len, set_map_len)

    def get_map(self, ):
        r"""SUMMARY

        get_map()

        @Return:

        @Error:
        """
        return self._map

    def set_map(self, map):
        r"""SUMMARY

        set_map(map)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._map = map

    map = property(get_map, set_map)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2x', self.map_len))
        buf.write(str(buffer(_array('B', self.map))))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class GetPointerMapping(object):
    r"""GetPointerMapping

    GetPointerMapping is a object.
    Responsibility:
    """

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class SetModifierMapping(object):
    r"""SetModifierMapping

    SetModifierMapping is a object.
    Responsibility:
    """
    def __init__(self, keycodes_per_modifier, keycodes):
        r"""

        @Arguments:
        - `keycodes_per_modifier`:
        - `keycodes`:
        """
        self._keycodes_per_modifier = keycodes_per_modifier
        self._keycodes = keycodes

    def get_keycodes_per_modifier(self, ):
        r"""SUMMARY

        get_keycodes_per_modifier()

        @Return:

        @Error:
        """
        return self._keycodes_per_modifier

    def set_keycodes_per_modifier(self, keycodes_per_modifier):
        r"""SUMMARY

        set_keycodes_per_modifier(keycodes_per_modifier)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._keycodes_per_modifier = keycodes_per_modifier

    keycodes_per_modifier = property(
        get_keycodes_per_modifier, set_keycodes_per_modifier)

    def get_keycodes(self, ):
        r"""SUMMARY

        get_keycodes()

        @Return:

        @Error:
        """
        return self._keycodes

    def set_keycodes(self, keycodes):
        r"""SUMMARY

        set_keycodes(keycodes)

        @Arguments:
        - [yas] elisp error!:

        @Return:

        @Error:
        """
        self._keycodes = keycodes

    keycodes = property(get_keycodes, set_keycodes)

    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2x', self.keycodes_per_modifier))
        buf.write(str(buffer(_array('B', self.keycodes))))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class GetModifierMapping(object):
    r"""GetModifierMapping

    GetModifierMapping is a object.
    Responsibility:
    """
    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()


class NoOperation(object):
    r"""NoOperation

    NoOperation is a object.
    Responsibility:
    """
    def get_buffer(self, ):
        r"""SUMMARY

        get_buffer()

        @Return:

        @Error:
        """
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return buf.getvalue()

    def __str__(self):
        return self.get_buffer()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# buffer.py ends here
