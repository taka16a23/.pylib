#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: display.py 173 2014-05-03 07:51:01Z t1 $
# $Revision: 173 $
# $Date: 2014-05-03 16:51:01 +0900 (Sat, 03 May 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-05-03 16:51:01 +0900 (Sat, 03 May 2014) $

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
