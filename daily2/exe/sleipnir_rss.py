#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: sleipnir_rss.py 442 2015-08-07 01:25:53Z t1 $
# $Revision: 442 $
# $Date: 2015-08-07 10:25:53 +0900 (Fri, 07 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-07 10:25:53 +0900 (Fri, 07 Aug 2015) $

r"""Name: sleipnir_rss.py

"""

from time import sleep
import sys
import os
import argparse
import subprocess as sbp

from junk.mypsutil import psexists
# from ref.CMD import sleipnir


from xahk.events import EventLoop
from xahk.listener import WindowListenerFactory
from xahk.listener import WindowListenerFactoryObserver
from xahk.piece import X11Button
from xahk.binder.define import ButtonIndex
from xahk.wm import Display
from xahk.wm.atom_cache import AtomCache
from xahk.windowspec import WindowWMClassSpec


# for debug
import cgitb
cgitb.enable(format='text')


__revision__ = '$Revision: 442 $'
__version__ = '0.0.1'

BIN = 'Sleipnir.exe'
LAUNCHER = '/root/.zsh/scripts/sleipnir'


class SleipnirRSS(WindowListenerFactoryObserver):
    r"""SleipnirRSS

    SleipnirRSS is a WindowListenerFactoryObserver.
    Responsibility:
    """
    def __init__(self, display):
        r"""

        @Arguments:
        - `display`:
        """
        WindowListenerFactoryObserver.__init__(self)
        self.display = display
        self.is_starting = False
        self.pid = None
        self._atom_cache = AtomCache(self.display, ['_NET_WM_WINDOW_TYPE_DIALOG',
                                                    '_NET_WM_WINDOW_TYPE_NORMAL'])
        self.left_button = X11Button(ButtonIndex.Left)
        self.window = None

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
        if not psexists(BIN):
            self.pid = sbp.Popen(LAUNCHER).pid
        else:
            windows = WindowListenerFactory(self.display).list_windows(
                WindowWMClassSpec('Sleipnir.exe'))
            if windows:
                self.window = windows[0]
                self.config_sleipnir()
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
        WindowListenerFactory(self.display).remove_observer(self)
        EventLoop(self.display).stop_loop()

    def on_created_window_listener(self, window):
        r"""SUMMARY

        on_created_window_listener(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        if 'FeedbackAgent.exe' in window.wmclass:
            window.close()
            return
        if 'Sleipnir.exe' not in window.wmclass:
            return
        if self._atom_cache.get_atom('_NET_WM_WINDOW_TYPE_DIALOG') == window.type:
            if window.title == 'セキュリティ警告':
                window.close()
                return
            else:
                window.close()
                sleep(0.5)
                self.config_sleipnir()
        if self._atom_cache.get_atom('_NET_WM_WINDOW_TYPE_NORMAL') == window.type:
            self.window = window
            self.config_sleipnir()

    def config_sleipnir(self, ):
        r"""SUMMARY

        config_sleipnir(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        if self.window.is_maximized():
            self.window.maximize(0)
        self.window.move(1380, 0)
        sleep(1)
        self.window.maximize()
        sleep(8)
        self.left_button.tap(self.window, 75, 130)
        self.left_button.display.flush()

    def on_destroyed_window_listener(self, window_id):
        r"""SUMMARY

        on_destroyed_window_listener(window_id)

        @Arguments:
        - `window_id`:

        @Return:

        @Error:
        """
        if self.window == window_id:
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
    display = Display()
    pnir = SleipnirRSS(display)
    pnir.start()
    return os.EX_OK

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sleipnir_rss.py ends here
