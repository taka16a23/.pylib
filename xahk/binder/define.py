#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: define.py 339 2015-07-23 18:01:26Z t1 $
# $Revision: 339 $
# $Date: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $

r"""define -- DESCRIPTION

"""
from enum import IntEnum as _IntEnum
from xcb import xproto


class ButtonIndex(_IntEnum):
    r"""ButtonIndex

    ButtonIndex is a _IntEnum.
    Responsibility:
    """
    Left = xproto.ButtonIndex._1
    Middle = xproto.ButtonIndex._2
    Right = xproto.ButtonIndex._3
    WheelUp = xproto.ButtonIndex._4
    WheelDown = xproto.ButtonIndex._5


class ModifierMask(_IntEnum):
    r"""SUMMARY
    """
    Null      = 0
    Shift     = xproto.KeyButMask.Shift
    Lock      = xproto.KeyButMask.Lock
    Control   = xproto.KeyButMask.Control
    Alt       = xproto.KeyButMask.Mod1
    Numlock   = xproto.KeyButMask.Mod2
    Hiper     = xproto.KeyButMask.Mod3
    Super     = xproto.KeyButMask.Mod4
    Mod5      = xproto.KeyButMask.Mod5
    Left      = xproto.KeyButMask.Button1
    Middle    = xproto.KeyButMask.Button2
    Right     = xproto.KeyButMask.Button3
    WheelUp   = xproto.KeyButMask.Button4
    WheelDown = xproto.KeyButMask.Button5
    Any       = 1 << 15 # 32768




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# define.py ends here
