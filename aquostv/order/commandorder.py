#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .order import Order
from .commandreceiver import CommandReceiver


class CommandOrder(Order):
    """Class CommandOrder
    """
    # Attributes:
    def __init__(self, command):
        r"""

        @Arguments:
        - `command`:
        """
        self._command = command

    # Operations
    def get_orderline(self):
        """function get_orderline

        returns string
        """
        return self._command.get_orderline() + '\n'

    def receive(self, received):
        """function receive

        string:

        returns
        """
        return CommandReceiver(received, self._command)

    def set_command(self, command):
        """function set_command

        returns
        """
        self._command = command

    def get_command(self):
        """function get_command

        returns
        """
        return self._command



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# commandorder.py ends here
