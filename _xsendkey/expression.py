#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""expression -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod
import xsend


class Expression(object):
    """Abstract class Expression
    """
    __metaclass__ = ABCMeta

    # Operations
    @abstractmethod
    def interpret(self, context):
        raise NotImplementedError()


class LeafExpression(Expression):
    """Class LeafExpression
    """
    # Attributes:
    def __init__(self, value):
        r"""

        @Arguments:
        - `value`:
        """
        self._value = value

    def interpret(self, context):
        """function interpret

        context:

        returns
        """
        return self._value


class ButtonExpression(LeafExpression):
    """Class ButtonExpression
    """


class KeyExpression(LeafExpression):
    """Class KeyExpression
    """


class NumExpression(LeafExpression):
    """Class NumExpression
    """


## NonTerminal
#
class NonTerminalExpression(Expression):
    """Class NonTerminalExpression
    """
    # Attributes:

    # Operations

class ModifierExpression(NonTerminalExpression):
    """Class ModifierExpression
    """
    # Attributes:
    def __init__(self, keybutton):
        r"""

        @Arguments:
        - `keybutton`:
        """
        self._keybutton = keybutton


class ShiftModifierExpression(ModifierExpression):
    """Class ShiftModifierExpression
    """

    # Operations
    def interpret(self, context):
        """function interpret

        context:

        returns
        """
        self._keybutton.setmodifier(1)
        return self._keybutton


class ControlModifierExpression(ModifierExpression):
    r"""ControlModifierExpression

    ControlModifierExpression is a ModifierExpression.
    Responsibility:
    """
    def interpret(self, context):
        r"""SUMMARY

        interpret(context)

        @Arguments:
        - `context`:

        @Return:

        @Error:
        """
        self._keybutton.setmodifier(1 << 2)
        return self._keybutton


class AltModifierExpression(ModifierExpression):
    """Class AltModifierExpression
    """
    # Attributes:

    # Operations
    def interpret(self, context):
        """function interpret

        context:

        returns
        """
        self._keybutton.setmodifier(1 << 3)
        return self._keybutton


class HiperModifierExpression(ModifierExpression):
    """Class HiperModifierExpression
    """
    # Attributes:

    # Operations
    def interpret(self, context):
        """function interpret

        context:

        returns
        """
        self._keybutton.setmodifier(1 << 5)
        return self._keybutton


## Behave
#
class BehaveExpression(NonTerminalExpression):
    """Class BehaveExpression
    """
    # Attributes:
    def __init__(self, keybutton):
        r"""

        @Arguments:
        - `keybutton`:
        """
        self._keybutton = keybutton


class PressBehaviorExpression(BehaveExpression):
    """Class PressBehaviorExpression
    """
    # Operations
    def interpret(self, context):
        """function interpret

        context:

        returns
        """
        self._keybutton.setbehave(1)
        return self._keybutton


class ReleaseBehaviorExpression(BehaveExpression):
    """Class ReleaseBehaviorExpression
    """
    # Attributes:

    # Operations
    def interpret(self, context):
        """function interpret

        context:

        returns
        """
        self._keybutton.setbehave(2)
        return self._keybutton


## Multiply
#
class MultiplyExpression(NonTerminalExpression):
    """Class MultiplyExpression
    """
    # Attributes:
    def __init__(self, keybutton, times):
        r"""

        @Arguments:
        - `keybutton`:
        - `times`:
        """
        self._keybutton = keybutton
        self._times = times

    # Operations
    def interpret(self, context):
        """function interpret

        context:

        returns
        """
        return xsend.SendRepeater(self._keybutton, self._times)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# expression.py ends here
