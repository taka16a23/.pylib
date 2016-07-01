#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""archiving2 -- DESCRIPTION

"""
import sys
from time import sleep
from ref.CMD import thunar

from mypath import MyArchive
from pathhandler import PathHandler

from xahk.listener.window_manager import WindowManagerListener
from xahk.listener.window_manager_observer import WindowManagerListenerObserver
from xahk.layout import GridLayout, GridSpec, LayoutParams
from xahk.x11.display import Display
from xahk.events import EventLoop


class Archiving(WindowManagerListenerObserver):
    r"""Archiving

    Archivhing is a WindowManagerListenerObserver.
    Responsibility:
    """
    archive_path = MyArchive().get_path()
    download_path = PathHandler('~/Downloads').expanduser()
    mytemp_path = PathHandler('~/homedata/MYTEMP').expanduser()

    row01 = GridSpec.create_with_size(0, 1)
    row0 = GridSpec.create(0)
    row1 = GridSpec.create(1)
    col0 = GridSpec.create(0)
    col1 = GridSpec.create(1)

    left_param = LayoutParams(row01, col0)
    rightup_param = LayoutParams(row0, col1)
    rightdown_param = LayoutParams(row1, col1)
    layout = GridLayout()
    layout.set_wspace(2)
    layout.set_hspace(6)
    layout.set_rows(2)
    layout.set_columns(2)

    def __init__(self, ):
        r"""
        """
        self.display = Display()
        self.windows = []
        self.titles = {}
        self._wm = WindowManagerListener()
        self.screen = self._wm.list_screens()[0]

    def start(self, ):
        """SUMMARY

        start()

        @Return:

        @Error:
        """
        self.windows = []
        self.titles.clear()
        self._wm.add_observer(self)
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
        EventLoop.get_instance(self.display).start_loop()

    def stop(self, ):
        """SUMMARY

        stop()

        @Return:

        @Error:
        """
        self._wm.remove_observer(self)
        for window in self.windows:
            window.close().check()
        EventLoop.get_instance(self.display).stop_loop()

    def on_created_window_client(self, window):
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
        self.display.flush()

    def on_destroyed_window_client(self, windowid):
        r"""SUMMARY

        on_destroyed_window_listener(window_id)

        @Arguments:
        - `window_id`:

        @Return:

        @Error:
        """
        if windowid in self.windows:
            self.windows.remove(windowid)
            self.stop()


def _main():
    Archiving().start()
    return 0

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# archiving2.py ends here
