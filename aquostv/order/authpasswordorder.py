#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: authpasswordorder.py 227 2014-09-13 08:15:46Z t1 $
# $Revision: 227 $
# $Date: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $

from .order import Order
from .authpasswordreceiver import AuthPasswordReceiver


class AuthPasswordOrder(Order):
    """Class AuthPasswordOrder
    """
    # Attributes:
    def __init__(self, password):
        r"""

        @Arguments:
        - `password`:
        """
        self._password = password

    # Operations
    def get_orderline(self):
        """function get_orderline

        returns string
        """
        return str(self._password) + '\n'

    def receive(self, received):
        """function receive

        string:

        returns
        """
        return AuthPasswordReceiver(received)

    def set_password(self, password):
        """function set_password

        returns
        """
        self._password = password

    def get_password(self):
        """function get_password

        returns
        """
        return self._password



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# authpasswordorder.py ends here
