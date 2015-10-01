#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: chrome_move.py 349 2015-08-04 22:35:27Z t1 $
# $Revision: 349 $
# $Date: 2015-08-05 07:35:27 +0900 (Wed, 05 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-05 07:35:27 +0900 (Wed, 05 Aug 2015) $

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


__revision__ = '$Revision: 349 $'
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
