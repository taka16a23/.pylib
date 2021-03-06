#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""commandcontroller -- DESCRIPTION

"""
from . import order


class CommandController(object):
    r"""CommandController

    CommandController is a object.
    Responsibility:
    """
    def __init__(self, connection, command):
        r"""

        @Arguments:
        - `connection`:
        - `command`:
        """
        self._connection = connection
        self._command = command

    def set_connection(self, connection):
        r"""SUMMARY

        set_connection()

        @Return:

        @Error:
        """
        self._connection = connection

    def get_connection(self, ):
        r"""SUMMARY

        get_connection()

        @Return:

        @Error:
        """
        return self._connection

    def set_command(self, cmd):
        r"""SUMMARY

        set_command(cmd)

        @Arguments:
        - `cmd`:

        @Return:

        @Error:
        """
        self._command = cmd

    def get_command(self, ):
        r"""SUMMARY

        get_command()

        @Return:

        @Error:
        """
        return self._command

    def _make_order(self, ):
        r"""SUMMARY

        _make_order()

        @Return:

        @Error:
        """
        return order.CommandOrder(self._command)

    def send(self, ):
        r"""SUMMARY

        send()

        @Return:

        @Error:
        """
        return self._connection.send(self._make_order())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# commandcontroller.py ends here
