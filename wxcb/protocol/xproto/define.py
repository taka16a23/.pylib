#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: define.py 280 2015-01-29 00:05:31Z t1 $
# $Revision: 280 $
# $Date: 2015-01-29 09:05:31 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:05:31 +0900 (Thu, 29 Jan 2015) $

r"""define -- DESCRIPTION

"""
import sys as _sys
import os as _os

from enum import IntEnum as _IntEnum


__all__ = ['Propagate', 'OwnerEvents', 'VisualClass', 'EventMask',
           'BackingStore', 'ImageOrder', 'Window', 'Motion', 'NotifyDetail',
           'NotifyMode', 'Visibility', 'Place', 'Property', 'Time', 'Atom',
           'ColormapState', 'Colormap', 'Mapping', 'WindowClass', 'BackPixmap',
           'Gravity', 'MapState', 'SetMode', 'ConfigWindow', 'StackMode',
           'Circulate', 'PropMode', 'GetPropertyType', 'SendEventDest',
           'GrabMode', 'GrabStatus', 'Cursor', 'ButtonIndex',
           'NamedButtonIndex', 'ModMask', 'KeyButMask', 'NamedKeyButMask',
           'NamedModifierMask', 'ButtonMask', 'NamedButtonMask', 'Grab',
           'Allow', 'InputFocus', 'FontDraw', 'LineStyle', 'CapStyle',
           'JoinStyle', 'FillStyle', 'FillRule', 'SubwindowMode', 'ArcMode',
           'ClipOrdering', 'CoordMode', 'PolyShape', 'ImageFormat',
           'ColormapAlloc', 'ColorFlag', 'Pixmap', 'Font', 'QueryShapeOf',
           'LedMode', 'AutoRepeatMode', 'Blanking', 'Exposures', 'HostMode',
           'Family', 'AccessControl', 'CloseDown', 'Kill', 'ScreenSaver',
           'MappingStatus', 'MapIndex', 'CW']

__revision__ = '$Revision: 280 $'


class Propagate(_IntEnum):
    r"""SUMMARY
    """
    TRUE = 1
    FALSE = 0


class OwnerEvents(_IntEnum):
    r"""SUMMARY
    """
    TRUE = 1
    FALSE = 0


class VisualClass(_IntEnum):
    StaticGray  = 0
    GrayScale   = 1
    StaticColor = 2
    PseudoColor = 3
    TrueColor   = 4
    DirectColor = 5


class EventMask(_IntEnum):
    NoEvent              = 0
    KeyPress             = 1
    KeyRelease           = 2
    ButtonPress          = 4
    ButtonRelease        = 8
    EnterWindow          = 16
    LeaveWindow          = 32
    PointerMotion        = 64
    PointerMotionHint    = 128
    Button1Motion        = 256
    Button2Motion        = 512
    Button3Motion        = 1024
    Button4Motion        = 2048
    Button5Motion        = 4096
    ButtonMotion         = 8192
    KeymapState          = 16384
    Exposure             = 32768
    VisibilityChange     = 65536
    StructureNotify      = 131072
    ResizeRedirect       = 262144
    SubstructureNotify   = 524288
    SubstructureRedirect = 1048576
    FocusChange          = 2097152
    PropertyChange       = 4194304
    ColorMapChange       = 8388608
    OwnerGrabButton      = 16777216


class BackingStore(_IntEnum):
    NotUseful  = 0
    WhenMapped = 1
    Always     = 2


class ImageOrder(_IntEnum):
    LSBFirst = 0
    MSBFirst = 1


class Window(_IntEnum):
    _None = 0


class Motion(_IntEnum):
    Normal = 0
    Hint   = 1


class NotifyDetail(_IntEnum):
    Ancestor         = 0
    Virtual          = 1
    Inferior         = 2
    Nonlinear        = 3
    NonlinearVirtual = 4
    Pointer          = 5
    PointerRoot      = 6
    _None            = 7


class NotifyMode(_IntEnum):
    Normal       = 0
    Grab         = 1
    Ungrab       = 2
    WhileGrabbed = 3


