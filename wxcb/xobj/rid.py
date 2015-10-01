#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""rid -- DESCRIPTION

"""
from userint import UserInt
from struct import pack

from wxcb.conn import connect


class Id(UserInt):
    r"""Id

    Id is a UserInt.
    Responsibility:
    """

    def kill_client(self, display):
        r"""SUMMARY

        kill_client(display)

        @Arguments:
        - `display`:

        @Return:

        @Error:
        """
        return connect(display).core.KillClient(self._value)

    def pack(self, ):
        r"""SUMMARY

        pack()

        @Return:

        @Error:
        """
        return pack('I', self._value)

    def getgeometry(self, display):
        r"""SUMMARY

        getgeometry(display)

        @Arguments:
        - `display`:

        @Return:

        @Error:
        """
        return connect(display).core.GetGeometry(self._value)

    def createpixmap(self, display, depth, pid, width, height):
        r"""SUMMARY

        createpixmap(display, depth, pid, width, height)

        @Arguments:
        - `display`:
        - `depth`:
        - `pid`:
        - `width`:
        - `height`:

        @Return:

        @Error:
        """
        return connect(display).core.CreatePixmap(
            depth, pid, self._value, width, height)

    def creategc(self, display, cid, value_mask, value_list):
        r"""SUMMARY

        creategc(display, cid, value_mask, value_list)

        @Arguments:
        - `display`:
        - `cid`:
        - `value_mask`:
        - `value_list`:

        @Return:

        @Error:
        """
        return connect(display).core.CreateGC(
            cid, self._value, value_mask, value_list)

    def copyarea(self, display, gc, dst_drawable, src_x, src_y, width, height,
                 dst_x, dst_y):
        r"""SUMMARY

        copyarea(display, gc, dst_drawable, src_x, src_y, width, height, dst_x, dst_y)

        @Arguments:
        - `display`:
        - `gc`:
        - `dst_drawable`:
        - `src_x`:
        - `src_y`:
        - `width`:
        - `height`:
        - `dst_x`:
        - `dst_y`:

        @Return:

        @Error:
        """
        return connect(display).core.CopyArea(
            self._value, dst_drawable, gc, src_x, src_y, dst_x, dst_y,
            width, height)

    def copyplane(self, display, gc, dst_drawable, src_x, src_y, width, height,
                   dst_x, dst_y, bit_plane):
        r"""SUMMARY

        copyplane(display, gc, dst_drawable, src_x, src_y, width, height,
                   dst_x, dst_y, bit_plane)

        @Arguments:
        - `display`:
        - `gc`:
        - `dst_drawable`:
        - `src_x`:
        - `src_y`:
        - `width`:
        - `height`:
        - `dst_x`:
        - `dst_y`:
        - `bit_plane`:

        @Return:

        @Error:
        """
        return connect(display).core.CopyPlane(
            self._value, gc, dst_drawable, src_x, src_y, width, height,
            dst_x, dst_y, bit_plane)

    def polypoint(self, display, coordinate_mode, gc, points_len, points):
        r"""SUMMARY

        polypoint(display, coordinate_mode, gc, points_len, points)

        @Arguments:
        - `display`:
        - `coordinate_mode`:
        - `gc`:
        - `points_len`:
        - `points`:

        @Return:

        @Error:
        """
        return connect(display).core.PolyPoint(
            coordinate_mode, self._value, gc, points_len, points)

    def polyline(self, display, coordinate_mode, gc, points_len, points):
        r"""SUMMARY

        polyline(display, coordinate_mode, gc, points_len, points)

        @Arguments:
        - `display`:
        - `coordinate_mode`:
        - `gc`:
        - `points_len`:
        - `points`:

        @Return:

        @Error:
        """
        return connect(display).core.PolyLine(
            coordinate_mode, self._value, gc, points_len, points)

    def polysegment(self, display, gc, segments_len, segments):
        r"""SUMMARY

        polysegment(display, gc, segments_len, segments)

        @Arguments:
        - `display`:
        - `gc`:
        - `segments_len`:
        - `segments`:

        @Return:

        @Error:
        """
        return connect(display).core.PolySegment(
            self._value, gc, segments_len, segments)

    def polyrectangle(self, display, gc, rectangles_len, rectangles):
        r"""SUMMARY

        polyrectangle(display, gc, rectangles_len, rectangles)

        @Arguments:
        - `display`:
        - `gc`:
        - `rectangles_len`:
        - `rectangles`:

        @Return:

        @Error:
        """
        return connect(display).core.PolyRectangle(
            self._value, gc, rectangles_len, rectangles)

    def polyarc(self, display, gc, arcs_len, arcs):
        r"""SUMMARY

        polyarc(display, gc, arcs_len, arcs)

        @Arguments:
        - `display`:
        - `gc`:
        - `arcs_len`:
        - `arcs`:

        @Return:

        @Error:
        """
        return connect(display).core.PolyArc(self._value, gc, arcs_len, arcs)

    def fillpoly(self, display, gc, shape, coordinate_mode, points_len, points):
        r"""SUMMARY

        fillpoly(display, gc, shape, coordinate_mode, points_len, points)

        @Arguments:
        - `display`:
        - `gc`:
        - `shape`:
        - `coordinate_mode`:
        - `points_len`:
        - `points`:

        @Return:

        @Error:
        """
        return connect(display).core.FillPoly(
            self._value, gc, shape, coordinate_mode, points_len, points)

    def polyfillrectangle(self, display, gc, rectangles_len, rectangles):
        r"""SUMMARY

        polyfillrectangle(display, gc, rectangles_len, rectangles)

        @Arguments:
        - `display`:
        - `gc`:
        - `rectangles_len`:
        - `rectangles`:

        @Return:

        @Error:
        """
        return connect(display).core.PolyFillRectangle(
            self._value, gc, rectangles_len, rectangles)

    def polyfillarc(self, display, gc, arcs_len, arcs):
        r"""SUMMARY

        polyfillarc(display, gc, arcs_len, arcs)

        @Arguments:
        - `display`:
        - `gc`:
        - `arcs_len`:
        - `arcs`:

        @Return:

        @Error:
        """
        return connect(display).core.PolyFillArc(
            self._value, gc, arcs_len, arcs)

    def putimage(self, display, format, gc, width, height, dst_x, dst_y,
                 left_pad, depth, data_len, data):
        r"""SUMMARY

        putimage(display, format, gc, width, height, dst_x, dst_y, left_pad,
                  depth, data_len, data)

        @Arguments:
        - `display`:
        - `format`:
        - `gc`:
        - `width`:
        - `height`:
        - `dst_x`:
        - `dst_y`:
        - `left_pad`:
        - `depth`:
        - `data_len`:
        - `data`:

        @Return:

        @Error:
        """
        return connect(display).core.PutImage(
            format, self._value, gc, width, height, dst_x, dst_y, left_pad,
            depth, data_len, data)

    def getimage(self, display, format, x, y, width, height, plane_mask):
        r"""SUMMARY

        getimage(display, format, x, y, width, height, plane_mask)

        @Arguments:
        - `display`:
        - `format`:
        - `x`:
        - `y`:
        - `width`:
        - `height`:
        - `plane_mask`:

        @Return:

        @Error:
        """
        return connect(display).core.GetImage(
            format, self._value, x, y, width, height, plane_mask)

    def polytext8(self, display, gc, x, y, items_len, items):
        r"""SUMMARY

        polytext8(display, gc, x, y, items_len, items)

        @Arguments:
        - `display`:
        - `gc`:
        - `x`:
        - `y`:
        - `items_len`:
        - `items`:

        @Return:

        @Error:
        """
        return connect(display).core.PolyText8(
             self._value, gc, x, y, items_len, items)

    def polytext16(self, display, gc, x, y, items_len, items):
        r"""SUMMARY

        polytext16(display, gc, x, y, items_len, items)

        @Arguments:
        - `display`:
        - `gc`:
        - `x`:
        - `y`:
        - `items_len`:
        - `items`:

        @Return:

        @Error:
        """
        return connect(display).core.PolyText16(
             self._value, gc, x, y, items_len, items)

    def imagetext8(self, display, string_len, gc, x, y, string):
        r"""SUMMARY

        imagetext8(display, string_len, gc, x, y, string)

        @Arguments:
        - `display`:
        - `string_len`:
        - `gc`:
        - `x`:
        - `y`:
        - `string`:

        @Return:

        @Error:
        """
        return connect(display).core.ImageText8(
            string_len, self._value, gc, x, y, string)

    def imagetext16(self, display, string_len, gc, x, y, string):
        r"""SUMMARY

        imagetext16(display, string_len, gc, x, y, string)

        @Arguments:
        - `display`:
        - `string_len`:
        - `gc`:
        - `x`:
        - `y`:
        - `string`:

        @Return:

        @Error:
        """
        return connect(display).core.ImageText16(
            string_len, self._value, gc, x, y, string)

    def querybestsize(self, display, _class, width, height):
        r"""SUMMARY

        querybestsize(display, _class, width, height)

        @Arguments:
        - `display`:
        - `_class`:
        - `width`:
        - `height`:

        @Return:

        @Error:
        """
        return connect(display).core.QueryBestSize(
            _class, self._value, width, height)

    def createwindow(self, display, depth, parent, x, y, width, height,
                     border_width, class_, visual, value_mask, value_list):
        r"""SUMMARY

        createwindow(display, depth, parent, x, y, width, height, border_width,
                     class_, visual, value_mask, value_list)

        @Arguments:
        - `display`:
        - `depth`:
        - `parent`:
        - `x`:
        - `y`:
        - `width`:
        - `height`:
        - `border_width`:
        - `class_`:
        - `visual`:
        - `value_mask`:
        - `value_list`:

        @Return:

        @Error:
        """
        return connect(display).core.CreateWindow(
            depth, self._value, parent, x, y, width, height, border_width,
            class_, visual, value_mask, value_list)

    def configurewindow(self, display, value_mask, value_list):
        r"""SUMMARY

        configurewindow(display, value_mask, value_list)

        @Arguments:
        - `display`:
        - `value_mask`:
        - `value_list`:

        @Return:

        @Error:
        """
        return connect(display).core.ConfigureWindow(
            self._value, value_mask, value_list)

    def cleararea(self, display, exposures, x, y, width, height):
        r"""SUMMARY

        cleararea(display, exposures, x, y, width, height)

        @Arguments:
        - `display`:
        - `exposures`:
        - `x`:
        - `y`:
        - `width`:
        - `height`:

        @Return:

        @Error:
        """
        return connect(display).core.ClearArea(
            exposures, self._value, x, y, width, height)

    def reparentwindow(self, display, parent, x, y):
        r"""SUMMARY

        reparentwindow(display, parent, x, y)

        @Arguments:
        - `display`:
        - `parent`:
        - `x`:
        - `y`:

        @Return:

        @Error:
        """
        return connect(display).core.ReparentWindow(
            self._value, parent, x, y)

    def getwindowattributes(self, display):
        r"""SUMMARY

        getwindowattributes(display)

        @Arguments:
        - `display`:

        @Return:

        @Error:
        """
        return connect(display).core.GetWindowAttributes(self._value)

    def changewindowattributes(self, display, value_mask, value_list):
        r"""SUMMARY

        changewindowattributes(display, value_mask, value_list)

        @Arguments:
        - `display`:
        - `value_mask`:
        - `value_list`:

        @Return:

        @Error:
        """
        return connect(display).core.ChangeWindowAttributes(
            self._value, value_mask, value_list)

    def createcolormap(self, display, alloc, mid, visual):
        r"""SUMMARY

        createcolormap(display, alloc, mid, visual)

        @Arguments:
        - `display`:
        - `alloc`:
        - `mid`:
        - `visual`:

        @Return:

        @Error:
        """
        return connect(display).core.CreateColormap(
            alloc, mid, self._value, visual)

    def listinstalledcolormaps(self, display):
        r"""SUMMARY

        listinstalledcolormaps(display)

        @Return:

        @Error:
        """
        return connect(display).core.ListInstalledColormaps(self._value)

    def circulatewindow(self, display, direction):
        r"""SUMMARY

        circulatewindow(display, direction)

        @Arguments:
        - `display`:
        - `direction`:

        @Return:

        @Error:
        """
        return connect(display).core.CirculateWindow(
            direction, self._value)

    def circulatewindow(self, display, direction):
        r"""SUMMARY

        circulatewindow(display, direction)

        @Arguments:
        - `display`:
        - `direction`:

        @Return:

        @Error:
        """
        return connect(display).core.CirculateWindow(direction, self._value)

    def changesaveset(self, display, mode):
        r"""SUMMARY

        changesaveset(display, mode)

        @Arguments:
        - `display`:
        - `mode`:

        @Return:

        @Error:
        """
        return connect(display).core.ChangeSaveSet(mode, self._value)

    def convertselection(self, display, requestor, selection, property, time):
        r"""SUMMARY

        convertselection(display, requestor, selection, property, time)

        @Arguments:
        - `display`:
        - `requestor`:
        - `selection`:
        - `property`:
        - `time`:

        @Return:

        @Error:
        """
        return connect(display).core.ConvertSelection(
            requestor, selection, self._value, property, time)

    def translatecoordinates(self, display, dst_window, src_x, src_y):
        r"""SUMMARY

        translatecoordinates(display, dst_window, src_x, src_y)

        @Arguments:
        - `display`:
        - `dst_window`:
        - `src_x`:
        - `src_y`:

        @Return:

        @Error:
        """
        return connect(display).core.TranslateCoordinates(
            self._value, dst_window, src_x, src_y)

    def getmotionevents(self, display, start, stop):
        r"""SUMMARY

        getmotionevents(display, start, stop)

        @Arguments:
        - `display`:
        - `start`:
        - `stop`:

        @Return:

        @Error:
        """
        return connect(display).core.GetMotionEvents(self._value, start, stop)

    def setinputfocus(self, display, revert_to, time):
        r"""SUMMARY

        setinputfocus(display, revert_to, time)

        @Arguments:
        - `display`:
        - `revert_to`:
        - `time`:

        @Return:

        @Error:
        """
        return connect(display).core.SetInputFocus(revert_to, self._value, time)

    def setselectionowner(self, display, owner, time):
        r"""SUMMARY

        setselectionowner(display, owner, time)

        @Arguments:
        - `display`:
        - `owner`:
        - `time`:

        @Return:

        @Error:
        """
        return connect(display).core.SetSelectionOwner(owner, self._value, time)

    def sendevent(self, display, propagate, event_mask, event):
        r"""SUMMARY

        sendevent(display, propagate, event_mask, event)

        @Arguments:
        - `display`:
        - `propagate`:
        - `event_mask`:
        - `event`:

        @Return:

        @Error:
        """
        return connect(display).core.SendEvent(
            propagate, self._value, event_mask, event)

    def mapwindow(self, display):
        r"""SUMMARY

        mapwindow(display)

        @Return:

        @Error:
        """
        return connect(display).core.MapWindow(self._value)

    def mapsubwindows(self, display):
        r"""SUMMARY

        mapsubwindows(display)

        @Arguments:
        - `display`:

        @Return:

        @Error:
        """
        return connect(display).core.MapSubwindows(self._value)

    def unmapwindow(self, display):
        r"""SUMMARY

        unmapwindow(display)

        @Arguments:
        - `display`:

        @Return:

        @Error:
        """
        return connect(display).core.UnmapWindow(self._value)

    def unmapsubwindows(self, display):
        r"""SUMMARY

        unmapsubwindows(display)

        @Arguments:
        - `display`:

        @Return:

        @Error:
        """
        return connect(display).core.UnmapSubwindows(self._value)

    def destroywindow(self, display):
        r"""SUMMARY

        destroywindow(display)

        @Arguments:
        - `display`:

        @Return:

        @Error:
        """
        return connect(display).core.DestroyWindow(self._value)

    def destroysubwindows(self, display):
        r"""SUMMARY

        destroysubwindows(display)

        @Arguments:
        - `display`:

        @Return:

        @Error:
        """
        return connect(display).core.DestroySubwindows(self._value)

    def querytree(self, display):
        r"""SUMMARY

        querytree(display)

        @Arguments:
        - `display`:

        @Return:

        @Error:
        """
        return connect(display).core.QueryTree(self._value)

    def getproperty(self, display, delete, property, type, long_offset,
                    long_length):
        r"""SUMMARY

        getproperty(display, delete, property, type, long_offset, long_length)

        @Arguments:
        - `display`:
        - `delete`:
        - `property`:
        - `type`:
        - `long_offset`:
        - `long_length`:

        @Return:

        @Error:
        """
        return connect(display).core.GetProperty(
            delete, self._value, property, type, long_offset, long_length)

    def changeproperty(self, display, mode, property, type, format, data_len,
                       data):
        r"""SUMMARY

        changeproperty(display, mode, property, type, format, data_len, data)

        @Arguments:
        - `display`:
        - `mode`:
        - `property`:
        - `type`:
        - `format`:
        - `data_len`:
        - `data`:

        @Return:

        @Error:
        """
        return connect(display).core.ChangeProperty(
            mode, self._value, property, type, format, data_len, data)

    def listproperties(self, display):
        r"""SUMMARY

        listproperties(display)

        @Arguments:
        - `display`:

        @Return:

        @Error:
        """
        return connect(display).core.ListProperties(self._value)

    def deleteproperty(self, display, property):
        r"""SUMMARY

        deleteproperty(display, property)

        @Arguments:
        - `display`:
        - `property`:

        @Return:

        @Error:
        """
        return connect(display).core.DeleteProperty(
            self._value, property)

    def rotateproperties(self, display, atoms_len, delta, atoms):
        r"""SUMMARY

        rotateproperties(display, atoms_len, delta, atoms)

        @Arguments:
        - `display`:
        - `atoms_len`:
        - `delta`:
        - `atoms`:

        @Return:

        @Error:
        """
        return connect(display).core.RotateProperties(
            self._value, atoms_len, delta, atoms)

    def grabkeyboard(self, display, owner_events, time, pointer_mode,
                     keyboard_mode):
        r"""SUMMARY

        grabkeyboard(display, owner_events, time, pointer_mode, keyboard_mode)

        @Arguments:
        - `display`:
        - `owner_events`:
        - `time`:
        - `pointer_mode`:
        - `keyboard_mode`:

        @Return:

        @Error:
        """
        return connect(display).core.GrabKeyboard(
            owner_events, self._value, time, pointer_mode, keyboard_mode)

    def grabkey(self, display, owner_events, modifiers, key, pointer_mode,
                keyboard_mode):
        r"""SUMMARY

        grabkey(display, owner_events, modifiers, key, pointer_mode, keyboard_mode)

        @Arguments:
        - `display`:
        - `owner_events`:
        - `modifiers`:
        - `key`:
        - `pointer_mode`:
        - `keyboard_mode`:

        @Return:

        @Error:
        """
        return connect(display).core.GrabKey(
            owner_events, self._value, modifiers, key, pointer_mode,
            keyboard_mode)

    def ungrabkey(self, display, key, modifiers):
        r"""SUMMARY

        ungrabkey(display, key, modifiers)

        @Arguments:
        - `display`:
        - `key`:
        - `modifiers`:

        @Return:

        @Error:
        """
        return connect(display).core.UngrabKey(key, self._value, modifiers)

    def grabbutton(self, display, owner_events, event_mask, pointer_mode,
                   keyboard_mode, confine_to, cursor, button, modifiers):
        r"""SUMMARY

        grabbutton(display,owner_events, event_mask, pointer_mode, keyboard_mode,
                   confine_to, cursor, button, modifiers)

        @Arguments:
        - `owner_events`:
        - `event_mask`:
        - `pointer_mode`:
        - `keyboard_mode`:
        - `confine_to`:
        - `cursor`:
        - `button`:
        - `modifiers`:

        @Return:

        @Error:
        """
        return connect(display).core.GrabButton(
            owner_events, self._value, event_mask, pointer_mode, keyboard_mode,
            confine_to, cursor, button, modifiers)

    def ungrabbutton(self, display, button, modifiers):
        r"""SUMMARY

        ungrabbutton(display, button, modifiers)

        @Arguments:
        - `display`:
        - `button`:
        - `modifiers`:

        @Return:

        @Error:
        """
        return connect(display).core.UngrabButton(
            button, self._value, modifiers)

    def grabpointer(self, display, owner_events, event_mask, pointer_mode,
                    keyboard_mode, confine_to, cursor, time):
        r"""SUMMARY

        grabpointer(display, owner_events, event_mask, pointer_mode,
                    keyboard_mode, confine_to, cursor, time)

        @Arguments:
        - `display`:
        - `owner_events`:
        - `event_mask`:
        - `pointer_mode`:
        - `keyboard_mode`:
        - `confine_to`:
        - `cursor`:
        - `time`:

        @Return:

        @Error:
        """
        return connect(display).core.GrabPointer(
            owner_events, self._value, event_mask, pointer_mode, keyboard_mode,
            confine_to, cursor, time)

    def querypointer(self, display):
        r"""SUMMARY

        querypointer(display)

        @Arguments:
        - `display`:

        @Return:

        @Error:
        """
        return connect(display).core.GrabPointer(self._value)

    def warppointer(self, display, dst_window, src_x, src_y, src_width,
                    src_height, dst_x, dst_y):
        r"""SUMMARY

        warppointer(display, dst_window, src_x, src_y, src_width, src_height,
                    dst_x, dst_y)

        @Arguments:
        - `display`:
        - `dst_window`:
        - `src_x`:
        - `src_y`:
        - `src_width`:
        - `src_height`:
        - `dst_x`:
        - `dst_y`:

        @Return:

        @Error:
        """
        return connect(display).core.WarpPointer(
            self._value, dst_window, src_x, src_y, src_width, src_height,
            dst_x, dst_y)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# rid.py ends here
