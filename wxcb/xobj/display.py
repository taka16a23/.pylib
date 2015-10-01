#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: display.py 280 2015-01-29 00:05:31Z t1 $
# $Revision: 280 $
# $Date: 2015-01-29 09:05:31 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:05:31 +0900 (Thu, 29 Jan 2015) $

r"""display -- DESCRIPTION

"""
import os as _os
import wxcb.conn


class Display(object):
    r"""Display

    Display is a object.
    Responsibility:
    """
    def __init__(self, display=None):
        r"""

        @Arguments:
        - `display`:
        """
        self._display = None
        self.set(display)

    def get(self, ):
        r"""SUMMARY

        get()

        @Return:

        @Error:
        """
        return self._display

    def set(self, display):
        r"""SUMMARY

        set(display)

        @Arguments:
        - `display`:

        @Return:

        @Error:
        """
        self._display = str(display or _os.environ.get('DISPLAY', ''))

    def flush(self, ):
        r"""SUMMARY

        flush()

        @Return:

        @Error:
        """
        wxcb.conn.connect(self._display).flush()

    def __str__(self):
        return self._display

    def __repr__(self):
        return '{0.__class__.__name__}("{0._display}")'.format(self)

    def __eq__(self, other):
        if isinstance(other, (self.__class__, )):
            return self._display == str(other)
        return self._display == other

    def __ne__(self, other):
        return not self == other

    def __cmp__(self, other):
        """
        self < other return -1
        self > other return 1
        self == other return 0
        """
        if isinstance(other, (self.__class__, )):
            return cmp(self._display, str(other))
        return cmp(self._display, other)

    def __hash__(self, ):
        return hash(self._display)

    # TODO: (Atami) [2015/01/23]
    # get_screen_number
    # get_host
    # get_display_number



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# display.py ends here
