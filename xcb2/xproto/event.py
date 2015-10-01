#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: event.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""event -- event

"""
from struct import unpack_from as _unpack_from

from xcb import xcb


__all__ = ['KeyButtonPointerBase', 'KeyPressEvent', 'KeyReleaseEvent',
           'ButtonPressEvent', 'ButtonReleaseEvent', 'MotionNotifyEvent',
           'EnterLeaveNotifyBase', 'EnterNotifyEvent', 'LeaveNotifyEvent',
           'FocusBase', 'FocusInEvent', 'FocusOutEvent', 'KeymapNotifyEvent',
           'ExposeEvent', 'GraphicsExposureEvent', 'NoExposureEvent',
           'VisibilityNotifyEvent', 'CreateNotifyEvent', 'DestroyNotifyEvent',
           'UnmapNotifyEvent', 'MapNotifyEvent', 'MapRequestEvent',
           'ReparentNotifyEvent', 'ConfigureNotifyEvent',
           'ConfigureRequestEvent', 'GravityNotifyEvent', 'ResizeRequestEvent',
           'CirculateBase', 'CirculateNotifyEvent', 'CirculateRequestEvent',
           'PropertyNotifyEvent', 'SelectionClearEvent',
           'SelectionRequestEvent', 'SelectionNotifyEvent',
           'ColormapNotifyEvent', 'ClientMessageData', 'ClientMessageEvent',
           'MappingNotifyEvent', '_EVENTS']


class KeyButtonPointerBase(xcb.Event):
    r"""SUMMARY
    """

    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        _unpacked = _unpack_from('xB2xIIIIhhhhHBx', parent, offset)
        self.detail      = _unpacked[0]
        self.time        = _unpacked[1]
        self.root        = _unpacked[2]
        self.event       = _unpacked[3]
        self.child       = _unpacked[4]
        self.root_x      = _unpacked[5]
        self.root_y      = _unpacked[6]
        self.event_x     = _unpacked[7]
        self.event_y     = _unpacked[8]
        self.state       = _unpacked[9]
        self.same_screen = _unpacked[10]


class KeyPressEvent(KeyButtonPointerBase):
    r"""SUMMARY
    """


class KeyReleaseEvent(KeyButtonPointerBase):
    r"""SUMMARY
    """


class ButtonPressEvent(KeyButtonPointerBase):
    r"""SUMMARY
    """


class ButtonReleaseEvent(KeyButtonPointerBase):
    r"""SUMMARY
    """


class MotionNotifyEvent(KeyButtonPointerBase):
    r"""SUMMARY
    """


class EnterLeaveNotifyBase(xcb.Event):
    r"""SUMMARY
    """

    def __init__(self, parent, offset=0):
        r"""
        """
        xcb.Event.__init__(self, parent, offset)
        _unpacked = _unpack_from('xB2xIIIIhhhhHBB', parent, offset)
        self.detail      = _unpacked[0]
        self.time        = _unpacked[1]
        self.root        = _unpacked[2]
        self.event       = _unpacked[3]
        self.child       = _unpacked[4]
        self.root_x      = _unpacked[5]
        self.root_y      = _unpacked[6]
        self.event_x     = _unpacked[7]
        self.event_y     = _unpacked[8]
        self.state       = _unpacked[9]
        self.mode        = _unpacked[10]
        self.same_screen = _unpacked[11]


class EnterNotifyEvent(EnterLeaveNotifyBase):
    r"""SUMMARY
    """


class LeaveNotifyEvent(EnterLeaveNotifyBase):
    r"""SUMMARY
    """


class FocusBase(xcb.Event):
    r"""SUMMARY
    """

    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        _unpacked = _unpack_from('xB2xIB3x', parent, offset)
        self.detail = _unpacked[0]
        self.event  = _unpacked[1]
        self.mode   = _unpacked[2]


class FocusInEvent(FocusBase):
    r"""SUMMARY
    """


class FocusOutEvent(FocusBase):
    r"""SUMMARY
    """


class KeymapNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        offset += 1
        self.keys = xcb.List(parent, offset, 31, 'B', 1)


class ExposeEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2xIHHHHH2x', parent, offset)
        self.window = _unpacked[0]
        self.x      = _unpacked[1]
        self.y      = _unpacked[2]
        self.width  = _unpacked[3]
        self.height = _unpacked[4]
        self.count  = _unpacked[5]


class GraphicsExposureEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2xIHHHHHHB3x', parent, offset)
        self.drawable     = _unpacked[0]
        self.x            = _unpacked[1]
        self.y            = _unpacked[2]
        self.width        = _unpacked[3]
        self.height       = _unpacked[4]
        self.minor_opcode = _unpacked[5]
        self.count        = _unpacked[6]
        self.major_opcode = _unpacked[7]


class NoExposureEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2xIHBx', parent, offset)
        self.drawable = _unpacked[0]
        self.minor_opcode = _unpacked[1]
        self.major_opcode = _unpacked[2]


class VisibilityNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2xIB3x', parent, offset)
        self.window = _unpacked[0]
        self.state  = _unpacked[1]


class CreateNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2xIIhhHHHBx', parent, offset)
        self.parent            = _unpacked[0]
        self.window            = _unpacked[1]
        self.x                 = _unpacked[2]
        self.y                 = _unpacked[3]
        self.width             = _unpacked[4]
        self.height            = _unpacked[5]
        self.border_width      = _unpacked[6]
        self.override_redirect = _unpacked[7]


class DestroyNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2xII', parent, offset)
        self.event  = _unpacked[0]
        self.window = _unpacked[1]


class UnmapNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2xIIB3x', parent, offset)
        self.event          = _unpacked[0]
        self.window         = _unpacked[1]
        self.from_configure = _unpacked[2]


class MapNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2xIIB3x', parent, offset)
        self.event             = _unpacked[0]
        self.window            = _unpacked[1]
        self.override_redirect = _unpacked[2]


class MapRequestEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2xII', parent, offset)
        self.parent = _unpacked[0]
        self.window = _unpacked[1]


class ReparentNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2xIIIhhB3x', parent, offset)
        self.event             = _unpacked[0]
        self.window            = _unpacked[1]
        self.parent            = _unpacked[2]
        self.x                 = _unpacked[3]
        self.y                 = _unpacked[4]
        self.override_redirect = _unpacked[5]


class ConfigureNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2xIIIhhHHHBx', parent, offset)
        self.event             = _unpacked[0]
        self.window            = _unpacked[1]
        self.above_sibling     = _unpacked[2]
        self.x                 = _unpacked[3]
        self.y                 = _unpacked[4]
        self.width             = _unpacked[5]
        self.height            = _unpacked[6]
        self.border_width      = _unpacked[7]
        self.override_redirect = _unpacked[8]


class ConfigureRequestEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        _unpacked = _unpack_from('xB2xIIIhhHHHH', parent, offset)
        self.stack_mode   = _unpacked[0]
        self.parent       = _unpacked[1]
        self.window       = _unpacked[2]
        self.sibling      = _unpacked[3]
        self.x            = _unpacked[4]
        self.y            = _unpacked[5]
        self.width        = _unpacked[6]
        self.height       = _unpacked[7]
        self.border_width = _unpacked[8]
        self.value_mask   = _unpacked[9]


class GravityNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2xIIhh', parent, offset)
        self.event  = _unpacked[0]
        self.window = _unpacked[1]
        self.x      = _unpacked[2]
        self.y      = _unpacked[3]


class ResizeRequestEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2xIHH', parent, offset)
        self.window = _unpacked[0]
        self.width  = _unpacked[1]
        self.height = _unpacked[2]


class CirculateBase(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2xII4xB3x', parent, offset)
        self.event  = _unpacked[0]
        self.window = _unpacked[1]
        self.place  = _unpacked[2]


class CirculateNotifyEvent(CirculateBase):
    r"""SUMMARY
    """


class CirculateRequestEvent(CirculateBase):
    """
    """


class PropertyNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2xIIIB3x', parent, offset)
        self.window = _unpacked[0]
        self.atom   = _unpacked[1]
        self.time   = _unpacked[2]
        self.state  = _unpacked[3]


class SelectionClearEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2xIII', parent, offset)
        self.time      = _unpacked[0]
        self.owner     = _unpacked[1]
        self.selection = _unpacked[2]


class SelectionRequestEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2xIIIIII', parent, offset)
        self.time      = _unpacked[0]
        self.owner     = _unpacked[1]
        self.requestor = _unpacked[2]
        self.selection = _unpacked[3]
        self.target    = _unpacked[4]
        self.property  = _unpacked[5]


class SelectionNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2xIIIII', parent, offset)
        self.time      = _unpacked[0]
        self.requestor = _unpacked[1]
        self.selection = _unpacked[2]
        self.target    = _unpacked[3]
        self.property  = _unpacked[4]


class ColormapNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2xIIBB2x', parent, offset)
        self.window   = _unpacked[0]
        self.colormap = _unpacked[1]
        self.new      = _unpacked[2]
        self.state    = _unpacked[3]


class ClientMessageData(xcb.Union):
    def __init__(self, parent, offset, size):
        xcb.Union.__init__(self, parent, offset, size)
        self.data8  = xcb.List(parent, offset, 20, 'B', 1)
        self.data16 = xcb.List(parent, offset, 10, 'H', 2)
        self.data32 = xcb.List(parent, offset, 5, 'I', 4)


class ClientMessageEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        _unpacked = _unpack_from('xB2xII', parent, offset)
        self.format = _unpacked[0]
        self.window = _unpacked[1]
        self.type   = _unpacked[2]
        self.data = ClientMessageData(parent, offset + 12, 60)


class MappingNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2xBBBx', parent, offset)
        self.request       = _unpacked[0]
        self.first_keycode = _unpacked[1]
        self.count         = _unpacked[2]


_EVENTS = {
    2 : KeyPressEvent,
    3 : KeyReleaseEvent,
    4 : ButtonPressEvent,
    5 : ButtonReleaseEvent,
    6 : MotionNotifyEvent,
    7 : EnterNotifyEvent,
    8 : LeaveNotifyEvent,
    9 : FocusInEvent,
    10 : FocusOutEvent,
    11 : KeymapNotifyEvent,
    12 : ExposeEvent,
    13 : GraphicsExposureEvent,
    14 : NoExposureEvent,
    15 : VisibilityNotifyEvent,
    16 : CreateNotifyEvent,
    17 : DestroyNotifyEvent,
    18 : UnmapNotifyEvent,
    19 : MapNotifyEvent,
    20 : MapRequestEvent,
    21 : ReparentNotifyEvent,
    22 : ConfigureNotifyEvent,
    23 : ConfigureRequestEvent,
    24 : GravityNotifyEvent,
    25 : ResizeRequestEvent,
    26 : CirculateNotifyEvent,
    27 : CirculateRequestEvent,
    28 : PropertyNotifyEvent,
    29 : SelectionClearEvent,
    30 : SelectionRequestEvent,
    31 : SelectionNotifyEvent,
    32 : ColormapNotifyEvent,
    33 : ClientMessageEvent,
    34 : MappingNotifyEvent,
    }



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# event.py ends here
