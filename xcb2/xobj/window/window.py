#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""window -- DESCRIPTION

"""
from struct import pack as _pack
from t1.listutil import get_first_index as gfi

from xcb2.logger import LOG
from xcb2.xobj.window.drawable import Drawable
from xcb2.xobj.window.windowtypes import WindowTypesDict, WindowUnknownType
from xcb2.xproto import BadWindow, PropMode


class Window(Drawable):
    r"""SUMMARY
    """
    fmt = 'I'

    def pack(self, ):
        r"""Convert Window ID to string of binary.

        @Return:
        (str)

        pack()
        """
        return _pack(self.fmt, self.id)

    def create_window(self, x, y, width, height, border_width, depth,
                      window_class, visual, **keys):
        pass

    def change_attributes(self, mask, value_list):
        """ChangeWindowAttributes

        @Arguments:
        - `mask`:
        - `value_list`:

        @Return:
        """
        return self.connection.core.ChangeWindowAttributes(
            self.id, mask, value_list)

    def get_attributes(self):
        """GetWindowAttributes"""
        return self.connection.core.GetWindowAttributes(self.id).reply()

    def destroy(self, ):
        """DestroyWindow"""
        return self.connection.core.DestroyWindow(self.id)

    def destroy_sub_windows(self, ):
        """DestroySubwindows"""
        return self.connection.core.DestroySubwindows(self.id)

    def change_save_set(self, mode):
        """ChangeSaveSet

        @Arguments:
        - `mode`:

        @Return:
        """
        return self.connection.core.ChangeSaveSet(mode, self.id)

    def reparent(self, parent, x, y):
        """ReparentWindow

        @Arguments:
        - `parent`:
        - `x`:
        - `y`:

        @Return:
        """
        return self.connection.core.ReparentWindow(self.id, parent, x, y)

    def map(self, ):
        """MapWindow"""
        return self.connection.core.MapWindow(self.id)

    def map_sub_windows(self, ):
        """MapSubwindows"""
        return self.connection.core.MapSubwindows(self.id)

    def unmap(self, ):
        """UnmapWindow"""
        return self.connection.core.UnmapWindow(self.id)

    def unmap_sub_windows(self, ):
        """UnmapSubwindows"""
        return self.connection.core.UnmapSubwindows(self.id)

    def configure(self, mask, values):
        """ConfigureWindow

        @Arguments:
        - `mask`:
        - `values`:

        @Return:
        """
        return self.connection.core.ConfigureWindow(self, mask, values)

    def circulate(self, direction):
        pass

    def raise_window(self,):
        pass

    def query_tree(self):
        """QueryTree"""
        return self.connection.core.QueryTree(self.id).reply().chileren

    def query_recursive_tree(self, ):
        r"""SUMMARY

        query_recursive_tree()

        @Return:
        """
        return self.connection.core.QueryTree.recursive(self)

    def change_property(self, property_, data_len, data, mode=PropMode.Replace):
        """ChangeProperty

        @Arguments:
        - `mode`:
        - `property_`:
        - `type_`:
        - `format_`:
        - `data_len`:
        - `data`:

        @Return:
        """
        return self.connection.core.ChangeProperty.changeproperty(
            self.id, property_, data_len, data, mode)

    def delete_property(self, property_):
        """DeleteProperty

        @Arguments:
        - `property_`:

        @Return:
        """
        return self.connection.core.DeleteProperty(self.id, property_)

    def get_property(self, property_, type_, offset=0, length=10, delete=0):
        """GetProperty

        @Arguments:
        - `property_`:
        - `type_`:
        - `offset`:
        - `length`:
        - `delete`:

        @Return:
        """
        return self.connection.core.GetProperty(
            delete, self.id, property_, type_, offset, length)

    def list_properties(self):
        """ListProperties"""
        return self.connection.core.ListProperties(self.id).reply().atoms

    def set_selection_owner(self, selection, time):
        pass

    def convert_selection(self, selection, target, property, time):
        pass

    def send_event(self, event, event_mask=0, propagate=0):
        """SendEvent

        @Arguments:
        - `event`:
        - `event_mask`:
        - `propagate`:

        @Return:
        """
        return self.connection.core.SendEvent(
            propagate, self.id, event_mask, event)

    def grab_pointer(self, owner_events, event_mask, pointer_mode, keyboard_mode,
                     confine_to, cursor, time):
        pass

    def grab_button(self, button, modifiers, event_mask,
                    pointer_mode=1, keyboard_mode=1, confine_to=0, cursor=0,
                    owner_events=True):
        """GrabButton

        @Arguments:
        - `button`:
        - `modifiers`:
        - `event_mask`:
        - `pointer_mode`:
        - `keyboard_mode`:
        - `confine_to`:
        - `cursor`:
        - `owner_events`:

        @Return:
        """
        self.connection.core.GrabButton(
            owner_events, self.id, event_mask,
            pointer_mode, keyboard_mode, confine_to, cursor, button, modifiers)
        self.flush()

    def ungrab_button(self, button, modifiers):
        """UngrabButton

        @Arguments:
        - `button`:
        - `modifiers`:

        @Return:
        """
        self.connection.core.UngrabButton(button, self.id, modifiers)
        self.flush()

    def grab_keyboard(self, time=0, pointer_mode=1, keyboard_mode=1,
                      owner_events=False):
        """GrabKeyboard

        @Arguments:
        - `time`:
        - `pointer_mode`:
        - `keyboard_mode`:
        - `owner_events`:

        @Return:
        """
        self.connection.core.GrabKeyboard(
            owner_events, self.id, time, pointer_mode, keyboard_mode)
        self.flush()

    def ungrab_keyboard(self, time=0):
        r"""UngrabKeyboard

        ungrab_keyboard(time=0)

        @Arguments:
        - `time`:

        @Return:
        """
        self.connection.core.UngrabKeyboard(time)
        self.flush()

    def grab_key(self, key, modifiers, owner_events=False,
                 pointer_mode=1, keyboard_mode=1):
        """GrabKey

        @Arguments:
        - `key`:
        - `modifiers`:
        - `owner_events`:
        - `pointer_mode`:
        - `keyboard_mode`:

        @Return:
        """
        self.connection.core.GrabKey(
            owner_events, self.id, modifiers, key, pointer_mode, keyboard_mode)
        self.flush()

    def ungrab_key(self, key, modifiers):
        """UngrabKey"""
        self.connection.core.UngrabKey(key, self.id, modifiers)
        self.flush()

    def query_pointer(self):
        pass

    def get_motion_events(self, start, stop):
        pass

    def translate_coords(self, src_window, src_x, src_y):
        pass

    def warp_pointer(self, x, y, src_window=0, src_x=0, src_y=0,
                     src_width=0, src_height=0):
        pass

    def set_input_focus(self, revert_to, time=0):
        """SetInputFocus

        @Arguments:
        - `revert_to`:
        - `time`:

        @Return:
        """
        return self.connection.core.SetInputFocus(revert_to, self.id, time)

    def clear_area(self, x=0, y=0, width=0, height=0, exposures=0):
        pass

    def create_colormap(self, visual, alloc):
        pass

    def list_installed_colormaps(self):
        pass

    def rotate_properties(self, properties, delta):
        pass

    def set_wm_name(self, data, mode=PropMode.Replace):
        """ChangeProperty WM_NAME

        @Arguments:
        - `name`:
        - `mode`:

        @Return:
        """
        return self.core.ChangeProperty.WM_NAME(self.id, data, mode)

    def get_wm_name(self):
        """GetProperty WM_NAME"""
        return self.core.GetProperty.WM_NAME(self.id).reply().get_full_value()

    def set_wm_icon_name(self, data, mode=PropMode.Replace):
        return self.core.ChangeProperty.WM_ICON_NAME(self.id, data, mode)

    def get_wm_icon_name(self):
        """GetProperty WM_ICON_NAME"""
        return self.core.GetProperty.WM_ICON_NAME(
            self.id).reply().get_full_value()

    def set_wm_class(self, data, mode=PropMode.Replace):
        return self.core.ChangeProperty.WM_CLASS(self.id, data, mode)

    def get_wm_class(self):
        """GetProperty WM_CLASS"""
        return self.core.GetProperty.WM_CLASS(self.id).reply().get_full_value()

    def set_wm_transient_for(self, data, mode=PropMode.Replace):
        return self.core.ChangeProperty.WM_TRANSIENT_FOR(self.id, data, mode)

    def get_wm_transient_for(self):
        """GetProperty WM_TRANSIENT_FOR"""
        return self.core.GetProperty.WM_TRANSIENT_FOR(
            self.id).reply().get_full_value()

    def set_wm_protocols(self, data, mode=PropMode.Replace):
        return self.core.ChangeProperty.WM_PROTOCOLS(self.id, data, mode)

    def get_wm_protocols(self):
        """GetProperty WM_PROTOCOLS"""
        return self.core.GetProperty.WM_PROTOCOLS(
            self.id).reply().get_full_value()

    def set_wm_colormap_windows(self, data, mode=PropMode.Replace):
        return self.core.ChangeProperty.WM_COLORMAP_WINDOWS(self.id, data, mode)

    def get_wm_colormap_windows(self):
        """GetProperty WM_COLORMAP_WINDOWS"""
        return self.core.GetProperty.WM_COLORMAP_WINDOWS(
            self.id).reply().get_full_value()

    def set_wm_client_machine(self, data, mode=PropMode.Replace):
        return self.core.ChangeProperty.WM_CLIENT_MACHINE(self.id, data, mode)

    def get_wm_client_machine(self):
        """GetProperty WM_CLIENT_MACHINE"""
        return self.core.GetProperty.WM_CLIENT_MACHINE(
            self.id).reply().get_full_value()

    def set_wm_normal_hints(self, hints={}, **keys):
        pass

    def get_wm_normal_hints(self):
        pass

    def set_wm_hints(self, hints={}, **keys):
        pass

    def get_wm_hints(self):
        pass

    def set_wm_state(self, hints={}, **keys):
        pass

    def get_wm_state(self):
        """GetProperty WM_STATE"""
        return self.core.GetProperty.WM_STATE(self.id).reply().get_full_value()

    def set_wm_icon_size(self, hints={}, **keys):
        pass

    def get_wm_icon_size(self):
        pass

    def set_net_wm_name(self, data, mode=PropMode.Replace):
        r"""SUMMARY

        set_net_wm_name(name)

        @Arguments:
        - `name`:

        @Return:
        """
        return self.core.ChangeProperty._NET_WM_NAME(self.id, data, mode)

    def get_net_wm_name(self, ):
        r"""GetProperty _NET_WM_NAME

        get_net_wm_name()

        @Return:
        """
        return self.core.GetProperty._NET_WM_NAME(
            self.id).reply().get_full_value()

    def set_net_wm_state(self, data, mode=PropMode.Replace):
        r"""SUMMARY

        set_net_wm_state(atoms)

        @Arguments:
        - `atoms`:

        @Return:
        """
        return self.core.ChangeProperty._NET_WM_STATE(self.id, data, mode)

    def get_net_wm_state(self, ):
        r"""SUMMARY

        get_net_wm_state()

        @Return:
        """
        return self.core.GetProperty._NET_WM_STATE(
            self.id).reply().get_full_value()

    def set_net_wm_pid(self, data, mode=PropMode.Replace):
        r"""SUMMARY

        set_net_wm_pid()

        @Arguments:

        @Return:
        """
        return self.core.ChangeProperty._NET_WM_PID(self.id, data, mode)

    def get_net_wm_pid(self, ):
        """GetProperty _NET_WM_PID"""
        return self.core.GetProperty._NET_WM_PID(
            self.id).reply().get_full_value()

    def set_net_wm_allowed_actions(self, data, mode=PropMode.Replace):
        r"""SUMMARY

        set_net_wm_allowed_actions()

        @Arguments:

        @Return:
        """
        return self.core.ChangeProperty._NET_WM_ALLOWED_ACTIONS(
            self.id, data, mode)

    def get_net_wm_allowed_actions(self, ):
        """GetProperty _NET_WM_ALLOWED_ACTIONS"""
        return self.core.GetProperty._NET_WM_ALLOWED_ACTIONS(
            self.id).reply().get_full_value()

    def set_net_supported(self, data, mode=PropMode.Replace):
        r"""SUMMARY

        set_net_supported()

        @Arguments:

        @Return:
        """
        return self.core.ChangeProperty._NET_SUPPORTED(self.id, data, mode)

    def get_net_supported(self, ):
        """GetProperty _NET_SUPPORTED"""
        return self.core.GetProperty._NET_SUPPORTED(
            self.id).reply().get_full_value()

    def set_net_wm_icon(self, data, mode=PropMode.Replace):
        r"""SUMMARY

        set_net_wm_icon()

        @Arguments:

        @Return:
        """
        return self.core.ChangeProperty._NET_WM_ICON_NAME(self.id, data, mode)

    def get_net_wm_icon(self, ):
        """GetProperty _NET_WM_ICON"""
        return self.core.GetProperty._NET_WM_ICON(
            self.id).reply().get_full_value()

    def set_net_wm_icon_geometry(self, data, mode=PropMode.Replace):
        r"""SUMMARY

        set_net_wm_icon_geometry()

        @Arguments:

        @Return:
        """
        pass

    def get_net_wm_icon_geometry(self, ):
        """GetProperty _NET_WM_ICON_GEOMETRY"""
        return self.core.GetProperty._NET_WM_ICON_GEOMETRY(
            self.id).reply().get_full_value()

    def set_net_wm_user_time(self, data, mode=PropMode.Replace):
        r"""SUMMARY

        set_net_wm_user_time()

        @Arguments:

        @Return:
        """
        return self.core.ChangeProperty._NET_WM_USER_TIME(self.id, data, mode)

    def get_net_wm_user_time(self, ):
        """GetProperty _NET_WM_USER_TIME"""
        return self.core.GetProperty._NET_WM_USER_TIME(
            self.id).reply().get_full_value()

    def set_net_wm_user_time_window(self, data, mode=PropMode.Replace):
        r"""SUMMARY

        set_net_wm_user_time_window()

        @Arguments:

        @Return:
        """
        return self.core.ChangeProperty._NET_WM_USER_TIME_WINDOW(
            self.id, data, mode)

    def get_net_wm_user_time_window(self, ):
        """GetProperty _NET_WM_USER_TIME_WINDOW"""
        return self.core.GetProperty._NET_WM_USER_TIME_WINDOW(
            self.id).reply().get_full_value()

    def set_net_wm_window_type(self, data, mode=PropMode.Replace):
        r"""SUMMARY

        set_net_wm_window_type()

        @Arguments:

        @Return:
        """
        return self.core.ChangeProperty._NET_WM_WINDOW_TYPE(
            self.id, data, mode)

    def get_net_wm_window_type(self, ):
        try:
            types = (self.connection.core.GetProperty._NET_WM_WINDOW_TYPE(self)
                     .reply().get_full_value())
        except BadWindow as err:
            LOG.warning('warning: {}'.format(err))
            types = ['']
        cls = WindowTypesDict.get(gfi(types))
        if cls == WindowUnknownType:
            root = self.connection.get_setup().roots[0].root
            if self.id == root:
                return root
        return cls(self)

    def set_net_workarea(self, data, mode=PropMode.Replace):
        r"""SUMMARY

        set_net_workarea()

        @Arguments:

        @Return:
        """
        return self.core.ChangeProperty._NET_WORKAREA(self.id, data, mode)

    def get_net_workarea(self, ):
        """GetProperty _NET_WORKAREA"""
        return self.core.GetProperty._NET_WORKAREA(
            self.id).reply().get_full_value()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# window.py ends here
