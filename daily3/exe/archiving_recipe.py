#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""archiving_recipe -- DESCRIPTION

"""
import sys
from time import sleep
from datetime import datetime

from ref.CMD import thunar

from recipe.menu2 import MenuManager
from recipe.menu2.common import DEFAULT_DIR
from recipe._recipe import ARCHIVE_PATH


from xahk.listener.window_manager import WindowManagerListener
from xahk.listener.window_manager_observer import WindowManagerListenerObserver
from xahk.layout import GridLayout, GridSpec, LayoutParams
from xahk.x11.display import Display
from xahk.events import EventLoop


class ArchivingRecipe(WindowManagerListenerObserver):
    r"""ArchivingRecipe

    ArchivingRecipe is a WindowManagerListenerObserver.
    Responsibility:
    """
    row12 = GridSpec.create_with_size(1, 1)
    col01 = GridSpec.create_with_size(0, 1)
    col23 = GridSpec.create_with_size(2, 1)

    left_param = LayoutParams(row12, col01)
    right_param = LayoutParams(row12, col23)
    layout = GridLayout()
    layout.set_wspace(3)
    layout.set_rows(4)
    layout.set_columns(4)

    def __init__(self, ):
        r"""
        """
        self.display = Display()
        self._wm = WindowManagerListener()
        self.screen = self._wm.list_screens()[0]
        self.windows = []
        self.titles = {}

    def start(self, ):
        """SUMMARY

        start()

        @Return:

        @Error:
        """
        self._wm.add_observer(self)
        man = MenuManager(DEFAULT_DIR)
        today_menu_path = man.get_menu(datetime.now()).get_path()
        thunar.openthunar(ARCHIVE_PATH)
        thunar.openthunar(today_menu_path)
        self.titles['left'] = '{} - File Manager'.format(
            ARCHIVE_PATH.get_basename())
        self.titles['right'] = '{} - File Manager'.format(
            today_menu_path.get_basename())
        EventLoop.get_instance(self.display).start_loop()

    def stop(self, ):
        """SUMMARY

        stop()

        @Return:

        @Error:
        """
        for window in self.windows:
            window.close().check()
        self._wm.remove_observer(self)
        EventLoop.get_instance(self.display).stop_loop()

    def on_created_window_client(self, window):
        """SUMMARY

        on_created_window_client(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        if window in self.windows:
            return
        if not window.title in self.titles.values():
            return
        if window.title == self.titles.get('left', None):
            self.layout.set_layout_item(window, self.left_param)
            self.windows.append(window)
        elif window.title == self.titles.get('right', None):
            self.layout.set_layout_item(window, self.right_param)
            self.windows.append(window)
        self.layout.layout(self.screen)
        self.display.flush()

    def on_destroyed_window_client(self, windowid):
        """SUMMARY

        on_destroyed_window(windowid)

        @Arguments:
        - `windowid`:

        @Return:

        @Error:
        """
        if windowid not in self.windows:
            return
        self.windows.remove(windowid)
        self.stop()


def _main():
    ArchivingRecipe().start()
    return 0

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# archiving_recipe.py ends here
