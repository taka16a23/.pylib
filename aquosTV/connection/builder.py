#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""builder -- DESCRIPTION

"""
import socket
from abc import ABCMeta, abstractmethod
from .connection import Connection


class ConnectionBuilderInterface(object):
    """ConnectionBuilderInterface

    ConnectionBuilderInterface is a object.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def connect(self, ):
        """SUMMARY

        connect()

        @Return:

        @Error:
        """

    @abstractmethod
    def authenticate(self, ):
        """SUMMARY

        authenticate()

        @Return:

        @Error:
        """

    @abstractmethod
    def get_connection(self, ):
        """SUMMARY

        get_connection()

        @Return:

        @Error:
        """


class ConnectionBuilder(ConnectionBuilderInterface):
    """ConnectionBuilder

    ConnectionBuilder is a ConnectionBuilderInterface.
    Responsibility:
    """
    def __init__(self, inetsocketaddr, account):
        """

        @Arguments:
        - `inetsocketaddr`:
        - `account`:
        """
        self.inetsocketaddr = inetsocketaddr
        self.account = account
        self._conn = None


    def connect(self, ):
        """SUMMARY

        connect()

        @Return:

        @Error:
        """
        sct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sct.connect((self.inetsocketaddr.get_host(),
                     self.inetsocketaddr.get_port()))
        self._conn = Connection(sct)

    def authenticate(self, ):
        """SUMMARY

        authenticate()

        @Return:

        @Error:
        """
        self._conn.send(self.account.get_user())
        self._conn.send(self.account.get_password())

    def get_connection(self, ):
        """SUMMARY

        get_socket()

        @Return:

        @Error:
        """
        return self._conn



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# builder.py ends here
