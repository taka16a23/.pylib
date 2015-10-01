#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: buttoncode.py 280 2015-01-29 00:05:31Z t1 $
# $Revision: 280 $
# $Date: 2015-01-29 09:05:31 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:05:31 +0900 (Thu, 29 Jan 2015) $

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
