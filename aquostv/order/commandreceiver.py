#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: commandreceiver.py 227 2014-09-13 08:15:46Z t1 $
# $Revision: 227 $
# $Date: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $

from .receiver import Receiver


class CommandReceiver(Receiver):
    """Class CommandReceiver
    """
    ok_code = 'OK\n'
    err_code = 'ERR\n'

    # Attributes:
    def __init__(self, received, command):
        r"""

        @Arguments:
        - `command`:
        """
        self._received = received
        self._command = command

    # Operations
    def set_received(self, received):
        """function set_received

        returns
        """
        self._received = received

    def get_received(self):
        """function get_received

        returns
        """
        return self._received

    def issuccess(self):
        """function issuccess

        returns bool
        """
        if self.ok_code == self._received:
            return True
        if self.err_code == self._received:
            return False
        # TODO: (Atami) [2014/09/03]
        raise StandardError()

    def get_command(self):
        """function get_command

        returns
        """
        return self._command

    def set_command(self, command):
        """function set_command

        returns
        """
        self._command = command



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# commandreceiver.py ends here
