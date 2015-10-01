#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""posix_functions -- DESCRIPTION

"""
import os as _os
import sys as _sys
from glob import glob as _glob

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'

PANEL_DIR = _os.path.expanduser('~/.config/xfce4/panel')


def iter_laucher_dir():
    r"""SUMMARY

    list_laucher_dir()

    @Return:
    """
    for path in _glob(_os.path.join(PANEL_DIR, '*')):
        if _os.path.isdir(path):
            yield path


def iter_desktops():
    r"""SUMMARY

    iter_desktop_config()

    @Return:
    """
    for dir_ in iter_laucher_dir():
        for file_ in _glob(_os.path.join(dir_, '*.desktop')):
            yield file_


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# posix_functions.py ends here
