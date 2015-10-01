#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Director(object):
    """Abstract class Director
    """
    __metaclass__ = ABCMeta
    # Operations
    @abstractmethod
    def direct(self):
        raise NotImplementedError()


class SocketDirector(Director):
    """Class SocketDirector
    """
    # Attributes:
    def __init__(self, builder):
        r"""

        @Arguments:
        - `builder`:
        """
        self._builder = builder

    # Operations
    def direct(self):
        """function direct

        returns
        """
        self._builder.create_socket()
        self._builder.connect()
        return self._builder.get_result()

    def set_socketbuilder(self, builder):
        """function set_socketbuilder

        returns
        """
        self._builder = builder

    def get_socketbuilder(self):
        """function get_socketbuilder

        returns
        """
        return self._builder


class LoginDirector(Director):
    """Class LoginDirector
    """
    # Attributes:
    def __init__(self, authenticator):
        r"""SUMMARY

        __init__(authenticator)

        @Arguments:
        - `authenticator`:

        @Return:

        @Error:
        """
        self._authenticator = authenticator

    # Operations
    def direct(self):
        """function direct

        returns
        """
        self._authenticator.auth_user()
        self._authenticator.auth_password()

    def set_authenticator(self, authenticator):
        """function set_authenticator

        returns
        """
        self._authenticator = authenticator

    def get_authenticator(self):
        """function get_authenticator

        returns
        """
        return self._authenticator


class CommandDirector(Director):
    """Class CommandDirector
    """
    # Attributes:
    def __init__(self, builder):
        r"""

        @Arguments:
        - `builder`:
        """
        self._builder = builder

    # Operations
    def direct(self):
        """function direct

        returns
        """
        self._builder.build_command_type()
        self._builder.build_parameter()
        return self._builder.get_result()

    def set_builder(self, builder):
        """function set_builder

        returns
        """
        self._builder = builder

    def get_builder(self):
        """function get_builder

        returns
        """
        return self._builder



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# director.py ends here
