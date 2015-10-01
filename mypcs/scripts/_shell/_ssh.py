#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""ssh -- DESCRIPTION

"""
from time import sleep
from mypcs.scripts._shell._shell import Shell
from mypcs.commons.stdstream import StandardStream


class SSH(Shell):
    """Class SSH
    """
    # Attributes:
    def __init__(self, sshclient, timeout=None, waitexit=1000):
        r"""

        @Arguments:
        - `sshclient`:
        """
        self._sshclient = sshclient
        self._timeout = timeout
        self._wait = waitexit

    # Operations
    def execute_command(self, cmdline):
        """function execute_command

        cmdline:

        returns StandardStream
        """
        commandline = cmdline + '\n'
        stdin, stdout, stderr = self._sshclient.exec_command(
            commandline, timeout=self._timeout)
        # TODO: (Atami) [2015/08/16]
        # agry
        counts = 0
        while not stdout.channel.exit_status_ready():
            counts += 1
            sleep(0.01)
            if self._wait < counts:
                break
        sleep(0.1)
        returncode = stdout.channel.exit_status
        return StandardStream(stdin, stdout, stderr, returncode)

    def get_sshclient(self):
        """function get_sshclient

        returns
        """
        return self._sshclient

    def set_sshclient(self, sshclient):
        """function set_sshclient

        sshclient:

        returns
        """
        self._sshclient = sshclient

    def get_timeout(self, ):
        r"""SUMMARY

        get_timeout()

        @Return:

        @Error:
        """
        return self._timeout

    def set_timeout(self, timeout):
        r"""SUMMARY

        set_timeout(timeout)

        @Arguments:
        - `timeout`:

        @Return:

        @Error:
        """
        self._timeout = timeout

    def delete_timeout(self, ):
        r"""SUMMARY

        delete_timeout()

        @Return:

        @Error:
        """
        self._timeout = None

    timeout = property(get_timeout, set_timeout)


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# ssh.py ends here
