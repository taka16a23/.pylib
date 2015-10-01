#!/usr/bin/env python
# -*- coding: utf-8 -*-
r""" _display -- part of wm


"""

import sys as _sys

from Xlib.display import Display


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'


class _Display(object):
    r"""Connect Xserver."""

    _display = Display()

    def __init__(self, display=None):
        r"""

        Arguments:
        - `display`:
        """
        if display is not None:
            self._display = display
        self._root = self._display.screen().root

    def _reload_display(self):
        r"""SUMMARY

        @Return:
        """
        old = self._display
        self._display = Display()
        return (not (hash(old) == hash(self._display)))

    def _reload_root(self):
        r"""SUMMARY

        @Return:
        """
        self._reload_display()
        old = self._root
        self._root = self._display.screen().root
        return (not (hash(old) == hash(self._root)))

    @classmethod
    def _atom(cls, name):
        r"""Return atom with given name."""
        return cls._display.intern_atom(name)

    def _sync(self):
        r"""SUMMARY

        @Return:
        """
        self._display.sync()


def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _display.py ends here
