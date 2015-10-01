#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: eventcode.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""eventcode -- a parts of xcb2

"""
from enum import IntEnum as _IntEnum


class EventCode(_IntEnum):
    r"""SUMMARY
    """
    KeyPress         = 2
    KeyRelease       = 3
    ButtonPress      = 4
    ButtonRelease    = 5
    MotionNotify     = 6
    EnterNotify      = 7
    LeaveNotify      = 8
    FocusIn          = 9
    FocusOut         = 10
    KeymapNotify     = 11
    Expose           = 12
    GraphicsExposure = 13
    NoExposure       = 14
    VisibilityNotify = 15
    CreateNotify     = 16
    DestroyNotify    = 17
    UnmapNotify      = 18
    MapNotify        = 19
    MapRequest       = 20
    ReparentNotify   = 21
    ConfigureNotify  = 22
    ConfigureRequest = 23
    GravityNotify    = 24
    ResizeRequest    = 25
    CirculateNotify  = 26
    CirculateRequest = 27
    PropertyNotify   = 28
    SelectionClear   = 29
    SelectionRequest = 30
    SelectionNotify  = 31
    ColormapNotify   = 32
    ClientMessage    = 33
    MappingNotify    = 34



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# eventcode.py ends here
