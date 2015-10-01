#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: create_recipe.py 451 2015-08-08 06:20:58Z t1 $
# $Revision: 451 $
# $Date: 2015-08-08 15:20:58 +0900 (Sat, 08 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-08 15:20:58 +0900 (Sat, 08 Aug 2015) $

r"""Name: create_recipe.py

"""

import sys
import os
import argparse

from mygoogle import chrome
from mygoogle.chrome.variables import DEFAULT_OPTS as CHROME_OPTS
from recipe._recipe import SEIKYO_URL, RECIPE_URL

from xahk.events import EventLoop
from xahk.listener import WindowListenerFactory
from xahk.listener import WindowListenerFactoryObserver
from xahk.listener import WindowListenerObserver
from xahk.wm import Display


__revision__ = '$Revision: 451 $'
__version__ = '0.0.1'

CHROME_OPTIONS = CHROME_OPTS + ['--new-window']


class CreateRecipe(WindowListenerFactoryObserver, WindowListenerObserver):
    r"""CreateRecipe

    CreateRecipe is a WindowListenerFactoryObserver.
    Responsibility:
    """
    def __init__(self, display):
        r"""

        @Arguments:
        - `display`:
        """
        WindowListenerFactoryObserver.__init__(self)
        WindowListenerObserver.__init__(self)
        self.display = display
        self.is_starting = False

    def start(self, ):
        r"""SUMMARY

        start()

        @Return:

        @Error:
        """
        if self.is_starting:
            return
        self.is_starting = True
        for window in WindowListenerFactory(self.display).list_windows():
            window.add_observer(self)
        WindowListenerFactory(self.display).add_observer(self)
        chrome.run(SEIKYO_URL, CHROME_OPTIONS)
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
        WindowListenerFactory(Display()).remove_observer(self)
        for window in WindowListenerFactory(self.display).list_windows():
            window.remove_observer(self)
        EventLoop(self.display).stop_loop()

    def on_window_title_changed(self, window):
        r"""SUMMARY

        on_window_title_changed(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        if window.title == "生活協同組合コープしが生協ログイン - Google Chrome":
            window.move(newx=1550, newy=70)
            if not window.is_maximized():
                window.maximize()
            chrome.run(RECIPE_URL)
            self.stop()

    def on_created_window_listener(self, window):
        r"""SUMMARY

        on_created_window_listener(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        window.add_observer(self)

    def on_destroyed_window_listener(self, window_id):
        r"""SUMMARY

        on_destroyed_window_listener(window_id)

        @Arguments:
        - `window_id`:

        @Return:

        @Error:
        """
        # if window_id in self.windows:
        #     self.windows.remove(window_id)
        #     self.stop()

    def __del__(self):
        """
        INTERNAL COMMENT
        Do not imprement `raise'!!
        """
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
    a = CreateRecipe(Display())
    a.start()
    return os.EX_OK

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# create_recipe.py ends here
