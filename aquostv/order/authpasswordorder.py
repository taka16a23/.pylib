#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