class Visibility(_IntEnum):
    Unobscured        = 0
    PartiallyObscured = 1
    FullyObscured     = 2


class Place(_IntEnum):
    OnTop    = 0
    OnBottom = 1


class Property(_IntEnum):
    NewValue = 0
    Delete   = 1


class Time(_IntEnum):
    CurrentTime = 0


class Atom(_IntEnum):
    _None               = 0
    Any                 = 0
    PRIMARY             = 1
    SECONDARY           = 2
    ARC                 = 3
    ATOM                = 4
    BITMAP              = 5
    CARDINAL            = 6
    COLORMAP            = 7
    CURSOR              = 8
    CUT_BUFFER0         = 9
    CUT_BUFFER1         = 10
    CUT_BUFFER2         = 11
    CUT_BUFFER3         = 12
    CUT_BUFFER4         = 13
    CUT_BUFFER5         = 14
    CUT_BUFFER6         = 15
    CUT_BUFFER7         = 16
    DRAWABLE            = 17
    FONT                = 18
    INTEGER             = 19
    PIXMAP              = 20
    POINT               = 21
    RECTANGLE           = 22
    RESOURCE_MANAGER    = 23
    RGB_COLOR_MAP       = 24
    RGB_BEST_MAP        = 25
    RGB_BLUE_MAP        = 26
    RGB_DEFAULT_MAP     = 27
    RGB_GRAY_MAP        = 28
    RGB_GREEN_MAP       = 29
    RGB_RED_MAP         = 30
    STRING              = 31
    VISUALID            = 32
    WINDOW              = 33
    WM_COMMAND          = 34
    WM_HINTS            = 35
    WM_CLIENT_MACHINE   = 36
    WM_ICON_NAME        = 37
    WM_ICON_SIZE        = 38
    WM_NAME             = 39
    WM_NORMAL_HINTS     = 40
    WM_SIZE_HINTS       = 41
    WM_ZOOM_HINTS       = 42
    MIN_SPACE           = 43
    NORM_SPACE          = 44
    MAX_SPACE           = 45
    END_SPACE           = 46
    SUPERSCRIPT_X       = 47
    SUPERSCRIPT_Y       = 48
    SUBSCRIPT_X         = 49
    SUBSCRIPT_Y         = 50
    UNDERLINE_POSITION  = 51
    UNDERLINE_THICKNESS = 52
    STRIKEOUT_ASCENT    = 53
    STRIKEOUT_DESCENT   = 54
    ITALIC_ANGLE        = 55
    X_HEIGHT            = 56
    QUAD_WIDTH          = 57
    WEIGHT              = 58
    POINT_SIZE          = 59
    RESOLUTION          = 60
    COPYRIGHT           = 61
    NOTICE              = 62
    FONT_NAME           = 63
    FAMILY_NAME         = 64
    FULL_NAME           = 65
    CAP_HEIGHT          = 66
    WM_CLASS            = 67
    WM_TRANSIENT_FOR    = 68


class ColormapState(_IntEnum):
    Uninstalled = 0
    Installed   = 1


class Colormap(_IntEnum):
    _None = 0


class Mapping(_IntEnum):
    Modifier = 0
    Keyboard = 1
    Pointer  = 2


class WindowClass(_IntEnum):
    CopyFromParent = 0
    InputOutput    = 1
    InputOnly      = 2


class CW(_IntEnum):
    BackPixmap       = 1
    BackPixel        = 2
    BorderPixmap     = 4
    BorderPixel      = 8
    BitGravity       = 16
    WinGravity       = 32
    BackingStore     = 64
    BackingPlanes    = 128
    BackingPixel     = 256
    OverrideRedirect = 512
    SaveUnder        = 1024
    EventMask        = 2048
    DontPropagate    = 4096
    Colormap         = 8192
    Cursor           = 16384


class BackPixmap(_IntEnum):
    _None          = 0
    ParentRelative = 1


