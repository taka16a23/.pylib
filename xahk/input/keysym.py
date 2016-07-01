#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""keysym -- DESCRIPTION

"""
from xcb import NoSymbol

from userint import UserInt
from keysymdef import LEGACY


class Keysym(UserInt):
    r"""Keysym

    Keysym is a UserInt.
    Responsibility:
    """

    def isspecial(self, ):
        r"""SUMMARY

        isspecial()

        @Return:

        @Error:
        """
        return self._value in (0, 0x00ffffff)

    def islatin1(self, ):
        r"""SUMMARY

        islatin1()

        @Return:

        @Error:
        """
        return (0x0020 <= self._value <= 0x007e or
                0x00a0 <= self._value <= 0x00ff)

    def isnosymbol(self, ):
        r"""SUMMARY

        isnosymbol()

        @Return:

        @Error:
        """
        return self._value == NoSymbol

    def isunicode(self, ):
        r"""SUMMARY

        isunicode()

        @Return:

        @Error:
        """
        return 0x01000100 <= self._value <= 0x0110ffff

    def islegacy(self, ):
        r"""SUMMARY

        islegacy()

        @Return:

        @Error:
        """
        return self._value in LEGACY

    def to_char(self, ):
        r"""SUMMARY

        to_char()

        @Return:

        @Error:
        """
        if self.isspecial():
            # TODO: (Atami) [2015/01/09]
            return ''
        if self.islatin1():
            return unichr(self._value)
        if self.isunicode():
            return unichr(self - 0x01000000)
        if self.islegacy():
            return unichr(LEGACY[self._value])
        # nothing
        # TODO: (Atami) [2015/01/09]
        return ''



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# keysym.py ends here
