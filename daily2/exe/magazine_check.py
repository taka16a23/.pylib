#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: magazine_check.py 351 2015-08-05 21:00:40Z t1 $
# $Revision: 351 $
# $Date: 2015-08-06 06:00:40 +0900 (Thu, 06 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-06 06:00:40 +0900 (Thu, 06 Aug 2015) $

r"""Name: magazine_check.py

"""

import sys
import os
import argparse

from mygoogle import chrome
from mygoogle.chrome.variables import DEFAULT_OPTS as CHROME_OPTS

from xahk.events import EventLoop
from xahk.listener import WindowListenerFactory
from xahk.listener import WindowListenerFactoryObserver
from xahk.wm import Display

# for debug
import cgitb
cgitb.enable(format='text')


__revision__ = '$Revision: 351 $'
__version__ = '0.0.1'


class MagazineCheck(WindowListenerFactoryObserver):
    r"""Webpage

    MagazineCheck is a WindowListenerFactoryObserver.
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
        urls = list(chrome.ChromeBMParse('Magazine'))
        chrome_opts = CHROME_OPTS + ['--new-window']
        chrome.run(urls, options=chrome_opts)
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
        if not 'Google-chrome' in window.wmclass:
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
    MagazineCheck(Display()).start()
    return os.EX_OK

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# magazine_check.py ends here
