#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""webpage -- DESCRIPTION

"""
import sys
from mygoogle import chrome
from mygoogle.chrome.variables import DEFAULT_OPTS as CHROME_OPTS
import argparse

from xahk.listener.window_manager import WindowManagerListener
from xahk.listener.window_manager_observer import WindowManagerListenerObserver
from xahk.x11.display import Display
from xahk.events import EventLoop
from xahk.utils.observer import Observable
from xahk.rectangle import Rectangle

from daily3.exe.specs import GOOGLE_CHROME_SPEC


class ChromeWebpageObserver(object):
    r"""ChromeWebpageObserver

    ChromeWebpageObserver is a object.
    Responsibility:
    """
    def on_chrome_window_created(self, webpage):
        """SUMMARY

        name()

        @Return:

        @Error:
        """

    def on_chrome_window_destroyed(self, webpage):
        """SUMMARY

        on_chrome_window_destroyed(windowid)

        @Arguments:
        - `windowid`:

        @Return:

        @Error:
        """


class ChromeWebpage(WindowManagerListenerObserver, Observable):
    r"""DailyWebpage

    DailyWebpage is a WindowManagerListenerObserver.
    Responsibility:
    """
    chrome_opts = CHROME_OPTS + ['--new-window']
    spec = GOOGLE_CHROME_SPEC

    def __init__(self, urls):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        Observable.__init__(self)
        self.window = None
        self.urls = urls
        self.wm = WindowManagerListener()
        self.display = Display()

    def start(self, ):
        """SUMMARY

        start()

        @Return:

        @Error:
        """
        if self.window:
            return
        if not self.wm.has_observer(self):
            self.wm.add_observer(self)
        chrome.run(self.urls, options=self.chrome_opts)
        EventLoop.get_instance(self.display).start_loop()

    def stop(self, ):
        """SUMMARY

        stop()

        @Return:

        @Error:
        """
        if self.wm.has_observer(self):
            self.wm.remove_observer(self)
        EventLoop.get_instance(self.display).stop_loop()

    def on_created_window_client(self, window):
        """SUMMARY

        on_created_window_client(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        if not self.spec.is_satisfied_window(window):
            return
        if self.window is not None:
            return
        self.window = window
        self.window.set_bounds(Rectangle.Builder(109, 50, 1112, 938).build()).check()
        self._notify_chrome_window_created()

    def _notify_chrome_window_created(self, ):
        """SUMMARY

        _notify_chrome_window_created()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_chrome_window_created(self)

    def on_destroyed_window_client(self, windowid):
        """SUMMARY

        on_destroyed_window_client(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        if self.window == windowid:
            self.stop()
            self._notify_chrome_window_destroyed()

    def _notify_chrome_window_destroyed(self, ):
        """SUMMARY

        _notify_chrome_window_destroyed(windowid)

        @Arguments:
        - `windowid`:

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_chrome_window_destroyed(self)


def _predef_options():
    parser = argparse.ArgumentParser(description="""""")
    parser.add_argument('--version',
                        dest='version',
                        action='version',
                        help='Version Strings.')
    parser.add_argument('--daily',
                        dest='daily',
                        action='store_true',
                        default=False,
                        required=False,
                        # (yas-expand-link "argparse_other_options" t)
                        help='A lot of messages.')
    parser.add_argument('--market',
                        dest='market',
                        action='store_true',
                        default=False,
                        required=False,
                        # (yas-expand-link "argparse_other_options" t)
                        help='A lot of messages.')
                        # (yas-expand-link "argparse_add_argument" t)
    parser.add_argument('--foreign',
                        dest='foreign',
                        action='store_true',
                        default=False,
                        required=False,
                        # (yas-expand-link "argparse_other_options" t)
                        help='A lot of messages.')
    parser.add_argument('--nation',
                        dest='nation',
                        action='store_true',
                        default=False,
                        required=False,
                        # (yas-expand-link "argparse_other_options" t)
                        help='A lot of messages.')
    parser.add_argument('--magazine',
                        dest='magazine',
                        action='store_true',
                        default=False,
                        required=False,
                        # (yas-expand-link "argparse_other_options" t)
                        help='A lot of messages.')


    return parser


def _main():
    parser = _predef_options()
    opts = parser.parse_args()
    urls = []
    if opts.daily:
        urls.extend(list(chrome.ChromeBMParse('Daily')))
    if opts.market:
        urls += list(chrome.ChromeBMParse('Market'))
    if opts.foreign:
        foregins = list(chrome.ChromeBMParse('Foreign News'))
        foregins.reverse()
        urls.extend(foregins)
    if opts.nation:
        nations = list(chrome.ChromeBMParse('Nation'))
        nations.reverse()
        urls.extend(nations)
    if opts.magazine:
        urls.extend(list(chrome.ChromeBMParse('Magazine')))
    if urls:
        ChromeWebpage(urls).start()
    return 0

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# webpage.py ends here
