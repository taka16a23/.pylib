#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""piece -- DESCRIPTION

"""


class Piece(object):
    """Class XPiece
    """
    # Attributes:
    def __init__(self, modifiers=0):
        r"""

        @Arguments:
        - `display`:
        - `modifiers`:
        """
        self._modifiers = modifiers

    # Operations
    def press(self, window, x=0, y=0):
        """function press

        window: int
        x:
        y:

        returns
        """
        self.press_impl(window, x, y)

    def release(self, window, x=0, y=0):
        """function release

        window: int
        x:
        y:

        returns
        """
        self.release_impl(window, x, y)

    def press_impl(self, window, x, y):
        """function press_impl

        window:
        x:
        y:

        returns
        """
        raise NotImplementedError()

    def release_impl(self, window, x, y):
        """function release_impl

        window:
        x:
        y:

        returns
        """
        raise NotImplementedError()

    def tap(self, window, x=0, y=0):
        """function tap

        window: Window
        x:
        y:

        returns
        """
        self.press(window, x, y)
        self.release(window, x, y)

    def add_modifiers(self, modifiers):
        """function add_modifier

        modifier:

        returns
        """
        self._modifiers |= modifiers

    def remove_modifiers(self, modifiers):
        """function remove_modifier

        modifier:

        returns
        """
        self._modifiers ^= modifiers

    def get_modifiers(self):
        """function get_modifiers

        returns Modifiers
        """
        return self._modifiers

    def set_modifiers(self, modifiers):
        """function set_modifiers

        mod: int

        returns None
        """
        self._modifiers = modifiers

    modifiers = property(get_modifiers, set_modifiers)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# piece.py ends here
