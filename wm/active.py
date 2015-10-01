#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id$
# $Revision$
# $Date$
# $Author$
# $LastChangedBy$
# $LastChangedDate$
r""" active -- part of wm

$Revision$

"""
import sys as _sys
import curses as _curses
from time import sleep as _sleep

from Xlib import error
from wm._core import ActiveWindow

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision$'
__version__ = '0.1.0'

__all__ = ['get', 'title', 'klass', 'pid', 'monitor']


def get():
    r"""SUMMARY

    @Return:
    """
    return ActiveWindow()

def title():
    r"""SUMMARY

    @Return:
    """
    return ActiveWindow().name


def klass():
    r"""SUMMARY

    @Return:
    """
    return ActiveWindow().klass

def pid():
    r"""SUMMARY

    @Return:
    """
    return ActiveWindow().pid

def id():
    r"""SUMMARY

    @Return:
    """
    return ActiveWindow().id

def monitor(idle=0.5):
    r"""Realtime monitoring active windows.

    Press "Control c" will exit.
    @Arguments:
    - `idle`: refresh time.
    """
    onerror = ''
    stdscr = _curses.initscr()
    _curses.noecho()
    _curses.cbreak()

    maxlen = 20
    while 1:
        try:
            win = ActiveWindow()
            stdscr.addstr(0, 0, '* Press "Control c" will exit. *')
            for num, str_ in enumerate(str(win).split('\n'), start=1):
                maxlen = max(len(str_), maxlen)
                stdscr.addstr(num, 0, str_ + ' ' * maxlen)
            # for cursor point to beggining of line
            stdscr.addstr(num + 1, 0, '')
            stdscr.refresh()
            _sleep(idle)
        except error.BadWindow:
            continue
        except KeyboardInterrupt:
            onerror = 'Keyboard Interrupted'
            break
        finally:
            _curses.echo()
            _curses.nocbreak()
            _curses.endwin()
            print(onerror)


def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# active.py ends here
