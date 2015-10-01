#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: archiving.py

"""
from time import sleep
import sys
import os
import argparse

from ref.CMD import thunar

from rectangle import Rectangle
from xcb import xinerama
from mypath import MyArchive
from pathhandler import PathHandler

from xahk.wm import Display
from xahk.events import EventLoop
from xahk.listener import WindowListenerFactory
from xahk.listener import WindowListenerFactoryObserver
from xahk.layout import GridLayout, GridSpec, LayoutParams


__version__ = '0.0.1'


class Archiving(WindowListenerFactoryObserver):
    r"""Archiving

    Archiving is a WindowListenerFactoryObserver.
    Responsibility:
    """
    archive_path = MyArchive().get_path()
    download_path = PathHandler('~/Downloads').expanduser()
    mytemp_path = PathHandler('/media/Data/MYTEMP')

    row01 = GridSpec.create_with_size(0, 1)
    row0 = GridSpec.create(0)
    row1 = GridSpec.create(1)
    col0 = GridSpec.create(0)
    col1 = GridSpec.create(1)

    left_param = LayoutParams(row01, col0)
    rightup_param = LayoutParams(row0, col1)
    rightdown_param = LayoutParams(row1, col1)

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
        self.layout.set_wspace(2)
        self.layout.set_hspace(6)
        self.layout.set_rows(2)
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
        thunar.openthunar(self.archive_path)
        thunar.openthunar(self.download_path)
        thunar.openthunar(self.mytemp_path)
        self.titles['left'] = '{} - File Manager'.format(
            self.archive_path.get_basename())
        self.titles['rightup'] = '{} - File Manager'.format(
            self.download_path.get_basename())
        self.titles['rightdown'] = '{} - File Manager'.format(
            self.mytemp_path.get_basename())
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
        elif window.title == self.titles.get('rightup', None):
            self.layout.set_layout_item(window, self.rightup_param)
            self.windows.append(window)
        elif window.title == self.titles.get('rightdown', None):
            self.layout.set_layout_item(window, self.rightdown_param)
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
    Archiving(Display()).start()
    return os.EX_OK

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# archiving.py ends here
