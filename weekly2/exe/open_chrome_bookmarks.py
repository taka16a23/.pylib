#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: open_chrome_bookmarks.py


c=54
h=43
r=27
o=32
m=58
e=26
:=48
b=56
k=45
a=38
r=35
/=61
s=39
"""
from time import sleep
import sys
import os
import argparse

from mygoogle import chrome
from mygoogle.chrome.variables import DEFAULT_OPTS as CHROME_OPTS

from xahk.events import EventLoop
from xahk.listener import WindowListenerFactory
from xahk.listener import WindowListenerFactoryObserver
from xahk.wm import Display
from xahk.piece import X11Key
from xahk.binder import ModifierMask

# for debug
import cgitb
cgitb.enable(format='text')


__version__ = '0.0.1'


class ChromeBookmark(WindowListenerFactoryObserver):
    r"""ChromeBookmark

    ChromeBookmark is a WindowListenerFactoryObserver.
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
        chrome.run('', options=CHROME_OPTS + ['--new-window'])
        sleep(1)
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
        c=54
        h=43
        r=27
        o=32
        m=58
        e=26
        :=48
        b=56
        k=45
        a=38
        r=27
        /=61
        s=39
        Enter=36

        54,43,27,32,58,26,48,61,61,56,32,32,45,58,38,27,45,39,61

        """
        if not 'Google-chrome' in window.wmclass:
            return
        if not self.window is None:
            return
        self.window = window
        sleep(3)
        key = X11Key(46, ModifierMask.Control)
        key.tap(window)
        key.display.flush()
        for code in [54,43,27,32,58,26,48,61,61,56,32,32,45,58,38,27,45,39,61]:
            X11Key(code).tap(window)
        key = X11Key(36)
        key.tap(window)
        key.display.flush()

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
    ChromeBookmark(Display()).start()
    return os.EX_OK

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# open_chrome_bookmarks.py ends here
