#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id$
# $Revision$
# $Date$
# $Author$
# $LastChangedBy$
# $LastChangedDate$

r"""Name: __init__.py


"""
import os
import sys
import re

import evdev

__revision__ = "$Revision$"
__version__ = "0.1.0"

__all__ = [ '' ]

KEY_DOWN = 1
KEY_UP = 0
KEY_HOLD = 2


def sendkey(ui, key, ctrl=False, alt=False, shift=False):
    r"""SUMMARY

    sendkey()

    @Return:
    """
    if ctrl:
        ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTCTRL, KEY_DOWN)
    if alt:
        ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTALT, KEY_DOWN)
    if shift:
        ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTSHIFT, KEY_DOWN)

    _sendkey(ui, key)

    if ctrl:
        ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTCTRL, KEY_UP)
    if alt:
        ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTALT, KEY_UP)
    if shift:
        ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTSHIFT, KEY_UP)
    ui.syn()


def _sendkey(ui, key):
    r"""SUMMARY

    _sendkey(ui, key)

    @Arguments:
    - `ui`:
    - `key`:

    @Return:
    """
    ui.write(evdev.ecodes.EV_KEY, key, KEY_DOWN)
    ui.write(evdev.ecodes.EV_KEY, key, KEY_UP)
    ui.syn()


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
