#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: socketbuilder.py 227 2014-09-13 08:15:46Z t1 $
# $Revision: 227 $
# $Date: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $
from abc import ABCMeta, abstractmethod
import socket
from .. import address


class SocketBuilder(object):
    """Abstract class SocketBuilder
    """
    __metaclass__ = ABCMeta

    # Operations
    @abstractmethod
    def create_socket(self):
        raise NotImplementedError()

    @abstractmethod
    def connect(self):
        raise NotImplementedError()


class AquosSocketBuilder(SocketBuilder):
    """Class AquosSocketBuilder
    """
    # Attributes:
    def __init__(self, ip, port):
        r"""

        @Arguments:
        - `ip`:
        - `port`:
        """
        self._address = address.Address(ip, port)
        self._socket = None

    # Operations
    def create_socket(self):
        """function create_socket

        returns socket
        """
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        """function connect

        returns
        """
        self._socket.connect((self._address.get_host().get(),
                              self._address.get_port().get()))

    def get_result(self):
        """function get_socket

        returns
        """
        return self._socket

    def get_address(self):
        """function get_address

        returns
        """
        return self._address

    def set_address(self, address):
        """function set_address

        returns
        """
        self._address = address



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# socketbuilder.py ends here
