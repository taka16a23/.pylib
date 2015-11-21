#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""active_window_model -- DESCRIPTION

"""
from xahk.listener.root_window_listener import RootWindowListener
from xahk.listener.root_window_listener_observer import RootWindowListenerObserver
from xahk.window_manager import WindowManager
from xahk.layout.layout_item import LayoutItem
from xahk.wm.window_client import WindowStateMode


class ActiveWindowModel(RootWindowListenerObserver, LayoutItem):
    r"""ActiveWindowModel

    ActiveWindowModel is a RootWindowListenerObserver.
    Responsibility:
    """
    def __init__(self, display):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        RootWindowListenerObserver.__init__(self)
        self._display = display
        root_window = RootWindowListener(self._display)
        root_window.add_observer(self)
        self._active_window = root_window.get_active_window()

    def on_changed_active_window(self, root_window):
        r"""SUMMARY

        on_changed_active_window(root_window)

        @Arguments:
        - `root_window`:

        @Return:

        @Error:
        """
        self._active_window = WindowManager(self._display).get_active_window()

    def __del__(self):
        # Do not imprement "raise"!!
        RootWindowListener(self._display).remove_observer(self)

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self._display

    display = property(get_display)

    def __int__(self):
        return int(self._active_window)

    def __eq__(self, other):
        return self._active_window == other

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return 'ActiveWindowModel(id={0.id}, wmclass={0.wmclass})'.format(self)

    def get_id(self, ):
        r"""SUMMARY

        get_id()

        @Return:

        @Error:
        """
        return self._active_window.get_id()

    id = property(get_id)

    def get_title(self, ):
        r"""SUMMARY

        get_title()

        @Return:

        @Error:
        """
        return self._active_window.get_title()

    def set_title(self, title):
        r"""SUMMARY

        set_title(title)

        @Arguments:
        - `title`:

        @Return:

        @Error:
        """
        self._active_window.set_title(title)

    property(get_title, set_title)

    def get_wmclass(self, ):
        r"""SUMMARY

        get_wmclass()

        @Return:

        @Error:
        """
        return self._active_window.get_wmclass()

    wmclass = property(get_wmclass)

    def get_pid(self, ):
        r"""SUMMARY

        get_pid()

        @Return:

        @Error:
        """
        return self._active_window.get_pid

    pid = property(get_pid)

    def get_bounds(self, ):
        r"""SUMMARY

        get_bounds()

        @Return:

        @Error:
        """
        return self._active_window.get_bounds()

    def set_bounds(self, newx, newy, width, height):
        r"""SUMMARY

        set_bounds(newx, newy, width, height)

        @Arguments:
        - `newx`:
        - `newy`:
        - `width`:
        - `height`:

        @Return:

        @Error:
        """
        self._active_window.set_bounds(newx, newy, width, height)

    def layout(self, rect):
        r"""SUMMARY

        layout(rect)

        @Arguments:
        - `rect`:

        @Return:

        @Error:
        """
        self._active_window.layout(rect)

    def move(self, newx, newy):
        r"""SUMMARY

        move(newx, newy)

        @Arguments:
        - `newx`:
        - `newy`:

        @Return:

        @Error:
        """
        self._active_window.move(newx, newy)

    def set_size(self, width, height):
        r"""SUMMARY

        set_size(width, height)

        @Arguments:
        - `width`:
        - `height`:

        @Return:

        @Error:
        """
        self._active_window.set_size(width, height)

    def minimize(self, ):
        r"""SUMMARY

        minimize()

        @Return:

        @Error:
        """
        self._active_window.minimize()

    def is_minimized(self, ):
        r"""SUMMARY

        is_minimized()

        @Return:

        @Error:
        """
        return self._active_window.is_minimized()

    def show(self, ):
        r"""SUMMARY

        show()

        @Return:

        @Error:
        """
        self._active_window.show()

    def maximize(self, mode=WindowStateMode.Set):
        r"""SUMMARY

        maximize(mode=WindowStateMode.Set)

        @Arguments:
        - `mode`:

        @Return:

        @Error:
        """
        self._active_window.maximized(mode)

    def is_maximized(self, ):
        r"""SUMMARY

        is_maximized()

        @Return:

        @Error:
        """
        return self._active_window.is_maximized()

    def restore(self, ):
        r"""SUMMARY

        restore()

        @Return:

        @Error:
        """
        self._active_window.restore()

    def deactivate(self, ):
        r"""SUMMARY

        deactivate()

        @Return:

        @Error:
        """
        self._active_window.deactivate()

    def set_always_on_top(self, mode=WindowStateMode.Set):
        r"""SUMMARY

        set_always_on_top(mode=WindowStateMode.Set)

        @Arguments:
        - `mode`:

        @Return:

        @Error:
        """
        self._active_window.set_always_on_top(mode)

    def is_always_on_top(self, ):
        r"""SUMMARY

        is_always_on_top()

        @Return:

        @Error:
        """
        return self._active_window.is_always_on_top()

    def set_always_on_bottom(self, mode=WindowStateMode.Set):
        r"""SUMMARY

        set_always_on_bottom(mode=WindowStateMode.Set)

        @Arguments:
        - `mode`:

        @Return:

        @Error:
        """
        self._active_window.set_always_on_bottom(mode)

    def is_always_on_bottom(self, ):
        r"""SUMMARY

        is_always_on_bottom()

        @Return:

        @Error:
        """
        return self._active_window.is_always_on_bottom()

    def set_fullscreen(self, mode=WindowStateMode.Set):
        r"""SUMMARY

        set_fullscreen(mode=WindowStateMode.Set)

        @Arguments:
        - `mode`:

        @Return:

        @Error:
        """
        self._active_window.set_fullscreen(mode)

    def is_fullscreened(self):
        """function is_fullscreened

        returns
        """
        return self._active_window.is_fullscreened()

    def set_shade(self, mode=WindowStateMode.Set):
        """function set_shade

        mode:

        returns
        """
        self._active_window.set_shade(mode)

    def is_shaded(self):
        """function is_shaded

        returns
        """
        return self._active_window.is_shaded()

    def hide(self):
        """function hide

        returns
        """
        self._active_window.hide()

    def close(self):
        """function close

        returns
        """
        return self._active_window.close()

    def delete(self):
        """function delete

        returns
        """
        return self._active_window.delete()

    def destroy(self):
        """function destroy

        returns
        """
        return self._active_window.destroy()

    def move_cursor_to(self, newx, newy):
        """function move_cursor_to

        point:

        returns
        """
        return self._active_window.move_cursor_to(newx, newy)

    def get_cursor_point(self, ):
        r"""SUMMARY

        get_cursor_point()

        @Return:

        @Error:
        """
        return self._active_window.get_cursor_point()

    def raise_window(self):
        """function raise_window

        returns
        """
        return self._active_window.raise_window()

    def lower_window(self):
        """function lower_window

        returns
        """
        return self._active_window.lower_window()

    def get_workspace(self):
        """function get_desktop

        returns
        """
        return self._active_window.get_workspace()

    def change_workspace(self, num):
        """function change_desktop

        returns
        """
        return self._active_window.change_workspace(num)

    def grab_key(self, accelerator):
        r"""SUMMARY

        grab_key(owner_events, key, modifiers, pointer_mode, keyboard_mode)

        @Arguments:
        - `owner_events`:
        - `key`:
        - `modifiers`:
        - `pointer_mode`:
        - `keyboard_mode`:

        @Return:

        @Error:
        """
        return self._active_window.grab_key(accelerator)

    def grab_keys(self, accelerators):
        r"""SUMMARY

        grab_keys(targets)

        @Arguments:
        - `targets`:

        @Return:

        @Error:
        """
        return self._active_window.grab_keys(accelerators)

    def ungrab_key(self, accelerator):
        r"""SUMMARY

        ungrab_key(accelerator)

        @Arguments:
        - `accelerator`:

        @Return:

        @Error:
        """
        return self._active_window.ungrab_key(accelerator)

    def ungrab_keys(self, accelerators):
        r"""SUMMARY

        ungrab_keys(accelerators)

        @Arguments:
        - `accelerators`:

        @Return:

        @Error:
        """
        return self._active_window.ungrab_keys(accelerators)

    def grab_button(self, accelerator):
        r"""SUMMARY

        grab_button(accelerator)

        @Arguments:
        - `accelerator`:

        @Return:

        @Error:
        """
        return self._active_window.grab_button(accelerator)

    def grab_buttons(self, accelerators):
        r"""SUMMARY

        grab_buttons(accelerators)

        @Arguments:
        - `accelerators`:

        @Return:

        @Error:
        """
        return self._active_window.grab_buttons(accelerators)

    def ungrab_button(self, accelerator):
        r"""SUMMARY

        ungrab_button(accelerator)

        @Arguments:
        - `accelerator`:

        @Return:

        @Error:
        """
        return self._active_window.ungrab_button(accelerator)

    def ungrab_buttons(self, accelerators):
        r"""SUMMARY

        ungrab_butotns(accelerators)

        @Arguments:
        - `accelerators`:

        @Return:

        @Error:
        """
        return self._active_window.ungrab_buttons(accelerators)

    def get_attributes(self, ):
        r"""SUMMARY

        get_attributes()

        @Return:

        @Error:
        """
        return self._active_window.get_attributes()

    def add_attributes(self, value):
        r"""SUMMARY

        add_attributes(value)

        @Arguments:
        - `value`:

        @Return:

        @Error:
        """
        return self._active_window.add_attributes(value)

    def remove_attributes(self, value):
        r"""SUMMARY

        remove_attributes(value)

        @Arguments:
        - `value`:

        @Return:

        @Error:
        """
        return self._active_window.remove_attributes(value)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# active_window_model.py ends here
