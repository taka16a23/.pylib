#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: analyze.py 305 2015-02-07 03:47:58Z t1 $
# $Revision: 305 $
# $Date: 2015-02-07 12:47:58 +0900 (Sat, 07 Feb 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-02-07 12:47:58 +0900 (Sat, 07 Feb 2015) $

r"""analyze -- DESCRIPTION

"""
from wxcb.protocol.xproto.define import NamedModifierMask, NamedButtonIndex

from xsendkey.parser.token import TokenType
from xsendkey.parser.err import XSKError
from xsendkey.xinput import XInputKey, XInputButton, Behave
from xsendkey.parser.expression import (
    StackExpressions, BehaveExpression, RepeatExpression,
    ModifierExpression, PointExpression, Expression, XInputExpression)
from xsendkey.converter import (
    CharConverter, NameConverter, CodeConverter, SymConverter)


MODIFIERS = {'^': NamedModifierMask.Control,
             '+': NamedModifierMask.Shift,
             '!': NamedModifierMask.Alt,
             '#': NamedModifierMask.Super,
             }


BUTTONS = {'LButton': NamedButtonIndex.Left,
           'LClick': NamedButtonIndex.Left,
           'RButton': NamedButtonIndex.Right,
           'RClick': NamedButtonIndex.Right,
           'MButton': NamedButtonIndex.Middle,
           'MClick': NamedButtonIndex.Middle,
           'WheelDown': NamedButtonIndex.WheelDown,
           'WheelUp': NamedButtonIndex.WheelUp,
           }


BEHAVE = {'up': Behave.up,
          'down': Behave.down,
          }


class EndMarker(Exception):
    r"""EndMarker

    EndMarker is a Exception.
    Responsibility:
    """


class Analyze(object):
    r"""Analyze

    Analyze is a object.
    Responsibility:
    """
    def __init__(self, ):
        r"""
        """
        self._exps = StackExpressions()

    def get_expressions(self, ):
        r"""SUMMARY

        get_expressions()

        @Return:

        @Error:
        """
        return self._exps

    def analyze_tokens(self, tokens, display=None):
        r"""SUMMARY

        analyze(tokens, display=None)

        @Arguments:
        - `tokens`:
        - `display`:

        @Return:

        @Error:
        """
        state = {}
        state['modifier'] = 0
        state['display'] = display
        try:
            for token in tokens:
                self.analyze_token(token, state)
        except EndMarker:
            pass

    def analyze_token(self, token, state=None):
        r"""SUMMARY

        analyze_token(token, state, display=None)

        @Arguments:
        - `token`:
        - `state`:
        - `display`:

        @Return:

        @Error:
        """
        state = state or {}
        if TokenType.endmarker == token:
            raise EndMarker()
        # terminal expression
        elif TokenType.code == token:
            exp = XInputExpression(XInputKey(0, int(token.getvalue()),
                                             display=state.get('display', None)))
        elif TokenType.sym == token:
            code, mod = SymConverter(token.getvalue()).to_code(
                state.get('display', None))
            exp = XInputExpression(
                XInputKey(0, code, mod, display=state.get('display', None)))
        elif TokenType.unicode == token:
            # TODO: (Atami) [2015/01/26]
            # '{}0020'.format('\u').encode().decode('unicode-escape')
            raise NotImplementedError()
        elif TokenType.name == token:
            code, mod = NameConverter(token.getvalue()).to_code(
                state.get('display', None))
            exp = XInputExpression(
                XInputKey(0, code, mod, display=state.get('display', None)))
        elif TokenType.char == token:
            code, mod = CharConverter(token.getvalue()).to_code(
                state.get('display', None))
            exp = XInputExpression(
                XInputKey(0, code, mod, display=state.get('display', None)))
        elif TokenType.button == token:
            exp = XInputExpression(
                XInputButton(0, BUTTONS.get(token.getvalue()),
                             display=state.get('display', None)))
        # TODO: (Atami) [2015/01/29]
        elif TokenType.repeat == token:
            exp = RepeatExpression(self._exps.pop(), int(token.getvalue()))
        # nonterminal expression
        elif TokenType.modifier == token:
            state['modifier'] |= MODIFIERS.get(token.getvalue())
            return
        elif TokenType.behave == token:
            exp = BehaveExpression(
                self._exps.pop(), BEHAVE.get(token.getvalue()))
        elif TokenType.point == token:
            exp = PointExpression(
                    self._exps.pop(), [int(x) for x in token.getvalue()])
        else:
            # TODO: (Atami) [2015/01/28]
            raise XSKError()
        # stack
        self.append_exp(exp, state)

    def append_exp(self, exp, state=None):
        r"""SUMMARY

        append_exp(exp, state={})

        @Arguments:
        - `exp`:
        - `state`:

        @Return:

        @Error:
        """
        expression = exp
        state = state or {}
        if state.get('modifier', 0) != 0:
            expression = ModifierExpression(exp, state.get('modifier', 0))
            state['modifier'] = 0
        self.append(expression)

    def append(self, exp):
        r"""SUMMARY

        append(exp)

        @Arguments:
        - `exp`:

        @Return:

        @Error:
        """
        if not isinstance(exp, (Expression, )):
            # TODO: (Atami) [2015/01/28]
            raise TypeError()
        self._exps.append(exp)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# analyze.py ends here
