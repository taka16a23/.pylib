#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""x11_piece -- DESCRIPTION

"""
from struct import pack
from xcb.xproto import EventMask

from xahk.wm.display import Display
from xahk.piece._piece import Piece
from xahk.wm.eventcode import EventCode
from xahk.binder.define import ButtonIndex, ModifierMask


class X11Piece(Piece):
    r"""X11Piece

    X11Piece is a Piece.
    Responsibility:
    """
    sequence = 0
    time = 0
    child = 0
    rootx = 0
    rooty = 0
    samescreen = 1

    def __init__(self, modifiers=0):
        r"""

        @Arguments:
        - `modifier`:
        """
        super(X11Piece, self).__init__(modifiers)
        self.display = Display()
        self.root = self.display.get_setup().roots[0].root

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self.display


class X11Key(X11Piece):
    r"""XKey

    XKey is a XPieces.
    Responsibility:
    """

    def __init__(self, code, modifiers=0):
        r"""

        @Arguments:
        - `code`:
        - `modifiers`:
        """
        super(X11Key, self).__init__(modifiers)
        self._code = code

    def get_code(self, ):
        r"""SUMMARY

        get_code()

        @Return:

        @Error:
        """
        return self._code

    def set_code(self, code):
        r"""SUMMARY

        set_code(code)

        @Arguments:
        - `code`:

        @Return:

        @Error:
        """
        self._code = code

    code = property(get_code, set_code)

    def press_impl(self, window, x, y):
        r"""SUMMARY

        press_impl(window, x, y)

        @Arguments:
        - `window`:
        - `x`:
        - `y`:

        @Return:

        @Error:
        """
        event = pack('BBH4I5HBx', EventCode.KeyPress, self.code, self.sequence,
                     self.time, self.root, window, self.child, self.rootx,
                     self.rooty, x, y, self.modifiers, self.samescreen)
        self.display.core.SendEvent(False, window, EventMask.KeyPress, event)

    def release_impl(self, window, x, y):
        r"""SUMMARY

        release_impl(window, x, y)

        @Arguments:
        - `window`:
        - `x`:
        - `y`:

        @Return:

        @Error:
        """
        event = pack('BBH4I5HBx', EventCode.KeyRelease, self.code, self.sequence,
                     self.time, self.root, window, self.child, self.rootx,
                     self.rooty, x, y, self.modifiers, self.samescreen)
        self.display.core.SendEvent(False, window, EventMask.KeyRelease, event)


class X11Button(X11Piece):
    r"""X11Button

    X11Button is a X11Piece.
    Responsibility:
    """
    _release_modifier = {ButtonIndex.Left: ModifierMask.Left,
                         ButtonIndex.Middle: ModifierMask.Middle,
                         ButtonIndex.Right: ModifierMask.Right,
                         ButtonIndex.WheelUp: ModifierMask.WheelUp,
                         ButtonIndex.WheelDown: ModifierMask.WheelDown,
                         }

    def __init__(self, code, modifiers=0):
        r"""

        @Arguments:
        - `code`:
        - `modifier`:
        """
        super(X11Button, self).__init__(modifiers)
        self.code = code

    def press_impl(self, window, x, y):
        r"""SUMMARY

        press_impl(window, x, y)

        @Arguments:
        - `window`:
        - `x`:
        - `y`:

        @Return:

        @Error:
        """
        try:
            event = pack('BBH4I5HBx', EventCode.ButtonPress, self.code,
                         self.sequence, self.time, self.root, window, self.child,
                         self.rootx, self.rooty, x, y, self.modifiers,
                         self.samescreen)
            # self.display.core.SendEvent(
            #     False, self.root, EventMask.ButtonPress, event)
        except:
            # TODO: (Atami) [2016/05/25]
            return
        self.display.core.SendEvent(
                False, window, EventMask.ButtonPress, event)

    def release_impl(self, window, x, y):
        r"""SUMMARY

        release_impl(window, x, y)

        @Arguments:
        - `window`:
        - `x`:
        - `y`:

        @Return:

        @Error:
        """
        try:
            event = pack('BBH4I5HBx', EventCode.ButtonRelease, self.code,
                     self.sequence, self.time, self.root, window, self.child,
                     self.rootx, self.rooty, x, y,
                     self.modifiers | self._release_modifier.get(self.code, 0),
                     self.samescreen)
        # self.display.core.SendEvent(
            # False, self.root, EventMask.ButtonRelease, event)
        except:
            # TODO: (Atami) [2016/05/25]
            return
        self.display.core.SendEvent(
            False, window, EventMask.ButtonRelease, event)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# x11_piece.py ends here
