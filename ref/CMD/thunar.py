#!/usr/bin/env python
# -*- coding: utf-8 -*-
r""" thunar -- thunar info


"""

from time import sleep
import os
import sys as _sys
import subprocess as sbp

import wm

from xahk4.wm.window_manager import WindowManager
from xahk4.bind.window_spec import WindowWMClassSpec


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'


BIN = 'thunar'
BINPATH = '/usr/bin/thunar'
CLASS = 'Thunar'
PSNAME = 'Thunar'

MYENV = os.environ
MYENV['LANG'] = 'en_US.UTF-8'


def openthunar(path):
    r"""SUMMARY

    openthunar(dir_)

    @Arguments:
    - `dir_`:

    @Return:
    """
    if not os.path.isdir(path) or not os.path.exists(path):
        raise ValueError()
    return sbp.Popen((BINPATH, path), env=MYENV)


class ThunarWMHandle(object):
    r"""
    """

    def __init__(self, path):
        r"""

        @Arguments:
        - `dir_`:
        """
        self.child = None
        self.title = None
        self.win = None
        self.sec = 10
        path = os.path.expanduser(path)
        if not os.path.isdir(path) and os.path.isfile(path):
            path = os.path.dirname(path)
        if not os.path.exists(path):
            raise ValueError()
        self.dir = path
        self.title = '{} - File Manager'.format(os.path.basename(self.dir))

    def open(self, ):
        r"""SUMMARY

        open()

        @Return:
        """
        self.child = sbp.Popen((BINPATH, self.dir), env=MYENV)
        try:
            wm.WinWait(sec=self.sec).win(title=self.title)
            sleep(0.5)
        except wm.error.TimeoutError:
            return False

    def move(self, **kwargs):
        r"""SUMMARY

        move()

        @Return:
        """
        if not self.getwin():
            return False
        self.win.move(**kwargs)

    def getwin(self, ):
        r"""SUMMARY

        getwin()

        @Return:
        """
        for win in wm.iter_matchwin(klass=CLASS):
            if self.title == win.title:
                self.win = win
                return True
        return False


def side_by_side(left, right):
    r"""SUMMARY

    side_by_side(left, right)

    @Arguments:
    - `left`:
    - `right`:

    @Return:
    """
    leftwm = ThunarWMHandle(left)
    leftwm.open()
    leftwm.move(x=1280, y=1, width=835, height=1024)
    rightwm = ThunarWMHandle(right)
    rightwm.open()
    rightwm.move(x=2120, y=1, width=840, height=1024)


def close_all():
    r"""Close all opened thunar.

    close_all()

    @Return:
    None
    """
    windows = WindowManager().client_list()
    spec = WindowWMClassSpec(CLASS)
    for win in windows:
        if spec.is_satisfied_window(win):
            win.close().check()
    # for win in wm.iter_matchwin(klass=CLASS):
        # win.close()


class ThunarManager(object):
    r"""ThunarManager

    ThunarManager is a object.
    Responsibility:
    """
    wmclass = ['Thunar', 'Thunar']
    spec = WindowWMClassSpec(wmclass[0])
    env = os.environ
    env['LANG'] = 'en_US.UTF-8'
    binpath = '/usr/bin/thunar'

    def __init__(self, display):
        r"""
        """
        self.display = display
        self.spec = WindowWMClassSpec(CLASS)
        self._wm = WindowManager()

    def list_thunar_windows(self, ):
        r"""SUMMARY

        list_thunar_windows()

        @Return:

        @Error:
        """
        return [x for x in self._wm.client_list() if self.spec.is_satisfied_window(x)]

    def open_thunar(self, path):
        r"""SUMMARY

        open_thunar(path)

        @Arguments:
        - `path`:

        @Return:

        @Error:
        """
        sbp.Popen((self.binpath, path), env=self.env)


def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# thunar.py ends here
