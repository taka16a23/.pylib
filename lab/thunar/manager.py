#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""manager -- DESCRIPTION

"""
import os

from xahk4.wm.window_manager import WindowManager
from xahk4.sendkeys.sendkeys import SendKeys

from lab.thunar.commons import THUNAR_WMSPEC


class ThunarClient(object):
    r"""ThunarClient

    ThunarClient is a object.
    Responsibility:
    """
    def __init__(self, window):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self.window = window

    def open_up(self, ):
        """SUMMARY

        open_up()

        @Return:

        @Error:
        """
        SendKeys('!{Up}').send(self.window)

    def back(self, ):
        """SUMMARY

        back()

        @Return:

        @Error:
        """
        SendKeys('!{Left}').send(self.window)

    def forward(self, ):
        """SUMMARY

        forward()

        @Return:

        @Error:
        """
        SendKeys('!{Right}').send(self.window)

    def home(self, ):
        """SUMMARY

        home()

        @Return:

        @Error:
        """
        SendKeys('!{Home}').send(self.window)

    def newtab(self, ):
        """SUMMARY

        newtab()

        @Return:

        @Error:
        """
        SendKeys('^t').send(self.window)

    def new_window(self, ):
        """SUMMARY

        new_window()

        @Return:

        @Error:
        """




class ThunarManager(object):
    r"""ThunarManager

    ThunarManager is a object.
    Responsibility:
    """
    spec = THUNAR_WMSPEC

    def __init__(self, ):
        r"""
        """
        self._wm = WindowManager()
        self._env = os.environ['LANG']

    def list_thunar_windows(self, ):
        """SUMMARY

        list_thunar_windows()

        @Return:

        @Error:
        """
        return [ThunarClient(x) for x in self._wm.client_list()
                if self.spec.is_satisfied_window(x)]

    def open_thunar(self, path):
        """SUMMARY

        open_thunar(path)

        @Arguments:
        - `path`:

        @Return:

        @Error:
        """
        sbp.Popen((self.binpath, path), env=self.env)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# manager.py ends here
