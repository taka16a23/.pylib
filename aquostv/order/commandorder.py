#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: commandorder.py 227 2014-09-13 08:15:46Z t1 $
# $Revision: 227 $
# $Date: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $

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
