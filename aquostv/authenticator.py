#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from .. import order


class Authenticator(object):
    """Abstract class Authenticator
    """
    __metaclass__ = ABCMeta

    # Operations
    @abstractmethod
    def auth_user(self):
        raise NotImplementedError()

    @abstractmethod
    def auth_password(self):
        raise NotImplementedError()


class AquosAuthenticator(Authenticator):
    """Class AquosAuthenticator
    """
    # Attributes:
    def __init__(self, connection):
        r"""

        @Arguments:
        - `connection`:
        - `account`:
        """
        self._connection = connection

    # Operations
    def _send(self, orderobj):
        r"""SUMMARY

        _send(orderobj)

        @Arguments:
        - `orderobj`:

        @Return:

        @Error:
        """
        received = self._connection.send(orderobj)
        if not received.issuccess():
            raise StandardError()

    def auth_user(self):
        """function auth_user

        returns
        """
        orderobj = order.AuthUserOrder(
            self._connection.get_account().get_user())
        self._send(orderobj)

    def auth_password(self):
        """function auth_password

        returns
        """
        orderobj = order.AuthPasswordOrder(
            self._connection.get_account().get_password())
        self._send(orderobj)

    def set_connection(self, connection):
        """function set_connection

        returns
        """
        self._connection = connection

    def get_connection(self):
        """function get_connection

        returns
        """
        return self._connection



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# authenticator.py ends here
