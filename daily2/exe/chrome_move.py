#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: chrome_move.py

"""

import sys
import os
import argparse

from xahk.wm import Display
from xahk.listener import WindowListenerFactory
from xahk.windowspec import WindowWMClassSpec


# for debug
import cgitb
cgitb.enable(format='text')


__version__ = '0.0.1'


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
    chrome_wins = WindowListenerFactory(Display()).list_windows(
        WindowWMClassSpec('Google-chrome'))
    shift = 0
    for win in chrome_wins:
        win.set_bounds(
            newx=99 + shift, newy=40 + shift, width=1112, height=938)
        shift += 10
    return os.EX_OK

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# chrome_move.py ends here
