#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""thunar -- DESCRIPTION

"""
import sys
from xahk.wm.window_spec import WindowWMClassSpec
from xahk.wm.window_manager import WindowManager


THUNAR_SPEC = WindowWMClassSpec('Thunar')



def _main():
    for window in WindowManager().client_list():
        if THUNAR_SPEC.is_satisfied_window(window):
            window.close().check()
    return 0

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# thunar.py ends here
