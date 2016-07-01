#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""globalbind -- DESCRIPTION

"""
import subprocess as sbp
import logging

from xahk.bind.key import KeyEventHandler, GlobalKeyBinder
from xahk.bind.accelerator import Accelerator
from xahk.x11.display import Display
from xahk.listener.window_manager import WindowManagerListener
from xahk.x11.modifier import Modifier


class TapDispatcher(object):
    r"""TapDispatcher

    TapDispatcher is a object.
    Responsibility:
    """
    def can_dispatch_times(self, times):
        """SUMMARY

        can_dispatch_times(times)

        @Arguments:
        - `times`:

        @Return:

        @Error:
        """

    def on_tapped(self, event, times):
        """SUMMARY

        name()

        @Return:

        @Error:
        """


class ControlRuncher(KeyEventHandler):
    r"""ControlRuncher

    ControlRuncher is a KeyEventHandler.
    Responsibility:

    tap runcher
    """
    def __init__(self, interval=180):
        r"""
        """
        self._lasttime = 0
        self._wm = WindowManagerListener()
        self.interval = interval

    def on_key_press(self, event):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        event.resend().check()

    def on_key_release(self, event):
        r"""SUMMARY

        on_key_release(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        if event.time == self._lasttime:
            return
        if event.time - self._lasttime <= self.interval:
            logging.getLogger('xahk').debug('control {}'.format(event.time - self._lasttime))
            self._lasttime = event.time
            exists = False
            for win in self._wm.client_list():
                if 'xfrun4' in win.wmclass:
                    win.close()
                    exists = True
            if not exists:
                sbp.Popen('xfrun4')
            else:
                self._lasttime = 0
            self._wm.display.flush()
            return
        event.resend().check()
        self._lasttime = event.time
        self._wm.display.flush()


class ControlRuncherSynapse(KeyEventHandler):
    r"""ControlRuncher

    ControlRuncher is a KeyEventHandler.
    Responsibility:

    tap runcher
    """
    def __init__(self, interval=180):
        r"""
        """
        self._lasttime = 0
        self._wm = WindowManagerListener()
        self.interval = interval

    def on_key_press(self, event):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        event.resend().check()

    def on_key_release(self, event):
        r"""SUMMARY

        on_key_release(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        if event.time == self._lasttime:
            return
        if event.time - self._lasttime <= self.interval:
            logging.getLogger('xahk').debug('control {}'.format(event.time - self._lasttime))
            self._lasttime = event.time
            exists = False
            for win in self._wm.client_list():
                if 'synapse' in win.wmclass:
                    win.close()
                    exists = True
            if not exists:
                sbp.Popen('/usr/bin/synapse')
            else:
                self._lasttime = 0
            self._wm.display.flush()
            return
        event.resend().check()
        self._lasttime = event.time
        self._wm.display.flush()


RUNCHER = ControlRuncherSynapse()
GLOBALKEY = GlobalKeyBinder()
GLOBALKEY.bind(Accelerator(66, ), RUNCHER)
GLOBALKEY.bind(Accelerator(66, Modifier.Mask.Control), RUNCHER)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# globalbind.py ends here
