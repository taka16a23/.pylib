#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""manager -- DESCRIPTION

"""
import os
import subprocess as sbp

from xahk.wm.window_manager import WindowManager
from xahk.sendkeys.sendkeys import SendKeys
from xahk.layout import HorizonLayout, VerticalLayout
from xahk.wm.client import WindowClient
from xahk.x11.window import Window
from lab.thunar.commons import THUNAR_WMSPEC, THUNAR_BIN_PATH


class ThunarClient(WindowClient):
    """ThunarClient

    ThunarClient is a object.
    Responsibility:
    """
    def __init__(self, window):
        """

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        WindowClient.__init__(self, window)

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
        SendKeys('^n').send(self.window)

    def close_all_windows(self, ):
        """SUMMARY

        close_all_windows()

        @Return:

        @Error:
        """
        SendKeys('^+w').send(self.window)

    def close_tab(self, ):
        """SUMMARY

        close_tab()

        @Return:

        @Error:
        """
        SendKeys('^w').send(self.window)

    def close_window(self, ):
        """SUMMARY

        close_window()

        @Return:

        @Error:
        """
        SendKeys('^q').send(self.window)

    def show_properties(self, ):
        """SUMMARY

        show_properties()

        @Return:

        @Error:
        """
        SendKeys('!{Return}').send(self.window)

    def reload(self, ):
        """SUMMARY

        reload()()

        @Return:

        @Error:
        """
        SendKeys('^r').send(self.window)


class ThunarManager(WindowManager):
    r"""ThunarManager

    ThunarManager is a object.
    Responsibility:
    """

    def _create_client(self, wid):
        """SUMMARY

        _create_client(wid)

        @Arguments:
        - `wid`:

        @Return:

        @Error:

        FactoryMethod
        """
        return ThunarClient(Window(self.display, wid))

    def get_active_window(self):
        """Return the window ID of the currently active window or None
        if no window has the focus.

        returns int
        """
        wins = self._get_property_windows('_NET_ACTIVE_WINDOW', 1)
        if not wins:
            return None
        client = self._create_client(wins[0])
        if not THUNAR_WMSPEC.is_satisfied_window(client):
            return None
        return client

    def client_list(self, ):
        """SUMMARY

        client_list()

        @Return:

        @Error:
        """
        windows = []
        clients = [self._create_client(i)
                   for i in self._get_property_windows('_NET_CLIENT_LIST', 20)]
        for client in clients:
            if THUNAR_WMSPEC.is_satisfied_window(client):
                windows.append(client)
        return windows

    def client_list_stacking(self, ):
        r"""SUMMARY

        client_list_stacking()

        @Return:

        @Error:
        """
        windows = []
        clients = [self._create_client(i)
                   for i in self._get_property_windows('_NET_CLIENT_LIST_STACKING', 20)]
        for client in clients:
            if THUNAR_WMSPEC.is_satisfied_window(client):
                windows.append(client)
        return windows

    def open_thunar(self, path):
        """SUMMARY

        open_thunar(path)

        @Arguments:
        - `path`:

        @Return:

        @Error:
        """
        sbp.Popen((THUNAR_BIN_PATH, path), env=os.environ['LANG'])

    def close_all(self, ):
        """SUMMARY

        close_all()

        @Return:

        @Error:
        """
        for x in self.client_list():
            if THUNAR_WMSPEC.is_satisfied_window(x):
                x.close().check()

    def horizontal_layout(self, screen):
        """SUMMARY

        horizontal_layout(screen)

        @Arguments:
        - `screen`:

        @Return:

        @Error:
        """
        layout = HorizonLayout()
        for window in self.client_list():
            layout.append(window)
        return layout.layout(screen)

    def vertical_layout(self, screen):
        """SUMMARY

        vertical_layout(screen)

        @Arguments:
        - `screen`:

        @Return:

        @Error:
        """
        layout = VerticalLayout()
        for window in self.client_list():
            layout.append(window)
        return layout.layout(screen)

    def count_thunar_windows(self, ):
        """SUMMARY

        count_thunar_windows()

        @Return:

        @Error:
        """
        return len(self.client_list())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# manager.py ends here
