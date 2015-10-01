#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""Name: __init__.py


"""
from cStringIO import StringIO as _StringIO
from array import array as _array
from struct import pack as _pack
from xcb import xcb

from xcb2.xproto.event import *
from xcb2.xproto.error import *
from xcb2.xproto.define import *
from xcb2.xproto.cookie import *
from xcb2.xproto.reply import *

# and import at end


class xprotoExtension(xcb.Extension):

    def CreateWindowChecked(self, depth, wid, parent, x, y, width, height, border_width, _class, visual, value_mask, value_list):
        buf = _StringIO()
        buf.write(_pack('=xB2xIIhhHHHHII', depth, wid, parent, x, y, width, height, border_width, _class, visual, value_mask))
        buf.write(str(buffer(_array('I', value_list))))
        return self.send_request(xcb.Request(buf.getvalue(), 1, True, True),
                                 xcb.VoidCookie())

    def CreateWindow(self, depth, wid, parent, x, y, width, height, border_width, _class, visual, value_mask, value_list):
        buf = _StringIO()
        buf.write(_pack('=xB2xIIhhHHHHII', depth, wid, parent, x, y, width, height, border_width, _class, visual, value_mask))
        buf.write(str(buffer(_array('I', value_list))))
        return self.send_request(xcb.Request(buf.getvalue(), 1, True, False),
                                 xcb.VoidCookie())

    def ChangeWindowAttributesChecked(self, window, value_mask, value_list):
        buf = _StringIO()
        buf.write(_pack('=xx2xII', window, value_mask))
        buf.write(str(buffer(_array('I', value_list))))
        return self.send_request(xcb.Request(buf.getvalue(), 2, True, True),
                                 xcb.VoidCookie())

    def ChangeWindowAttributes(self, window, value_mask, value_list):
        buf = _StringIO()
        buf.write(_pack('=xx2xII', window, value_mask))
        buf.write(str(buffer(_array('I', value_list))))
        return self.send_request(xcb.Request(buf.getvalue(), 2, True, False),
                                 xcb.VoidCookie())

    def GetWindowAttributes(self, window):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 3, False, True),
                                 GetWindowAttributesCookie(),
                                 GetWindowAttributesReply)

    def GetWindowAttributesUnchecked(self, window):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 3, False, False),
                                 GetWindowAttributesCookie(),
                                 GetWindowAttributesReply)

    def DestroyWindowChecked(self, window):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 4, True, True),
                                 xcb.VoidCookie())

    def DestroyWindow(self, window):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 4, True, False),
                                 xcb.VoidCookie())

    def DestroySubwindowsChecked(self, window):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 5, True, True),
                                 xcb.VoidCookie())

    def DestroySubwindows(self, window):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 5, True, False),
                                 xcb.VoidCookie())

    def ChangeSaveSetChecked(self, mode, window):
        buf = _StringIO()
        buf.write(_pack('=xB2xI', mode, window))
        return self.send_request(xcb.Request(buf.getvalue(), 6, True, True),
                                 xcb.VoidCookie())

    def ChangeSaveSet(self, mode, window):
        buf = _StringIO()
        buf.write(_pack('=xB2xI', mode, window))
        return self.send_request(xcb.Request(buf.getvalue(), 6, True, False),
                                 xcb.VoidCookie())

    def ReparentWindowChecked(self, window, parent, x, y):
        buf = _StringIO()
        buf.write(_pack('=xx2xIIhh', window, parent, x, y))
        return self.send_request(xcb.Request(buf.getvalue(), 7, True, True),
                                 xcb.VoidCookie())

    def ReparentWindow(self, window, parent, x, y):
        buf = _StringIO()
        buf.write(_pack('=xx2xIIhh', window, parent, x, y))
        return self.send_request(xcb.Request(buf.getvalue(), 7, True, False),
                                 xcb.VoidCookie())

    def MapWindowChecked(self, window):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 8, True, True),
                                 xcb.VoidCookie())

    def MapWindow(self, window):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 8, True, False),
                                 xcb.VoidCookie())

    def MapSubwindowsChecked(self, window):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 9, True, True),
                                 xcb.VoidCookie())

    def MapSubwindows(self, window):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 9, True, False),
                                 xcb.VoidCookie())

    def UnmapWindowChecked(self, window):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 10, True, True),
                                 xcb.VoidCookie())

    def UnmapWindow(self, window):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 10, True, False),
                                 xcb.VoidCookie())

    def UnmapSubwindowsChecked(self, window):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 11, True, True),
                                 xcb.VoidCookie())

    def UnmapSubwindows(self, window):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 11, True, False),
                                 xcb.VoidCookie())

    def ConfigureWindowChecked(self, window, value_mask, value_list):
        buf = _StringIO()
        buf.write(_pack('=xx2xIH2x', window, value_mask))
        buf.write(str(buffer(_array('I', value_list))))
        return self.send_request(xcb.Request(buf.getvalue(), 12, True, True),
                                 xcb.VoidCookie())

    def ConfigureWindow(self, window, value_mask, value_list):
        buf = _StringIO()
        buf.write(_pack('=xx2xIH2x', window, value_mask))
        buf.write(str(buffer(_array('I', value_list))))
        return self.send_request(xcb.Request(buf.getvalue(), 12, True, False),
                                 xcb.VoidCookie())

    def CirculateWindowChecked(self, direction, window):
        buf = _StringIO()
        buf.write(_pack('=xB2xI', direction, window))
        return self.send_request(xcb.Request(buf.getvalue(), 13, True, True),
                                 xcb.VoidCookie())

    def CirculateWindow(self, direction, window):
        buf = _StringIO()
        buf.write(_pack('=xB2xI', direction, window))
        return self.send_request(xcb.Request(buf.getvalue(), 13, True, False),
                                 xcb.VoidCookie())

    def GetGeometry(self, drawable):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', drawable))
        return self.send_request(xcb.Request(buf.getvalue(), 14, False, True),
                                 GetGeometryCookie(),
                                 GetGeometryReply)

    def GetGeometryUnchecked(self, drawable):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', drawable))
        return self.send_request(xcb.Request(buf.getvalue(), 14, False, False),
                                 GetGeometryCookie(),
                                 GetGeometryReply)

    def QueryTree(self, window):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 15, False, True),
                                 QueryTreeCookie(),
                                 QueryTreeReply)

    def QueryTreeUnchecked(self, window):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 15, False, False),
                                 QueryTreeCookie(),
                                 QueryTreeReply)

    def InternAtom(self, only_if_exists, name_len, name):
        buf = _StringIO()
        buf.write(_pack('=xB2xH2x', only_if_exists, name_len))
        buf.write(str(buffer(_array('b', name))))
        return self.send_request(xcb.Request(buf.getvalue(), 16, False, True),
                                 InternAtomCookie(),
                                 InternAtomReply)

    def InternAtomUnchecked(self, only_if_exists, name_len, name):
        buf = _StringIO()
        buf.write(_pack('=xB2xH2x', only_if_exists, name_len))
        buf.write(str(buffer(_array('b', name))))
        return self.send_request(xcb.Request(buf.getvalue(), 16, False, False),
                                 InternAtomCookie(),
                                 InternAtomReply)

    def GetAtomName(self, atom):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', atom))
        return self.send_request(xcb.Request(buf.getvalue(), 17, False, True),
                                 GetAtomNameCookie(),
                                 GetAtomNameReply)

    def GetAtomNameUnchecked(self, atom):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', atom))
        return self.send_request(xcb.Request(buf.getvalue(), 17, False, False),
                                 GetAtomNameCookie(),
                                 GetAtomNameReply)

    def ChangePropertyChecked(self, mode, window, property, type, format, data_len, data):
        buf = _StringIO()
        buf.write(_pack('=xB2xIIIB3xI', mode, window, property, type, format, data_len))
        buf.write(str(buffer(_array('B', data))))
        return self.send_request(xcb.Request(buf.getvalue(), 18, True, True),
                                 xcb.VoidCookie())

    def ChangeProperty(self, mode, window, property, type, format, data_len, data):
        buf = _StringIO()
        buf.write(_pack('=xB2xIIIB3xI', mode, window, property, type, format, data_len))
        buf.write(str(buffer(_array('B', data))))
        return self.send_request(xcb.Request(buf.getvalue(), 18, True, False),
                                 xcb.VoidCookie())

    def DeletePropertyChecked(self, window, property):
        buf = _StringIO()
        buf.write(_pack('=xx2xII', window, property))
        return self.send_request(xcb.Request(buf.getvalue(), 19, True, True),
                                 xcb.VoidCookie())

    def DeleteProperty(self, window, property):
        buf = _StringIO()
        buf.write(_pack('=xx2xII', window, property))
        return self.send_request(xcb.Request(buf.getvalue(), 19, True, False),
                                 xcb.VoidCookie())

    def GetProperty(self, delete, window, property, type, long_offset, long_length):
        buf = _StringIO()
        buf.write(_pack('=xB2xIIIII', delete, window, property, type, long_offset, long_length))
        return self.send_request(xcb.Request(buf.getvalue(), 20, False, True),
                                 GetPropertyCookie(),
                                 GetPropertyReply)

    def GetPropertyUnchecked(self, delete, window, property, type, long_offset, long_length):
        buf = _StringIO()
        buf.write(_pack('=xB2xIIIII', delete, window, property, type, long_offset, long_length))
        return self.send_request(xcb.Request(buf.getvalue(), 20, False, False),
                                 GetPropertyCookie(),
                                 GetPropertyReply)

    def ListProperties(self, window):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 21, False, True),
                                 ListPropertiesCookie(),
                                 ListPropertiesReply)

    def ListPropertiesUnchecked(self, window):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 21, False, False),
                                 ListPropertiesCookie(),
                                 ListPropertiesReply)

    def SetSelectionOwnerChecked(self, owner, selection, time):
        buf = _StringIO()
        buf.write(_pack('=xx2xIII', owner, selection, time))
        return self.send_request(xcb.Request(buf.getvalue(), 22, True, True),
                                 xcb.VoidCookie())

    def SetSelectionOwner(self, owner, selection, time):
        buf = _StringIO()
        buf.write(_pack('=xx2xIII', owner, selection, time))
        return self.send_request(xcb.Request(buf.getvalue(), 22, True, False),
                                 xcb.VoidCookie())

    def GetSelectionOwner(self, selection):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', selection))
        return self.send_request(xcb.Request(buf.getvalue(), 23, False, True),
                                 GetSelectionOwnerCookie(),
                                 GetSelectionOwnerReply)

    def GetSelectionOwnerUnchecked(self, selection):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', selection))
        return self.send_request(xcb.Request(buf.getvalue(), 23, False, False),
                                 GetSelectionOwnerCookie(),
                                 GetSelectionOwnerReply)

    def ConvertSelectionChecked(self, requestor, selection, target, property, time):
        buf = _StringIO()
        buf.write(_pack('=xx2xIIIII', requestor, selection, target, property, time))
        return self.send_request(xcb.Request(buf.getvalue(), 24, True, True),
                                 xcb.VoidCookie())

    def ConvertSelection(self, requestor, selection, target, property, time):
        buf = _StringIO()
        buf.write(_pack('=xx2xIIIII', requestor, selection, target, property, time))
        return self.send_request(xcb.Request(buf.getvalue(), 24, True, False),
                                 xcb.VoidCookie())

    def SendEventChecked(self, propagate, destination, event_mask, event):
        buf = _StringIO()
        buf.write(_pack('=xB2xII', propagate, destination, event_mask))
        buf.write(str(buffer(_array('b', event))))
        print(repr(buf.getvalue()))
        return self.send_request(xcb.Request(buf.getvalue(), 25, True, True),
                                 xcb.VoidCookie())

    def SendEvent(self, propagate, destination, event_mask, event):
        buf = _StringIO()
        buf.write(_pack('=xB2xII', propagate, destination, event_mask))
        buf.write(str(buffer(_array('b', event))))
        print(repr(buf.getvalue()))
        return self.send_request(xcb.Request(buf.getvalue(), 25, True, False),
                                 xcb.VoidCookie())

    def GrabPointer(self, owner_events, grab_window, event_mask, pointer_mode, keyboard_mode, confine_to, cursor, time):
        buf = _StringIO()
        buf.write(_pack('=xB2xIHBBIII', owner_events, grab_window, event_mask, pointer_mode, keyboard_mode, confine_to, cursor, time))
        return self.send_request(xcb.Request(buf.getvalue(), 26, False, True),
                                 GrabPointerCookie(),
                                 GrabPointerReply)

    def GrabPointerUnchecked(self, owner_events, grab_window, event_mask, pointer_mode, keyboard_mode, confine_to, cursor, time):
        buf = _StringIO()
        buf.write(_pack('=xB2xIHBBIII', owner_events, grab_window, event_mask, pointer_mode, keyboard_mode, confine_to, cursor, time))
        return self.send_request(xcb.Request(buf.getvalue(), 26, False, False),
                                 GrabPointerCookie(),
                                 GrabPointerReply)

    def UngrabPointerChecked(self, time):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', time))
        return self.send_request(xcb.Request(buf.getvalue(), 27, True, True),
                                 xcb.VoidCookie())

    def UngrabPointer(self, time):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', time))
        return self.send_request(xcb.Request(buf.getvalue(), 27, True, False),
                                 xcb.VoidCookie())

    def GrabButtonChecked(self, owner_events, grab_window, event_mask, pointer_mode, keyboard_mode, confine_to, cursor, button, modifiers):
        buf = _StringIO()
        buf.write(_pack('=xB2xIHBBIIBxH', owner_events, grab_window, event_mask, pointer_mode, keyboard_mode, confine_to, cursor, button, modifiers))
        return self.send_request(xcb.Request(buf.getvalue(), 28, True, True),
                                 xcb.VoidCookie())

    def GrabButton(self, owner_events, grab_window, event_mask, pointer_mode, keyboard_mode, confine_to, cursor, button, modifiers):
        buf = _StringIO()
        buf.write(_pack('=xB2xIHBBIIBxH', owner_events, grab_window, event_mask, pointer_mode, keyboard_mode, confine_to, cursor, button, modifiers))
        return self.send_request(xcb.Request(buf.getvalue(), 28, True, False),
                                 xcb.VoidCookie())

    def UngrabButtonChecked(self, button, grab_window, modifiers):
        buf = _StringIO()
        buf.write(_pack('=xB2xIH2x', button, grab_window, modifiers))
        return self.send_request(xcb.Request(buf.getvalue(), 29, True, True),
                                 xcb.VoidCookie())

    def UngrabButton(self, button, grab_window, modifiers):
        buf = _StringIO()
        buf.write(_pack('=xB2xIH2x', button, grab_window, modifiers))
        return self.send_request(xcb.Request(buf.getvalue(), 29, True, False),
                                 xcb.VoidCookie())

    def ChangeActivePointerGrabChecked(self, cursor, time, event_mask):
        buf = _StringIO()
        buf.write(_pack('=xx2xIIH2x', cursor, time, event_mask))
        return self.send_request(xcb.Request(buf.getvalue(), 30, True, True),
                                 xcb.VoidCookie())

    def ChangeActivePointerGrab(self, cursor, time, event_mask):
        buf = _StringIO()
        buf.write(_pack('=xx2xIIH2x', cursor, time, event_mask))
        return self.send_request(xcb.Request(buf.getvalue(), 30, True, False),
                                 xcb.VoidCookie())

    def GrabKeyboard(self, owner_events, grab_window, time, pointer_mode, keyboard_mode):
        buf = _StringIO()
        buf.write(_pack('=xB2xIIBB2x', owner_events, grab_window, time, pointer_mode, keyboard_mode))
        return self.send_request(xcb.Request(buf.getvalue(), 31, False, True),
                                 GrabKeyboardCookie(),
                                 GrabKeyboardReply)

    def GrabKeyboardUnchecked(self, owner_events, grab_window, time, pointer_mode, keyboard_mode):
        buf = _StringIO()
        buf.write(_pack('=xB2xIIBB2x', owner_events, grab_window, time, pointer_mode, keyboard_mode))
        return self.send_request(xcb.Request(buf.getvalue(), 31, False, False),
                                 GrabKeyboardCookie(),
                                 GrabKeyboardReply)

    def UngrabKeyboardChecked(self, time):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', time))
        return self.send_request(xcb.Request(buf.getvalue(), 32, True, True),
                                 xcb.VoidCookie())

    def UngrabKeyboard(self, time):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', time))
        return self.send_request(xcb.Request(buf.getvalue(), 32, True, False),
                                 xcb.VoidCookie())

    def GrabKeyChecked(self, owner_events, grab_window, modifiers, key, pointer_mode, keyboard_mode):
        buf = _StringIO()
        buf.write(_pack('=xB2xIHBBB3x', owner_events, grab_window, modifiers, key, pointer_mode, keyboard_mode))
        return self.send_request(xcb.Request(buf.getvalue(), 33, True, True),
                                 xcb.VoidCookie())

    def GrabKey(self, owner_events, grab_window, modifiers, key, pointer_mode, keyboard_mode):
        buf = _StringIO()
        buf.write(_pack('=xB2xIHBBB3x', owner_events, grab_window, modifiers, key, pointer_mode, keyboard_mode))
        return self.send_request(xcb.Request(buf.getvalue(), 33, True, False),
                                 xcb.VoidCookie())

    def UngrabKeyChecked(self, key, grab_window, modifiers):
        buf = _StringIO()
        buf.write(_pack('=xB2xIH2x', key, grab_window, modifiers))
        return self.send_request(xcb.Request(buf.getvalue(), 34, True, True),
                                 xcb.VoidCookie())

    def UngrabKey(self, key, grab_window, modifiers):
        buf = _StringIO()
        buf.write(_pack('=xB2xIH2x', key, grab_window, modifiers))
        return self.send_request(xcb.Request(buf.getvalue(), 34, True, False),
                                 xcb.VoidCookie())

    def AllowEventsChecked(self, mode, time):
        buf = _StringIO()
        buf.write(_pack('=xB2xI', mode, time))
        return self.send_request(xcb.Request(buf.getvalue(), 35, True, True),
                                 xcb.VoidCookie())

    def AllowEvents(self, mode, time):
        buf = _StringIO()
        buf.write(_pack('=xB2xI', mode, time))
        return self.send_request(xcb.Request(buf.getvalue(), 35, True, False),
                                 xcb.VoidCookie())

    def GrabServerChecked(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 36, True, True),
                                 xcb.VoidCookie())

    def GrabServer(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 36, True, False),
                                 xcb.VoidCookie())

    def UngrabServerChecked(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 37, True, True),
                                 xcb.VoidCookie())

    def UngrabServer(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 37, True, False),
                                 xcb.VoidCookie())

    def QueryPointer(self, window):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 38, False, True),
                                 QueryPointerCookie(),
                                 QueryPointerReply)

    def QueryPointerUnchecked(self, window):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 38, False, False),
                                 QueryPointerCookie(),
                                 QueryPointerReply)

    def GetMotionEvents(self, window, start, stop):
        buf = _StringIO()
        buf.write(_pack('=xx2xIII', window, start, stop))
        return self.send_request(xcb.Request(buf.getvalue(), 39, False, True),
                                 GetMotionEventsCookie(),
                                 GetMotionEventsReply)

    def GetMotionEventsUnchecked(self, window, start, stop):
        buf = _StringIO()
        buf.write(_pack('=xx2xIII', window, start, stop))
        return self.send_request(xcb.Request(buf.getvalue(), 39, False, False),
                                 GetMotionEventsCookie(),
                                 GetMotionEventsReply)

    def TranslateCoordinates(self, src_window, dst_window, src_x, src_y):
        buf = _StringIO()
        buf.write(_pack('=xx2xIIhh', src_window, dst_window, src_x, src_y))
        return self.send_request(xcb.Request(buf.getvalue(), 40, False, True),
                                 TranslateCoordinatesCookie(),
                                 TranslateCoordinatesReply)

    def TranslateCoordinatesUnchecked(self, src_window, dst_window, src_x, src_y):
        buf = _StringIO()
        buf.write(_pack('=xx2xIIhh', src_window, dst_window, src_x, src_y))
        return self.send_request(xcb.Request(buf.getvalue(), 40, False, False),
                                 TranslateCoordinatesCookie(),
                                 TranslateCoordinatesReply)

    def WarpPointerChecked(self, src_window, dst_window, src_x, src_y, src_width, src_height, dst_x, dst_y):
        buf = _StringIO()
        buf.write(_pack('=xx2xIIhhHHhh', src_window, dst_window, src_x, src_y, src_width, src_height, dst_x, dst_y))
        return self.send_request(xcb.Request(buf.getvalue(), 41, True, True),
                                 xcb.VoidCookie())

    def WarpPointer(self, src_window, dst_window, src_x, src_y, src_width, src_height, dst_x, dst_y):
        buf = _StringIO()
        buf.write(_pack('=xx2xIIhhHHhh', src_window, dst_window, src_x, src_y, src_width, src_height, dst_x, dst_y))
        return self.send_request(xcb.Request(buf.getvalue(), 41, True, False),
                                 xcb.VoidCookie())

    def SetInputFocusChecked(self, revert_to, focus, time):
        buf = _StringIO()
        buf.write(_pack('=xB2xII', revert_to, focus, time))
        return self.send_request(xcb.Request(buf.getvalue(), 42, True, True),
                                 xcb.VoidCookie())

    def SetInputFocus(self, revert_to, focus, time):
        buf = _StringIO()
        buf.write(_pack('=xB2xII', revert_to, focus, time))
        return self.send_request(xcb.Request(buf.getvalue(), 42, True, False),
                                 xcb.VoidCookie())

    def GetInputFocus(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 43, False, True),
                                 GetInputFocusCookie(),
                                 GetInputFocusReply)

    def GetInputFocusUnchecked(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 43, False, False),
                                 GetInputFocusCookie(),
                                 GetInputFocusReply)

    def QueryKeymap(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 44, False, True),
                                 QueryKeymapCookie(),
                                 QueryKeymapReply)

    def QueryKeymapUnchecked(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 44, False, False),
                                 QueryKeymapCookie(),
                                 QueryKeymapReply)

    def OpenFontChecked(self, fid, name_len, name):
        buf = _StringIO()
        buf.write(_pack('=xx2xIH2x', fid, name_len))
        buf.write(str(buffer(_array('b', name))))
        return self.send_request(xcb.Request(buf.getvalue(), 45, True, True),
                                 xcb.VoidCookie())

    def OpenFont(self, fid, name_len, name):
        buf = _StringIO()
        buf.write(_pack('=xx2xIH2x', fid, name_len))
        buf.write(str(buffer(_array('b', name))))
        return self.send_request(xcb.Request(buf.getvalue(), 45, True, False),
                                 xcb.VoidCookie())

    def CloseFontChecked(self, font):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', font))
        return self.send_request(xcb.Request(buf.getvalue(), 46, True, True),
                                 xcb.VoidCookie())

    def CloseFont(self, font):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', font))
        return self.send_request(xcb.Request(buf.getvalue(), 46, True, False),
                                 xcb.VoidCookie())

    def QueryFont(self, font):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', font))
        return self.send_request(xcb.Request(buf.getvalue(), 47, False, True),
                                 QueryFontCookie(),
                                 QueryFontReply)

    def QueryFontUnchecked(self, font):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', font))
        return self.send_request(xcb.Request(buf.getvalue(), 47, False, False),
                                 QueryFontCookie(),
                                 QueryFontReply)

    def QueryTextExtents(self, font, string_len, string):
        buf = _StringIO()
        buf.write(_pack('=x', ))
        buf.write(_pack('=B', (string_len & 1)))
        buf.write(_pack('=2xI', font))
        for elt in xcb.Iterator(string, 2, 'string', True):
            buf.write(_pack('=BB', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 48, False, True),
                                 QueryTextExtentsCookie(),
                                 QueryTextExtentsReply)

    def QueryTextExtentsUnchecked(self, font, string_len, string):
        buf = _StringIO()
        buf.write(_pack('=x', ))
        buf.write(_pack('=B', (string_len & 1)))
        buf.write(_pack('=2xI', font))
        for elt in xcb.Iterator(string, 2, 'string', True):
            buf.write(_pack('=BB', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 48, False, False),
                                 QueryTextExtentsCookie(),
                                 QueryTextExtentsReply)

    def ListFonts(self, max_names, pattern_len, pattern):
        buf = _StringIO()
        buf.write(_pack('=xx2xHH', max_names, pattern_len))
        buf.write(str(buffer(_array('b', pattern))))
        return self.send_request(xcb.Request(buf.getvalue(), 49, False, True),
                                 ListFontsCookie(),
                                 ListFontsReply)

    def ListFontsUnchecked(self, max_names, pattern_len, pattern):
        buf = _StringIO()
        buf.write(_pack('=xx2xHH', max_names, pattern_len))
        buf.write(str(buffer(_array('b', pattern))))
        return self.send_request(xcb.Request(buf.getvalue(), 49, False, False),
                                 ListFontsCookie(),
                                 ListFontsReply)

    def ListFontsWithInfo(self, max_names, pattern_len, pattern):
        buf = _StringIO()
        buf.write(_pack('=xx2xHH', max_names, pattern_len))
        buf.write(str(buffer(_array('b', pattern))))
        return self.send_request(xcb.Request(buf.getvalue(), 50, False, True),
                                 ListFontsWithInfoCookie(),
                                 ListFontsWithInfoReply)

    def ListFontsWithInfoUnchecked(self, max_names, pattern_len, pattern):
        buf = _StringIO()
        buf.write(_pack('=xx2xHH', max_names, pattern_len))
        buf.write(str(buffer(_array('b', pattern))))
        return self.send_request(xcb.Request(buf.getvalue(), 50, False, False),
                                 ListFontsWithInfoCookie(),
                                 ListFontsWithInfoReply)

    def SetFontPathChecked(self, font_qty, font):
        buf = _StringIO()
        buf.write(_pack('=xx2xH2x', font_qty))
        for elt in xcb.Iterator(font, -1, 'font', True):
            buf.write(_pack('=None', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 51, True, True),
                                 xcb.VoidCookie())

    def SetFontPath(self, font_qty, font):
        buf = _StringIO()
        buf.write(_pack('=xx2xH2x', font_qty))
        for elt in xcb.Iterator(font, -1, 'font', True):
            buf.write(_pack('=None', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 51, True, False),
                                 xcb.VoidCookie())

    def GetFontPath(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 52, False, True),
                                 GetFontPathCookie(),
                                 GetFontPathReply)

    def GetFontPathUnchecked(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 52, False, False),
                                 GetFontPathCookie(),
                                 GetFontPathReply)

    def CreatePixmapChecked(self, depth, pid, drawable, width, height):
        buf = _StringIO()
        buf.write(_pack('=xB2xIIHH', depth, pid, drawable, width, height))
        return self.send_request(xcb.Request(buf.getvalue(), 53, True, True),
                                 xcb.VoidCookie())

    def CreatePixmap(self, depth, pid, drawable, width, height):
        buf = _StringIO()
        buf.write(_pack('=xB2xIIHH', depth, pid, drawable, width, height))
        return self.send_request(xcb.Request(buf.getvalue(), 53, True, False),
                                 xcb.VoidCookie())

    def FreePixmapChecked(self, pixmap):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', pixmap))
        return self.send_request(xcb.Request(buf.getvalue(), 54, True, True),
                                 xcb.VoidCookie())

    def FreePixmap(self, pixmap):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', pixmap))
        return self.send_request(xcb.Request(buf.getvalue(), 54, True, False),
                                 xcb.VoidCookie())

    def CreateGCChecked(self, cid, drawable, value_mask, value_list):
        buf = _StringIO()
        buf.write(_pack('=xx2xIII', cid, drawable, value_mask))
        buf.write(str(buffer(_array('I', value_list))))
        return self.send_request(xcb.Request(buf.getvalue(), 55, True, True),
                                 xcb.VoidCookie())

    def CreateGC(self, cid, drawable, value_mask, value_list):
        buf = _StringIO()
        buf.write(_pack('=xx2xIII', cid, drawable, value_mask))
        buf.write(str(buffer(_array('I', value_list))))
        return self.send_request(xcb.Request(buf.getvalue(), 55, True, False),
                                 xcb.VoidCookie())

    def ChangeGCChecked(self, gc, value_mask, value_list):
        buf = _StringIO()
        buf.write(_pack('=xx2xII', gc, value_mask))
        buf.write(str(buffer(_array('I', value_list))))
        return self.send_request(xcb.Request(buf.getvalue(), 56, True, True),
                                 xcb.VoidCookie())

    def ChangeGC(self, gc, value_mask, value_list):
        buf = _StringIO()
        buf.write(_pack('=xx2xII', gc, value_mask))
        buf.write(str(buffer(_array('I', value_list))))
        return self.send_request(xcb.Request(buf.getvalue(), 56, True, False),
                                 xcb.VoidCookie())

    def CopyGCChecked(self, src_gc, dst_gc, value_mask):
        buf = _StringIO()
        buf.write(_pack('=xx2xIII', src_gc, dst_gc, value_mask))
        return self.send_request(xcb.Request(buf.getvalue(), 57, True, True),
                                 xcb.VoidCookie())

    def CopyGC(self, src_gc, dst_gc, value_mask):
        buf = _StringIO()
        buf.write(_pack('=xx2xIII', src_gc, dst_gc, value_mask))
        return self.send_request(xcb.Request(buf.getvalue(), 57, True, False),
                                 xcb.VoidCookie())

    def SetDashesChecked(self, gc, dash_offset, dashes_len, dashes):
        buf = _StringIO()
        buf.write(_pack('=xx2xIHH', gc, dash_offset, dashes_len))
        buf.write(str(buffer(_array('B', dashes))))
        return self.send_request(xcb.Request(buf.getvalue(), 58, True, True),
                                 xcb.VoidCookie())

    def SetDashes(self, gc, dash_offset, dashes_len, dashes):
        buf = _StringIO()
        buf.write(_pack('=xx2xIHH', gc, dash_offset, dashes_len))
        buf.write(str(buffer(_array('B', dashes))))
        return self.send_request(xcb.Request(buf.getvalue(), 58, True, False),
                                 xcb.VoidCookie())

    def SetClipRectanglesChecked(self, ordering, gc, clip_x_origin, clip_y_origin, rectangles_len, rectangles):
        buf = _StringIO()
        buf.write(_pack('=xB2xIhh', ordering, gc, clip_x_origin, clip_y_origin))
        for elt in xcb.Iterator(rectangles, 4, 'rectangles', True):
            buf.write(_pack('=hhHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 59, True, True),
                                 xcb.VoidCookie())

    def SetClipRectangles(self, ordering, gc, clip_x_origin, clip_y_origin, rectangles_len, rectangles):
        buf = _StringIO()
        buf.write(_pack('=xB2xIhh', ordering, gc, clip_x_origin, clip_y_origin))
        for elt in xcb.Iterator(rectangles, 4, 'rectangles', True):
            buf.write(_pack('=hhHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 59, True, False),
                                 xcb.VoidCookie())

    def FreeGCChecked(self, gc):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', gc))
        return self.send_request(xcb.Request(buf.getvalue(), 60, True, True),
                                 xcb.VoidCookie())

    def FreeGC(self, gc):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', gc))
        return self.send_request(xcb.Request(buf.getvalue(), 60, True, False),
                                 xcb.VoidCookie())

    def ClearAreaChecked(self, exposures, window, x, y, width, height):
        buf = _StringIO()
        buf.write(_pack('=xB2xIhhHH', exposures, window, x, y, width, height))
        return self.send_request(xcb.Request(buf.getvalue(), 61, True, True),
                                 xcb.VoidCookie())

    def ClearArea(self, exposures, window, x, y, width, height):
        buf = _StringIO()
        buf.write(_pack('=xB2xIhhHH', exposures, window, x, y, width, height))
        return self.send_request(xcb.Request(buf.getvalue(), 61, True, False),
                                 xcb.VoidCookie())

    def CopyAreaChecked(self, src_drawable, dst_drawable, gc, src_x, src_y, dst_x, dst_y, width, height):
        buf = _StringIO()
        buf.write(_pack('=xx2xIIIhhhhHH', src_drawable, dst_drawable, gc, src_x, src_y, dst_x, dst_y, width, height))
        return self.send_request(xcb.Request(buf.getvalue(), 62, True, True),
                                 xcb.VoidCookie())

    def CopyArea(self, src_drawable, dst_drawable, gc, src_x, src_y, dst_x, dst_y, width, height):
        buf = _StringIO()
        buf.write(_pack('=xx2xIIIhhhhHH', src_drawable, dst_drawable, gc, src_x, src_y, dst_x, dst_y, width, height))
        return self.send_request(xcb.Request(buf.getvalue(), 62, True, False),
                                 xcb.VoidCookie())

    def CopyPlaneChecked(self, src_drawable, dst_drawable, gc, src_x, src_y, dst_x, dst_y, width, height, bit_plane):
        buf = _StringIO()
        buf.write(_pack('=xx2xIIIhhhhHHI', src_drawable, dst_drawable, gc, src_x, src_y, dst_x, dst_y, width, height, bit_plane))
        return self.send_request(xcb.Request(buf.getvalue(), 63, True, True),
                                 xcb.VoidCookie())

    def CopyPlane(self, src_drawable, dst_drawable, gc, src_x, src_y, dst_x, dst_y, width, height, bit_plane):
        buf = _StringIO()
        buf.write(_pack('=xx2xIIIhhhhHHI', src_drawable, dst_drawable, gc, src_x, src_y, dst_x, dst_y, width, height, bit_plane))
        return self.send_request(xcb.Request(buf.getvalue(), 63, True, False),
                                 xcb.VoidCookie())

    def PolyPointChecked(self, coordinate_mode, drawable, gc, points_len, points):
        buf = _StringIO()
        buf.write(_pack('=xB2xII', coordinate_mode, drawable, gc))
        for elt in xcb.Iterator(points, 2, 'points', True):
            buf.write(_pack('=hh', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 64, True, True),
                                 xcb.VoidCookie())

    def PolyPoint(self, coordinate_mode, drawable, gc, points_len, points):
        buf = _StringIO()
        buf.write(_pack('=xB2xII', coordinate_mode, drawable, gc))
        for elt in xcb.Iterator(points, 2, 'points', True):
            buf.write(_pack('=hh', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 64, True, False),
                                 xcb.VoidCookie())

    def PolyLineChecked(self, coordinate_mode, drawable, gc, points_len, points):
        buf = _StringIO()
        buf.write(_pack('=xB2xII', coordinate_mode, drawable, gc))
        for elt in xcb.Iterator(points, 2, 'points', True):
            buf.write(_pack('=hh', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 65, True, True),
                                 xcb.VoidCookie())

    def PolyLine(self, coordinate_mode, drawable, gc, points_len, points):
        buf = _StringIO()
        buf.write(_pack('=xB2xII', coordinate_mode, drawable, gc))
        for elt in xcb.Iterator(points, 2, 'points', True):
            buf.write(_pack('=hh', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 65, True, False),
                                 xcb.VoidCookie())

    def PolySegmentChecked(self, drawable, gc, segments_len, segments):
        buf = _StringIO()
        buf.write(_pack('=xx2xII', drawable, gc))
        for elt in xcb.Iterator(segments, 4, 'segments', True):
            buf.write(_pack('=hhhh', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 66, True, True),
                                 xcb.VoidCookie())

    def PolySegment(self, drawable, gc, segments_len, segments):
        buf = _StringIO()
        buf.write(_pack('=xx2xII', drawable, gc))
        for elt in xcb.Iterator(segments, 4, 'segments', True):
            buf.write(_pack('=hhhh', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 66, True, False),
                                 xcb.VoidCookie())

    def PolyRectangleChecked(self, drawable, gc, rectangles_len, rectangles):
        buf = _StringIO()
        buf.write(_pack('=xx2xII', drawable, gc))
        for elt in xcb.Iterator(rectangles, 4, 'rectangles', True):
            buf.write(_pack('=hhHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 67, True, True),
                                 xcb.VoidCookie())

    def PolyRectangle(self, drawable, gc, rectangles_len, rectangles):
        buf = _StringIO()
        buf.write(_pack('=xx2xII', drawable, gc))
        for elt in xcb.Iterator(rectangles, 4, 'rectangles', True):
            buf.write(_pack('=hhHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 67, True, False),
                                 xcb.VoidCookie())

    def PolyArcChecked(self, drawable, gc, arcs_len, arcs):
        buf = _StringIO()
        buf.write(_pack('=xx2xII', drawable, gc))
        for elt in xcb.Iterator(arcs, 6, 'arcs', True):
            buf.write(_pack('=hhHHhh', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 68, True, True),
                                 xcb.VoidCookie())

    def PolyArc(self, drawable, gc, arcs_len, arcs):
        buf = _StringIO()
        buf.write(_pack('=xx2xII', drawable, gc))
        for elt in xcb.Iterator(arcs, 6, 'arcs', True):
            buf.write(_pack('=hhHHhh', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 68, True, False),
                                 xcb.VoidCookie())

    def FillPolyChecked(self, drawable, gc, shape, coordinate_mode, points_len, points):
        buf = _StringIO()
        buf.write(_pack('=xx2xIIBB2x', drawable, gc, shape, coordinate_mode))
        for elt in xcb.Iterator(points, 2, 'points', True):
            buf.write(_pack('=hh', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 69, True, True),
                                 xcb.VoidCookie())

    def FillPoly(self, drawable, gc, shape, coordinate_mode, points_len, points):
        buf = _StringIO()
        buf.write(_pack('=xx2xIIBB2x', drawable, gc, shape, coordinate_mode))
        for elt in xcb.Iterator(points, 2, 'points', True):
            buf.write(_pack('=hh', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 69, True, False),
                                 xcb.VoidCookie())

    def PolyFillRectangleChecked(self, drawable, gc, rectangles_len, rectangles):
        buf = _StringIO()
        buf.write(_pack('=xx2xII', drawable, gc))
        for elt in xcb.Iterator(rectangles, 4, 'rectangles', True):
            buf.write(_pack('=hhHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 70, True, True),
                                 xcb.VoidCookie())

    def PolyFillRectangle(self, drawable, gc, rectangles_len, rectangles):
        buf = _StringIO()
        buf.write(_pack('=xx2xII', drawable, gc))
        for elt in xcb.Iterator(rectangles, 4, 'rectangles', True):
            buf.write(_pack('=hhHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 70, True, False),
                                 xcb.VoidCookie())

    def PolyFillArcChecked(self, drawable, gc, arcs_len, arcs):
        buf = _StringIO()
        buf.write(_pack('=xx2xII', drawable, gc))
        for elt in xcb.Iterator(arcs, 6, 'arcs', True):
            buf.write(_pack('=hhHHhh', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 71, True, True),
                                 xcb.VoidCookie())

    def PolyFillArc(self, drawable, gc, arcs_len, arcs):
        buf = _StringIO()
        buf.write(_pack('=xx2xII', drawable, gc))
        for elt in xcb.Iterator(arcs, 6, 'arcs', True):
            buf.write(_pack('=hhHHhh', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 71, True, False),
                                 xcb.VoidCookie())

    def PutImageChecked(self, format, drawable, gc, width, height, dst_x, dst_y, left_pad, depth, data_len, data):
        buf = _StringIO()
        buf.write(_pack('=xB2xIIHHhhBB2x', format, drawable, gc, width, height, dst_x, dst_y, left_pad, depth))
        buf.write(str(buffer(_array('B', data))))
        return self.send_request(xcb.Request(buf.getvalue(), 72, True, True),
                                 xcb.VoidCookie())

    def PutImage(self, format, drawable, gc, width, height, dst_x, dst_y, left_pad, depth, data_len, data):
        buf = _StringIO()
        buf.write(_pack('=xB2xIIHHhhBB2x', format, drawable, gc, width, height, dst_x, dst_y, left_pad, depth))
        buf.write(str(buffer(_array('B', data))))
        return self.send_request(xcb.Request(buf.getvalue(), 72, True, False),
                                 xcb.VoidCookie())

    def GetImage(self, format, drawable, x, y, width, height, plane_mask):
        buf = _StringIO()
        buf.write(_pack('=xB2xIhhHHI', format, drawable, x, y, width, height, plane_mask))
        return self.send_request(xcb.Request(buf.getvalue(), 73, False, True),
                                 GetImageCookie(),
                                 GetImageReply)

    def GetImageUnchecked(self, format, drawable, x, y, width, height, plane_mask):
        buf = _StringIO()
        buf.write(_pack('=xB2xIhhHHI', format, drawable, x, y, width, height, plane_mask))
        return self.send_request(xcb.Request(buf.getvalue(), 73, False, False),
                                 GetImageCookie(),
                                 GetImageReply)

    def PolyText8Checked(self, drawable, gc, x, y, items_len, items):
        buf = _StringIO()
        buf.write(_pack('=xx2xIIhh', drawable, gc, x, y))
        buf.write(str(buffer(_array('B', items))))
        return self.send_request(xcb.Request(buf.getvalue(), 74, True, True),
                                 xcb.VoidCookie())

    def PolyText8(self, drawable, gc, x, y, items_len, items):
        buf = _StringIO()
        buf.write(_pack('=xx2xIIhh', drawable, gc, x, y))
        buf.write(str(buffer(_array('B', items))))
        return self.send_request(xcb.Request(buf.getvalue(), 74, True, False),
                                 xcb.VoidCookie())

    def PolyText16Checked(self, drawable, gc, x, y, items_len, items):
        buf = _StringIO()
        buf.write(_pack('=xx2xIIhh', drawable, gc, x, y))
        buf.write(str(buffer(_array('B', items))))
        return self.send_request(xcb.Request(buf.getvalue(), 75, True, True),
                                 xcb.VoidCookie())

    def PolyText16(self, drawable, gc, x, y, items_len, items):
        buf = _StringIO()
        buf.write(_pack('=xx2xIIhh', drawable, gc, x, y))
        buf.write(str(buffer(_array('B', items))))
        return self.send_request(xcb.Request(buf.getvalue(), 75, True, False),
                                 xcb.VoidCookie())

    def ImageText8Checked(self, string_len, drawable, gc, x, y, string):
        buf = _StringIO()
        buf.write(_pack('=xB2xIIhh', string_len, drawable, gc, x, y))
        buf.write(str(buffer(_array('b', string))))
        return self.send_request(xcb.Request(buf.getvalue(), 76, True, True),
                                 xcb.VoidCookie())

    def ImageText8(self, string_len, drawable, gc, x, y, string):
        buf = _StringIO()
        buf.write(_pack('=xB2xIIhh', string_len, drawable, gc, x, y))
        buf.write(str(buffer(_array('b', string))))
        return self.send_request(xcb.Request(buf.getvalue(), 76, True, False),
                                 xcb.VoidCookie())

    def ImageText16Checked(self, string_len, drawable, gc, x, y, string):
        buf = _StringIO()
        buf.write(_pack('=xB2xIIhh', string_len, drawable, gc, x, y))
        for elt in xcb.Iterator(string, 2, 'string', True):
            buf.write(_pack('=BB', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 77, True, True),
                                 xcb.VoidCookie())

    def ImageText16(self, string_len, drawable, gc, x, y, string):
        buf = _StringIO()
        buf.write(_pack('=xB2xIIhh', string_len, drawable, gc, x, y))
        for elt in xcb.Iterator(string, 2, 'string', True):
            buf.write(_pack('=BB', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 77, True, False),
                                 xcb.VoidCookie())

    def CreateColormapChecked(self, alloc, mid, window, visual):
        buf = _StringIO()
        buf.write(_pack('=xB2xIII', alloc, mid, window, visual))
        return self.send_request(xcb.Request(buf.getvalue(), 78, True, True),
                                 xcb.VoidCookie())

    def CreateColormap(self, alloc, mid, window, visual):
        buf = _StringIO()
        buf.write(_pack('=xB2xIII', alloc, mid, window, visual))
        return self.send_request(xcb.Request(buf.getvalue(), 78, True, False),
                                 xcb.VoidCookie())

    def FreeColormapChecked(self, cmap):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', cmap))
        return self.send_request(xcb.Request(buf.getvalue(), 79, True, True),
                                 xcb.VoidCookie())

    def FreeColormap(self, cmap):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', cmap))
        return self.send_request(xcb.Request(buf.getvalue(), 79, True, False),
                                 xcb.VoidCookie())

    def CopyColormapAndFreeChecked(self, mid, src_cmap):
        buf = _StringIO()
        buf.write(_pack('=xx2xII', mid, src_cmap))
        return self.send_request(xcb.Request(buf.getvalue(), 80, True, True),
                                 xcb.VoidCookie())

    def CopyColormapAndFree(self, mid, src_cmap):
        buf = _StringIO()
        buf.write(_pack('=xx2xII', mid, src_cmap))
        return self.send_request(xcb.Request(buf.getvalue(), 80, True, False),
                                 xcb.VoidCookie())

    def InstallColormapChecked(self, cmap):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', cmap))
        return self.send_request(xcb.Request(buf.getvalue(), 81, True, True),
                                 xcb.VoidCookie())

    def InstallColormap(self, cmap):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', cmap))
        return self.send_request(xcb.Request(buf.getvalue(), 81, True, False),
                                 xcb.VoidCookie())

    def UninstallColormapChecked(self, cmap):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', cmap))
        return self.send_request(xcb.Request(buf.getvalue(), 82, True, True),
                                 xcb.VoidCookie())

    def UninstallColormap(self, cmap):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', cmap))
        return self.send_request(xcb.Request(buf.getvalue(), 82, True, False),
                                 xcb.VoidCookie())

    def ListInstalledColormaps(self, window):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 83, False, True),
                                 ListInstalledColormapsCookie(),
                                 ListInstalledColormapsReply)

    def ListInstalledColormapsUnchecked(self, window):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 83, False, False),
                                 ListInstalledColormapsCookie(),
                                 ListInstalledColormapsReply)

    def AllocColor(self, cmap, red, green, blue):
        buf = _StringIO()
        buf.write(_pack('=xx2xIHHH2x', cmap, red, green, blue))
        return self.send_request(xcb.Request(buf.getvalue(), 84, False, True),
                                 AllocColorCookie(),
                                 AllocColorReply)

    def AllocColorUnchecked(self, cmap, red, green, blue):
        buf = _StringIO()
        buf.write(_pack('=xx2xIHHH2x', cmap, red, green, blue))
        return self.send_request(xcb.Request(buf.getvalue(), 84, False, False),
                                 AllocColorCookie(),
                                 AllocColorReply)

    def AllocNamedColor(self, cmap, name_len, name):
        buf = _StringIO()
        buf.write(_pack('=xx2xIH2x', cmap, name_len))
        buf.write(str(buffer(_array('b', name))))
        return self.send_request(xcb.Request(buf.getvalue(), 85, False, True),
                                 AllocNamedColorCookie(),
                                 AllocNamedColorReply)

    def AllocNamedColorUnchecked(self, cmap, name_len, name):
        buf = _StringIO()
        buf.write(_pack('=xx2xIH2x', cmap, name_len))
        buf.write(str(buffer(_array('b', name))))
        return self.send_request(xcb.Request(buf.getvalue(), 85, False, False),
                                 AllocNamedColorCookie(),
                                 AllocNamedColorReply)

    def AllocColorCells(self, contiguous, cmap, colors, planes):
        buf = _StringIO()
        buf.write(_pack('=xB2xIHH', contiguous, cmap, colors, planes))
        return self.send_request(xcb.Request(buf.getvalue(), 86, False, True),
                                 AllocColorCellsCookie(),
                                 AllocColorCellsReply)

    def AllocColorCellsUnchecked(self, contiguous, cmap, colors, planes):
        buf = _StringIO()
        buf.write(_pack('=xB2xIHH', contiguous, cmap, colors, planes))
        return self.send_request(xcb.Request(buf.getvalue(), 86, False, False),
                                 AllocColorCellsCookie(),
                                 AllocColorCellsReply)

    def AllocColorPlanes(self, contiguous, cmap, colors, reds, greens, blues):
        buf = _StringIO()
        buf.write(_pack('=xB2xIHHHH', contiguous, cmap, colors, reds, greens, blues))
        return self.send_request(xcb.Request(buf.getvalue(), 87, False, True),
                                 AllocColorPlanesCookie(),
                                 AllocColorPlanesReply)

    def AllocColorPlanesUnchecked(self, contiguous, cmap, colors, reds, greens, blues):
        buf = _StringIO()
        buf.write(_pack('=xB2xIHHHH', contiguous, cmap, colors, reds, greens, blues))
        return self.send_request(xcb.Request(buf.getvalue(), 87, False, False),
                                 AllocColorPlanesCookie(),
                                 AllocColorPlanesReply)

    def FreeColorsChecked(self, cmap, plane_mask, pixels_len, pixels):
        buf = _StringIO()
        buf.write(_pack('=xx2xII', cmap, plane_mask))
        buf.write(str(buffer(_array('I', pixels))))
        return self.send_request(xcb.Request(buf.getvalue(), 88, True, True),
                                 xcb.VoidCookie())

    def FreeColors(self, cmap, plane_mask, pixels_len, pixels):
        buf = _StringIO()
        buf.write(_pack('=xx2xII', cmap, plane_mask))
        buf.write(str(buffer(_array('I', pixels))))
        return self.send_request(xcb.Request(buf.getvalue(), 88, True, False),
                                 xcb.VoidCookie())

    def StoreColorsChecked(self, cmap, items_len, items):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', cmap))
        for elt in xcb.Iterator(items, 5, 'items', True):
            buf.write(_pack('=IHHHBx', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 89, True, True),
                                 xcb.VoidCookie())

    def StoreColors(self, cmap, items_len, items):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', cmap))
        for elt in xcb.Iterator(items, 5, 'items', True):
            buf.write(_pack('=IHHHBx', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 89, True, False),
                                 xcb.VoidCookie())

    def StoreNamedColorChecked(self, flags, cmap, pixel, name_len, name):
        buf = _StringIO()
        buf.write(_pack('=xB2xIIH2x', flags, cmap, pixel, name_len))
        buf.write(str(buffer(_array('b', name))))
        return self.send_request(xcb.Request(buf.getvalue(), 90, True, True),
                                 xcb.VoidCookie())

    def StoreNamedColor(self, flags, cmap, pixel, name_len, name):
        buf = _StringIO()
        buf.write(_pack('=xB2xIIH2x', flags, cmap, pixel, name_len))
        buf.write(str(buffer(_array('b', name))))
        return self.send_request(xcb.Request(buf.getvalue(), 90, True, False),
                                 xcb.VoidCookie())

    def QueryColors(self, cmap, pixels_len, pixels):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', cmap))
        buf.write(str(buffer(_array('I', pixels))))
        return self.send_request(xcb.Request(buf.getvalue(), 91, False, True),
                                 QueryColorsCookie(),
                                 QueryColorsReply)

    def QueryColorsUnchecked(self, cmap, pixels_len, pixels):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', cmap))
        buf.write(str(buffer(_array('I', pixels))))
        return self.send_request(xcb.Request(buf.getvalue(), 91, False, False),
                                 QueryColorsCookie(),
                                 QueryColorsReply)

    def LookupColor(self, cmap, name_len, name):
        buf = _StringIO()
        buf.write(_pack('=xx2xIH2x', cmap, name_len))
        buf.write(str(buffer(_array('b', name))))
        return self.send_request(xcb.Request(buf.getvalue(), 92, False, True),
                                 LookupColorCookie(),
                                 LookupColorReply)

    def LookupColorUnchecked(self, cmap, name_len, name):
        buf = _StringIO()
        buf.write(_pack('=xx2xIH2x', cmap, name_len))
        buf.write(str(buffer(_array('b', name))))
        return self.send_request(xcb.Request(buf.getvalue(), 92, False, False),
                                 LookupColorCookie(),
                                 LookupColorReply)

    def CreateCursorChecked(self, cid, source, mask, fore_red, fore_green, fore_blue, back_red, back_green, back_blue, x, y):
        buf = _StringIO()
        buf.write(_pack('=xx2xIIIHHHHHHHH', cid, source, mask, fore_red, fore_green, fore_blue, back_red, back_green, back_blue, x, y))
        return self.send_request(xcb.Request(buf.getvalue(), 93, True, True),
                                 xcb.VoidCookie())

    def CreateCursor(self, cid, source, mask, fore_red, fore_green, fore_blue, back_red, back_green, back_blue, x, y):
        buf = _StringIO()
        buf.write(_pack('=xx2xIIIHHHHHHHH', cid, source, mask, fore_red, fore_green, fore_blue, back_red, back_green, back_blue, x, y))
        return self.send_request(xcb.Request(buf.getvalue(), 93, True, False),
                                 xcb.VoidCookie())

    def CreateGlyphCursorChecked(self, cid, source_font, mask_font, source_char, mask_char, fore_red, fore_green, fore_blue, back_red, back_green, back_blue):
        buf = _StringIO()
        buf.write(_pack('=xx2xIIIHHHHHHHH', cid, source_font, mask_font, source_char, mask_char, fore_red, fore_green, fore_blue, back_red, back_green, back_blue))
        return self.send_request(xcb.Request(buf.getvalue(), 94, True, True),
                                 xcb.VoidCookie())

    def CreateGlyphCursor(self, cid, source_font, mask_font, source_char, mask_char, fore_red, fore_green, fore_blue, back_red, back_green, back_blue):
        buf = _StringIO()
        buf.write(_pack('=xx2xIIIHHHHHHHH', cid, source_font, mask_font, source_char, mask_char, fore_red, fore_green, fore_blue, back_red, back_green, back_blue))
        return self.send_request(xcb.Request(buf.getvalue(), 94, True, False),
                                 xcb.VoidCookie())

    def FreeCursorChecked(self, cursor):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', cursor))
        return self.send_request(xcb.Request(buf.getvalue(), 95, True, True),
                                 xcb.VoidCookie())

    def FreeCursor(self, cursor):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', cursor))
        return self.send_request(xcb.Request(buf.getvalue(), 95, True, False),
                                 xcb.VoidCookie())

    def RecolorCursorChecked(self, cursor, fore_red, fore_green, fore_blue, back_red, back_green, back_blue):
        buf = _StringIO()
        buf.write(_pack('=xx2xIHHHHHH', cursor, fore_red, fore_green, fore_blue, back_red, back_green, back_blue))
        return self.send_request(xcb.Request(buf.getvalue(), 96, True, True),
                                 xcb.VoidCookie())

    def RecolorCursor(self, cursor, fore_red, fore_green, fore_blue, back_red, back_green, back_blue):
        buf = _StringIO()
        buf.write(_pack('=xx2xIHHHHHH', cursor, fore_red, fore_green, fore_blue, back_red, back_green, back_blue))
        return self.send_request(xcb.Request(buf.getvalue(), 96, True, False),
                                 xcb.VoidCookie())

    def QueryBestSize(self, _class, drawable, width, height):
        buf = _StringIO()
        buf.write(_pack('=xB2xIHH', _class, drawable, width, height))
        return self.send_request(xcb.Request(buf.getvalue(), 97, False, True),
                                 QueryBestSizeCookie(),
                                 QueryBestSizeReply)

    def QueryBestSizeUnchecked(self, _class, drawable, width, height):
        buf = _StringIO()
        buf.write(_pack('=xB2xIHH', _class, drawable, width, height))
        return self.send_request(xcb.Request(buf.getvalue(), 97, False, False),
                                 QueryBestSizeCookie(),
                                 QueryBestSizeReply)

    def QueryExtension(self, name_len, name):
        buf = _StringIO()
        buf.write(_pack('=xx2xH2x', name_len))
        buf.write(str(buffer(_array('b', name))))
        return self.send_request(xcb.Request(buf.getvalue(), 98, False, True),
                                 QueryExtensionCookie(),
                                 QueryExtensionReply)

    def QueryExtensionUnchecked(self, name_len, name):
        buf = _StringIO()
        buf.write(_pack('=xx2xH2x', name_len))
        buf.write(str(buffer(_array('b', name))))
        return self.send_request(xcb.Request(buf.getvalue(), 98, False, False),
                                 QueryExtensionCookie(),
                                 QueryExtensionReply)

    def ListExtensions(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 99, False, True),
                                 ListExtensionsCookie(),
                                 ListExtensionsReply)

    def ListExtensionsUnchecked(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 99, False, False),
                                 ListExtensionsCookie(),
                                 ListExtensionsReply)

    def ChangeKeyboardMappingChecked(self, keycode_count, first_keycode, keysyms_per_keycode, keysyms):
        buf = _StringIO()
        buf.write(_pack('=xB2xBB2x', keycode_count, first_keycode, keysyms_per_keycode))
        buf.write(str(buffer(_array('I', keysyms))))
        return self.send_request(xcb.Request(buf.getvalue(), 100, True, True),
                                 xcb.VoidCookie())

    def ChangeKeyboardMapping(self, keycode_count, first_keycode, keysyms_per_keycode, keysyms):
        buf = _StringIO()
        buf.write(_pack('=xB2xBB2x', keycode_count, first_keycode, keysyms_per_keycode))
        buf.write(str(buffer(_array('I', keysyms))))
        return self.send_request(xcb.Request(buf.getvalue(), 100, True, False),
                                 xcb.VoidCookie())

    def GetKeyboardMapping(self, first_keycode, count):
        buf = _StringIO()
        buf.write(_pack('=xx2xBB', first_keycode, count))
        return self.send_request(xcb.Request(buf.getvalue(), 101, False, True),
                                 GetKeyboardMappingCookie(),
                                 GetKeyboardMappingReply)

    def GetKeyboardMappingUnchecked(self, first_keycode, count):
        buf = _StringIO()
        buf.write(_pack('=xx2xBB', first_keycode, count))
        return self.send_request(xcb.Request(buf.getvalue(), 101, False, False),
                                 GetKeyboardMappingCookie(),
                                 GetKeyboardMappingReply)

    def ChangeKeyboardControlChecked(self, value_mask, value_list):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', value_mask))
        buf.write(str(buffer(_array('I', value_list))))
        return self.send_request(xcb.Request(buf.getvalue(), 102, True, True),
                                 xcb.VoidCookie())

    def ChangeKeyboardControl(self, value_mask, value_list):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', value_mask))
        buf.write(str(buffer(_array('I', value_list))))
        return self.send_request(xcb.Request(buf.getvalue(), 102, True, False),
                                 xcb.VoidCookie())

    def GetKeyboardControl(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 103, False, True),
                                 GetKeyboardControlCookie(),
                                 GetKeyboardControlReply)

    def GetKeyboardControlUnchecked(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 103, False, False),
                                 GetKeyboardControlCookie(),
                                 GetKeyboardControlReply)

    def BellChecked(self, percent):
        buf = _StringIO()
        buf.write(_pack('=xb2x', percent))
        return self.send_request(xcb.Request(buf.getvalue(), 104, True, True),
                                 xcb.VoidCookie())

    def Bell(self, percent):
        buf = _StringIO()
        buf.write(_pack('=xb2x', percent))
        return self.send_request(xcb.Request(buf.getvalue(), 104, True, False),
                                 xcb.VoidCookie())

    def ChangePointerControlChecked(self, acceleration_numerator, acceleration_denominator, threshold, do_acceleration, do_threshold):
        buf = _StringIO()
        buf.write(_pack('=xx2xhhhBB', acceleration_numerator, acceleration_denominator, threshold, do_acceleration, do_threshold))
        return self.send_request(xcb.Request(buf.getvalue(), 105, True, True),
                                 xcb.VoidCookie())

    def ChangePointerControl(self, acceleration_numerator, acceleration_denominator, threshold, do_acceleration, do_threshold):
        buf = _StringIO()
        buf.write(_pack('=xx2xhhhBB', acceleration_numerator, acceleration_denominator, threshold, do_acceleration, do_threshold))
        return self.send_request(xcb.Request(buf.getvalue(), 105, True, False),
                                 xcb.VoidCookie())

    def GetPointerControl(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 106, False, True),
                                 GetPointerControlCookie(),
                                 GetPointerControlReply)

    def GetPointerControlUnchecked(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 106, False, False),
                                 GetPointerControlCookie(),
                                 GetPointerControlReply)

    def SetScreenSaverChecked(self, timeout, interval, prefer_blanking, allow_exposures):
        buf = _StringIO()
        buf.write(_pack('=xx2xhhBB', timeout, interval, prefer_blanking, allow_exposures))
        return self.send_request(xcb.Request(buf.getvalue(), 107, True, True),
                                 xcb.VoidCookie())

    def SetScreenSaver(self, timeout, interval, prefer_blanking, allow_exposures):
        buf = _StringIO()
        buf.write(_pack('=xx2xhhBB', timeout, interval, prefer_blanking, allow_exposures))
        return self.send_request(xcb.Request(buf.getvalue(), 107, True, False),
                                 xcb.VoidCookie())

    def GetScreenSaver(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 108, False, True),
                                 GetScreenSaverCookie(),
                                 GetScreenSaverReply)

    def GetScreenSaverUnchecked(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 108, False, False),
                                 GetScreenSaverCookie(),
                                 GetScreenSaverReply)

    def ChangeHostsChecked(self, mode, family, address_len, address):
        buf = _StringIO()
        buf.write(_pack('=xB2xBxH', mode, family, address_len))
        buf.write(str(buffer(_array('B', address))))
        return self.send_request(xcb.Request(buf.getvalue(), 109, True, True),
                                 xcb.VoidCookie())

    def ChangeHosts(self, mode, family, address_len, address):
        buf = _StringIO()
        buf.write(_pack('=xB2xBxH', mode, family, address_len))
        buf.write(str(buffer(_array('B', address))))
        return self.send_request(xcb.Request(buf.getvalue(), 109, True, False),
                                 xcb.VoidCookie())

    def ListHosts(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 110, False, True),
                                 ListHostsCookie(),
                                 ListHostsReply)

    def ListHostsUnchecked(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 110, False, False),
                                 ListHostsCookie(),
                                 ListHostsReply)

    def SetAccessControlChecked(self, mode):
        buf = _StringIO()
        buf.write(_pack('=xB2x', mode))
        return self.send_request(xcb.Request(buf.getvalue(), 111, True, True),
                                 xcb.VoidCookie())

    def SetAccessControl(self, mode):
        buf = _StringIO()
        buf.write(_pack('=xB2x', mode))
        return self.send_request(xcb.Request(buf.getvalue(), 111, True, False),
                                 xcb.VoidCookie())

    def SetCloseDownModeChecked(self, mode):
        buf = _StringIO()
        buf.write(_pack('=xB2x', mode))
        return self.send_request(xcb.Request(buf.getvalue(), 112, True, True),
                                 xcb.VoidCookie())

    def SetCloseDownMode(self, mode):
        buf = _StringIO()
        buf.write(_pack('=xB2x', mode))
        return self.send_request(xcb.Request(buf.getvalue(), 112, True, False),
                                 xcb.VoidCookie())

    def KillClientChecked(self, resource):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', resource))
        return self.send_request(xcb.Request(buf.getvalue(), 113, True, True),
                                 xcb.VoidCookie())

    def KillClient(self, resource):
        buf = _StringIO()
        buf.write(_pack('=xx2xI', resource))
        return self.send_request(xcb.Request(buf.getvalue(), 113, True, False),
                                 xcb.VoidCookie())

    def RotatePropertiesChecked(self, window, atoms_len, delta, atoms):
        buf = _StringIO()
        buf.write(_pack('=xx2xIHh', window, atoms_len, delta))
        buf.write(str(buffer(_array('I', atoms))))
        return self.send_request(xcb.Request(buf.getvalue(), 114, True, True),
                                 xcb.VoidCookie())

    def RotateProperties(self, window, atoms_len, delta, atoms):
        buf = _StringIO()
        buf.write(_pack('=xx2xIHh', window, atoms_len, delta))
        buf.write(str(buffer(_array('I', atoms))))
        return self.send_request(xcb.Request(buf.getvalue(), 114, True, False),
                                 xcb.VoidCookie())

    def ForceScreenSaverChecked(self, mode):
        buf = _StringIO()
        buf.write(_pack('=xB2x', mode))
        return self.send_request(xcb.Request(buf.getvalue(), 115, True, True),
                                 xcb.VoidCookie())

    def ForceScreenSaver(self, mode):
        buf = _StringIO()
        buf.write(_pack('=xB2x', mode))
        return self.send_request(xcb.Request(buf.getvalue(), 115, True, False),
                                 xcb.VoidCookie())

    def SetPointerMapping(self, map_len, map):
        buf = _StringIO()
        buf.write(_pack('=xB2x', map_len))
        buf.write(str(buffer(_array('B', map))))
        return self.send_request(xcb.Request(buf.getvalue(), 116, False, True),
                                 SetPointerMappingCookie(),
                                 SetPointerMappingReply)

    def SetPointerMappingUnchecked(self, map_len, map):
        buf = _StringIO()
        buf.write(_pack('=xB2x', map_len))
        buf.write(str(buffer(_array('B', map))))
        return self.send_request(xcb.Request(buf.getvalue(), 116, False, False),
                                 SetPointerMappingCookie(),
                                 SetPointerMappingReply)

    def GetPointerMapping(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 117, False, True),
                                 GetPointerMappingCookie(),
                                 GetPointerMappingReply)

    def GetPointerMappingUnchecked(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 117, False, False),
                                 GetPointerMappingCookie(),
                                 GetPointerMappingReply)

    def SetModifierMapping(self, keycodes_per_modifier, keycodes):
        buf = _StringIO()
        buf.write(_pack('=xB2x', keycodes_per_modifier))
        buf.write(str(buffer(_array('B', keycodes))))
        return self.send_request(xcb.Request(buf.getvalue(), 118, False, True),
                                 SetModifierMappingCookie(),
                                 SetModifierMappingReply)

    def SetModifierMappingUnchecked(self, keycodes_per_modifier, keycodes):
        buf = _StringIO()
        buf.write(_pack('=xB2x', keycodes_per_modifier))
        buf.write(str(buffer(_array('B', keycodes))))
        return self.send_request(xcb.Request(buf.getvalue(), 118, False, False),
                                 SetModifierMappingCookie(),
                                 SetModifierMappingReply)

    def GetModifierMapping(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 119, False, True),
                                 GetModifierMappingCookie(),
                                 GetModifierMappingReply)

    def GetModifierMappingUnchecked(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 119, False, False),
                                 GetModifierMappingCookie(),
                                 GetModifierMappingReply)

    def NoOperationChecked(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 127, True, True),
                                 xcb.VoidCookie())

    def NoOperation(self, ):
        buf = _StringIO()
        buf.write(_pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 127, True, False),
                                 xcb.VoidCookie())


xcb._add_core(xprotoExtension, Setup, _EVENTS, _ERRORS)
from xcb2.xproto.xconnection import connect, Connection



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
