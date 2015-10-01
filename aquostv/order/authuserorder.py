#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: authuserorder.py 227 2014-09-13 08:15:46Z t1 $
# $Revision: 227 $
# $Date: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $

from .order import Order
from .authuserreceiver import AuthUserReceiver


class AuthUserOrder(Order):
    """Class AuthUserOrder
    """
    # Attributes:
    def __init__(self, user):
        r"""

        @Arguments:
        - `user`:
        """
        self._user = user

    # Operations
    def get_orderline(self):
        """function get_orderline

        returns string
        """
        return str(self._user) + '\n'

    def receive(self, received):
        """function receive

        string:

        returns
        """
        return AuthUserReceiver(received)

    def set_user(self, user):
        """function set_user

        returns
        """
        self._user = user

    def get_user(self):
        """function get_user

        returns
        """
        return self._user



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# authuserorder.py ends here
