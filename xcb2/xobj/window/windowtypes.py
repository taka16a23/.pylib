#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: windowtypes.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""windowtypes -- DESCRIPTION

"""
import psutil
from t1.listutil import get_first_index as gfi

from xcb2.xproto import ConfigWindow, StackMode
from xcb2.xobj.geometry import GeometryInfo, WindowGeometry
from xcb2.xobj.window.wm_class import WMCLASS


class WindowTypesAbstract(object):
    r"""SUMMARY
    """

    def __init__(self, window):
        r"""

        @Arguments:
        - `window`:
        """
        self.window = window

    @property
    def _connection(self, ):
        r"""SUMMARY

        connection()

        @Return:
        """
        return self.window.connection

    @property
    def _core(self, ):
        r"""SUMMARY

        core()

        @Return:
        """
        return self._connection.core

    @property
    def x(self, ):
        r"""SUMMARY

        x()

        @Return:
        """
        return self.get_geometry().translate_coords().x

    @property
    def y(self, ):
        r"""SUMMARY

        y()

        @Return:
        """
        return self.get_geometry().translate_coords().y

    @property
    def width(self, ):
        r"""SUMMARY

        width()

        @Return:
        """
        return self.get_geometry().translate_coords().width

    @property
    def height(self, ):
        r"""SUMMARY

        height()

        @Return:
        """
        return self.get_geometry().translate_coords().height

    def get_geometry(self, ):
        r"""SUMMARY

        get_geometry()

        @Return:
        """
        return self.window.get_geometry()

    def pack(self, ):
        r"""SUMMARY

        pack()

        @Return:
        """
        return self.window.pack()

    def flush(self, ):
        r"""SUMMARY

        flush()

        @Return:
        """
        self.window.flush()

    def grab_key(self, key, modifiers, owner_events=False,
                 pointer_mode=1, keyboard_mode=1):
        r"""SUMMARY

        grab_key(key, modifiers, owner_events=False,
        pointer_mode=1, keyboard_mode=1)

        @Arguments:
        - `key`:
        - `modifiers`:
        - `owner_events`:
        - `pointer_mode`:
        - `keyboard_mode`:

        @Return:
        """
        self.window.grab_key(
            key, modifiers, owner_events, pointer_mode, keyboard_mode)

    def ungrab_key(self, key, modifiers):
        r"""SUMMARY

        ungrab_key(key, modifiers)

        @Arguments:
        - `key`:
        - `modifiers`:

        @Return:
        """
        self.window.ungrab_key(key, modifiers)

    def grab_keyboard(self, time=0, pointer_mode=1, keyboard_mode=1,
                      owner_events=False):
        r"""SUMMARY

        grab_keyboard(time=0, pointer_mode=1,
        keyboard_mode=1, owner_events=False)

        @Arguments:
        - `time`:
        - `pointer_mode`:
        - `keyboard_mode`:
        - `owner_events`:

        @Return:
        """
        self.window.grab_keyboard(
            time, pointer_mode, keyboard_mode, owner_events)

    def ungrab_keyboard(self, time=0):
        r"""SUMMARY

        ungrab_keyboard(time=0)

        @Arguments:
        - `time`:

        @Return:
        """
        self.window.ungrab_keyboard(time)

    def grab_button(self, button, modifiers, event_mask,
                    pointer_mode=1, keyboard_mode=1, confine_to=0, cursor=0,
                    owner_events=True):
        r"""SUMMARY
        grab_button(button, modifiers, event_mask,
                    pointer_mode=1, keyboard_mode=1, confine_to=0, cursor=0,
                    owner_events=True)

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
        self.window.grab_button(
            button, modifiers, event_mask, pointer_mode, keyboard_mode,
            confine_to, cursor, owner_events)

    def ungrab_button(self, button, modifiers):
        r"""SUMMARY

        ungrab_button(button, modifiers)

        @Arguments:
        - `button`:
        - `modifiers`:

        @Return:
        """
        self.window.ungrab_button(button, modifiers)

    def query_tree(self, ):
        r"""SUMMARY

        query_tree()

        @Return:
        """
        return self.window.query_tree()

    def query_subwindows(self, ):
        r"""SUMMARY

        query_subwindows()

        @Return:
        """
        return self.window.query_recursive_tree()

    def list_properties(self, ):
        r"""SUMMARY

        list_properties()

        @Return:
        """
        return self.window.list_properties()

    def __int__(self, ):
        return int(self.window)

    def __cmp__(self, other):
        if isinstance(other, self.__class__):
            return cmp(self.window, other.window)
        return cmp(int(self), other)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.window == other.window
        return int(self) == other

    def __hash__(self, ):
        return hash(self.window)

    def __repr__(self, ):
        return '{0.__class__.__name__}(window={1})'.format(self, int(self))


