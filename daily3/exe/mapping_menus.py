#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""mapping_menus -- DESCRIPTION

"""
from time import sleep
import sys
from ref.CMD import thunar
from recipe.menu2 import MenuManager
from recipe.menu2.common import DEFAULT_DIR
from recipe._recipe import ARCHIVE_PATH
from t1 import dateutil

from xahk4.listener.window_manager import WindowManagerListener
from xahk4.listener.window_manager_observer import WindowManagerListenerObserver
from xahk4.layout import GridLayout, GridSpec, LayoutParams
from xahk4.x11.display import Display
from xahk4.events import EventLoop


class MappingMenus(WindowManagerListenerObserver):
    r"""MappingMenus

    MappingMenus is a WindowManagerListenerObserver.
    Responsibility:
    """
    row02 = GridSpec.create_with_size(0, 2)
    row0 = GridSpec.create(0)
    row1 = GridSpec.create(1)
    row2 = GridSpec.create(2)
    row3 = GridSpec.create(3)
    row4 = GridSpec.create(4)
    col0 = GridSpec.create(0)
    col1 = GridSpec.create(1)

    main_param = LayoutParams(row02, col0)
    thu_param = LayoutParams(row3, col0)
    fri_param = LayoutParams(row4, col0)
    sat_param = LayoutParams(row0, col1)
    sun_param = LayoutParams(row1, col1)
    mon_param = LayoutParams(row2, col1)
    tue_param = LayoutParams(row3, col1)
    wed_param = LayoutParams(row4, col1)

    layout = GridLayout()
    layout.set_wspace(2)
    layout.set_rows(5)
    layout.set_columns(2)

    def __init__(self, ):
        r"""

        @Arguments:
        - `display`:
        """
        self.display = Display()
        self._wm = WindowManagerListener()
        self.screen = self._wm.list_screens()[1]
        self.windows = []
        self.titles = {}

    def start(self, ):
        """SUMMARY

        start()

        @Return:

        @Error:
        """
        self.windows = []
        self.titles.clear()
        self._wm.add_observer(self)
        thunar.openthunar(str(ARCHIVE_PATH))
        self.titles['main'] = '{} - File Manager'.format(
            ARCHIVE_PATH.get_basename())
        today = dateutil.datetime.now()
        year, weekn, _ = today.isocalendar()
        thisthu = dateutil.datetime.strptime(
            '{} {} {}'.format(year, weekn - 1, 4), "%Y %W %w")
        seven = dateutil.timedelta(7)
        nextthu_to_wed = thisthu + seven
        nextthu_to_wed += seven
        next2thu_to_wed = nextthu_to_wed + seven
        menus = list(MenuManager(DEFAULT_DIR).iter_menus(
            nextthu_to_wed, next2thu_to_wed))
        for menu in menus:
            menu.open_editor()
            self.titles[menu.get_date().weekday()] = '{} - File Manager'.format(
                menu.get_path().get_basename())
        for window in self._wm.client_list():
            self.on_created_window_client(window)
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

        if window.title == self.titles.get('main', None):
            self.layout.set_layout_item(window, self.main_param)
            self.windows.append(window)
        elif window.title == self.titles.get(dateutil.THU, None):
            self.layout.set_layout_item(window, self.thu_param)
            self.windows.append(window)
        elif window.title == self.titles.get(dateutil.FRI, None):
            self.layout.set_layout_item(window, self.fri_param)
            self.windows.append(window)
        elif window.title == self.titles.get(dateutil.SAT, None):
            self.layout.set_layout_item(window, self.sat_param)
            self.windows.append(window)
        elif window.title == self.titles.get(dateutil.SUN, None):
            self.layout.set_layout_item(window, self.sun_param)
            self.windows.append(window)
        elif window.title == self.titles.get(dateutil.MON, None):
            self.layout.set_layout_item(window, self.mon_param)
            self.windows.append(window)
        elif window.title == self.titles.get(dateutil.TUE, None):
            self.layout.set_layout_item(window, self.tue_param)
            self.windows.append(window)
        elif window.title == self.titles.get(dateutil.WED, None):
            self.layout.set_layout_item(window, self.wed_param)
            self.windows.append(window)
        self.layout.layout(self.screen)
        self.display.flush()

    def on_destroyed_window_client(self, windowid):
        """SUMMARY

        on_destroyed_window_client(windowid)

        @Arguments:
        - `windowid`:

        @Return:

        @Error:
        """
        if not windowid in self.windows:
            return
        self.windows.remove(windowid)
        self.stop()



def _main():
    MappingMenus().start()
    return 0

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# mapping_menus.py ends here
