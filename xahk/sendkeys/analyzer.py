#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""analyzer -- DESCRIPTION

"""
from collections import deque

from .scanner import TokenType
from . import expressions as exps
from xahk.input.keyboard import Keyboard
from xahk.input.mouse import Mouse


def get_key(keyboard, label):
    r"""SUMMARY

    get_key(keyboard)

    @Arguments:
    - `keyboard`:

    @Return:

    @Error:
    """
    keys = keyboard.list_keys()
    for key in keys:
        if key.is_labeled(label):
            return key
    return None


class Analyzer(object):
    r"""Analyzer

    Analyzer is a object.
    Responsibility:
    """
    def analyze(self, display, tokens):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        keyboard = Keyboard(display)
        shift = keyboard.get_shift_key()
        modifiers = {'+': shift,}
        _modifiers = keyboard.list_modifiers()
        for _mod in _modifiers:
            if _mod.get_label() == 'Control_L':
                modifiers['^'] = _mod
            elif _mod.get_label() == 'Alt_L':
                modifiers['!'] = _mod
            elif _mod.get_label() == 'Super_L':
                modifiers['#'] = _mod
        mouse = Mouse(display)
        buttons = {'lbutton': mouse.get_left_button(),
                   'lclick': mouse.get_left_button(),
                   'mbutton': mouse.get_middle_button(),
                   'mclick': mouse.get_middle_button(),
                   'rbutton': mouse.get_right_button(),
                   'rclick': mouse.get_right_button(),
                   'wheelup': mouse.get_wheelup_button(),
                   'wheeldown': mouse.get_wheeldown_button(),
        }
        stack = exps.StackExpressions()
        mods = deque()
        geox = None
        for token in tokens:
            if token.gettype() == TokenType.key:
                key = get_key(keyboard, token.getvalue())
                keyexp = exps.SendExpression(key, geox=0, geoy=0)
                if token.getvalue() == key.get_shift_label():
                    keyexp = exps.ModifierExpression(keyexp, shift)
                # add modifier
                if mods:
                    while mods:
                        keyexp = exps.ModifierExpression(keyexp, mods.popleft())
                stack.add(keyexp)
            elif token.gettype() == TokenType.button:
                button = exps.SendExpression(buttons.get(token.getvalue()))
                if mods:
                    while mods:
                        button = exps.ModifierExpression(button, mods.popleft())
                stack.add(button)
            elif token.gettype() == TokenType.modifier:
                mods.append(modifiers.get(token.getvalue()))
            elif token.gettype() == TokenType.repeat:
                stack.add(exps.RepeatExpression(stack.pop(), token.getvalue()))
            elif token.gettype() == TokenType.behave:
                exp = stack.pop()
                if token.getvalue() == 'press':
                    exp.set_behave(exps.Behave.press)
                elif token.getvalue() == 'release':
                    exp.set_behave(exps.Behave.release)
                stack.add(exp)
            elif token.gettype == TokenType.geometry:
                if geox is None:
                    geox = token.getvalue
                else:
                    exp = stack.pop()
                    exp.set_geox(geox)
                    geox = None
                    exp.set_geoy(token.getvalue())
                    stack.add(exp)
        return stack



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# analyzer.py ends here