class WindowRootType(WindowTypesAbstract):
    r"""SUMMARY
    """
    name = ''
    wmclass = WMCLASS()
    pid = None

    def get_user_time(self, ):
        r"""SUMMARY

        get_user_time()

        @Return:
        """
        return self.window.get_net_wm_user_time()

    def client_list(self, ):
        r"""SUMMARY

        client_list()

        @Return:
        """
        return self._core.GetProperty._NET_CLIENT_LIST(
            self.window).reply().get_full_value()

    def client_list_stacking(self, ):
        r"""SUMMARY

        client_list_stacking()

        @Return:
        """
        return self._core.GetProperty._NET_CLIENT_LIST_STACKING(
            self.window).reply().get_full_value()

    def get_desktop_name(self, ):
        r"""SUMMARY

        get_desktop_name()

        @Return:
        """
        return self._core.GetProperty._NET_DESKTOP_NAMES(
            self.window).reply().get_full_value()

    def get_active_window(self, ):
        r"""SUMMARY

        get_active_window()

        @Return:
        """
        return gfi(self._core.GetProperty._NET_ACTIVE_WINDOW(
            self.window).reply().get_full_value()).get_net_wm_window_type()

    def get_current_desktop(self, ):
        r"""SUMMARY

        get_current_desktop()

        @Return:
        """
        return self._core.GetProperty._NET_CURRENT_DESKTOP(
            self.window).reply().get_full_value()

    def get_desktop_viewport(self, ):
        r"""SUMMARY

        get_desktop_viewport()

        @Return:
        """
        return self._core.GetProperty._NET_DESKTOP_VIEWPORT(
            self.window).reply().get_full_value()

    def get_desktop_geometry(self, ):
        r"""SUMMARY

        get_desktop_geometry()

        @Return:
        """
        return self._core.GetProperty._NET_DESKTOP_GEOMETRY(
            self.window).reply().get_full_value()

    def get_supporting_wm_check(self, ):
        r"""SUMMARY

        get_supporting_wm_check()

        @Return:
        """
        return self._core.GetProperty._NET_SUPPORTING_WM_CHECK(
            self.window).reply().get_full_value()

    def get_supported(self, ):
        r"""SUMMARY

        get_supported()

        @Return:
        """
        return self._core.GetProperty._NET_SUPPORTED(
            self.window).reply().get_full_value()

    def get_workarea(self, ):
        r"""SUMMARY

        get_workarea()

        @Return:
        """
        return self._core.GetProperty._NET_WORKAREA(
            self.window).reply().get_full_value()

    def get_workspace_count(self, ):
        r"""SUMMARY

        get_workspace_count()

        @Return:
        """
        pass

    def get_number_of_desktops(self, ):
        r"""SUMMARY

        get_number_of_desktops()

        @Return:
        """
        pass

    def get_desktop_layout(self, ):
        r"""SUMMARY

        get_desktop_layout()

        @Return:
        """
        return self._core.GetProperty._NET_DESKTOP_LAYOUT(
            self.window).reply().get_full_value()

    def get_showing_desktop(self, ):
        r"""SUMMARY

        get_showing_desktop()

        @Return:
        """
        return self._core.GetProperty._NET_SHOWING_DESKTOP(
            self.window).reply().get_full_value()


