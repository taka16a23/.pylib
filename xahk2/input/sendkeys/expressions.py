#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""expressions -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod
from enum import Enum

from xahk2.input.cursor import X11Cursor


class Behave(Enum):
    r"""Behave

    Behave is a Enum.
    Responsibility:
    """
    PRESS = 1
    RELEASE = 2
    TAP = 3


class Expression(object):
    r"""Expression

    Expression is a object.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_behave(self, behave):
        r"""SUMMARY

        set_behave(behave)

        @Arguments:
        - `behave`:

        @Return:

        @Error:
        """

    @abstractmethod
    def interpret(self, ):
        r"""SUMMARY

        interpret()

        @Return:

        @Error:
        """


class XTestSendKeyExpression(Expression):
    r"""XTestSendKeyExpression

    XTestSendKeyExpression is a Expression.
    Responsibility:
    """
    def __init__(self, inputs, behave=Behave.TAP):
        r"""

        @Arguments:
        """
        self._inputs = inputs
        self._behave = behave

    def interpret(self, ):
        r"""SUMMARY

        interpret()

        @Return:

        @Error:
        """
        if self._behave in (Behave.PRESS, Behave.TAP):
            self._inputs.press()
        if self._behave in (Behave.RELEASE, Behave.TAP):
            self._inputs.release()

    def set_behave(self, behave):
        r"""SUMMARY

        set_behave(behave)

        @Arguments:
        - `behave`:

        @Return:

        @Error:
        """
        self._behave = behave


class NoneTerminalExpression(Expression):
    r"""NoneTerminalExpression

    NoneTerminalExpression is a Expression.
    Responsibility:
    """
    def __init__(self, expression):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self._expression = expression

    def set_behave(self, behave):
        r"""SUMMARY

        set_behave(behave)

        @Arguments:
        - `behave`:

        @Return:

        @Error:
        """
        self._expression.set_behave(behave)

    def interpret(self, ):
        r"""SUMMARY

        interpret()

        @Return:

        @Error:
        """
        pass


class BehaveExpression(NoneTerminalExpression):
    r"""BehaveExpression

    BehaveExpression is a NoneTerminalExpression.
    Responsibility:
    """
    def __init__(self, expression, behave):
        r"""

        @Arguments:
        - `expression`:
        - `behave`:
        """
        NoneTerminalExpression.__init__(self, expression)
        self._behave = behave

    def interpret(self, ):
        r"""SUMMARY

        interpret()

        @Return:

        @Error:
        """
        self._expression.set_behave(self._behave)


class RepeatExpression(NoneTerminalExpression):
    r"""RepeatExpression

    RepeatExpression is a NoneTerminalExpression.
    Responsibility:
    """
    def __init__(self, expression, times):
        r"""

        @Arguments:
        - `expression`:
        - `times`:
        """
        NoneTerminalExpression.__init__(self, expression)
        self._times = times

    def interpret(self, ):
        r"""SUMMARY

        interpret()

        @Return:

        @Error:
        """
        for _ in xrange(self._times):
            self._expression.interpret()


class ModifierExpression(NoneTerminalExpression):
    r"""ModifierExpression

    ModifierExpression is a NoneTerminalExpression.
    Responsibility:
    """
    def __init__(self, expression, modifier):
        r"""

        @Arguments:
        - `expression`:
        - `modifier`:
        """
        NoneTerminalExpression.__init__(self, expression)
        self._modifier = modifier

    def interpret(self, ):
        r"""SUMMARY

        interpret()

        @Return:

        @Error:
        """
        self._modifier.press()
        self._expression.interpret()
        self._modifier.release()


class PointExpression(NoneTerminalExpression):
    r"""PointExpression

    PointExpression is a NoneTerminalExpression.
    Responsibility:
    """
    def __init__(self, expression, point, display):
        r"""

        @Arguments:
        - `expression`:
        - `point`:
        """
        NoneTerminalExpression.__init__(self, expression)
        self._point = point
        self._cursor = X11Cursor(display)

    def interpret(self, ):
        r"""SUMMARY

        interpret()

        @Return:

        @Error:
        """
        self._cursor.set_point(self._point.get_x(), self._point.get_y())
        self._expression.interpret()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# expressions.py ends here
