#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""_functions -- DESCRIPTION

"""

from xahk.wm import WindowManager, Display


def list_windows():
    r"""SUMMARY

    list_windows()

    @Return:

    @Error:
    """
    return WindowManager(Display()).list_windows()





# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _functions.py ends here
