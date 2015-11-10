#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: close_all_thunar.py

"""

import sys
import os
import argparse

from ref.CMD.thunar import ThunarManager
from xahk.wm import Display

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
    tm = ThunarManager(Display())
    for thnr in tm.list_thunar_windows():
        thnr.close()
    return os.EX_OK

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# close_all_thunar.py ends here