#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: archiving_recipe.py

"""

from time import sleep
import sys
import os
import argparse
from ref.CMD import thunar

from datetime import datetime

from rectangle import Rectangle
from recipe.menu2 import MenuManager
from recipe.menu2.common import DEFAULT_DIR
from recipe._recipe import ARCHIVE_PATH
from xcb import xinerama

from xahk.wm import Display
from xahk.events import EventLoop
from xahk.listener import WindowListenerFactory
from xahk.listener import WindowListenerFactoryObserver
from xahk.layout import GridLayout, GridSpec, LayoutParams

# for debug
import cgitb
cgitb.enable(format='text')


__version__ = '0.0.1'


class ArchivingRecipe(WindowListenerFactoryObserver):
    r"""ArchivingRecipe

    ArchivingRecipe is a WindowListenerFactoryObserver.
    Responsibility:
    """
    row12 = GridSpec.create_with_size(1, 1)
    col01 = GridSpec.create_with_size(0, 1)
    col23 = GridSpec.create_with_size(2, 1)

    left_param = LayoutParams(row12, col01)
    right_param = LayoutParams(row12, col23)

    def __init__(self, display):
        r"""

        @Arguments:
        - `display`:
        """
        WindowListenerFactoryObserver.__init__(self)
        self.display = display
        xinrm = display(xinerama.key)
        s = xinrm.QueryScreens().reply().screen_info[0]
        self.screen = Rectangle(s.x_org, s.y_org, s.width, s.height)
        self.layout = GridLayout()
        self.layout.set_wspace(3)
        self.layout.set_rows(4)
        self.layout.set_columns(4)
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
        man = MenuManager(DEFAULT_DIR)
        today_menu_path = man.get_menu(datetime.now()).get_path()
        thunar.openthunar(ARCHIVE_PATH)
        thunar.openthunar(today_menu_path)
        self.titles['left'] = '{} - File Manager'.format(
            ARCHIVE_PATH.get_basename())
        self.titles['right'] = '{} - File Manager'.format(
            today_menu_path.get_basename())
        sleep(0.5)
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
        if window.title == self.titles.get('left', None):
            self.layout.set_layout_item(window, self.left_param)
            self.windows.append(window)
        elif window.title == self.titles.get('right', None):
            self.layout.set_layout_item(window, self.right_param)
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
    a = ArchivingRecipe(Display())
    a.start()
    return os.EX_OK

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# archiving_recipe.py ends here
