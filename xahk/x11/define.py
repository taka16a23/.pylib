#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""define -- DESCRIPTION

"""
from enum import IntEnum as _IntEnum


class NamedModifierMask(_IntEnum):
    r"""SUMMARY
    """
    Null      = 0
    Shift     = 1
    Lock      = 1 << 1
    Control   = 1 << 2
    Alt       = 1 << 3
    Numlock   = 1 << 4
    Hiper     = 1 << 5
    Super     = 1 << 6
    Mod5      = 1 << 7
    Left      = 1 << 8
    Middle    = 1 << 9
    Right     = 1 << 10
    WheelUp   = 1 << 11
    WheelDown = 1 << 12
    Any       = 1 << 15 # 32768



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# define.py ends here
