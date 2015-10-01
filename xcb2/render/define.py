#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: define.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""define -- DESCRIPTION

"""
from enum import IntEnum as _IntEnum


class PictType(_IntEnum):
    r"""SUMMARY
    """
    Indexed = 0
    Direct = 1


class Picture(_IntEnum):
    _None = 0


class PictOp(_IntEnum):
    Clear = 0
    Src = 1
    Dst = 2
    Over = 3
    OverReverse = 4
    In = 5
    InReverse = 6
    Out = 7
    OutReverse = 8
    Atop = 9
    AtopReverse = 10
    Xor = 11
    Add = 12
    Saturate = 13
    DisjointClear = 16
    DisjointSrc = 17
    DisjointDst = 18
    DisjointOver = 19
    DisjointOverReverse = 20
    DisjointIn = 21
    DisjointInReverse = 22
    DisjointOut = 23
    DisjointOutReverse = 24
    DisjointAtop = 25
    DisjointAtopReverse = 26
    DisjointXor = 27
    ConjointClear = 32
    ConjointSrc = 33
    ConjointDst = 34
    ConjointOver = 35
    ConjointOverReverse = 36
    ConjointIn = 37
    ConjointInReverse = 38
    ConjointOut = 39
    ConjointOutReverse = 40
    ConjointAtop = 41
    ConjointAtopReverse = 42
    ConjointXor = 43
    Multiply = 48
    Screen = 49
    Overlay = 50
    Darken = 51
    Lighten = 52
    ColorDodge = 53
    ColorBurn = 54
    HardLight = 55
    SoftLight = 56
    Difference = 57
    Exclusion = 58
    HSLHue = 59
    HSLSaturation = 60
    HSLColor = 61
    HSLLuminosity = 62


class PolyEdge(_IntEnum):
    Sharp = 0
    Smooth = 1


class PolyMode(_IntEnum):
    Precise = 0
    Imprecise = 1


class CP(_IntEnum):
    Repeat = 1
    AlphaMap = 2
    AlphaXOrigin = 4
    AlphaYOrigin = 8
    ClipXOrigin = 16
    ClipYOrigin = 32
    ClipMask = 64
    GraphicsExposure = 128
    SubwindowMode = 256
    PolyEdge = 512
    PolyMode = 1024
    Dither = 2048
    ComponentAlpha = 4096


class SubPixel(_IntEnum):
    Unknown = 0
    HorizontalRGB = 1
    HorizontalBGR = 2
    VerticalRGB = 3
    VerticalBGR = 4
    _None = 5


class Repeat(_IntEnum):
    _None = 0
    Normal = 1
    Pad = 2
    Reflect = 3



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# define.py ends here