class WindowUnknownType(WindowTypesAbstract):
    r"""
    """
    typesname = ''

    @property
    def name(self, ):
        r"""SUMMARY

        get_name()

        @Return:
        """
        return self.window.get_net_wm_name() or self.window.get_wm_name()

    @property
    def wmclass(self, ):
        r"""SUMMARY

        get_class()

        @Return:
        """
        wmclass = self.window.get_wm_class()
        if wmclass == '':
            return WMCLASS(self._connection)
        return WMCLASS(self._connection, *wmclass.split('\0')[:2])

    @property
    def types(self, ):
        r"""SUMMARY

        types()

        @Return:
        """
        return self._connection.core.atomidentify(self.typesname)

    @property
    def pid(self, ):
        r"""SUMMARY

        get_pid()

        @Return:
        """
        pid = gfi(self.window.get_net_wm_pid())
        if pid:
            return psutil.Process(pid)
        return None

    def list_states(self, ):
        r"""SUMMARY

        get_states()

        @Return:
        """
        return self.window.get_net_wm_state()

    def list_allowed_actions(self, ):
        r"""SUMMARY

        get_allowed_actions()

        @Return:
        """
        return self.window.get_net_wm_allowed_actions()

    def get_user_window_time(self, ):
        r"""SUMMARY

        get_user_window_time()

        @Return:
        """
        return self.window.get_net_wm_user_time()

    def __setattr__(self, name, value):
        if isinstance(value, int) and name in ('x', 'y', 'width', 'height'):
            self.move(**{name: value,})
        else:
            super(WindowUnknownType, self).__setattr__(name, value)

    def move(self, **changes):
        r"""SUMMARY

        move(**kwargs)

        @Arguments:
        - `**kwargs`:

        @Return:
        """
        geo = WindowGeometry(
            self._connection, GeometryInfo(**changes), self.window.id)
        geo.move()

    def focus(self, revert_to, time=0):
        r"""SUMMARY

        focus()

        @Return:
        """
        return self.window.set_input_focus(revert_to, time=0)

    def close(self, ):
        r"""SUMMARY

        close()

        @Return:
        """
        return self._core.SendEvent.ClientMessage.close(self.window.id)

    def destroy(self, ):
        r"""SUMMARY

        kill()

        @Return:
        """
        return self._core.SendEvent.ClientMessage.delete(self.window.id)

    def isabove(self, ):
        r"""SUMMARY

        isabove()

        @Return:
        """
        states = self.list_states()
        for atom in self._core.SendEvent.ClientMessage.above.atoms:
            if atom in states:
                return True
        return False

    def isbelow(self, ):
        r"""SUMMARY

        isbelow()

        @Return:
        """
        states = self.list_states()
        for atom in self._core.SendEvent.ClientMessage.below.atoms:
            if atom in states:
                return True
        return False

    def isfullscreen(self, ):
        r"""SUMMARY

        isfullscreen()

        @Return:
        """
        states = self.list_states()
        for atom in self._core.SendEvent.ClientMessage.fullscreen.atoms:
            if atom in states:
                return True
        return False

    def isshade(self, ):
        r"""SUMMARY

        isshade()

        @Return:
        """
        states = self.list_states()
        for atom in self._core.SendEvent.ClientMessage.shade.atoms:
            if atom in states:
                return True
        return False

    def ismaximize(self, ):
        r"""SUMMARY

        isshade()

        @Return:
        """
        states = self.list_states()
        for atom in self._core.SendEvent.ClientMessage.maximize.atoms:
            if atom in states:
                return True
        return False

    def stackabove(self, ):
        r"""SUMMARY

        stackabove()

        @Return:
        """
        return self.window.configure(ConfigWindow.StackMode, [StackMode.Above])

    def stackbelow(self, ):
        r"""SUMMARY

        stackbelow()

        @Return:
        """
        return self.window.configure(ConfigWindow.StackMode, [StackMode.Below])

    def setabove(self, ):
        r"""SUMMARY

        set_above()

        @Return:
        """
        return self._core.SendEvent.ClientMessage.above.set(self.window.id)

    def unsetabove(self, ):
        r"""SUMMARY

        unset_above()

        @Return:
        """
        return self._core.SendEvent.ClientMessage.above.unset(self.window.id)

    def toggleabove(self, ):
        r"""SUMMARY

        toggle_above()

        @Return:
        """
        return self._core.SendEvent.ClientMessage.above.toggle(self.window.id)

    def setbelow(self, ):
        r"""SUMMARY

        set_below()

        @Return:
        """
        return self._core.SendEvent.ClientMessage.below.set(self.window.id)

    def unsetbelow(self, ):
        r"""SUMMARY

        unset_below()

        @Return:
        """
        return self._core.SendEvent.ClientMessage.below.unset(self.window.id)

    def togglebelow(self, ):
        r"""SUMMARY

        toggle_below()

        @Return:
        """
        return self._core.SendEvent.ClientMessage.below.toggle(self.window.id)

    def setfullscreen(self, ):
        r"""SUMMARY

        set_fullscreen()

        @Return:
        """
        return self._core.SendEvent.ClientMessage.fullscreen.set(self.window.id)

    def unsetfullscreen(self, ):
        r"""SUMMARY

        unset_fullscreen()

        @Return:
        """
        return self._core.SendEvent.ClientMessage.fullscreen.unset(
            self.window.id)

    def togglefullscreen(self, ):
        r"""SUMMARY

        toggle_fullscreen()

        @Return:
        """
        return self._core.SendEvent.ClientMessage.fullscreen.toggle(
            self.window.id)

    def setmaximize(self, ):
        r"""SUMMARY

        set_maximize()

        @Return:
        """
        return self._core.SendEvent.ClientMessage.maximize.set(self.window.id)

    def unsetmaximize(self, ):
        r"""SUMMARY

        unset_maximize()

        @Return:
        """
        return self._core.SendEvent.ClientMessage.maximize.unset(
            self.window.id)

    def togglemaximize(self, ):
        r"""SUMMARY

        toggle_maximize()

        @Return:
        """
        return self._core.SendEvent.ClientMessage.maximize.toggle(
            self.window.id)


