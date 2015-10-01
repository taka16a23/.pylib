#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .receiver import Receiver


class AuthPasswordReceiver(Receiver):
    """Class AuthPasswordReceiver
    """
    success_code = '\r\n'
    false_code = ''

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
        expect = self.get_expect()
        if self._received == expect:
            return True
        if self._received == self.false_code:
            return False
        raise StandardError()

    def get_expect(self):
        """function get_expect

        returns
        """
        return self.success_code



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# authpasswordreceiver.py ends here
