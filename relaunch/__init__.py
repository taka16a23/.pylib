#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


0.1.1: Modified
"subprocess.Popen" to "os.execl"

"""
import os as _os
import sys as _sys

__version__ = "0.1.1"

__all__ = ['relaunch', ]


def relaunch():
    r"""SUMMARY

    realunch()

    @Return:
    """
    python = _sys.executable
    _os.execl(python, python, *_sys.argv)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