class WindowDesktopType(WindowUnknownType):
    r"""
    """
    typesname = '_NET_WM_WINDOW_TYPE_DESKTOP'


class WindowDockType(WindowUnknownType):
    r"""
    """
    # TODO: (Atami) [2014/03/02]

    typesname = '_NET_WM_WINDOW_TYPE_DOCK'


class WindowSplashType(WindowUnknownType):
    r"""
    """
    typesname = '_NET_WM_WINDOW_TYPE_SPLASH'


class WindowNormalType(WindowUnknownType):
    r"""
    """
    typesname = '_NET_WM_WINDOW_TYPE_NORMAL'


class WindowToolbarType(WindowUnknownType):
    r"""
    """
    # TODO: (Atami) [2014/03/02]
    typesname = '_NET_WM_WINDOW_TYPE_TOOLBAR'


class WindowMenuType(WindowUnknownType):
    r"""
    """
    # TODO: (Atami) [2014/03/02]
    typesname = '_NET_WM_WINDOW_TYPE_MENU'


class WindowUtilityType(WindowUnknownType):
    r"""
    """
    # TODO: (Atami) [2014/03/02]
    typesname = '_NET_WM_WINDOW_TYPE_UTILITY'


class WindowDialogType(WindowUnknownType):
    r"""
    """
    # TODO: (Atami) [2014/03/02]
    typesname = '_NET_WM_WINDOW_TYPE_DIALOG'


class WindowDropdownMenuType(WindowUnknownType):
    r"""
    """
    # TODO: (Atami) [2014/03/02]
    typesname = '_NET_WM_WINDOW_TYPE_DROPDOWN_MENU'


class WindowPopupMenuType(WindowUnknownType):
    r"""
    """
    # TODO: (Atami) [2014/03/02]
    typesname = '_NET_WM_WINDOW_TYPE_POPUP_MENU'


class WindowTooltipType(WindowUnknownType):
    r"""
    """
    # TODO: (Atami) [2014/03/02]
    typesname = '_NET_WM_WINDOW_TYPE_TOOLTIP'


class WindowNotificationType(WindowUnknownType):
    r"""
    """
    # TODO: (Atami) [2014/03/02]
    typesname = '_NET_WM_WINDOW_TYPE_NOTIFICATION'


class WindowComboType(WindowUnknownType):
    r"""
    """
    # TODO: (Atami) [2014/03/02]
    typesname = '_NET_WM_WINDOW_TYPE_COMBO'


class WindowDNDType(WindowUnknownType):
    r"""
    """
    # TODO: (Atami) [2014/03/02]
    typesname = '_NET_WM_WINDOW_TYPE_DND'


class WindowTypesDict(object):
    r"""SUMMARY
    """
    dic = {
        '_NET_WM_WINDOW_TYPE_NORMAL'        : WindowNormalType,
        '_NET_WM_WINDOW_TYPE_SPLASH'        : WindowSplashType,
        '_NET_WM_WINDOW_TYPE_DESKTOP'       : WindowDesktopType,
        '_NET_WM_WINDOW_TYPE_DOCK'          : WindowDockType,
        '_NET_WM_WINDOW_TYPE_TOOLBAR'       : WindowToolbarType,
        '_NET_WM_WINDOW_TYPE_MENU'          : WindowMenuType,
        '_NET_WM_WINDOW_TYPE_UTILITY'       : WindowUtilityType,
        '_NET_WM_WINDOW_TYPE_DIALOG'        : WindowDialogType,
        '_NET_WM_WINDOW_TYPE_DROPDOWN_MENU' : WindowDropdownMenuType,
        '_NET_WM_WINDOW_TYPE_POPUP_MENU'    : WindowPopupMenuType,
        '_NET_WM_WINDOW_TYPE_TOOLTIP'       : WindowTooltipType,
        '_NET_WM_WINDOW_TYPE_NOTIFICATION'  : WindowNotificationType,
        '_NET_WM_WINDOW_TYPE_COMBO'         : WindowComboType,
        '_NET_WM_WINDOW_TYPE_DND'           : WindowDNDType,
        }

    @staticmethod
    def get(name):
        r"""SUMMARY

        get(name)

        @Arguments:
        - `name`:

        @Return:
        """
        return WindowTypesDict.dic.get(str(name), WindowUnknownType)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# windowtypes.py ends here
