#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: TCPPort.py 227 2014-09-13 08:15:46Z t1 $
# $Revision: 227 $
# $Date: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $

r"""TCPPort -- DESCRIPTION

"""
from .port import Port


class TCPPort(Port):
    """Class TCPPort
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
