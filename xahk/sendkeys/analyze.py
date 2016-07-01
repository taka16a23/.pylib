#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""analyze -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod
from collections import deque

from xahk.input.keysymdef import STRKEYSYMS
from xahk.input.mouse import Mouse
from xahk.x11.modifier import Modifier
from .scanner import TokenType
from .input_event import KeyEvent, ButtonEvent


class KeyboardMapping(object):
    r"""K

    K is a object.
    Responsibility:
    """
    def __init__(self, display):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self.display = display
        setup = self.display.get_setup()
        mincode, maxcode = int(setup.min_keycode), int(setup.max_keycode)
        count = maxcode - mincode + 1
        rep = self.display.core.GetKeyboardMapping(mincode, count).reply()
        keymapping = zip(*[iter(rep.keysyms)] * rep.keysyms_per_keycode)
        self._mapping = {}
        for keycode, symcodes in enumerate(keymapping, start=mincode):
            self._mapping[STRKEYSYMS.get(symcodes[0])] = (keycode, Modifier.Mask.Null)
            self._mapping[STRKEYSYMS.get(symcodes[1])] = (keycode, Modifier.Mask.Shift)

    def get_code(self, symname):
        r"""SUMMARY

        get_code(symname)

        @Arguments:
        - `symname`:

        @Return:

        @Error:
        """
        ret = self._mapping.get(symname, None)
        if ret is None:
            return (None, Modifier.Mask.Null)
        return ret


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

    StackExpressions is a Expression.
    Responsibility:
    """
    def __init__(self, ):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self._modifiers = 0
        self._exps = deque()

    def add_expression(self, exp):
        r"""SUMMARY

        add_expression(exp)

        @Arguments:
        - `exp`:

        @Return:

        @Error:
        """
        modifiers = exp.get_modifiers()
        exp.set_modifiers(modifiers|self._modifiers)
        self._modifiers = 0
        self._exps.append(exp)

    def pop_expression(self, ):
        r"""SUMMARY

        pop_expression()

        @Return:

        @Error:
        """
        return self._exps.pop()

    def add_modifier(self, mod):
        r"""SUMMARY

        add_modifier(mod)

        @Arguments:
        - `mod`:

        @Return:

        @Error:
        """
        self._modifiers |= mod

    def interpret(self, ):
        r"""SUMMARY

        interpret()

        @Return:

        @Error:
        """
        cookies = []
        extend = cookies.extend
        for exp in self._exps:
            extend(exp.interpret())
        return cookies


class InputExpression(Expression):
    r"""InputExpression

    InputExpression is a Expression.
    Responsibility:
    """
    def __init__(self, value):
        r"""

        @Arguments:
        - `value`:
        """
        self._value = value

    def get_modifiers(self, ):
        r"""SUMMARY

        get_modifiers()

        @Return:

        @Error:
        """
        return self._value.get_modifiers()

    def set_modifiers(self, mod):
        r"""SUMMARY

        set_modifiers(mod)

        @Arguments:
        - `mod`:

        @Return:

        @Error:
        """
        self._value.set_modifiers(mod)

    def interpret(self, ):
        r"""SUMMARY

        interpret()

        @Return:

        @Error:
        """
        return (self._value.press(), self._value.release())

    def set_x(self, newx):
        r"""SUMMARY

        set_x(newx)

        @Arguments:
        - `newx`:

        @Return:

        @Error:
        """
        self._value.set_x(newx)

    def set_y(self, newy):
        r"""SUMMARY

        set_y(newy)

        @Arguments:
        - `newy`:

        @Return:

        @Error:
        """
        self._value.set_y(newy)


class RepeatExpression(Expression):
    r"""RepeatExpression

    RepeatExpression is a Expression.
    Responsibility:
    """
    def __init__(self, exp, times):
        r"""

        @Arguments:
        - `exp`:
        """
        self._exp = exp
        self._times = times

    def get_modifiers(self, ):
        r"""SUMMARY

        get_modifiers()

        @Return:

        @Error:
        """
        return self._exp.get_modifiers()

    def set_modifiers(self, mod):
        r"""SUMMARY

        set_modifiers(mod)

        @Arguments:
        - `mod`:

        @Return:

        @Error:
        """
        self._exp.set_modifiers(mod)

    def interpret(self, ):
        r"""SUMMARY

        interpret()

        @Return:

        @Error:
        """
        cookies = []
        extend = cookies.extend
        for _ in xrange(self._times):
            extend(self._exp.interpret())
        return cookies


class Analyzer(object):
    r"""Analyzer

    Analyzer is a object.
    Responsibility:
    """
    _modifiers = {'+': Modifier.Mask.Shift,
                  '^': Modifier.Mask.Control,
                  '!': Modifier.Mask.Alt,
                  '#': Modifier.Mask.Super,
    }
    _buttons = {'lbutton': Mouse.Button.Index.Left,
                'lclick': Mouse.Button.Index.Left,
                'mbutton': Mouse.Button.Index.Middle,
                'mclick': Mouse.Button.Index.Middle,
                'rbutton': Mouse.Button.Index.Right,
                'rclick': Mouse.Button.Index.Right,
                'wheelup': Mouse.Button.Index.WheelUp,
                'wheeldown': Mouse.Button.Index.WheelDown,
    }

    def analyze(self, context, tokens):
        r"""SUMMARY

        analyze(tokens)

        @Arguments:
        - `tokens`:

        @Return:

        @Error:
        """
        display = context.get('display')
        point = context.get('point')
        keymapping = KeyboardMapping(display)
        stack = StackExpressions()
        geox = None
        for token in tokens:
            if token.gettype() == TokenType.key:
                code, shifted = keymapping.get_code(token.getvalue())
                stack.add_expression(
                    InputExpression(KeyEvent(context, code, shifted, point)))
            elif token.gettype() == TokenType.button:
                stack.add_expression(
                    InputExpression(
                        ButtonEvent(context, self._buttons.get(token.getvalue()),
                                    0, point)))
            elif token.gettype() == TokenType.modifier:
                stack.add_modifier(self._modifiers.get(token.getvalue(), 0))
            elif token.gettype() == TokenType.geometry:
                if geox is None:
                    geox = token.getvalue()
                else:
                    exp = stack.pop_expression()
                    exp.set_x(geox)
                    geox = None
                    exp.set_y(token.getvalue())
                    stack.add_expression(exp)
        return stack



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# analyze.py ends here
