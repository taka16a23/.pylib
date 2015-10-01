#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: window.py 306 2015-02-07 03:48:07Z t1 $
# $Revision: 306 $
# $Date: 2015-02-07 12:48:07 +0900 (Sat, 07 Feb 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-02-07 12:48:07 +0900 (Sat, 07 Feb 2015) $

r"""window -- DESCRIPTION

"""
import wxcb.xobj.drawable as _drawable


class Window(_drawable.Drawable):
    r"""Window

    Window is a _drawable.Drawable.
    Responsibility:
    """
    def create(self, depth, parent, x, y, width, height, border_width,
               class_, visual, value_mask, value_list):
        r"""SUMMARY

        create(depth, parent, x, y, width, height, border_width, class_,
        visual, value_mask, value_list)

        @Arguments:
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
        """
        return self.id.createwindow(
            self.display, depth, parent, x, y, width, height, border_width,
            class_, visual, value_mask, value_list)

    def configure(self, value_mask, value_list):
        r"""SUMMARY

        configure(value_mask, value_list)

        @Arguments:
        - `value_mask`:
        - `value_list`:

        @Return:
        """
        return self.id.configurewindow(self.display, value_mask, value_list)

    def cleararea(self, exposures, x, y, width, height):
        r"""SUMMARY

        cleararea(exposures, x, y, width, height)

        @Arguments:
        - `exposures`:
        - `x`:
        - `y`:
        - `width`:
        - `height`:

        @Return:
        """
        return self.id.cleararea(self.display, exposures, x, y, width, height)

    def reparent(self, parent, x, y):
        r"""SUMMARY

        reparent(parent, x, y)

        @Arguments:
        - `parent`:
        - `x`:
        - `y`:

        @Return:
        """
        return self.id.reparentwindow(self.display, parent, x, y)

    def getattributes(self, ):
        r"""SUMMARY

        get_attributes()

        @Return:
        """
        return self.id.getwindowattributes(self.display)

    def changeattributes(self, value_mask, value_list):
        r"""SUMMARY

        change_attributes(value_mask, value_list)

        @Arguments:
        - `value_mask`:
        - `value_list`:

        @Return:
        """
        return self.id.changewindowattributes(
            self.display, value_mask, value_list)

    def createcolormap(self, alloc, mid, visual):
        r"""SUMMARY

        create_colormap(alloc, mid, visual)

        @Arguments:
        - `alloc`:
        - `mid`:
        - `visual`:

        @Return:
        """
        return self.id.createcolormap(self.display, alloc, mid, visual)

    def listinstalledcolormaps(self, ):
        r"""SUMMARY

        list_installed_colormaps()

        @Return:
        """
        return self.id.listinstalledcolormaps(self.display)

    def circulate(self, direction):
        r"""SUMMARY

        circulate(direction)

        @Arguments:
        - `direction`:

        @Return:
        """
        return self.id.circulatewindow(self.display, direction)

    def changesaveset(self, mode):
        r"""SUMMARY

        change_save_set(mode)

        @Arguments:
        - `mode`:

        @Return:
        """
        return self.id.changesaveset(self.display, mode)

    def convertselection(self, requestor, selection, property, time):
        r"""SUMMARY

        convert_selection(requestor, selection, property, time)

        @Arguments:
        - `requestor`:
        - `selection`:
        - `property`:
        - `time`:

        @Return:
        """
        return self.id.convertselection(
            self.display, requestor, selection, property, time)

    def translatecoordinates(self, dst_window, src_x, src_y):
        r"""SUMMARY

        translatecoordinates(dst_window, src_x, src_y)

        @Arguments:
        - `dst_window`:
        - `src_x`:
        - `src_y`:

        @Return:
        """
        return self.id.convertselection(self.display, dst_window, src_x, src_y)

    def getmotionevents(self, start, stop):
        r"""SUMMARY

        get_motion_events(start, stop)

        @Arguments:
        - `start`:
        - `stop`:

        @Return:
        """
        return self.id.getmotionevents(self.display, start, stop)

    def setinputfocus(self, revert_to, time):
        r"""SUMMARY

        set_input_focus(revert_to, time)

        @Arguments:
        - `revert_to`:
        - `time`:

        @Return:
        """
        return self.id.setinputfocus(self.display, revert_to, time)

    def setselectionowner(self, owner, time):
        r"""SUMMARY

        set_selection_owner(owner, time)

        @Arguments:
        - `owner`:
        - `time`:

        @Return:
        """
        return self.id.setselectionowner(self.display, owner, time)

    def sendevent(self, propagate, event_mask, event):
        r"""SUMMARY

        sendevent(propagate, event_mask, event)

        @Arguments:
        - `propagate`:
        - `event_mask`:
        - `event`:

        @Return:
        """
        return self.id.sendevent(self.display, propagate, event_mask, event)

    def map(self, ):
        r"""SUMMARY

        map()

        @Return:
        """
        return self.id.mapwindow(self.display)

    def mapsubwindows(self, ):
        r"""SUMMARY

        mapsubwindows()

        @Return:
        """
        return self.id.mapsubwindows(self.display)

    def unmap(self, ):
        r"""SUMMARY

        unmap()

        @Return:
        """
        return self.id.unmapwindow(self.display)

    def unmapsubwindows(self, ):
        r"""SUMMARY

        unmapsubwindows()

        @Return:
        """
        return self.id.unmapsubwindows(self.display)

    def destroy(self, ):
        r"""SUMMARY

        destroy()

        @Return:
        """
        return self.id.destroywindow(self.display)

    def destroysubwindows(self, ):
        r"""SUMMARY

        destroysubwindows()

        @Return:
        """
        return self.id.destroysubwindows(self.display)

    def querytree(self, ):
        r"""SUMMARY

        querytree()

        @Return:
        """
        return self.id.querytree(self.display)

    def getproperty(self, delete, property, type, long_offset, long_length):
        r"""SUMMARY

        getproperty(delete, property, type, long_offset, long_length)

        @Arguments:
        - `delete`:
        - `property`:
        - `type`:
        - `long_offset`:
        - `long_length`:

        @Return:
        """
        return self.id.getproperty(
            self.display, delete, property, type, long_offset, long_length)

    def changeproperty(self, mode, property, type, format, data_len, data):
        r"""SUMMARY

        changeproperty(mode, property, type, format, data_len, data)

        @Arguments:
        - `mode`:
        - `property`:
        - `type`:
        - `format`:
        - `data_len`:
        - `data`:

        @Return:
        """
        return self.id.changeproperty(
            self.display, mode, property, type, format, data_len, data)

    def listproperties(self, ):
        r"""SUMMARY

        listproperties()

        @Return:
        """
        return self.id.listproperties(self.display)

    def deleteproperty(self, property):
        r"""SUMMARY

        deleteproperty(property)

        @Arguments:
        - `property`:

        @Return:
        """
        return self.id.deleteproperty(self.display, property)

    def rotateproperties(self, atoms_len, delta, atoms):
        r"""SUMMARY

        rotateproperties(atoms_len, delta, atoms)

        @Arguments:
        - `atoms_len`:
        - `delta`:
        - `atoms`:

        @Return:
        """
        return self.id.rotateproperties(self.display, atoms_len, delta, atoms)

    def grabkeyboard(self, owner_events, time, pointer_mode, keyboard_mode):
        r"""SUMMARY

        grabkeyboard(owner_events, time, pointer_mode, keyboard_mode)

        @Arguments:
        - `owner_events`:
        - `time`:
        - `pointer_mode`:
        - `keyboard_mode`:

        @Return:
        """
        return self.id.grabkeyboard(
            self.display, owner_events, time, pointer_mode, keyboard_mode)

    def grabkey(self, owner_events, modifiers, key,
                pointer_mode, keyboard_mode):
        r"""SUMMARY

        grabkey(owner_events, modifiers, key, pointer_mode, keyboard_mode)

        @Arguments:
        - `owner_events`:
        - `modifiers`:
        - `key`:
        - `pointer_mode`:
        - `keyboard_mode`:

        @Return:
        """
        return self.id.grabkey(self.display, owner_events, modifiers, key,
                               pointer_mode, keyboard_mode)

    def ungrabkey(self, key, modifiers):
        r"""SUMMARY

        ungrabkey(key, modifiers)

        @Arguments:
        - `key`:
        - `modifiers`:

        @Return:
        """
        return self.id.ungrabkey(self.display, key, modifiers)

    def grabbutton(self, owner_events, event_mask, pointer_mode,
                   keyboard_mode, confine_to, cursor, button, modifiers):
        r"""SUMMARY

        grabbutton(owner_events, event_mask, pointer_mode,
                   keyboard_mode, confine_to, cursor, button, modifiers)

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
        """
        return self.id.grabbutton(
            self.display, owner_events, event_mask, pointer_mode, keyboard_mode,
            confine_to, cursor, button, modifiers)

    def ungrabbutton(self, button, modifiers):
        r"""SUMMARY

        ungrabbutton(button, modifiers)

        @Arguments:
        - `button`:
        - `modifiers`:

        @Return:
        """
        return self.id.ungrabbutton(self.display, button, modifiers)

    def grabpointer(self, owner_events, event_mask, pointer_mode,
                    keyboard_mode, confine_to, cursor, time):
        r"""SUMMARY

        grabpointer(owner_events, event_mask, pointer_mode,
                    keyboard_mode, confine_to, cursor, time)

        @Arguments:
        - `owner_events`:
        - `event_mask`:
        - `pointer_mode`:
        - `keyboard_mode`:
        - `confine_to`:
        - `cursor`:
        - `time`:

        @Return:
        """
        return self.id.grabpointer(
            self.display, owner_events, event_mask, pointer_mode,
            keyboard_mode, confine_to, cursor, time)

    def querypointer(self, ):
        r"""SUMMARY

        querypointer()

        @Return:
        """
        return self.id.querypointer(self.display)

    def warppointer(self, dst_window, src_x, src_y, src_width,
                    src_height, dst_x, dst_y):
        r"""SUMMARY

        warppointer(dst_window, src_x, src_y, src_width,
                    src_height, dst_x, dst_y)

        @Arguments:
        - `dst_window`:
        - `src_x`:
        - `src_y`:
        - `src_width`:
        - `src_height`:
        - `dst_x`:
        - `dst_y`:

        @Return:
        """
        return self.id.warppointer(
            self.display, dst_window, src_x, src_y, src_width, src_height,
            dst_x, dst_y)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# window.py ends here
