#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""mouse -- DESCRIPTION

"""
from xahk2.input.button import X11Button
from xahk2.input.cursor import X11Cursor


class X11Mouse(object):
    """Class X11Mouse
    """
    # Attributes:
    def __init__(self, display):
        r"""

        @Arguments:
        - `display`:
        """
        self._cursor = X11Cursor(display)
        self._buttons = [X11Button(display, code) for code in xrange(1, 6)]

    # Operations
    def get_display(self):
        """function get_display

        returns
        """
        return self._cursor.get_display()

    display = property(get_display)

    def get_cursor(self):
        """function get_cursor

        returns
        """
        return self._cursor

    def list_buttons(self):
        """function list_buttons

        returns
        """
        return self._buttons[:] # new list

    def get_point(self):
        """function get_point

        returns
        """
        return self._cursor.get_point()

    def set_point(self, newx, newy):
        """function set_point

        newx:
        newy:

        returns
        """
        self._cursor.set_point(newx, newy)

    # def set_point(self, point):
    #     """function set_point

    #     point: Point

    #     returns
    #     """
    #     return None # should raise NotImplementedError()

    def get_button(self, code):
        """function get_button

        code:

        returns
        """
        if code not in xrange(1, 6):
            # TODO: (Atami) [2015/12/09]
            raise StandardError()
        for button in self._buttons:
            if code == button.get_code():
                return button



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# mouse.py ends here
