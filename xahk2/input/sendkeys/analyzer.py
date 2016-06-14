#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""analyzer -- DESCRIPTION

"""
# TODO: (Atami) [2015/12/12]
# Refactoring

from abc import ABCMeta, abstractmethod
from collections import deque

from rectangle import Point

from xahk2.input.sendkeys.token import TokenTypes
from xahk2.input.key import X11Key
from xahk2.input.button import X11Button
from xahk2.input.keyboard import X11Keyboard
from xahk2.input.mouse import X11Mouse
from xahk2.input.keysym import KeySym
from xahk2.input.sendkeys.expressions import (XTestSendKeyExpression,
                                              ModifierExpression,
                                              RepeatExpression,
                                              PointExpression,
                                              BehaveExpression,
                                              Behave,)


class Analyzer(object):
    """Abstract class Analyzer
    """
    __metaclass__ = ABCMeta

    # Attributes:
    def __init__(self, ):
        r"""
        """
        self._expressions = []

    # Operations
    def list_expressions(self):
        """function list_expressions

        returns
        """
        return self._expressions[:] # return new list

    def clear(self):
        """function clear

        returns
        """
        self._expressions = []

    @abstractmethod
    def analyze(self, token):
        """function analyze

        token:

        returns
        """
        raise NotImplementedError()


class XTestAnalyzer(Analyzer):
    r"""XTestAnalyzer

    XTestAnalyzer is a Analyzer.
    Responsibility:
    """
    __modkeysyms = {'+': KeySym.from_name('Shift_L'),
                    '!': KeySym.from_name('Alt_L'),
                    '^': KeySym.from_name('Control_L'),
                    '#': KeySym.from_name('Super_L'),}

    __behave = {'press': Behave.PRESS,
                'release': Behave.RELEASE,}

    def __init__(self, display):
        r"""
        """
        Analyzer.__init__(self, )
        self._modifiers = deque()
        self._keyboard = X11Keyboard(display)
        self._keys = self._keyboard.list_keys()
        self._symmap = {}
        for key in self._keys:
            syms = key.list_keysyms()
            self._symmap.setdefault(syms[0], (key, False)) # bool is Shift Flag
            self._symmap.setdefault(syms[1], (key, True))
        self._mouse = X11Mouse(display)
        self._buttonmap = {'lbutton': self._mouse.get_button(1),
                           'lclick': self._mouse.get_button(1),
                           'mbutton': self._mouse.get_button(2),
                           'mclick': self._mouse.get_button(2),
                           'rbutton': self._mouse.get_button(3),
                           'rclick': self._mouse.get_button(3),
                           'wheelup': self._mouse.get_button(4),
                           'wheeldown': self._mouse.get_button(5),}
        self._modkeys = {}

    @property
    def display(self, ):
        r"""SUMMARY

        display()

        @Return:

        @Error:
        """
        return self._keyboard.get_display()

    def _add_expression(self, expression):
        r"""SUMMARY

        @Arguments:

        @Return:

        @Error:
        """
        exp = expression
        while self._modifiers:
            exp = ModifierExpression(exp, self._modifiers.popleft())
        self._expressions.append(exp)

    def _analyze_modifier(self, value):
        r"""SUMMARY

        _analyze_modifier(token)

        @Arguments:
        - `token`:

        @Return:

        @Error:
        """
        # convert '+!^#' to keysym
        modsym = self.__modkeysyms.get(value, None)
        if modsym is None:
            # TODO: (Atami) [2015/12/12]
            raise StandardError('not supported character mod')
        # get modifier key
        key, _ = self._symmap.get(modsym, (None, False))
        if key is None:
            # TODO: (Atami) [2015/12/12]
            raise StandardError()
        self._modifiers.append(key)

    def analyze(self, token):
        r"""SUMMARY

        analyze(token)

        @Arguments:
        - `token`:

        @Return:

        @Error:
        """
        if token.equal_types(TokenTypes.KEY_NAME):
            keysym = KeySym.from_name(token.get_value())
            key, shifted = self._symmap.get(keysym, (None, False))
            if key is None:
                # TODO: (Atami) [2015/12/12]
                raise StandardError('Unknown keysym')
            if shifted:
                self._analyze_modifier('+')
            self._add_expression(XTestSendKeyExpression(key))
            return
        if token.equal_types(TokenTypes.BUTTON_NAME):
            button = self._buttonmap.get(token.get_value().lower(), None)
            if button is None:
                raise StandardError('Unknown button')
            self._add_expression(XTestSendKeyExpression(button))
            return
        if token.equal_types(TokenTypes.KEYCODE):
            key = X11Key(self.display, int(token.get_value()))
            self._add_expression(XTestSendKeyExpression(key))
            return
        if token.equal_types(TokenTypes.BUTTONCODE):
            button = self._mouse.get_button(int(token.get_value()))
            self._add_expression(XTestSendKeyExpression(button))
            return
        if token.equal_types(TokenTypes.MODIFIER):
            return self._analyze_modifier(token.get_value())
        if token.equal_types(TokenTypes.REPEAT):
            if not self._expressions:
                raise StandardError('Analyze Error token grammer')
            last_exp = self._expressions.pop()
            self._expressions.append(
                RepeatExpression(last_exp, int(token.get_value())))
            return
        if token.equal_types(TokenTypes.BEHAVE):
            behave = self.__behave.get(token.get_value().lower(), None)
            if behave is None:
                # TODO: (Atami) [2015/12/12]
                raise StandardError('Unknown behave')
            last_exp = self._expressions.pop()
            self._expressions.append(BehaveExpression(last_exp, behave))
            return
        if token.equal_types(TokenTypes.POINT):
            point = token.get_value().split('-')
            if len(point) != 2:
                # TODO: (Atami) [2015/12/12]
                raise StandardError('not point query')
            last_exp = self._expressions.pop()
            exp = PointExpression(
                last_exp, Point(int(point[0]), int(point[1])), self.display)
            self._expressions.append(exp)
            return
        raise StandardError('Unknown Token', token)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# analyzer.py ends here
