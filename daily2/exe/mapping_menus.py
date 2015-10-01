#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: mapping_menus.py 451 2015-08-08 06:20:58Z t1 $
# $Revision: 451 $
# $Date: 2015-08-08 15:20:58 +0900 (Sat, 08 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-08 15:20:58 +0900 (Sat, 08 Aug 2015) $

r"""Name: mapping_menus.py

"""
import sys
import os
import argparse
from ref.CMD import thunar
from recipe.menu2 import MenuManager
from recipe.menu2.common import DEFAULT_DIR
from recipe._recipe import ARCHIVE_PATH

from rectangle import Rectangle
from xcb import xinerama
from t1 import dateutil

from xahk.wm import Display
from xahk.events import EventLoop
from xahk.listener import WindowListenerFactory
from xahk.listener import WindowListenerFactoryObserver
from xahk.layout import GridLayout, GridSpec, LayoutParams



__revision__ = '$Revision: 451 $'
__version__ = '0.0.1'


class MappingMenus(WindowListenerFactoryObserver):
    r"""MappingMenus

    MappingMenus is a WindowListenerFactoryObserver.
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

    def __init__(self, display):
        r"""

        @Arguments:
        - `display`:
        """
        WindowListenerFactoryObserver.__init__(self)
        self.display = display
        xinrm = display(xinerama.key)
        s = xinrm.QueryScreens().reply().screen_info[1]
        self.screen = Rectangle(s.x_org, s.y_org, s.width - 8, s.height - 24)
        self.layout = GridLayout()
        self.layout.set_wspace(2)
        self.layout.set_rows(5)
        self.layout.set_columns(2)
        self.windows = []
        self.is_starting = False
        self.titles = {}

    def start(self, ):
        r"""SUMMARY

        start()

        @Return:

        @Error:
        """
        if self.is_starting:
            return
        self.is_starting = True
        WindowListenerFactory(self.display).add_observer(self)
        thunar.openthunar(str(ARCHIVE_PATH))
        self.titles['main'] = '{} - File Manager'.format(
            ARCHIVE_PATH.get_basename())
        today = dateutil.datetime.now()
        year, weekn, _ = today.isocalendar()
        thisthu = dateutil.datetime.strptime(
            '{} {} {}'.format(year, weekn - 1, 4), "%Y %W %w")
        seven = dateutil.timedelta(7)
        nextthu_to_wed = thisthu + seven
        next2thu_to_wed = nextthu_to_wed + seven
        menus = list(MenuManager(DEFAULT_DIR).iter_menus(
            nextthu_to_wed, next2thu_to_wed))
        for menu in menus:
            menu.open_editor()
            self.titles[menu.get_date().weekday()] = '{} - File Manager'.format(
                menu.get_path().get_basename())
        EventLoop(self.display).start_loop()

    def stop(self, ):
        r"""SUMMARY

        stop()

        @Return:

        @Error:
        """
        if not self.is_starting:
            return
        self.is_starting = False
        for window in self.windows:
            window.close()
        WindowListenerFactory(Display()).remove_observer(self)
        EventLoop(self.display).stop_loop()

    def on_created_window_listener(self, window):
        r"""SUMMARY

        on_created_window_listener(window)

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

    def on_destroyed_window_listener(self, window_id):
        r"""SUMMARY

        on_destroyed_window_listener(window_id)

        @Arguments:
        - `window_id`:

        @Return:

        @Error:
        """
        if window_id in self.windows:
            self.windows.remove(window_id)
            self.stop()


def _predef_options():
    parser = argparse.ArgumentParser(description="""""")
    parser.add_argument('--version',
                        dest='version',
                        action='version',
                        version=__version__,
                        help='Version Strings.')
    # (yas/expand-link "argparse_add_argument" t)
    return parser

def _main():
    r"""Main function."""
    parser = _predef_options()
    opts = parser.parse_args()
    # parser.print_usage()
    mpping = MappingMenus(Display())
    mpping.start()
    return os.EX_OK

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# mapping_menus.py ends here
