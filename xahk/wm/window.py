#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: window.py 339 2015-07-23 18:01:26Z t1 $
# $Revision: 339 $
# $Date: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $

r"""window -- DESCRIPTION

"""


class Drawable(object):
    """Class Drawable
    """
    # Attributes:
    def __init__(self, display, wid):
        r"""

        @Arguments:
        - `display`:
        - `wid`:
        """
        self.display = display
        self._wid = wid

    # Operations
    def get_display(self):
        """function get_display

        returns
        """
        return self.display

    def get_id(self, ):
        r"""SUMMARY

        get_id()

        @Return:

        @Error:
        """
        return self._wid

    id = property(get_id)

    def get_geometry(self):
        """function get_geometry

        returns
        """
        return self.display.core.GetGeometry(self.id)

    def get_geometry_unchecked(self):
        """function get_geometry_unchecked

        returns
        """
        return self.display.core.GetGeometryUnchecked(self.id)

    def __int__(self):
        return self._wid

    def __eq__(self, other):
        if isinstance(other, (Drawable, )):
            return self.id == other.id
        return self.id == other

    def __ne__(self, other):
        return not self == other


class Window(Drawable):
    """Class Window
    """
    # Operations
    def send_event(self, propagate, event_mask, event):
        """function send_event

        propagate:
        event_mask:
        event:

        returns
        """
        return self.display.core.SendEvent(
            propagate, self.id, event_mask, event)

    def send_event_checked(self, propagate, event_mask, event):
        """function send_event_checked

        propagate:
        event_mask:
        event:

        returns
        """
        return self.display.core.SendEventChecked(
            propagate, self.id, event_mask, event)

    def destroy(self):
        """function destroy

        returns
        """
        return self.display.core.DestroyWindow(self.id)

    def destroy_checked(self):
        """function destroy_checked

        returns
        """
        return self.display.core.DestroyWindowChecked(self.id)

    def create_window(self, depth, parent, x, y, width, height, border_width,
                      _class, visual, value_mask, value_list):
        """function create_window

        depth:
        parent:
        x:
        y:
        width:
        height:
        border_width:
        _class:
        visual:
        value_mask:
        value_list:

        returns
        """
        return self.display.core.CreateWindow(
            depth, self.id, parent, x, y, width, height, border_width,
            _class, visual, value_mask, value_list)

    def create_window_checked(self, depth, parent, x, y, width, height,
                              border_width, _class, visual, value_mask,
                              value_list):
        """function create_window_checked

        depth:
        parent:
        x:
        y:
        width:
        height:
        border_width:
        _class:
        visual:
        value_mask:
        value_list:

        returns
        """
        return self.display.core.CreateWindowChecked(
            depth, self.id, parent, x, y, width, height, border_width,
            _class, visual, value_mask, value_list)

    def change_attributes(self, value_mask, value_list):
        """function change_attributes

        value_mask:
        value_list:

        returns
        """
        return self.display.core.ChangeWindowAttributes(
            self.id, value_mask, value_list)

    def change_attributes_checked(self, value_mask, value_list):
        """function change_attributes_checked

        value_mask:
        value_list:

        returns
        """
        return self.display.core.ChangeWindowAttributesChecked(
            self.id, value_mask, value_list)

    def get_attributes(self):
        """function get_attributes

        returns
        """
        return self.display.core.GetWindowAttributes(self.id)

    def get_attributes_unchecked(self):
        """function get_attributes_unchecked

        returns
        """
        return self.display.core.GetWindowAttributesUnchecked(self.id)

    def destroy_subwindows(self):
        """function destroy_subwindows

        returns
        """
        return self.display.core.DestroySubwindows(self.id)

    def destroy_subwindows_checked(self):
        """function destroy_subwindows_checked

        returns
        """
        return self.display.core.DestroySubwindowsChecked(self.id)

    def change_save_set(self, mode):
        """function change_save_set

        mode:

        returns
        """
        return self.display.core.ChangeSaveSet(mode, self.id)

    def change_save_set_checked(self, mode):
        """function change_save_set_checked

        mode:

        returns
        """
        return self.display.core.ChangeSaveSetChecked(mode, self.id)

    def reparent(self, parent, x, y):
        """function reparent

        parent:
        x:
        y:

        returns
        """
        return self.display.core.ReparentWindow(self.id, parent, x, y)

    def reparent_checked(self, parent, x, y):
        """function reparent_checked

        parent:
        x:
        y:

        returns
        """
        return self.display.core.ReparentWindowChecked(self.id, parent, x, y)

    def map(self):
        """function map

        returns
        """
        return self.display.core.MapWindow(self.id)

    def map_checked(self):
        """function map_checked

        returns
        """
        return self.display.core.MapWindowChecked(self.id)

    def map_subwindows(self):
        """function map_subwindows

        returns
        """
        return self.display.core.MapSubwindows(self.id)

    def map_subwindows_checked(self):
        """function map_subwindows_checked

        returns
        """
        return self.display.core.MapSubwindowsChecked(self.id)

    def unmap(self):
        """function unmap

        returns
        """
        return self.display.core.UnmapWindow(self.id)

    def unmap_checked(self):
        """function unmap_checked

        returns
        """
        return self.display.core.UnmapWindowChecked(self.id)

    def unmap_subwindows(self):
        """function unmap_subwindows

        returns
        """
        return self.display.core.UnmapSubwindows(self.id)

    def unmap_subwindows_checked(self):
        """function unmap_subwindows_checked

        returns
        """
        return self.display.core.UnmapSubwindowsChecked(self.id)

    def configure(self, value_mask, value_list):
        """function configure

        value_mask:
        value_list:

        returns
        """
        return self.display.core.ConfigureWindow(
            self.id, value_mask, value_list)

    def configure_checked(self, value_mask, value_list):
        """function configure_checked

        value_mask:
        value_list:

        returns
        """
        return self.display.core.ConfigureWindowChecked(
            self.id, value_mask, value_list)

    def circulate(self, direction):
        """function circulate

        diretion:

        returns
        """
        return self.display.core.CirculateWindow(direction, self.id)

    def circulate_checked(self, direction):
        """function circulate_checked

        direction:

        returns
        """
        return self.display.core.CirculateWindowChecked(direction, self.id)

    def query_tree(self):
        """function query_tree

        returns
        """
        return self.display.core.QueryTree(self.id)

    def query_tree_unchecked(self):
        """function query_tree_unchecked

        returns
        """
        return self.display.core.QueryTreeUnchecked(self.id)

    def change_property(self, mode, property, type, format, data_len, data):
        """function change_property

        mode:
        property:
        type:
        format:
        data_len:
        data:

        returns
        """
        return self.display.core.ChangeProperty(
            mode, self.id, property, type, format, data_len, data)

    def change_property_checked(self, mode, property, type, format,
                                data_len, data):
        """function change_property_checked

        mode:
        property:
        type:
        format:
        data_len:
        data:

        returns
        """
        return self.display.core.ChangePropertyChecked(
            mode, self.id, property, type, format, data_len, data)

    def delete_property(self, property):
        """function delete_property

        property:

        returns
        """
        return self.display.core.DeleteProperty(self.id, property)

    def delete_property_checked(self, property):
        """function delete_property_checked

        property:

        returns
        """
        return self.display.core.DeletePropertyChecked(self.id, property)

    def get_property(self, delete, property, type, long_offset, long_length):
        """function get_property

        delete:
        property:
        type:
        long_offset:
        long_length:

        returns
        """
        return self.display.core.GetProperty(
            delete, self.id, property, type, long_offset, long_length)

    def get_property_unchecked(self, delete, property, type, long_offset,
                               long_length):
        """function get_property_unchecked

        delete:
        property:
        type:
        long_offset:
        long_length:

        returns
        """
        return self.display.core.GetPropertyUnchecked(
            delete, self.id, property, type, long_offset, long_length)

    def list_properties(self):
        """function list_properties

        returns
        """
        return self.display.core.ListProperties(self.id)

    def list_properties_unchecked(self):
        """function list_properties_unchecked

        returns
        """
        return self.display.core.ListPropertiesUnchecked(self.id)

    def set_selection_owner(self, owner, time):
        """function set_selection_owner

        owner:
        time:

        returns
        """
        return self.display.core.SetSelectionOwner(owner, self.id, time)

    def set_selection_owner_checked(self, owner, time):
        """function set_selection_owner_checked

        owner:
        time:

        returns
        """
        return self.display.core.SetSelectionOwnerChecked(owner, self.id, time)

    def get_selection_owner(self):
        """function get_selection_owner

        returns
        """
        return self.display.core.GetSelectionOwner(self.id)

    def get_selection_owner_unchecked(self):
        """function get_selection_owner_unchecked

        returns
        """
        return self.display.core.GetSelectionOwnerUnchecked(self.id)

    def convert_selection(self, requestor, target, property, time):
        """function convert_selection

        requestor:
        target:
        property:
        time:

        returns
        """
        return self.display.core.ConvertSelection(
            requestor, self.id, target, property, time)

    def convert_selection_checked(self, requestor, target, property, time):
        """function convert_selection_checked

        requestor:
        target:
        property:
        time:

        returns
        """
        return self.display.core.ConvertSelectionChecked(
            requestor, self.id, target, property, time)

    def grab_pointer(self, owner_events, event_mask, pointer_mode,
                     keyboard_mode, confine_to, cursor, time):
        """function grab_pointer

        owner_events:
        event_mask:
        pointer_mode:
        keyboard_mode:
        confine_to:
        cursor:
        time:

        returns
        """
        return self.display.core.GrabPointer(
            owner_events, self.id, event_mask, pointer_mode, keyboard_mode,
            confine_to, cursor, time)

    def grab_pointer_unchecked(self, owner_events, event_mask, pointer_mode,
                               keyboard_mode, confine_to, cursor, time):
        """function grab_pointer_unchecked

        owner_events:
        event_mask:
        pointer_mode:
        keyboard_mode:
        confine_to:
        cursor:
        time:

        returns
        """
        return self.display.core.GrabPointerUnchecked(
            owner_events, self.id, event_mask, pointer_mode, keyboard_mode,
            confine_to, cursor, time)

    def ungrab_poiter(self, time):
        """function ungrab_poiter

        time:

        returns
        """
        return self.display.core.UngrabPointer(time)

    def ungrab_pointer_checked(self, time):
        """function ungrab_pointer_checked

        returns
        """
        return self.display.core.UngrabPointerChecked(time)

    def grab_button(self, owner_events, event_mask, pointer_mode,
                    keyboard_mode, confine_to, cursor, button, modifiers):
        """function grab_button

        owner_events:
        event_mask:
        pointer_mode:
        keyboard_mode:
        confine_to:
        cursor:
        button:
        modifiers:

        returns
        """
        return self.display.core.GrabButton(
            owner_events, self.id, event_mask, pointer_mode, keyboard_mode,
            confine_to, cursor, button, modifiers)

    def grab_butotn_checked(self, owner_events, event_mask, pointer_mode,
                            keyboard_mode, confine_to, cursor, button,
                            modifiers):
        """function grab_butotn_checked

        owner_events:
        event_mask:
        pointer_mode:
        keyboard_mode:
        confine_to:
        cursor:
        button:
        modifiers:

        returns
        """
        return self.display.core.GrabButtonChecked(
            owner_events, self.id, event_mask, pointer_mode, keyboard_mode,
            confine_to, cursor, button, modifiers)

    def ungrab_button(self, button, modifiers):
        """function ungrab_button

        button:
        modifeirs:

        returns
        """
        return self.display.core.UngrabButton(button, self.id, modifiers)

    def ungrab_button_checked(self, button, modifiers):
        """function ungrab_button_checked

        button:
        modifiers:

        returns
        """
        return self.display.core.UngrabButtonChecked(button, self.id, modifiers)

    def grab_keyboard(self, owner_events, time, pointer_mode, keyboard_mode):
        """function grab_keyboard

        owner_events:
        time:
        pointer_mode:
        keyboard_mode:

        returns
        """
        return self.display.core.GrabKeyboard(
            owner_events, self.id, time, pointer_mode, keyboard_mode)

    def grab_keyboard_unchecked(self, owner_events, time, pointer_mode,
                                keyboard_mode):
        """function grab_keyboard_unchecked

        owner_events:
        time:
        pointer_mode:
        keyboard_mode:

        returns
        """
        return self.display.core.GrabKeyboardUnchecked(
            owner_events, self.id, time, pointer_mode, keyboard_mode)

    def ungrab_keyboard(self, time):
        """function ungrab_keyboard

        time:

        returns
        """
        return self.display.core.UngrabKeyboard(time)

    def ungrab_keyboard_checked(self, time):
        """function ungrab_keyboard_checked

        time:

        returns
        """
        return self.display.core.UngrabKeyboardChecked(time)

    def grab_key(self, owner_events, modifiers, key, pointer_mode,
                 keyboard_mode):
        """function grab_key

        owner_events:
        modifiers:
        key:
        pointer_mode:
        keyboard_mode:

        returns
        """
        return self.display.core.GrabKey(
            owner_events, self.id, modifiers, key, pointer_mode, keyboard_mode)

    def grab_key_checked(self, owner_events, modifiers, key, pointer_mode,
                         keyboard_mode):
        """function grab_key_checked

        owner_events:
        modifiers:
        key:
        pointer_mode:
        keyboard_mode:

        returns
        """
        return self.display.core.GrabKeyChecked(
            owner_events, self.id, modifiers, key, pointer_mode, keyboard_mode)

    def ungrab_key(self, key, modifiers):
        r"""SUMMARY

        ungrab_key(key, modifiers)

        @Arguments:
        - `key`:
        - `modifiers`:

        @Return:

        @Error:
        """
        return self.display.core.UngrabKey(key, self.id, modifiers)

    def ungrab_key_checked(self, key, modifiers):
        r"""SUMMARY

        ungrab_key_checked(key, modifiers)

        @Arguments:
        - `key`:
        - `modifiers`:

        @Return:

        @Error:
        """
        return self.display.core.UngrabKeyChecked(key, self.id, modifiers)

    def grab_button(self, owner_events, event_mask, pointer_mode,
                    keyboard_mode, confine_to, cursor, button, modifiers):
        r"""SUMMARY

        grab_button(owner_events, event_mask, pointer_mode, keyboard_mode, confine_to, cursor, button, modifiers)

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
        return self.display.core.GrabButton(
            owner_events, self.id, event_mask, pointer_mode,
            keyboard_mode, confine_to, cursor, button, modifiers)

    def grab_button_checked(self, owner_events, event_mask, pointer_mode,
                            keyboard_mode, confine_to, cursor, button,
                            modifiers):
        r"""SUMMARY

        grab_button_checked()

        @Return:

        @Error:
        """
        return self.display.core.GrabButtonChecked(
            owner_events, self.id, event_mask, pointer_mode,
            keyboard_mode, confine_to, cursor, button, modifiers)

    def ungrab_button(self, button, modifiers):
        r"""SUMMARY

        ungrab_button(button, modifiers)

        @Arguments:
        - `button`:
        - `modifiers`:

        @Return:

        @Error:
        """
        return self.display.core.UngrabButton(button, self.id, modifiers)

    def ungrab_button_checked(self, button, modifiers):
        r"""SUMMARY

        ungrab_button_checked(button, modifiers)

        @Arguments:
        - `button`:
        - `modifiers`:

        @Return:

        @Error:
        """
        return self.display.core.UngrabButtonChecked(
            button, self.id, modifiers)

    def query_pointer(self):
        """function query_pointer

        returns
        """
        return self.display.core.QueryPointer(self.id)

    def query_pointer_unchecked(self):
        """function query_pointer_unchecked

        returns
        """
        return self.display.core.QueryPointerUnchecked(self.id)

    def get_motion_events(self, start, stop):
        """function get_motion_events

        start:
        stop:

        returns
        """
        return self.display.core.GetMotionEvents(self.id, start, stop)

    def get_motion_events_unchecked(self, start, stop):
        """function get_motion_events_unchecked

        start:
        stop:

        returns
        """
        return self.display.core.GetMotionEventsUnchecked(self.id, start, stop)

    def translate_coordinates(self, dst_window, src_x, src_y):
        """function translate_coordinates

        dst_window:
        src_x:
        src_y:

        returns
        """
        return self.display.core.TranslateCoordinates(
            self.id, dst_window, src_x, src_y)

    def translate_coordinates_unchecked(self, dst_window, src_x, src_y):
        """function translate_coordinates_unchecked

        dst_window:
        src_x:
        src_y:

        returns
        """
        return self.display.core.TranslateCoordinatesUnchecked(
            self.id, dst_window, src_x, src_y)

    def warp_pointer(self, src_window, src_x, src_y, src_width, src_height,
                     dst_x, dst_y):
        """function warp_pointer

        src_window:
        src_x:
        src_y:
        src_width:
        src_height:
        dst_x:
        dst_y:

        returns
        """
        return self.display.core.WarpPointer(
            src_window, self.id, src_x, src_y, src_width, src_height,
            dst_x, dst_y)

    def warp_pointer_checked(self, src_window, src_x, src_y, src_width,
                             src_height, dst_x, dst_y):
        """function warp_pointer_checked

        src_window:
        src_x:
        src_y:
        src_width:
        src_height:
        dst_x:
        dst_y:

        returns
        """
        return self.display.core.WarpPointerChecked(
            src_window, self.id, src_x, src_y, src_width, src_height,
            dst_x, dst_y)

    def set_input_focus(self, revert_to, time):
        """function set_input_focus

        revert_to:
        time:

        returns
        """
        return self.display.core.SetInputFocus(revert_to, self.id, time)

    def set_input_focus_checked(self, revert_to, time):
        """function set_input_focus_checked

        revert_to:
        time:

        returns
        """
        return self.display.core.SetInputFocusChecked(revert_to, self.id, time)

    def clear_area(self, exposures, x, y, width, height):
        """function clear_area

        exposures:
        x:
        y:
        width:
        height:

        returns
        """
        return self.display.core.ClearArea(
            exposures, self.id, x, y, width, height)

    def clear_area_checked(self, exposures, x, y, width, height):
        """function clear_area_checked

        exposures:
        x:
        y:
        width:
        height:

        returns
        """
        return self.display.core.ClearAreaChecked(
            exposures, self.id, x, y, width, height)

    def list_installed_colormaps(self):
        """function list_installed_colormaps

        returns
        """
        return self.display.core.ListInstalledColormaps(self.id)

    def list_installed_colormaps_unchecked(self):
        """function list_installed_colormaps_unchecked

        returns
        """
        return self.display.core.ListInstalledColormapsUnchecked(self.id)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# window.py ends here
