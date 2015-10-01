#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""UDPPort -- DESCRIPTION

"""
from .port import Port


class UDPPort(Port):
    """Class UDPPort
    """
    # Attributes:
    def __init__(self, port):
        r"""

        @Arguments:
        - `port`:
        """
        self._number = port

    # Operations
    def get(self):
        """function get

        returns
        """
        return self._number

    def set(self, port):
        """function set

        returns
        """
        self._number = port

    def get_description(self):
        """function get_description

        returns
        """
        return None # should raise NotImplementedError()

    def __int__(self):
        return int(self.get())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# port.py ends here
