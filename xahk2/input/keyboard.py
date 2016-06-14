#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""keyboard -- DESCRIPTION

"""
from xahk2.input.key import X11Key


class X11Keyboard(object):
    """Class X11Keyboard
    """
    # Attributes:
    def __init__(self, display):
        r"""

        @Arguments:
        - `display`:
        """
        self.display = display
        setup = self.display.get_setup()
        self.code_range = xrange(setup.min_keycode, setup.max_keycode + 1)
        self._keys = [X11Key(self.display, code) for code in self.code_range]

    # Operations
    def get_display(self):
        """function get_display

        returns
        """
        return self.display

    def min_keycode(self, ):
        r"""SUMMARY

        min_keycode()

        @Return:

        @Error:
        """
        return min(self.code_range)

    def max_keycode(self, ):
        r"""SUMMARY

        max_keycode()

        @Return:

        @Error:
        """
        return max(self.code_range)

    def list_keys(self):
        """function list_keys

        returns
        """
        return self._keys[:] # new list

    def get_key(self, keycode):
        """function get_key

        keycode:

        returns
        """
        if keycode not in self.code_range:
            # TODO: (Atami) [2015/12/09]
            raise StandardError()
        for key in self._keys:
            if keycode == key.get_code():
                return key



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# keyboard.py ends here