class Gravity(_IntEnum):
    BitForget = 0
    WinUnmap  = 0
    NorthWest = 1
    North     = 2
    NorthEast = 3
    West      = 4
    Center    = 5
    East      = 6
    SouthWest = 7
    South     = 8
    SouthEast = 9
    Static    = 10


class MapState(_IntEnum):
    Unmapped   = 0
    Unviewable = 1
    Viewable   = 2


class SetMode(_IntEnum):
    Insert = 0
    Delete = 1


class ConfigWindow(_IntEnum):
    X           = 1
    Y           = 2
    Width       = 4
    Height      = 8
    BorderWidth = 16
    Sibling     = 32
    StackMode   = 64


class StackMode(_IntEnum):
    Above    = 0
    Below    = 1
    TopIf    = 2
    BottomIf = 3
    Opposite = 4


class Circulate(_IntEnum):
    RaiseLowest  = 0
    LowerHighest = 1


class PropMode(_IntEnum):
    Replace = 0
    Prepend = 1
    Append  = 2


class GetPropertyType(_IntEnum):
    Any = 0


class SendEventDest(_IntEnum):
    PointerWindow = 0
    ItemFocus     = 1


class GrabMode(_IntEnum):
    Sync  = 0
    Async = 1


class GrabStatus(_IntEnum):
    Success        = 0
    AlreadyGrabbed = 1
    InvalidTime    = 2
    NotViewable    = 3
    Frozen         = 4


class Cursor(_IntEnum):
    _None = 0


class ButtonIndex(_IntEnum):
    Any = 0
    _1  = 1
    _2  = 2
    _3  = 3
    _4  = 4
    _5  = 5


class NamedButtonIndex(_IntEnum):
    r"""SUMMARY
    """
    Any       = 0
    Left      = 1
    Middle    = 2
    Right     = 3
    WheelUp   = 4
    WheelDown = 5


class ModMask(_IntEnum):
    Shift   = 1
    Lock    = 2
    Control = 4
    _1      = 8
    _2      = 16
    _3      = 32
    _4      = 64
    _5      = 128
    Any     = 32768


class KeyButMask(_IntEnum):
    Shift   = 1
    Lock    = 2
    Control = 4
    Mod1    = 8
    Mod2    = 16
    Mod3    = 32
    Mod4    = 64
    Mod5    = 128
    Button1 = 256
    Button2 = 512
    Button3 = 1024
    Button4 = 2048
    Button5 = 4096


class NamedKeyButMask(_IntEnum):
    Shift     = 1
    Lock      = 2
    Control   = 4
    Alt       = 8
    Mod2      = 16
    Mod3      = 32
    Super     = 64
    Mod5      = 128
    Left      = 256
    Middle    = 512
    Right     = 1024
    WheelUp   = 2048
    WheelDown = 4096


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


class ButtonMask(_IntEnum):
    _1  = 256
    _2  = 512
    _3  = 1024
    _4  = 2048
    _5  = 4096
    Any = 32768


class NamedButtonMask(_IntEnum):
    r"""SUMMARY
    """
    Left      = 256
    Middle    = 512
    Right     = 1024
    WheelUp   = 2048
    WheelDown = 4096
    Any       = 32768


class Grab(_IntEnum):
    Any = 0


class Allow(_IntEnum):
    AsyncPointer   = 0
    SyncPointer    = 1
    ReplayPointer  = 2
    AsyncKeyboard  = 3
    SyncKeyboard   = 4
    ReplayKeyboard = 5
    AsyncBoth      = 6
    SyncBoth       = 7


class InputFocus(_IntEnum):
    _None          = 0
    PointerRoot    = 1
    Parent         = 2
    FollowKeyboard = 3


class FontDraw(_IntEnum):
    LeftToRight = 0
    RightToLeft = 1


