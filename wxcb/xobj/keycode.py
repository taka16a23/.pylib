#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""keycode -- DESCRIPTION

"""
from struct import pack
from userint import UserInt


class Keycode(UserInt):
    """Class Keycode
    """
    # Operations
    def set(self, value):
        """function set

        value: int

        returns None
        """
        integer = int(value)
        if integer < 8 or 255 < integer:
            # TODO: (Atami) [2014/12/29]
            raise StandardError('range error {}'.format(integer))
        super(Keycode, self).set(value)

    def pack(self, ):
        r"""SUMMARY

        pack()

        @Return:

        @Error:
        """
        return pack('B', int(self))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# keycode.py ends here
