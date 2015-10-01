#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""buttoncode -- DESCRIPTION

"""
from userint import UserInt
from wxcb.protocol.xproto.define import NamedButtonIndex


class Buttoncode(UserInt):
    """Class Buttoncode
    """
    # Operations
    def set(self, value):
        """function set

        value: int

        returns None
        """
        super(Buttoncode, self).set(NamedButtonIndex(value))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# buttoncode.py ends here
