#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""sendkeys -- DESCRIPTION

"""
from .analyzer import Analyzer

from .scanner import Scanner
from .replacer import REPLACER

from xahk.sendkeys import analyze
from xahk.wm.window_manager import WindowManager
from xahk.input.cursor import Cursor


class Sendkeys(object):
    r"""Sendkeys

    Sendkeys is a object.
    Responsibility:
    """
    def __init__(self, display, line):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self.display = display
        self.line = line
        self._exp = None
        self._load()

    def _load(self, ):
        r"""SUMMARY

        _load()

        @Return:

        @Error:
        """
        line = self.line
        for target, replace in REPLACER:
            line = line.replace(target, replace)
        self._exp = Analyzer().analyze(self.display, Scanner().scan(line))

    def send(self, ):
        r"""SUMMARY

        send()

        @Return:

        @Error:
        """
        self._exp.interpret()


class SendKeys(object):
    r"""SendKeys

    SendKeys is a object.
    Responsibility:
    """
    analyzer = analyze.Analyzer()

    def __init__(self, line):
        r"""

        @Arguments:
        - `display`:

        """
        self._wm = WindowManager()
        self._cursor = Cursor()
        self._context = {'child': 0,
                         'display': self.display,
                         'root': self._wm.root,
                         'rootx': 0,
                         'rooty': 0,
                         'samescreen': 1,
                         'sequence': 0,
                         'time': 0,
                         }
        self.line = line
        for target, replace in REPLACER:
            line = line.replace(target, replace)
        self._tokens = Scanner().scan(line)

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self._wm.get_display()

    display = property(get_display)

    def _make_exps(self, ):
        r"""SUMMARY

        _make_exps()

        @Return:

        @Error:
        """
        return self.analyzer.analyze(self._context, self._tokens)

    def send(self, window=None):
        r"""SUMMARY

        send(window=None)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        win = window or self._wm.get_active_window()
        self._context['window'] = int(win)
        point = self._cursor.get_point()
        rep = self.display.core.TranslateCoordinates(
            self._context['window'], self._context['root'], point.x, point.y).reply()
        point.set_x(-(rep.dst_x - (2 * point.x)))
        point.set_y(-(rep.dst_y - (2 * point.y)))
        self._context['point'] = point
        exps = self._make_exps()
        for cookie in exps.interpret():
            cookie.check()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sendkeys.py ends here
