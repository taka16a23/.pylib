#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: stoken.py 189 2014-05-17 09:44:59Z t1 $
# $Revision: 189 $
# $Date: 2014-05-17 18:44:59 +0900 (Sat, 17 May 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-05-17 18:44:59 +0900 (Sat, 17 May 2014) $

r"""stoken -- DESCRIPTION

"""
from enum import Enum
from xcb2.xproto import NamedModifierMask, NamedButtonIndex
from sendkeys.display import KeymapDisplay
from sendkeys.code import KeyChar, ButtonCode
from sendkeys.modifierstate import ModifierState


MODIFIERS = {'^': ModifierState(NamedModifierMask.Control),
             '+': ModifierState(NamedModifierMask.Shift),
             '!': ModifierState(NamedModifierMask.Alt),
             '#': ModifierState(NamedModifierMask.Super),
             }

BUTTONS = {'LButton': ButtonCode(NamedButtonIndex.Left),
           'LClick': ButtonCode(NamedButtonIndex.Left),
           'RButton': ButtonCode(NamedButtonIndex.Right),
           'RClick': ButtonCode(NamedButtonIndex.Right),
           'MButton': ButtonCode(NamedButtonIndex.Middle),
           'MClick': ButtonCode(NamedButtonIndex.Middle),
           'WheelDown': ButtonCode(NamedButtonIndex.WheelDown),
           'WheelUp': ButtonCode(NamedButtonIndex.WheelUp),
           }


class TokenType(Enum):
    r"""SUMMARY
    """
    KEY       = 1
    MODIFIER   = 2
    REPEAT     = 3
    KEYUP      = 4
    KEYDOWN    = 5
    BUTTON     = 6
    KEYCODE    = 7
    UNICODE    = 8
    CURLYSTART = 9
    CURLYEND   = 10
    GEOX       = 11
    GEOY       = 12


class TokenAbstract(KeymapDisplay):
    r"""SUMMARY
    """

    def __init__(self, token, display=None):
        r"""

        @Arguments:
        - `token`:
        """
        KeymapDisplay.__init__(self, display)
        self.token = token

    def __repr__(self, ):
        return '{0.__class__.__name__}(token="{0.token}")'.format(self)


class TokenKey(TokenAbstract):
    r"""SUMMARY
    """
    types = TokenType.KEY

    def get(self, ):
        r"""SUMMARY

        get_analyzed()

        @Return:
        """
        return KeyChar(self.token, self.display).to_keycode()


class TokenModifier(TokenAbstract):
    r"""SUMMARY
    """
    types = TokenType.MODIFIER

    def get(self, ):
        r"""SUMMARY

        get()

        @Return:
        """
        return MODIFIERS.get(self.token)

    def __int__(self, ):
        return int(self.get())


class TokenButton(TokenAbstract):
    r"""SUMMARY
    """
    types = TokenType.BUTTON

    def get(self, ):
        r"""SUMMARY

        get()

        @Return:
        """
        # KLUDGE: (Atami) [2014/04/29]
        button = BUTTONS.get(self.token)
        button.display = self.display
        return button


class TokenRepeat(TokenAbstract):
    r"""SUMMARY
    """
    types = TokenType.REPEAT

    def get(self, ):
        r"""SUMMARY

        get()

        @Return:
        """
        return int(self.token)


class TokenKeyup(TokenAbstract):
    r"""SUMMARY
    """
    types = TokenType.KEYUP


class TokenKeydown(TokenAbstract):
    r"""SUMMARY
    """
    types = TokenType.KEYDOWN


class TokenKeycode(TokenAbstract):
    r"""SUMMARY
    """
    types = TokenType.KEYCODE

    def get(self, ):
        r"""SUMMARY

        get()

        @Return:
        """
        return


class TokenUnicode(TokenAbstract):
    r"""SUMMARY
    """
    types = TokenType.UNICODE

    def get(self, ):
        r"""SUMMARY

        get()

        @Return:
        """
        return


class TokenCurlystart(TokenAbstract):
    r"""SUMMARY
    """
    types = TokenType.CURLYSTART


class TokenCurlyend(TokenAbstract):
    r"""SUMMARY
    """
    types = TokenType.CURLYEND


class TokenGeoX(TokenAbstract):
    r"""SUMMARY
    """
    types = TokenType.GEOX

    def get(self, ):
        r"""SUMMARY

        get()

        @Return:
        """
        return {'event_x': int(self.token),}


class TokenGeoY(TokenAbstract):
    r"""SUMMARY
    """
    types = TokenType.GEOY

    def get(self, ):
        r"""SUMMARY

        get()

        @Return:
        """
        return {'event_y': int(self.token),}




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# stoken.py ends here
