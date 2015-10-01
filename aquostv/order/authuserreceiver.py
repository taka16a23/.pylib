#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: authuserreceiver.py 227 2014-09-13 08:15:46Z t1 $
# $Revision: 227 $
# $Date: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $

from .receiver import Receiver


class AuthUserReceiver(Receiver):
    """Class AuthUserReceiver
    """
    success_code = '\r\nPassword:'

    # Attributes:
    def __init__(self, received):
        r"""

        @Arguments:
        - `received`:
        """
        self._received = received

    # Operations
    def set_received(self, received):
        """function set_received

        string:

        returns
        """
        self._received = received

    def get_received(self):
        """function get_received

        returns string
        """
        return self._received

    def issuccess(self):
        """function issuccess

        returns bool
        """
        return self._received == self.get_expect()

    def get_expect(self):
        """function get_expect

        returns string
        """
        return self.success_code



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# authuserreceiver.py ends here