class GC(_IntEnum):
    Function           = 1
    PlaneMask          = 2
    Foreground         = 4
    Background         = 8
    LineWidth          = 16
    LineStyle          = 32
    CapStyle           = 64
    JoinStyle          = 128
    FillStyle          = 256
    FillRule           = 512
    Tile               = 1024
    Stipple            = 2048
    TileStippleOriginX = 4096
    TileStippleOriginY = 8192
    Font               = 16384
    SubwindowMode      = 32768
    GraphicsExposures  = 65536
    ClipOriginX        = 131072
    ClipOriginY        = 262144
    ClipMask           = 524288
    DashOffset         = 1048576
    DashList           = 2097152
    ArcMode            = 4194304


class GX(_IntEnum):
    clear        = 0
    _and         = 1
    andReverse   = 2
    copy         = 3
    andInverted  = 4
    noop         = 5
    xor          = 6
    _or          = 7
    nor          = 8
    equiv        = 9
    invert       = 10
    orReverse    = 11
    copyInverted = 12
    orInverted   = 13
    nand         = 14
    set          = 15


class LineStyle(_IntEnum):
    Solid      = 0
    OnOffDash  = 1
    DoubleDash = 2


class CapStyle(_IntEnum):
    NotLast    = 0
    Butt       = 1
    Round      = 2
    Projecting = 3


class JoinStyle(_IntEnum):
    Miter = 0
    Round = 1
    Bevel = 2


class FillStyle(_IntEnum):
    Solid          = 0
    Tiled          = 1
    Stippled       = 2
    OpaqueStippled = 3


class FillRule(_IntEnum):
    EvenOdd = 0
    Winding = 1


class SubwindowMode(_IntEnum):
    ClipByChildren   = 0
    IncludeInferiors = 1


class ArcMode(_IntEnum):
    Chord    = 0
    PieSlice = 1


class ClipOrdering(_IntEnum):
    Unsorted = 0
    YSorted  = 1
    YXSorted = 2
    YXBanded = 3


class CoordMode(_IntEnum):
    Origin   = 0
    Previous = 1


class PolyShape(_IntEnum):
    Complex   = 0
    Nonconvex = 1
    Convex    = 2


class ImageFormat(_IntEnum):
    XYBitmap = 0
    XYPixmap = 1
    ZPixmap  = 2


class ColormapAlloc(_IntEnum):
    _None = 0
    All   = 1


class ColorFlag(_IntEnum):
    Red   = 1
    Green = 2
    Blue  = 4


class Pixmap(_IntEnum):
    _None = 0


class Font(_IntEnum):
    _None = 0


class QueryShapeOf(_IntEnum):
    LargestCursor  = 0
    FastestTile    = 1
    FastestStipple = 2


class KB(_IntEnum):
    KeyClickPercent = 1
    BellPercent     = 2
    BellPitch       = 4
    BellDuration    = 8
    Led             = 16
    LedMode         = 32
    Key             = 64
    AutoRepeatMode  = 128


class LedMode(_IntEnum):
    Off = 0
    On  = 1


class AutoRepeatMode(_IntEnum):
    Off     = 0
    On      = 1
    Default = 2


class Blanking(_IntEnum):
    NotPreferred = 0
    Preferred    = 1
    Default      = 2


class Exposures(_IntEnum):
    NotAllowed = 0
    Allowed    = 1
    Default    = 2


class HostMode(_IntEnum):
    Insert = 0
    Delete = 1


class Family(_IntEnum):
    Internet          = 0
    DECnet            = 1
    Chaos             = 2
    ServerInterpreted = 5
    Internet6         = 6


class AccessControl(_IntEnum):
    Disable = 0
    Enable  = 1


class CloseDown(_IntEnum):
    DestroyAll      = 0
    RetainPermanent = 1
    RetainTemporary = 2


class Kill(_IntEnum):
    AllTemporary = 0


class ScreenSaver(_IntEnum):
    Reset  = 0
    Active = 1


class MappingStatus(_IntEnum):
    Success = 0
    Busy    = 1
    Failure = 2


class MapIndex(_IntEnum):
    Shift   = 0
    Lock    = 1
    Control = 2
    _1      = 3
    _2      = 4
    _3      = 5
    _4      = 6
    _5      = 7



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# define.py ends here
