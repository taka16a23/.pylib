#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""chrome_move -- DESCRIPTION

"""
import os
import sys
import argparse
from xahk.wm.window_manager import WindowManager
from xahk.rectangle import Rectangle
from daily3.exe.specs import GOOGLE_CHROME_SPEC


def _predef_options():
    parser = argparse.ArgumentParser(description="""""")
    parser.add_argument('--version',
                        dest='version',
                        action='version',
                        help='Version Strings.')
    # (yas/expand-link "argparse_add_argument" t)
    return parser


LEFT_SCREEN_POSISION = Rectangle.Builder(99, 40, 1112, 938).build()


def _main():
    """SUMMARY

    _main()

    @Return:

    @Error:
    """
    parser = _predef_options()
    opts = parser.parse_args()
    wm = WindowManager()
    chromes = [x for x in wm.client_list() if GOOGLE_CHROME_SPEC.is_satisfied_window(x)]
    rect = Rectangle.Builder().set_rectangle(LEFT_SCREEN_POSISION).build()
    for win in chromes:
        win.set_bounds(rect).check()
        rect.set_x(rect.get_x() + 10)
        rect.set_y(rect.get_y() + 10)
    return os.EX_OK


if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# chrome_move.py ends here
