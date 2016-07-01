#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""expressions -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod
from enum import Enum
from collections import deque

from xahk.input.cursor import Cursor


Behave = Enum('Behave', 'both press release')


class Expression(object):
    r"""Expression

    Expression is a object.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def interpret(self, ):
        r"""SUMMARY

        interpret()

        @Return:

        @Error:
        """


class StackExpressions(Expression):
    r"""StackExpressions

    StackExpressions is a object.
    Responsibility:
    """
    def __init__(self, ):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self.exps = deque()

    def add(self, exp):
        r"""SUMMARY

        add(exp)

        @Arguments:
        - `exp`:

        @Return:

        @Error:
        """
        self.exps.append(exp)

    def pop(self, ):
        r"""SUMMARY

        pop()

        @Return:

        @Error:
        """
        return self.exps.pop()

    def interpret(self, ):
        r"""SUMMARY

        interpret()

        @Return:

        @Error:
        """
        cookies = []
        extend = cookies.extend
        for exp in self.exps:
            extend(exp.interpret())
        for cookie in cookies:
            cookie.check()


class SendExpression(Expression):
    r"""SendExpression

    SendExpression is a Expression.
    Responsibility:
    """
    def __init__(self, value, geox=None, geoy=None):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self.value = value
        self.behave = Behave.both
        self.geox = geox
        self.geoy = geoy

    def set_behave(self, behave):
        r"""SUMMARY

        set_behave(behave)

        @Arguments:
        - `behave`:

        @Return:

        @Error:
        """
        self.behave = behave

    def set_geox(self, newx):
        r"""SUMMARY

        set_geox(newx)

        @Arguments:
        - `newx`:

        @Return:

        @Error:
        """
        self.geox = newx

    def set_geoy(self, newy):
        r"""SUMMARY

        set_geoy(newy)

        @Arguments:
        - `newy`:

        @Return:

        @Error:
        """
        self.geoy = newy

    def interpret(self, ):
        r"""SUMMARY

        interpret()

        @Return:

        @Error:
        """
        # for button press and release if has not geometry
        if None in (self.geox, self.geoy):
            cursor = Cursor(self.value.get_display())
            point = cursor.get_point()
            self.geox = self.geox or point.x
            self.geoy = self.geoy or point.y
        cookies = []
        if self.behave in (Behave.both, Behave.press):
            cookies.append(self.value.press(x=self.geox, y=self.geoy))
        if self.behave in (Behave.both, Behave.release):
            cookies.append(self.value.release(x=self.geox, y=self.geoy))
        return cookies


#### None Terminal Expression
##
class NoneTerminalExpression(object):
    r"""NoneTerminalExpression

    NoneTerminalExpression is a Expression.
    Responsibility:
    """

    def __init__(self, exp):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self.exp = exp

    def set_behave(self, behave):
        r"""SUMMARY

        set_behave(behave)

        @Arguments:
        - `behave`:

        @Return:

        @Error:
        """
        self.exp.set_behave(behave)

    def set_geox(self, geox):
        r"""SUMMARY

        set_geox(geox)

        @Arguments:
        - `geox`:

        @Return:

        @Error:
        """
        self.exp.set_geox(geox)

    def set_geoy(self, geoy):
        r"""SUMMARY

        set_geoy(geoy)

        @Arguments:
        - `geoy`:

        @Return:

        @Error:
        """
        self.exp.set_geoy(geoy)




class RepeatExpression(NoneTerminalExpression):
    r"""RepeatExpression

    RepeatExpression is a object.
    Responsibility:
    """
    def __init__(self, exp, times):
        r"""

        @Arguments:
        - `exp`:
        - `times`:
        """
        NoneTerminalExpression.__init__(self, exp)
        self.times = times

    def interpret(self, ):
        r"""SUMMARY

        interpret()

        @Return:

        @Error:
        """
        cookies = []
        extend = cookies.extend
        for _ in xrange(self.times):
            extend(self.exp.interpret())
        return cookies


class ModifierExpression(NoneTerminalExpression):
    r"""ModifierExpression

    ModifierExpression is a NoneTerminalExpression.
    Responsibility:
    """
    def __init__(self, exp, modkey):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        NoneTerminalExpression.__init__(self, exp)
        self.modkey = modkey

    def interpret(self, ):
        r"""SUMMARY

        interpret()

        @Return:

        @Error:
        """
        cookies = []
        cookies.append(self.modkey.press())
        cookies.extend(self.exp.interpret())
        cookies.append(self.modkey.release())
        return cookies



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# expressions.py ends here
