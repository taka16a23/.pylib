#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: address.py 227 2014-09-13 08:15:46Z t1 $
# $Revision: 227 $
# $Date: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $

r"""address -- DESCRIPTION

"""
from .ip import IP
from .port import TCPPort


class Address:
    """Class Address
    """
    # Attributes:
    def __init__(self, ipadder, port):
        r"""

        @Arguments:
        - `ipadder`:
        - `port`:
        """
        self._ipadder = IP(ipadder)
        self._port = TCPPort(port)

    # Operations
    def set_host(self, ipadder):
        r"""SUMMARY

        set_host(ipadder)

        @Arguments:
        - `ipadder`:

        @Return:

        @Error:
        """
        self._ipadder = ipadder

    def get_host(self):
        """function get_host

        returns
        """
        return self._ipadder

    def set_port(self, port):
        r"""SUMMARY

        set_port(port)

        @Arguments:
        - `port`:

        @Return:

        @Error:
        """
        self._port = port

    def get_port(self):
        """function get_port

        returns
        """
        return self._port



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# address.py ends here
