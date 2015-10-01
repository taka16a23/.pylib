#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""\
Name: __init__.py

from http://ubuntueasysetuper.googlecode.com/svn/trunk/FutureWork/sendkey.py
"""

__revision__ = "$Revision: 115 $"
__version__ = "0.1.0"

__all__ = [ 'sendkey' ]

import Xlib
import Xlib.display
import Xlib.X
import Xlib.XK
import Xlib.protocol.event
import Xlib.ext.xtest



display = Xlib.display.Display()

special_X_keysyms = {
    ' ' : "space",
    '\t' : "Tab",
    '\n' : "Return",  # for some reason this needs to be cr, not lf
    '\r' : "Return",
    '\e' : "Escape",
    '!' : "exclam",
    '#' : "numbersign",
    '%' : "percent",
    '$' : "dollar",
    '&' : "ampersand",
    '"' : "quotedbl",
    '\'' : "apostrophe",
    '(' : "parenleft",
    ')' : "parenright",
    '*' : "asterisk",
    '=' : "equal",
    '+' : "plus",
    ',' : "comma",
    '-' : "minus",
    '.' : "period",
    '/' : "slash",
    ':' : "colon",
    ';' : "semicolon",
    '<' : "less",
    '>' : "greater",
    '?' : "question",
    '@' : "at",
    '[' : "bracketleft",
    ']' : "bracketright",
    '\\' : "backslash",
    '^' : "asciicircum",
    '_' : "underscore",
    '`' : "grave",
    '{' : "braceleft",
    '|' : "bar",
    '}' : "braceright",
    '~' : "asciitilde"
    }


def get_keysym(ch) :
    keysym = Xlib.XK.string_to_keysym(ch)
    if keysym == 0 :
        # Unfortunately, although this works to get the correct keysym
        # i.e. keysym for '#' is returned as "numbersign"
        # the subsequent display.keysym_to_keycode("numbersign") is 0.
        keysym = Xlib.XK.string_to_keysym(special_X_keysyms[ch])
    return keysym

def char2keycode(ch) :
    keysym = get_keysym(ch)
    keycode = display.keysym_to_keycode(keysym)
    return keycode

CTRL_L = display.keysym_to_keycode(Xlib.XK.XK_Control_L)
ALT_L = display.keysym_to_keycode(Xlib.XK.XK_Alt_L)
SHIFT_L = display.keysym_to_keycode(Xlib.XK.XK_Shift_L)

def sendkey2(keystroke):
    ctrl = alt = shift = 0
    key = ""
    splitted = keystroke.split(" ")
    for stroke in splitted:
        if stroke == "Ctrl":
            ctrl = 1
        elif stroke == "Shift":
            shift = 1
        elif stroke == "Alt":
            alt = 1
        elif stroke == "Space":
            key = char2keycode(" ")
        else: # an ordinary key
            key = char2keycode(stroke)
    if ctrl==1:
        Xlib.ext.xtest.fake_input(display, Xlib.X.KeyPress, CTRL_L)
    if alt==1:
        Xlib.ext.xtest.fake_input(display, Xlib.X.KeyPress, ALT_L)
    if shift==1:
        Xlib.ext.xtest.fake_input(display, Xlib.X.KeyPress, SHIFT_L)
    Xlib.ext.xtest.fake_input(display, Xlib.X.KeyPress, key)
    Xlib.ext.xtest.fake_input(display, Xlib.X.KeyRelease, key)
    if ctrl==1:
        Xlib.ext.xtest.fake_input(display, Xlib.X.KeyRelease, CTRL_L)
    if alt==1:
        Xlib.ext.xtest.fake_input(display, Xlib.X.KeyRelease, ALT_L)
    if shift==1:
        Xlib.ext.xtest.fake_input(display, Xlib.X.KeyRelease, SHIFT_L)
    display.sync()

def sendkey(key, ctrl=False, alt=False, shift=False):

    flag_spkeys = zip([ctrl, alt, shift], [CTRL_L, ALT_L, SHIFT_L])

    # hold ctrl, alt or shift
    for flag, spkey in flag_spkeys:
        if flag is True:
            Xlib.ext.xtest.fake_input(display, Xlib.X.KeyPress, spkey)

    key = char2keycode(key)
    Xlib.ext.xtest.fake_input(display, Xlib.X.KeyPress, key)
    Xlib.ext.xtest.fake_input(display, Xlib.X.KeyRelease, key)

    # release key
    for flag, spkey in flag_spkeys:
        if flag is True:
            Xlib.ext.xtest.fake_input(display, Xlib.X.KeyRelease, spkey)

    display.sync()

def sendkeys(str_):
    r"""SUMMARY

    @Arguments:
    - `str_`:

    @Return:
    """
    for s in str_:
        sendkey(s)

def click():
    r"""SUMMARY

    @Return:
    """
    Xlib.ext.xtest.fake_input(display, Xlib.X.ButtonPress, 2)
    Xlib.ext.xtest.fake_input(display, Xlib.X.ButtonRelease, 2)
    display.sync()

# 1=left, 2=middle, 3=right


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
