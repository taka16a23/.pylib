#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""remotecontroller -- DESCRIPTION

"""
from . import commandgenerator
from . import commandcontroller
from . import connection



class RemoteController(object):
    r"""RemoteController

    RemoteController is a object.
    Responsibility:
    """
    def __init__(self, ip, port, user, password):
        r"""

        @Arguments:
        - `connection`:
        - `cmd`:
        """
        self._connection = connection.Connection(ip, port, user, password)
        self._cmds = {}
        self._make_cmds()

    def _make_cmds(self, ):
        r"""SUMMARY

        _make_cmds()

        @Return:

        @Error:
        """
        gen = commandgenerator.CommandGenerator()
        for cmdtype in gen.list_candidate():
            self._cmds[cmdtype] = gen.generate(cmdtype)

    def get_cmd(self, cmdtype):
        r"""SUMMARY

        get_cmd(cmdtype)

        @Arguments:
        - `cmdtype`:

        @Return:

        @Error:
        """
        cmd = self._cmds.get(cmdtype)
        return commandcontroller.CommandController(self._connection, cmd)

    def list_cmdtypes(self, ):
        r"""SUMMARY

        list_cmdtypes()

        @Return:

        @Error:
        """
        return self._cmds.keys()

    def get_connection(self, ):
        r"""SUMMARY

        get_connection()

        @Return:

        @Error:
        """
        return self._connection

    def set_connection(self, connection):
        r"""SUMMARY

        set_connection(connection)

        @Arguments:
        - `connection`:

        @Return:

        @Error:
        """
        self._connection = connection

    def reset_cmd(self, cmdtype):
        r"""SUMMARY

        reset_cmd(cmdtype)

        @Arguments:
        - `cmdtype`:

        @Return:

        @Error:
        """
        gen = commandgenerator.CommandGenerator()
        self._cmds[cmdtype] = gen.generate(cmdtype)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# remotecontroller.py ends here
