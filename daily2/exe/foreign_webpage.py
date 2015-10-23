#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: foreign_webpage.py

"""

import sys
import os
import argparse

import busywait

from mygoogle import chrome
from mygoogle.chrome.variables import DEFAULT_OPTS as CHROME_OPTS

from xahk.events import EventLoop
from xahk.listener import WindowListenerFactory
from xahk.listener import WindowListenerFactoryObserver
from xahk.wm import Display

# for debug
import cgitb
cgitb.enable(format='text')


__version__ = '0.0.1'


class ForeignWebpage(WindowListenerFactoryObserver):
    r"""ForeignWebpage

    ForeignWebpage is a WindowListenerFactoryObserver.
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
        urls = list(chrome.ChromeBMParse('Foreign News'))
        try:
            chrome.run(urls.pop(), CHROME_OPTS + ['--new-window'])
        except IndexError:
            pass
        bwait = busywait.BusyWait(50)
        while urls:
            try:
                bwait.wait_timeout(interval=1, timeout=15)
            except busywait.TimeOut:
                pass
            chrome.run(urls.pop(), CHROME_OPTS)
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
        if not 'google-chrome' in window.wmclass:
            return
        if not self.window is None:
            return
        self.window = window

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
    ForeignWebpage(Display()).start()
    return os.EX_OK

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# foreign_webpage.py ends here
