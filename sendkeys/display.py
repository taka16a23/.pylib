#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""display -- DESCRIPTION

"""
from xcb2 import Display
from sendkeys.keymap import KeyboardMapping


class KeymapDisplay(Display):
    r"""SUMMARY
    """
    attr = 'keymap'

    def __init__(self, display=None):
        r"""

        @Arguments:
        - `display`:
        """
        Display.__init__(self, display)
        keymap = 'keymap'
        if not hasattr(self.connection, self.attr):
            setattr(self.connection, self.attr,
                    KeyboardMapping(self.connection))
        elif not isinstance(getattr(self.connection, self.attr),
                            KeyboardMapping):
            raise StandardError('already hasattr other instance.')

    @property
    def keymap(self, ):
        r"""SUMMARY

        keymap()

        @Return:
        """
        return getattr(self.connection, self.attr)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# display.py ends here
