#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""expression -- DESCRIPTION

"""
from collections import deque
from abc import ABCMeta, abstractmethod

from xsendkey.xinput import RepeatXInput


class Expression(object):
    """Abstract class Expression
    """
    # Attributes:
    __metaclass__ = ABCMeta

    # Operations
    @abstractmethod
    def interpret(self, ):
        """function interpret

        context:

        returns
        """
        raise NotImplementedError()


class StackExpressions(Expression):
    r"""StackExpressions

    StackExpressions is a Expression.
    Responsibility:
    """
    def __init__(self, ):
        r"""
        """
        self._exps = deque()

    def append(self, exp):
        r"""SUMMARY

        append(exp)

        @Arguments:
        - `exp`:

        @Return:

        @Error:
        """
        self._exps.append(exp)

    def pop(self, ):
        r"""SUMMARY

        pop()

        @Return:

        @Error:
        """
        return self._exps.pop()

    def clear(self, ):
        r"""SUMMARY

        clear()

        @Return:

        @Error:
        """
        self._exps.clear()

    def interpret(self, ):
        r"""SUMMARY

        interpret()

        @Return:

        @Error:
        """
        return [exp.interpret() for exp in self._exps]


class LeafExpression(Expression):
    """Class LeafExpression
    """
    # Attributes:
    def __init__(self, value):
        r"""

        @Arguments:
        - `value`:
        """
        self.value = value


class XInputExpression(LeafExpression):
    r"""XInputExpression

    XInputExpression is a LeafExpression.
    Responsibility:
    """
    def interpret(self, ):
        r"""SUMMARY

        interpret()

        @Return:

        @Error:
        """
        return self.value


class NonTerminalExpression(Expression):
    """Class NonTerminalExpression
    """
    # Attributes:

    # Operations


class BehaveExpression(NonTerminalExpression):
    """Class BehaveExpression
    """
    # Attributes:

    def __init__(self, exp, behave):
        r"""

        @Arguments:
        - `exp`:
        - `behave`:
        """
        NonTerminalExpression.__init__(self)
        self._exp = exp
        self._behave = behave

    # Operations
    def interpret(self):
        """function interpret

        returns
        """
        interpreted = self._exp.interpret()
        interpreted.set_behave(self._behave)
        return interpreted


class RepeatExpression(NonTerminalExpression):
    """Class RepeatExpression
    """
    # Attributes:
    def __init__(self, exp, num):
        r"""

        @Arguments:
        - `exp`:
        - `num`:
        """
        self._exp = exp
        self._num = num

    # Operations
    def interpret(self):
        """function interpret

        returns
        """
        return RepeatXInput(self._exp.interpret(), self._num)


class ModifierExpression(NonTerminalExpression):
    """Class ModifierExpression
    """
    # Attributes:
    def __init__(self, exp, modifier):
        r"""

        @Arguments:
        - `exp`:
        - `modifier`:
        """
        self._exp = exp
        self._modifier = modifier

    # Operations
    def interpret(self):
        """function interpret

        returns
        """
        interpreted = self._exp.interpret()
        interpreted.add_modifier(self._modifier)
        return interpreted


class PointExpression(NonTerminalExpression):
    r"""PointExpression

    PointExpression is a NonTerminalExpression.
    Responsibility:
    """
    def __init__(self, exp, point):
        r"""

        @Arguments:
        - `exp`:
        - `point`:
        """
        self._exp = exp
        self._point = point

    def interpret(self, ):
        r"""SUMMARY

        interpret()

        @Return:

        @Error:
        """
        interpreted = self._exp.interpret()
        interpreted.set_event_point(self._point)
        return interpreted



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# expression.py ends here
